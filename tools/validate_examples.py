#!/usr/bin/env python3
"""
Validate all example JSON files against their resolved schemas.

Uses tools/resolve_schema.py's resolver to fully inline $ref references before
validation, so $defs and cross-file references are handled correctly.

Usage:
    python tools/validate_examples.py           # validate all examples
    python tools/validate_examples.py --verbose  # show pass/fail for each
    python tools/validate_examples.py --filter person  # only matching paths
"""

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from resolve_schema import resolve_file, strip_metadata_keys

from jsonschema import Draft202012Validator


REPO_ROOT = Path(__file__).resolve().parent.parent
SOURCES_DIR = REPO_ROOT / "_sources"


def find_example_schema_pairs():
    """Find all (example.json, schema.yaml) pairs in the sources tree."""
    pairs = []
    for example_path in sorted(SOURCES_DIR.rglob("example*.json")):
        schema_path = example_path.parent / "schema.yaml"
        if schema_path.exists():
            pairs.append((example_path, schema_path))
    return pairs


def resolve_for_validation(schema_path: Path) -> dict:
    """Resolve a schema file into a fully-inlined JSON Schema dict."""
    resolved = resolve_file(schema_path.resolve(), seen=set())
    resolved = strip_metadata_keys(resolved, is_root=True)
    resolved.pop("$schema", None)
    return resolved


def validate_example(example_path: Path, schema: dict):
    """Validate a JSON example against a resolved schema. Returns list of error strings."""
    with open(example_path) as f:
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
    args = parser.parse_args()

    pairs = find_example_schema_pairs()
    if args.filter:
        pairs = [(e, s) for e, s in pairs if args.filter.lower() in str(e).lower()]

    passed = 0
    failed = 0
    errored = 0
    failures = []

    for example_path, schema_path in pairs:
        rel = example_path.relative_to(REPO_ROOT)
        try:
            schema = resolve_for_validation(schema_path)
            errors = validate_example(example_path, schema)
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
