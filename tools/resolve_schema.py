#!/usr/bin/env python3
"""
Resolve OGC Building Block schemas into a single complete JSON Schema.

Recursively resolves ALL $ref references from the modular YAML/JSON source
schemas into one fully-inlined schema — purely for validation and inspection,
with no form simplifications.

$ref patterns handled:
  1. Relative path:       $ref: ../cdifCatalogRecord/schema.yaml
  2. Fragment-only:       $ref: '#/$defs/Identifier'
  3. Cross-file fragment: $ref: ../cdifCatalogRecord/schema.yaml#/$defs/conformsTo_item
  4. URL ref:             $ref: https://usgin.github.io/metadataBuildingBlocks/_sources/.../schema.yaml
  5. Protocol-relative:   $ref: //usgin.github.io/metadataBuildingBlocks/_sources/.../schema.yaml
  6. Both YAML and JSON file extensions

Usage:
    python tools/resolve_schema.py adaEMPA
    python tools/resolve_schema.py adaProduct
    python tools/resolve_schema.py CDIFDiscovery
    python tools/resolve_schema.py --file path/to/any/schema.yaml
    python tools/resolve_schema.py adaEMPA -o resolved.json
    python tools/resolve_schema.py adaEMPA --flatten-allof
    python tools/resolve_schema.py --all
"""

import argparse
import copy
import json
import os
import sys
import tempfile
import yaml
from pathlib import Path
from typing import Any
from urllib.parse import urlparse
from urllib.request import urlopen
from urllib.error import URLError

REPO_ROOT = Path(__file__).resolve().parent.parent
SOURCES_DIR = REPO_ROOT / "_sources"

# Keys to strip from schemas (metadata, not useful for validation/inspection)
STRIP_KEYS = {"$id", "x-jsonld-prefixes", "x-jsonld-context", "x-jsonld-extra-terms"}

# Cache for fetched URL schemas (URL string -> local Path)
_URL_CACHE: dict[str, Path] = {}
_URL_CACHE_DIR = Path(tempfile.mkdtemp(prefix="resolve_schema_"))


def _is_url(ref: str) -> bool:
    """Return True if ref is an absolute HTTP(S) URL or protocol-relative URL."""
    return ref.startswith("https://") or ref.startswith("http://") or ref.startswith("//")


def _fetch_url_schema(url: str) -> Path:
    """Fetch a schema from a URL and cache it locally. Returns the local file path."""
    if url in _URL_CACHE:
        return _URL_CACHE[url]

    # Normalise protocol-relative URLs
    fetch_url = url
    if fetch_url.startswith("//"):
        fetch_url = "https:" + fetch_url

    try:
        with urlopen(fetch_url, timeout=30) as resp:
            data = resp.read()
    except URLError as e:
        print(f"  WARNING: Failed to fetch {fetch_url}: {e}", file=sys.stderr)
        return None

    # Determine extension from URL path
    parsed = urlparse(fetch_url)
    url_path = parsed.path
    ext = ".yaml" if url_path.endswith((".yaml", ".yml")) else ".json"

    # Write to a temp file preserving directory structure for relative refs
    # Use the URL path to create a unique cache path
    safe_name = url_path.strip("/").replace("/", os.sep)
    cache_path = _URL_CACHE_DIR / safe_name
    cache_path.parent.mkdir(parents=True, exist_ok=True)
    cache_path.write_bytes(data)

    _URL_CACHE[url] = cache_path
    return cache_path


# ---------------------------------------------------------------------------
# File loading
# ---------------------------------------------------------------------------

def load_schema_file(path: Path) -> dict:
    """Load a schema file (YAML or JSON) based on extension."""
    with open(path, "r", encoding="utf-8") as f:
        if path.suffix in (".yaml", ".yml"):
            return yaml.safe_load(f) or {}
        else:
            return json.load(f)


# ---------------------------------------------------------------------------
# JSON Pointer resolution
# ---------------------------------------------------------------------------

def resolve_fragment(schema: dict, pointer: str) -> Any:
    """Resolve a JSON Pointer (e.g., '/$defs/Identifier') within a schema."""
    parts = pointer.lstrip("/").split("/")
    current = schema
    for part in parts:
        if isinstance(current, dict) and part in current:
            current = current[part]
        elif isinstance(current, list):
            current = current[int(part)]
        else:
            raise KeyError(f"Cannot resolve pointer /{'/'.join(parts)} at part '{part}'")
    return current


# ---------------------------------------------------------------------------
# Metadata stripping
# ---------------------------------------------------------------------------

def strip_metadata_keys(schema: Any, is_root: bool = True) -> Any:
    """Recursively remove $id, x-jsonld-*, and nested $schema keys."""
    if isinstance(schema, dict):
        result = {}
        for k, v in schema.items():
            if k in STRIP_KEYS:
                continue
            if k.startswith("x-jsonld"):
                continue
            if k == "$schema" and not is_root:
                continue
            result[k] = strip_metadata_keys(v, is_root=False)
        return result
    elif isinstance(schema, list):
        return [strip_metadata_keys(item, is_root=False) for item in schema]
    return schema


# ---------------------------------------------------------------------------
# Deep merge (for allOf flattening)
# ---------------------------------------------------------------------------

_SCHEMA_DEF_KEYS = frozenset({"type", "oneOf", "anyOf", "allOf", "$ref"})


def _is_complete_schema(d: dict) -> bool:
    """Return True if d looks like a complete schema definition (has type, composition, or $ref)."""
    return bool(d.keys() & _SCHEMA_DEF_KEYS)


def deep_merge(base: dict, overlay: dict) -> dict:
    """
    Deep merge overlay into base. Overlay values take precedence.
    For dicts, merge recursively. For everything else, overlay replaces base.

    Special handling for ``properties`` dicts: when an overlay provides a
    property definition that already exists in the base AND the overlay looks
    like a complete schema definition (has ``type``, ``oneOf``, ``anyOf``,
    ``allOf``, or ``$ref``), the overlay **replaces** the base definition
    entirely.  This prevents invalid schemas where, e.g., cdifMandatory's
    distribution (``anyOf``) and adaProduct's (``oneOf``) get combined.

    When the overlay is a partial constraint patch (no ``type`` or composition
    keywords at the property level — just nested ``items.properties…``), it is
    deep-merged so that the base structure (``type``, ``description``, ``oneOf``,
    etc.) is preserved alongside the new constraints.
    """
    return _deep_merge_inner(base, overlay, in_properties=False)


def _deep_merge_inner(base: dict, overlay: dict, in_properties: bool) -> dict:
    result = copy.deepcopy(base)
    for k, v in overlay.items():
        if k in result and isinstance(result[k], dict) and isinstance(v, dict):
            if in_properties and _is_complete_schema(v):
                # Complete property definition → replace entirely
                result[k] = copy.deepcopy(v)
            elif k == "properties":
                result[k] = _deep_merge_inner(result[k], v, in_properties=True)
            elif k == "contains":
                # contains is a complete sub-schema constraint; overlay replaces
                result[k] = copy.deepcopy(v)
            else:
                result[k] = _deep_merge_inner(result[k], v, in_properties=False)
        else:
            result[k] = copy.deepcopy(v)
    return result


# ---------------------------------------------------------------------------
# Core resolution
# ---------------------------------------------------------------------------

def resolve_file(path: Path, seen: set) -> dict:
    """Load a YAML or JSON schema file and resolve all $ref within it."""
    canonical = path.resolve()
    if canonical in seen:
        return {"$comment": f"circular ref to {canonical}"}
    seen = seen | {canonical}  # Copy to avoid mutation across branches

    schema = load_schema_file(canonical)
    if not isinstance(schema, dict):
        return schema

    # Resolve $defs so fragment-only refs (#/$defs/X) can find them.
    # Two-pass strategy:
    #   Pass 1 — resolve every def with an empty local-defs dict.  This expands
    #            all external file $refs but leaves cross-def fragment refs as
    #            "$comment: unresolved …" placeholders.
    #   Pass 2 — re-resolve every def, this time with the fully-populated defs
    #            dict so that cross-def fragment refs can be found.
    defs = {}
    if "$defs" in schema:
        raw_defs = schema["$defs"]
        for def_name, def_schema in raw_defs.items():
            defs[def_name] = resolve_node(def_schema, canonical.parent, {}, seen)
        # Pass 2: re-resolve with full defs.  Because pass 1 may have left
        # "$comment" placeholders instead of the resolved content, we also
        # inline those placeholders by re-walking the defs.
        for def_name in list(defs.keys()):
            defs[def_name] = _inline_unresolved_defs(defs[def_name], defs, canonical.parent, seen)

    # Walk and resolve the entire schema
    resolved = resolve_node(schema, canonical.parent, defs, seen)

    # Remove $defs from final output (they've been inlined)
    if isinstance(resolved, dict):
        resolved.pop("$defs", None)

    return resolved


def resolve_node(node: Any, base_dir: Path, defs: dict, seen: set) -> Any:
    """Recursively resolve $ref in a schema node."""
    if isinstance(node, dict):
        if "$ref" in node:
            ref = node["$ref"]
            resolved = _resolve_ref(ref, base_dir, defs, seen)

            # If $ref has sibling keys, merge resolved with siblings
            siblings = {k: v for k, v in node.items() if k != "$ref"}
            if siblings:
                siblings = resolve_node(siblings, base_dir, defs, seen)
                if isinstance(resolved, dict):
                    resolved = deep_merge(resolved, siblings)
                # If resolved is not a dict (unlikely), siblings are lost
            return resolved

        # Recurse into all dict values
        result = {}
        for k, v in node.items():
            result[k] = resolve_node(v, base_dir, defs, seen)
        return result

    elif isinstance(node, list):
        return [resolve_node(item, base_dir, defs, seen) for item in node]

    return node


def _inline_unresolved_defs(node: Any, defs: dict, base_dir: Path, seen: set) -> Any:
    """
    Walk *node* and replace ``{"$comment": "unresolved fragment ref: #/$defs/X"}``
    placeholders with the actual resolved content from *defs*.
    Also re-resolve any remaining $ref nodes with the full defs dict.
    """
    if isinstance(node, dict):
        # Check for placeholder left by pass 1
        if "$comment" in node and len(node) == 1:
            comment = node["$comment"]
            if comment.startswith("unresolved fragment ref: #/$defs/"):
                def_name = comment.split("/")[-1]
                if def_name in defs:
                    return copy.deepcopy(defs[def_name])
        # Also resolve any leftover $ref
        if "$ref" in node:
            ref = node["$ref"]
            resolved = _resolve_ref(ref, base_dir, defs, seen)
            siblings = {k: v for k, v in node.items() if k != "$ref"}
            if siblings:
                siblings = _inline_unresolved_defs(siblings, defs, base_dir, seen)
                if isinstance(resolved, dict):
                    resolved = deep_merge(resolved, siblings)
            return resolved
        result = {}
        for k, v in node.items():
            result[k] = _inline_unresolved_defs(v, defs, base_dir, seen)
        return result
    elif isinstance(node, list):
        return [_inline_unresolved_defs(item, defs, base_dir, seen) for item in node]
    return node


def _resolve_ref(ref: str, base_dir: Path, defs: dict, seen: set) -> Any:
    """Parse and resolve a $ref string."""
    if ref == "#":
        # Bare self-reference (recursive schema) -- mark as circular
        return {"$comment": "circular-ref"}

    if ref.startswith("#/"):
        # Fragment-only ref (e.g., #/$defs/Identifier)
        pointer = ref[1:]  # Strip leading #
        # Try the local defs dict first
        parts = pointer.lstrip("/").split("/")
        if len(parts) == 2 and parts[0] == "$defs" and parts[1] in defs:
            return copy.deepcopy(defs[parts[1]])
        # Fall through: shouldn't happen if $defs were resolved, but handle gracefully
        return {"$comment": f"unresolved fragment ref: {ref}"}

    # File ref, possibly with fragment
    if "#" in ref:
        file_part, fragment = ref.split("#", 1)
    else:
        file_part, fragment = ref, None

    # Handle URL refs (absolute or protocol-relative)
    if _is_url(file_part):
        local_path = _fetch_url_schema(file_part)
        if local_path is None:
            return {"$comment": f"failed to fetch URL: {file_part}"}
        file_path = local_path
    else:
        file_path = (base_dir / file_part).resolve()

    if not file_path.exists():
        return {"$comment": f"file not found: {file_path}"}

    resolved = resolve_file(file_path, seen)

    if fragment:
        try:
            resolved = resolve_fragment(resolved, fragment)
        except KeyError as e:
            return {"$comment": f"could not resolve fragment {fragment} in {file_path}: {e}"}
        # The fragment result might itself contain refs — resolve them
        resolved = resolve_node(resolved, file_path.parent, {}, seen)

    return resolved


# ---------------------------------------------------------------------------
# allOf flattening (optional)
# ---------------------------------------------------------------------------

def flatten_allof(schema: Any) -> Any:
    """
    Recursively flatten allOf entries into a single object.
    Merges properties, required, and other constraints from all allOf entries.
    Preserves anyOf/oneOf as-is (they represent valid polymorphic choices).

    Special handling for ``contains``: when multiple allOf entries (or the
    parent object) each define a ``contains`` constraint, they are preserved
    as separate ``allOf`` entries with ``{"contains": ...}`` rather than
    deep-merged (which would overwrite one constraint with another).
    """
    if isinstance(schema, dict):
        # Recurse first so nested allOf in properties/items are handled
        result = {}
        for k, v in schema.items():
            result[k] = flatten_allof(v)

        # Now flatten allOf in the current object
        if "allOf" in result:
            all_of = result.pop("allOf")
            merged = {}
            # Collect all non-allOf keys from the current object
            for k, v in result.items():
                merged[k] = v

            # Collect contains constraints separately to avoid overwrite
            contains_list = []
            if "contains" in merged:
                contains_list.append(merged.pop("contains"))

            for entry in all_of:
                if isinstance(entry, dict):
                    entry_copy = copy.deepcopy(entry)
                    if "contains" in entry_copy:
                        contains_list.append(entry_copy.pop("contains"))
                    if entry_copy:  # remaining keys after extracting contains
                        merged = deep_merge(merged, entry_copy)

            # Re-attach contains constraints
            if len(contains_list) == 1:
                merged["contains"] = contains_list[0]
            elif len(contains_list) > 1:
                residual = merged.get("allOf", [])
                for c in contains_list:
                    residual.append({"contains": c})
                merged["allOf"] = residual

            return merged

        return result

    elif isinstance(schema, list):
        return [flatten_allof(item) for item in schema]

    return schema


# ---------------------------------------------------------------------------
# Profile entry point resolution
# ---------------------------------------------------------------------------

def _find_profile_dir(name: str) -> Path:
    """Find the profile directory by searching subdirectories of profiles/."""
    profiles_root = SOURCES_DIR / "profiles"
    # Search subdirectories (adaProfiles/, cdifProfiles/)
    for subdir in profiles_root.iterdir():
        if subdir.is_dir():
            candidate = subdir / name
            if candidate.is_dir():
                return candidate
    # Fall back to direct child (legacy flat layout)
    direct = profiles_root / name
    if direct.is_dir():
        return direct
    raise FileNotFoundError(f"Profile directory not found: {name}")


def find_profile_schema(name: str) -> Path:
    """Find the schema entry point for a profile name."""
    try:
        profile_dir = _find_profile_dir(name)
    except FileNotFoundError:
        print(f"ERROR: Cannot find schema for profile '{name}'", file=sys.stderr)
        print(f"  Looked in: {SOURCES_DIR / 'profiles'}", file=sys.stderr)
        sys.exit(1)

    # Try schema.yaml first
    yaml_path = profile_dir / "schema.yaml"
    if yaml_path.exists():
        return yaml_path

    # Fall back to any .json file in the profile directory (e.g., CDIFDiscoverySchema.json)
    json_files = sorted(profile_dir.glob("*Schema.json"))
    if json_files:
        return json_files[0]
    # Try any .json that isn't bblock.json or example files
    for jf in sorted(profile_dir.glob("*.json")):
        if jf.name not in ("bblock.json",) and "example" not in jf.name.lower():
            return jf

    print(f"ERROR: Cannot find schema for profile '{name}'", file=sys.stderr)
    print(f"  Looked in: {profile_dir}", file=sys.stderr)
    sys.exit(1)


# ---------------------------------------------------------------------------
# Scan for building blocks with external $refs
# ---------------------------------------------------------------------------

def _has_external_refs(node: Any) -> bool:
    """Return True if *node* contains any $ref pointing to an external file."""
    if isinstance(node, dict):
        if "$ref" in node and not node["$ref"].startswith("#"):
            return True
        return any(_has_external_refs(v) for v in node.values())
    if isinstance(node, list):
        return any(_has_external_refs(item) for item in node)
    return False


def find_all_schemas_with_external_refs() -> list[Path]:
    """Find every schema.yaml under _sources/ that contains external $refs."""
    results = []
    for schema_path in sorted(SOURCES_DIR.rglob("schema.yaml")):
        schema = load_schema_file(schema_path)
        if isinstance(schema, dict) and _has_external_refs(schema):
            results.append(schema_path)
    return results


def resolve_and_write(schema_path: Path, flatten: bool) -> Path:
    """Resolve a schema and write resolvedSchema.json next to it. Returns output path."""
    resolved = resolve_file(schema_path, seen=set())
    resolved = strip_metadata_keys(resolved, is_root=True)
    if flatten:
        resolved = flatten_allof(resolved)
    out_path = schema_path.parent / "resolvedSchema.json"
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(json.dumps(resolved, indent=2, ensure_ascii=False) + "\n")
    return out_path


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Resolve OGC Building Block schemas into a single complete JSON Schema.",
    )
    parser.add_argument(
        "profile",
        nargs="?",
        help="Profile name (e.g., adaEMPA, adaProduct, CDIFDiscovery)",
    )
    parser.add_argument(
        "--file",
        type=Path,
        help="Resolve an arbitrary schema file instead of a profile",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Find and resolve all building blocks with external $refs",
    )
    parser.add_argument(
        "-o", "--output",
        type=Path,
        help="Write output to file (default: stdout). Ignored with --all.",
    )
    parser.add_argument(
        "--flatten-allof",
        action="store_true",
        help="Merge allOf entries into single objects",
    )
    args = parser.parse_args()

    if args.all:
        schemas = find_all_schemas_with_external_refs()
        print(f"Found {len(schemas)} building blocks with external $refs", file=sys.stderr)
        for schema_path in schemas:
            rel = schema_path.relative_to(REPO_ROOT)
            out_path = resolve_and_write(schema_path, args.flatten_allof)
            print(f"  {rel} -> {out_path.name}", file=sys.stderr)
        print(f"Resolved {len(schemas)} schemas", file=sys.stderr)
        return

    if not args.profile and not args.file:
        parser.error("Specify a profile name, --file <path>, or --all")

    if args.file:
        schema_path = args.file.resolve()
        if not schema_path.exists():
            print(f"ERROR: File not found: {schema_path}", file=sys.stderr)
            sys.exit(1)
    else:
        schema_path = find_profile_schema(args.profile)

    print(f"Resolving: {schema_path}", file=sys.stderr)

    # Resolve all $ref recursively
    resolved = resolve_file(schema_path, seen=set())

    # Strip metadata keys
    resolved = strip_metadata_keys(resolved, is_root=True)

    # Optionally flatten allOf
    if args.flatten_allof:
        resolved = flatten_allof(resolved)

    # Output
    output_json = json.dumps(resolved, indent=2, ensure_ascii=False) + "\n"

    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(output_json)
        print(f"Wrote: {args.output}", file=sys.stderr)
    else:
        sys.stdout.write(output_json)


if __name__ == "__main__":
    main()
