#!/usr/bin/env python3
"""
Validate all example JSON files against their resolved schemas.

Validates against the committed resolvedSchema.json beside each schema.yaml --
the snapshot this repo actually ships -- so a run is deterministic and offline.

--live re-resolves schema.yaml instead, following every $ref over the network.
That used to be the only behaviour, and it made this suite a live test of other
people's repos: a cross-repo $ref restructure upstream turned the run red with
no commit here, and a green run said "matches upstream right now", not "matches
what we ship". Use --live deliberately, to see whether upstream has moved; use
`resolve_schema.py --all --check` to get that answer as a list of files.

A block with no resolvedSchema.json falls back to resolving, since there is no
snapshot to check against; the summary reports how many did.

Usage:
    python tools/validate_examples.py            # validate against the snapshot
    python tools/validate_examples.py --live     # re-resolve $refs over the network
    python tools/validate_examples.py --verbose  # show pass/fail for each
    python tools/validate_examples.py --filter person  # only matching paths
"""

import argparse
import contextlib
import io
import json
import sys
import yaml
from pathlib import Path

# tools/resolve_schema.py -- the same resolver that writes resolvedSchema.json,
# so the gate validates the artifact that actually ships. Previously this used
# the frozen root schema_resolver.py, which resolves some schemas differently:
# an example could pass here and be invalid against the published block, or the
# reverse. See agents.md, "One resolver, not two".
_repo_root = str(Path(__file__).resolve().parent.parent)
sys.path.insert(0, _repo_root)

import importlib.util
_tools_spec = importlib.util.spec_from_file_location(
    "tools_resolve_schema",
    str(Path(__file__).resolve().parent / "resolve_schema.py"))
_tools_resolver = importlib.util.module_from_spec(_tools_spec)
_tools_spec.loader.exec_module(_tools_resolver)
_structured_resolve = _tools_resolver.resolve_structured
_fallback_resolve_file = _tools_resolver.resolve_file
_fallback_strip = _tools_resolver.strip_metadata_keys

from jsonschema import Draft202012Validator


REPO_ROOT = Path(__file__).resolve().parent.parent
SOURCES_DIR = REPO_ROOT / "_sources"


def find_example_schema_pairs():
    """Find all (example.json, schema.yaml) pairs in the sources tree.

    Two sources are merged and de-duplicated:
      1. every ``example*.json`` sitting beside a ``schema.yaml`` (the fast
         default), and
      2. every ``*.json`` registered as a snippet ``ref`` in an
         ``examples.yaml`` — this catches examples whose filename does not
         match the ``example*`` glob (e.g. ``CDIF-XAS-Full.json``), validated
         against the ``schema.yaml`` of the block that registers them.

    Negative-test fixtures (referenced from ``tests.yaml``, not
    ``examples.yaml``) are intentionally not picked up.
    """
    pairs = {}  # (example_path, schema_path) -> None; dict preserves order + dedupes

    def add(example_path: Path, schema_path: Path):
        if example_path.exists() and schema_path.exists():
            pairs.setdefault((example_path.resolve(), schema_path.resolve()), None)

    # 1. example*.json glob
    for example_path in sorted(SOURCES_DIR.rglob("example*.json")):
        add(example_path, example_path.parent / "schema.yaml")

    # 2. examples.yaml snippet refs
    for examples_yaml in sorted(SOURCES_DIR.rglob("examples.yaml")):
        try:
            entries = yaml.safe_load(examples_yaml.read_text(encoding="utf-8")) or []
        except Exception:
            continue
        if not isinstance(entries, list):
            continue
        schema_path = examples_yaml.parent / "schema.yaml"
        for entry in entries:
            if not isinstance(entry, dict):
                continue
            for snippet in entry.get("snippets", []) or []:
                ref = snippet.get("ref") if isinstance(snippet, dict) else None
                if isinstance(ref, str) and ref.endswith(".json"):
                    add(examples_yaml.parent / ref, schema_path)

    return sorted(pairs.keys())


def resolve_for_validation(schema_path: Path) -> dict:
    """Resolve a schema file into a JSON Schema dict for validation.

    Uses resolve_schema.py's structured resolver -- the code that writes
    resolvedSchema.json -- so an example is checked against the schema the
    published building block carries. Falls back to the same module's inline
    resolver when recursion defeats structured resolution.
    """
    try:
        # resolve_structured narrates its work on stderr (24 print sites);
        # useful when regenerating, noise that buries the pass/fail report here.
        # Its fetch warnings are silenced with it -- acceptable because every
        # $ref this repo resolves is local.
        with contextlib.redirect_stderr(io.StringIO()), \
                contextlib.redirect_stdout(io.StringIO()):
            resolved = _structured_resolve(schema_path.resolve())
        resolved.pop("$schema", None)
        return resolved
    except RecursionError:
        resolved = _fallback_resolve_file(schema_path.resolve(), set())
        _fallback_strip(resolved)
        resolved.pop("$schema", None)
        return resolved


def load_schema(schema_path: Path, live: bool):
    """Return (schema, source) for validation.

    source is "snapshot" when the committed resolvedSchema.json was used and
    "resolved" when the schema was re-resolved over the network -- either
    because --live was passed or because the block has no snapshot yet.
    """
    if not live:
        snapshot = schema_path.parent / "resolvedSchema.json"
        if snapshot.exists():
            schema = json.loads(snapshot.read_text(encoding="utf-8"))
            schema.pop("$schema", None)
            return schema, "snapshot"
    return resolve_for_validation(schema_path), "resolved"


def validate_example(example_path: Path, schema: dict):
    """Validate a JSON example against a resolved schema. Returns list of error strings."""
    # encoding is explicit: without it Python uses the platform default, which
    # is cp1252 on Windows, and an example carrying any non-ASCII character
    # (a degree sign, an accented author name) fails to open at all -- reported
    # as an error rather than as the pass it is.
    with open(example_path, encoding="utf-8") as f:
        instance = json.load(f)

    validator = Draft202012Validator(schema)
    errors = []
    for error in validator.iter_errors(instance):
        path = "/".join(str(p) for p in error.absolute_path) or "(root)"
        errors.append(f"  {path}: {error.message[:200]}")
    return errors


def main():
    parser = argparse.ArgumentParser(description="Validate all example JSON files against their schemas.")
    parser.add_argument("--verbose", "-v", action="store_true", help="Show pass/fail for each example")
    parser.add_argument("--filter", "-f", type=str, default="", help="Only validate paths containing this string")
    parser.add_argument("--live", action="store_true",
                        help="Re-resolve $refs over the network instead of "
                             "using the committed resolvedSchema.json")
    args = parser.parse_args()

    pairs = find_example_schema_pairs()
    if args.filter:
        pairs = [(e, s) for e, s in pairs if args.filter.lower() in str(e).lower()]

    passed = 0
    failed = 0
    errored = 0
    resolved_live = 0
    failures = []

    for example_path, schema_path in pairs:
        rel = example_path.relative_to(REPO_ROOT)
        try:
            schema, source = load_schema(schema_path, args.live)
            if source == "resolved":
                resolved_live += 1
            try:
                errors = validate_example(example_path, schema)
            except RecursionError:
                # Root resolver may produce circular $ref that jsonschema
                # can't handle; fall back to tools resolver which inlines fully
                resolved = _fallback_resolve_file(schema_path.resolve(), set())
                _fallback_strip(resolved)
                resolved.pop("$schema", None)
                errors = validate_example(example_path, resolved)
            if errors:
                failed += 1
                failures.append((rel, errors))
                if args.verbose:
                    print(f"FAIL {rel}")
                    for e in errors[:5]:
                        print(e)
            else:
                passed += 1
                if args.verbose:
                    print(f"PASS {rel}")
        except Exception as ex:
            errored += 1
            failures.append((rel, [f"  {type(ex).__name__}: {str(ex)[:200]}"]))
            if args.verbose:
                print(f"ERROR {rel}: {type(ex).__name__}: {str(ex)[:150]}")

    print(f"\n{'='*60}")
    print(f"Results: {passed} passed, {failed} failed, {errored} errors (of {len(pairs)} total)")
    # Say which schema each result came from. "17 passed" means something
    # different offline than it does against a repo that moved this morning.
    if args.live:
        print(f"Source: re-resolved over the network (--live)")
    elif resolved_live:
        print(f"Source: committed resolvedSchema.json, except {resolved_live} "
              f"with no snapshot, which were resolved")
    else:
        print(f"Source: committed resolvedSchema.json")
    print(f"{'='*60}")

    if failures:
        print("\nFailures:")
        for rel, errors in failures:
            print(f"\n{rel}:")
            for e in errors[:5]:
                print(e)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
