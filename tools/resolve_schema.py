#!/usr/bin/env python3
# resolve_schema.py — canonical copy lives in metadataBuildingBlocks/tools/
# Sync to domain repos via: python tools/sync_resolve_schema.py
# VERSION: 2026-03-20
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
    python tools/resolve_schema.py CDIFDiscovery --structured
    python tools/resolve_schema.py --all --structured
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


def _try_fetch_relative_from_cache(file_path: Path) -> Path:
    """If file_path is inside the URL cache but doesn't exist, reconstruct
    the full URL from a previously cached URL's scheme+host and fetch it.
    Returns the (possibly updated) file_path."""
    try:
        file_path.relative_to(_URL_CACHE_DIR)  # only proceed if in cache
    except ValueError:
        return file_path
    for cached_url, cached_path in _URL_CACHE.items():
        try:
            file_rel = file_path.relative_to(_URL_CACHE_DIR)
            parsed = urlparse(cached_url if not cached_url.startswith("//") else "https:" + cached_url)
            target_url = f"{parsed.scheme}://{parsed.netloc}/{str(file_rel).replace(os.sep, '/')}"
            local_path = _fetch_url_schema(target_url)
            if local_path is not None:
                return local_path
        except (ValueError, Exception):
            continue
    return file_path


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
    entirely.  This prevents invalid schemas where, e.g., cdifCore's
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
                # Complete property definition → replace entirely, BUT
                # preserve accumulated contains constraints from prior merges
                base_has_contains = "contains" in result[k]
                base_has_accumulated = any(
                    isinstance(e, dict) and "contains" in e
                    for e in result[k].get("allOf", [])
                ) if not base_has_contains else False
                overlay_has_contains = "contains" in v

                if overlay_has_contains and (base_has_contains or base_has_accumulated):
                    overlay_schema = copy.deepcopy(v)
                    overlay_contains = overlay_schema.pop("contains")
                    # Collect existing contains entries
                    accumulated = []
                    if base_has_contains:
                        accumulated.append({"contains": result[k].pop("contains")})
                    if base_has_accumulated:
                        for e in result[k].get("allOf", []):
                            if isinstance(e, dict) and "contains" in e:
                                accumulated.append(e)
                    accumulated.append({"contains": overlay_contains})
                    # Merge non-contains parts (overlay wins)
                    result[k] = overlay_schema
                    result[k]["allOf"] = accumulated
                else:
                    result[k] = copy.deepcopy(v)
            elif k == "properties":
                result[k] = _deep_merge_inner(result[k], v, in_properties=True)
            elif k == "contains":
                # Both base and overlay have contains — accumulate as allOf entries
                # so that both constraints are enforced (e.g., multiple conformsTo URIs)
                base_contains = result.pop("contains")
                overlay_contains = copy.deepcopy(v)
                residual = result.get("allOf", [])
                residual.append({"contains": base_contains})
                residual.append({"contains": overlay_contains})
                result["allOf"] = residual
            else:
                result[k] = _deep_merge_inner(result[k], v, in_properties=False)
        elif k == "contains" and isinstance(v, dict):
            # Base has no contains but overlay does — check if base already has
            # accumulated contains in allOf from previous merges
            existing_allof = result.get("allOf", [])
            has_accumulated = any(
                isinstance(e, dict) and "contains" in e for e in existing_allof
            )
            if has_accumulated:
                existing_allof.append({"contains": copy.deepcopy(v)})
            else:
                result[k] = copy.deepcopy(v)
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
        file_path = _try_fetch_relative_from_cache(file_path)
    if not file_path.exists():
        return {"$comment": f"file not found: {file_path}"}

    # For cross-file $defs fragment refs, resolve the defs from the raw schema
    # before resolve_file strips them.
    if fragment:
        parts = fragment.lstrip("/").split("/")
        if len(parts) >= 2 and parts[0] == "$defs":
            raw_schema = load_schema_file(file_path.resolve())
            if isinstance(raw_schema, dict) and "$defs" in raw_schema:
                canonical = file_path.resolve()
                file_seen = seen | {canonical}
                raw_defs = raw_schema["$defs"]
                resolved_defs = {}
                for def_name, def_schema in raw_defs.items():
                    resolved_defs[def_name] = resolve_node(
                        def_schema, canonical.parent, {}, file_seen
                    )
                for def_name in list(resolved_defs.keys()):
                    resolved_defs[def_name] = _inline_unresolved_defs(
                        resolved_defs[def_name], resolved_defs, canonical.parent, file_seen
                    )
                target_name = parts[1]
                if target_name in resolved_defs:
                    return copy.deepcopy(resolved_defs[target_name])
            return {"$comment": f"could not resolve fragment {fragment} in {file_path}"}

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
# Structured mode: resolve with $defs preserved
# ---------------------------------------------------------------------------

def _derive_def_name(file_path: Path) -> str:
    """Derive a PascalCase $def name from a schema file path.

    Uses the parent directory name (e.g., .../identifier/schema.yaml -> Identifier,
    .../cdifCatalogRecord/schema.yaml -> CdifCatalogRecord).
    """
    name = file_path.resolve().parent.name
    # PascalCase: split on non-alpha, capitalise each part
    import re
    parts = re.split(r'[_\-]+', name)
    return "".join(p[0].upper() + p[1:] if p else "" for p in parts)


def _collect_defs_from_bb(bb_path: Path, global_defs: dict, file_to_def: dict,
                          visited: set):
    """Collect $defs from a single building block schema file.

    Populates global_defs (defName -> canonical Path) and file_to_def (canonical Path -> defName).
    Only promotes $defs whose value is an external file $ref (not inline schemas).
    Then recursively scans each resolved type BB for its own $defs and inline $refs.
    """
    canonical = bb_path.resolve()
    if canonical in visited:
        return
    visited.add(canonical)

    schema = load_schema_file(canonical)
    if not isinstance(schema, dict):
        return

    defs = schema.get("$defs", {})
    for def_name, def_schema in defs.items():
        if not isinstance(def_schema, dict):
            continue
        ref = def_schema.get("$ref")
        if ref and isinstance(ref, str) and not ref.startswith("#"):
            # External file ref — this is a promotable $def
            if _is_url(ref):
                continue  # skip URL refs for structured mode
            ref_path = (canonical.parent / ref.split("#")[0]).resolve()
            if ref_path in file_to_def:
                # Already registered — just ensure consistent name
                continue
            global_defs[def_name] = ref_path
            file_to_def[ref_path] = def_name
            # Recursively collect from the target file too
            if ref_path.exists():
                _collect_defs_from_bb(ref_path, global_defs, file_to_def, visited)
        # else: inline schema (like action's target_type) — skip

    # Also scan the schema body for inline $refs to other BB files
    _scan_inline_refs(schema, canonical.parent, file_to_def, global_defs, visited)


def _scan_inline_refs(node: Any, base_dir: Path, file_to_def: dict,
                      global_defs: dict, visited: set):
    """Walk a schema node looking for $ref to external files not yet in file_to_def.

    When found, adds them to global_defs/file_to_def and recursively scans them.
    This catches cases like person -> ../identifier/schema.yaml.
    """
    if isinstance(node, dict):
        if "$ref" in node:
            ref = node["$ref"]
            if isinstance(ref, str) and not ref.startswith("#") and not _is_url(ref):
                ref_file = ref.split("#")[0]
                ref_path = (base_dir / ref_file).resolve()
                if ref_path not in file_to_def and ref_path.exists():
                    def_name = _derive_def_name(ref_path)
                    # Avoid name collisions
                    if def_name in global_defs and global_defs[def_name] != ref_path:
                        # Append parent dir for disambiguation
                        def_name = _derive_def_name(ref_path.parent.parent / ref_path.parent.name / ref_path.name)
                    global_defs[def_name] = ref_path
                    file_to_def[ref_path] = def_name
                    _collect_defs_from_bb(ref_path, global_defs, file_to_def, visited)
            return  # don't recurse into $ref node's other keys for scanning
        for v in node.values():
            _scan_inline_refs(v, base_dir, file_to_def, global_defs, visited)
    elif isinstance(node, list):
        for item in node:
            _scan_inline_refs(item, base_dir, file_to_def, global_defs, visited)


def collect_global_defs(schema_path: Path) -> tuple[dict, dict]:
    """Phase 1: Collect all global $defs from a schema and its composing BBs.

    For profiles (top-level allOf of $refs), collects from each composing BB.
    For non-profiles, collects from the schema itself.

    Returns (global_defs: {name: Path}, file_to_def: {Path: name}).
    """
    schema = load_schema_file(schema_path.resolve())
    global_defs = {}    # defName -> canonical file path
    file_to_def = {}    # canonical file path -> defName
    visited = set()

    # Check if this is a profile (top-level allOf with $refs)
    all_of = schema.get("allOf", [])
    composing_bbs = []
    for entry in all_of:
        if isinstance(entry, dict) and "$ref" in entry:
            ref = entry["$ref"]
            if isinstance(ref, str) and not ref.startswith("#"):
                bb_path = (schema_path.resolve().parent / ref).resolve()
                if bb_path.exists():
                    composing_bbs.append(bb_path)

    if composing_bbs:
        # Profile: collect from each composing BB
        for bb_path in composing_bbs:
            _collect_defs_from_bb(bb_path, global_defs, file_to_def, visited)
    else:
        # Non-profile: collect from the schema itself
        _collect_defs_from_bb(schema_path.resolve(), global_defs, file_to_def, visited)

    return global_defs, file_to_def


def _resolve_node_structured(node: Any, base_dir: Path, local_defs: dict,
                             file_to_def: dict, seen: set) -> Any:
    """Phase 2 node walker: resolve $refs but emit #/$defs/X for known types.

    - External file $refs whose target is in file_to_def -> {"$ref": "#/$defs/Name"}
    - Fragment-only $refs (#/$defs/X) where X maps to a known file -> {"$ref": "#/$defs/GlobalName"}
    - Internal $defs (not in file_to_def) -> resolved inline normally
    - Everything else -> recursed into
    """
    if isinstance(node, dict):
        if "$ref" in node:
            ref = node["$ref"]
            siblings = {k: v for k, v in node.items() if k != "$ref"}

            resolved_ref = _resolve_ref_structured(ref, base_dir, local_defs,
                                                    file_to_def, seen)

            if siblings:
                siblings = _resolve_node_structured(siblings, base_dir, local_defs,
                                                     file_to_def, seen)
                if isinstance(resolved_ref, dict) and "$ref" not in resolved_ref:
                    resolved_ref = deep_merge(resolved_ref, siblings)
                elif isinstance(resolved_ref, dict) and "$ref" in resolved_ref:
                    # $ref with siblings: wrap in allOf
                    return {"allOf": [resolved_ref, siblings]}
            return resolved_ref

        result = {}
        for k, v in node.items():
            if k == "$defs":
                continue  # Strip $defs; they're promoted to global
            result[k] = _resolve_node_structured(v, base_dir, local_defs,
                                                  file_to_def, seen)
        return result

    elif isinstance(node, list):
        return [_resolve_node_structured(item, base_dir, local_defs,
                                          file_to_def, seen) for item in node]
    return node


def _resolve_ref_structured(ref: str, base_dir: Path, local_defs: dict,
                             file_to_def: dict, seen: set) -> Any:
    """Resolve a $ref, returning #/$defs/X for known types or inline content."""
    if ref == "#":
        return {"$comment": "circular-ref"}

    if ref.startswith("#/"):
        # Fragment-only ref (e.g., #/$defs/Identifier)
        pointer = ref[1:]
        parts = pointer.lstrip("/").split("/")
        if len(parts) == 2 and parts[0] == "$defs" and parts[1] in local_defs:
            local_def = local_defs[parts[1]]
            # Check if this local def points to an external file in file_to_def
            if isinstance(local_def, dict) and "$ref" in local_def:
                inner_ref = local_def["$ref"]
                if isinstance(inner_ref, str) and not inner_ref.startswith("#"):
                    ref_path = (base_dir / inner_ref.split("#")[0]).resolve()
                    if ref_path in file_to_def:
                        return {"$ref": f"#/$defs/{file_to_def[ref_path]}"}
            # Check if the def name itself matches a known global def name
            # (defs may already be resolved)
            if parts[1] in local_defs:
                raw = local_defs[parts[1]]
                if isinstance(raw, dict) and "$ref" in raw:
                    inner_ref = raw["$ref"]
                    if isinstance(inner_ref, str) and not inner_ref.startswith("#"):
                        ref_path = (base_dir / inner_ref.split("#")[0]).resolve()
                        if ref_path in file_to_def:
                            return {"$ref": f"#/$defs/{file_to_def[ref_path]}"}
                # Inline def (not external) — resolve normally
                return _resolve_node_structured(copy.deepcopy(raw), base_dir,
                                                local_defs, file_to_def, seen)
        return {"$comment": f"unresolved fragment ref: {ref}"}

    # File ref, possibly with fragment
    if "#" in ref:
        file_part, fragment = ref.split("#", 1)
    else:
        file_part, fragment = ref, None

    if _is_url(file_part):
        # URL refs: fall back to full inline resolution
        local_path = _fetch_url_schema(file_part)
        if local_path is None:
            return {"$comment": f"failed to fetch URL: {file_part}"}
        file_path = local_path
    else:
        file_path = (base_dir / file_part).resolve()

    if not file_path.exists():
        file_path = _try_fetch_relative_from_cache(file_path)
    if not file_path.exists():
        return {"$comment": f"file not found: {file_path}"}

    # If the target file (without fragment) is a known $def, emit a $ref
    if not fragment and file_path in file_to_def:
        return {"$ref": f"#/$defs/{file_to_def[file_path]}"}

    # For cross-file fragment refs to $defs
    if fragment:
        parts = fragment.lstrip("/").split("/")
        if len(parts) >= 2 and parts[0] == "$defs":
            raw_schema = load_schema_file(file_path)
            if isinstance(raw_schema, dict) and "$defs" in raw_schema:
                target_name = parts[1]
                target_def = raw_schema["$defs"].get(target_name)
                if isinstance(target_def, dict) and "$ref" in target_def:
                    inner_ref = target_def["$ref"]
                    if isinstance(inner_ref, str) and not inner_ref.startswith("#"):
                        ref_path = (file_path.parent / inner_ref).resolve()
                        if ref_path in file_to_def:
                            return {"$ref": f"#/$defs/{file_to_def[ref_path]}"}
            # Fall through to full resolution
            return resolve_file(file_path, seen)

    # Not a known def — resolve fully with def-awareness
    return resolve_def_aware(file_path, file_to_def, seen)


def resolve_def_aware(path: Path, file_to_def: dict, seen: set) -> dict:
    """Phase 2: Resolve a schema file with def-awareness.

    Like resolve_file but emits #/$defs/X refs for known types instead of inlining.
    """
    canonical = path.resolve()
    if canonical in seen:
        return {"$comment": f"circular ref to {canonical}"}
    seen = seen | {canonical}

    schema = load_schema_file(canonical)
    if not isinstance(schema, dict):
        return schema

    # Build local defs dict (raw, unresolved) for fragment ref lookup
    local_defs = schema.get("$defs", {})

    resolved = _resolve_node_structured(schema, canonical.parent, local_defs,
                                         file_to_def, seen)

    # Remove $defs (already stripped by _resolve_node_structured, but just in case)
    if isinstance(resolved, dict):
        resolved.pop("$defs", None)

    return resolved


def merge_profile_structured(profile_path: Path, global_defs: dict,
                              file_to_def: dict) -> dict:
    """Phase 3: Merge composing BBs for a profile, preserving $defs references.

    Returns the merged schema with properties, allOf constraints, and $defs.
    """
    schema = load_schema_file(profile_path.resolve())
    base_dir = profile_path.resolve().parent

    top_all_of = schema.get("allOf", [])
    merged_properties = {}
    constraint_entries = []  # allOf entries that aren't composing BB refs

    for entry in top_all_of:
        if isinstance(entry, dict) and "$ref" in entry:
            ref = entry["$ref"]
            if isinstance(ref, str) and not ref.startswith("#"):
                bb_path = (base_dir / ref).resolve()
                if bb_path.exists():
                    # Resolve the BB with def-awareness
                    resolved_bb = resolve_def_aware(bb_path, file_to_def, seen=set())

                    # Extract properties and merge
                    bb_props = resolved_bb.get("properties", {})
                    merged_properties = _deep_merge_inner(merged_properties, bb_props,
                                                          in_properties=True)

                    # Process allOf entries from the BB: merge properties,
                    # collect non-property constraints
                    bb_allof = resolved_bb.get("allOf", [])
                    for constraint in bb_allof:
                        if isinstance(constraint, dict) and "properties" in constraint:
                            # Merge properties from allOf sub-entries
                            sub_props = constraint.get("properties", {})
                            merged_properties = _deep_merge_inner(
                                merged_properties, sub_props, in_properties=True)
                            # Keep non-properties parts as constraints
                            non_prop = {k: v for k, v in constraint.items()
                                        if k != "properties"}
                            if non_prop:
                                constraint_entries.append(non_prop)
                        else:
                            constraint_entries.append(constraint)

                    # Collect top-level type, required, etc. that aren't properties/allOf
                    for k, v in resolved_bb.items():
                        if k not in ("properties", "allOf", "$schema", "type",
                                     "title", "description"):
                            # Merge other top-level keys (like contains constraints)
                            if k not in merged_properties:
                                merged_properties[k] = v
                    continue

        # Non-$ref allOf entries are constraint entries
        if isinstance(entry, dict):
            resolved_entry = _resolve_node_structured(entry, base_dir,
                                                       schema.get("$defs", {}),
                                                       file_to_def, set())
            constraint_entries.append(resolved_entry)

    # Resolve global $defs
    resolved_defs = {}
    for def_name, def_path in global_defs.items():
        resolved_defs[def_name] = resolve_def_aware(def_path, file_to_def, seen=set())

    # Build output schema
    result = {}
    if "$schema" in schema:
        result["$schema"] = schema["$schema"]
    result["type"] = schema.get("type", "object")
    if "title" in schema:
        result["title"] = schema["title"]
    if "description" in schema:
        result["description"] = schema["description"]

    if merged_properties:
        result["properties"] = merged_properties

    if constraint_entries:
        result["allOf"] = constraint_entries

    if resolved_defs:
        result["$defs"] = resolved_defs

    return result


def _merge_non_profile_structured(schema_path: Path, global_defs: dict,
                                   file_to_def: dict) -> dict:
    """Resolve a non-profile BB with def-awareness and attach global $defs."""
    resolved = resolve_def_aware(schema_path.resolve(), file_to_def, seen=set())

    # Resolve global $defs
    resolved_defs = {}
    for def_name, def_path in global_defs.items():
        resolved_defs[def_name] = resolve_def_aware(def_path, file_to_def, seen=set())

    if resolved_defs:
        resolved["$defs"] = resolved_defs

    return resolved


def count_def_refs(schema: Any) -> dict:
    """Phase 4: Count occurrences of {"$ref": "#/$defs/X"} in the schema."""
    counts = {}
    _count_refs_walk(schema, counts)
    return counts


def _count_refs_walk(node: Any, counts: dict):
    if isinstance(node, dict):
        if "$ref" in node:
            ref = node["$ref"]
            if isinstance(ref, str) and ref.startswith("#/$defs/"):
                name = ref[len("#/$defs/"):]
                counts[name] = counts.get(name, 0) + 1
        for v in node.values():
            _count_refs_walk(v, counts)
    elif isinstance(node, list):
        for item in node:
            _count_refs_walk(item, counts)


def inline_low_use_defs(schema: dict, threshold: int = 2) -> dict:
    """Phase 5: Inline $defs used <= threshold times. Iterate until stable.

    Inlines one def per pass to avoid dangling refs when an inlined def's
    content references another def that was removed in the same pass.
    """
    schema = copy.deepcopy(schema)
    while True:
        counts = count_def_refs(schema)
        defs = schema.get("$defs", {})
        # Find one def to inline
        to_inline = None
        for name in list(defs):
            if counts.get(name, 0) <= threshold:
                to_inline = name
                break
        if to_inline is None:
            break
        replacement = defs.pop(to_inline)
        schema = _replace_ref_everywhere(schema, to_inline, replacement)
        if not defs:
            schema.pop("$defs", None)
            break
    return schema


def _replace_ref_everywhere(node: Any, def_name: str, replacement: Any) -> Any:
    """Replace all {"$ref": "#/$defs/<def_name>"} with the replacement content."""
    if isinstance(node, dict):
        if "$ref" in node and node["$ref"] == f"#/$defs/{def_name}":
            siblings = {k: v for k, v in node.items() if k != "$ref"}
            result = copy.deepcopy(replacement)
            if siblings and isinstance(result, dict):
                result = deep_merge(result, siblings)
            return result
        return {k: _replace_ref_everywhere(v, def_name, replacement)
                for k, v in node.items()}
    elif isinstance(node, list):
        return [_replace_ref_everywhere(item, def_name, replacement) for item in node]
    return node


def _is_profile_schema(schema: dict) -> bool:
    """Check if a schema is a profile (top-level allOf with external $refs only)."""
    all_of = schema.get("allOf", [])
    if not all_of:
        return False
    # A profile has allOf entries that are all external $refs
    has_ext_ref = False
    for entry in all_of:
        if isinstance(entry, dict) and "$ref" in entry:
            ref = entry["$ref"]
            if isinstance(ref, str) and not ref.startswith("#"):
                has_ext_ref = True
    # Also check: no properties at top level (profiles just compose BBs)
    return has_ext_ref and "properties" not in schema


def resolve_structured(schema_path: Path) -> dict:
    """Orchestrator: produce a structured schema with $defs.

    Phase 1: collect global $defs
    Phase 2-3: resolve/merge with def-awareness
    Phase 4-5: count and inline low-use defs
    Phase 6: strip metadata, output
    """
    schema_path = schema_path.resolve()
    schema = load_schema_file(schema_path)

    # Phase 1: collect global defs
    global_defs, file_to_def = collect_global_defs(schema_path)

    print(f"  Collected {len(global_defs)} global $defs", file=sys.stderr)
    for name, path in sorted(global_defs.items()):
        rel = path.relative_to(REPO_ROOT) if path.is_relative_to(REPO_ROOT) else path
        print(f"    {name}: {rel}", file=sys.stderr)

    # Phase 2-3: resolve/merge
    if _is_profile_schema(schema):
        result = merge_profile_structured(schema_path, global_defs, file_to_def)
    else:
        result = _merge_non_profile_structured(schema_path, global_defs, file_to_def)

    # Phase 4-5: inline low-use defs
    result = inline_low_use_defs(result, threshold=2)

    # Phase 6: strip metadata
    result = strip_metadata_keys(result, is_root=True)

    return result


def _structured_output_name(schema_path: Path) -> str:
    """Derive the structured output filename from the schema's parent directory.

    E.g., .../CDIFDiscovery/schema.yaml -> CDIFDiscoveryStructuredSchema.json
          .../cdifCore/schema.yaml       -> cdifCoreStructuredSchema.json
    """
    bb_name = schema_path.resolve().parent.name
    return f"{bb_name}StructuredSchema.json"


def resolve_and_write_structured(schema_path: Path) -> Path:
    """Resolve structured and write <bbName>StructuredSchema.json next to schema. Returns output path."""
    structured = resolve_structured(schema_path)
    out_name = _structured_output_name(schema_path)
    out_path = schema_path.parent / out_name
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(json.dumps(structured, indent=2, ensure_ascii=False) + "\n")
    return out_path


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
    parser.add_argument(
        "--structured",
        action="store_true",
        help="Produce structured output with $defs and merged allOf (writes structuredSchema.json)",
    )
    args = parser.parse_args()

    if args.all:
        schemas = find_all_schemas_with_external_refs()
        print(f"Found {len(schemas)} building blocks with external $refs", file=sys.stderr)
        for schema_path in schemas:
            rel = schema_path.relative_to(REPO_ROOT)
            if args.structured:
                out_path = resolve_and_write_structured(schema_path)
                print(f"  {rel} -> {out_path.name}", file=sys.stderr)
            else:
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

    if args.structured:
        structured = resolve_structured(schema_path)
        output_json = json.dumps(structured, indent=2, ensure_ascii=False) + "\n"

        if args.output:
            out_path = args.output
        else:
            out_path = schema_path.parent / _structured_output_name(schema_path)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(output_json)
        print(f"Wrote structured schema: {out_path}", file=sys.stderr)

        # Report stats
        defs = structured.get("$defs", {})
        print(f"  $defs: {len(defs)} ({', '.join(sorted(defs.keys()))})",
              file=sys.stderr)
        print(f"  Size: {len(output_json):,} bytes", file=sys.stderr)
        return

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
