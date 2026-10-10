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
_find_unresolved = _tools_resolver.find_unresolved

from jsonschema import Draft202012Validator


REPO_ROOT = Path(__file__).resolve().parent.parent
SOURCES_DIR = REPO_ROOT / "_sources"

# SHACL shapes for remote blocks, vendored so a run stays offline. Kept in its
# own tree and lock because resolve_schema.py rewrites vendor/remote-lock.json
# from whatever it fetched, which would drop any pin added here.
SHAPES_DIR = REPO_ROOT / "vendor" / "shapes"
SHAPES_LOCK = REPO_ROOT / "vendor" / "shapes-lock.json"
REMOTE_LOCK = REPO_ROOT / "vendor" / "remote-lock.json"


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


class UnresolvedRefs(Exception):
    """A schema resolved with $refs left as placeholders.

    resolve_schema.py substitutes {"$comment": "failed to fetch URL: ..."} for a
    $ref it cannot resolve. That is an empty schema, and an empty schema accepts
    anything, so validating against it reports a pass for every example whose
    constraints lived in the part that went missing. --all already refuses to
    WRITE such a schema; this suite must equally refuse to JUDGE against one.
    """


def _require_resolved(schema: dict, schema_path: Path) -> dict:
    """Return the schema, or raise if any $ref resolved to a placeholder."""
    unresolved = _find_unresolved(schema)
    if not unresolved:
        return schema
    # Action first: main() truncates the message, and the fix matters more than
    # the inventory. `resolve_schema.py --all` prints every unresolved ref.
    where, _why = unresolved[0]
    raise UnresolvedRefs(
        f"{len(unresolved)} $ref(s) unresolved, so this schema accepts anything "
        f"they stand for. Run `resolve_schema.py --refresh-remote` to vendor "
        f"remote refs, or --all to list them. First: {where}"
    )


def resolve_for_validation(schema_path: Path) -> dict:
    """Resolve a schema file into a JSON Schema dict for validation.

    Uses resolve_schema.py's structured resolver -- the code that writes
    resolvedSchema.json -- so an example is checked against the schema the
    published building block carries. Falls back to the same module's inline
    resolver when recursion defeats structured resolution.

    Raises UnresolvedRefs if resolution left placeholders behind.
    """
    try:
        # resolve_structured narrates its work on stderr (24 print sites);
        # useful when regenerating, noise that buries the pass/fail report here.
        # Fetch failures are silenced with it, which is why the result is
        # checked for placeholders below rather than trusted: a repo that $refs
        # another register by URL resolves nothing locally.
        with contextlib.redirect_stderr(io.StringIO()), \
                contextlib.redirect_stdout(io.StringIO()):
            resolved = _structured_resolve(schema_path.resolve())
        resolved.pop("$schema", None)
        return _require_resolved(resolved, schema_path)
    except RecursionError:
        resolved = _fallback_resolve_file(schema_path.resolve(), set())
        _fallback_strip(resolved)
        resolved.pop("$schema", None)
        return _require_resolved(resolved, schema_path)


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


SEVERITIES = ("Violation", "Warning", "Info")


def refresh_shapes():
    """Fetch the rules.shacl beside each vendored schema and pin it.

    The URL set is derived from vendor/remote-lock.json rather than listed here,
    so vendoring a new remote block brings its shapes along on the next refresh.
    Not every block has shapes; a 404 is normal and simply means none.
    """
    import hashlib
    from urllib.error import HTTPError, URLError
    from urllib.parse import urlparse
    from urllib.request import urlopen

    if not REMOTE_LOCK.exists():
        print(f"No {REMOTE_LOCK.relative_to(REPO_ROOT)} — run "
              f"`resolve_schema.py --all --refresh-remote` first.", file=sys.stderr)
        return 1

    lock, fetched, missing = {}, 0, 0
    for schema_url in sorted(json.loads(REMOTE_LOCK.read_text(encoding="utf-8"))):
        url = schema_url.rsplit("/", 1)[0] + "/rules.shacl"
        parsed = urlparse(url)
        dest = SHAPES_DIR / parsed.netloc / parsed.path.strip("/")
        try:
            with urlopen(url, timeout=30) as resp:
                data = resp.read()
        except HTTPError as e:
            if e.code == 404:
                missing += 1
                continue
            print(f"  WARNING: {url}: {e}", file=sys.stderr)
            continue
        except URLError as e:
            print(f"  WARNING: {url}: {e}", file=sys.stderr)
            continue
        dest.parent.mkdir(parents=True, exist_ok=True)
        previous = dest.read_bytes() if dest.exists() else None
        dest.write_bytes(data)
        if previous is not None and previous != data:
            print(f"  CHANGED upstream: {url}", file=sys.stderr)
        lock[url] = {"bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}
        fetched += 1

    SHAPES_LOCK.parent.mkdir(parents=True, exist_ok=True)
    SHAPES_LOCK.write_text(json.dumps(lock, indent=2, sort_keys=True) + "\n",
                           encoding="utf-8")
    print(f"Pinned {fetched} shape file(s) in "
          f"{SHAPES_DIR.relative_to(REPO_ROOT)} ({missing} block(s) have none)",
          file=sys.stderr)
    return 0


def load_shapes():
    """Parse each rules.shacl into its OWN graph -- this register's plus vendored.

    Returns (list of (label, graph), local_count, vendored_count), or
    (None, ...) if SHACL support is unavailable.

    One graph per file, never a union: the registers reuse shape URIs across
    files (cdifd:CDIFIdentifierShape appears in several), so merging them lands
    two sh:path values on one PropertyShape and pyshacl refuses the whole graph
    with a ShapeLoadError. Validating file by file is also what the
    bblocks-postprocess reports do, which keeps local results comparable to CI.
    """
    try:
        from rdflib import Graph
    except ImportError:
        return None, 0, 0
    local = sorted(SOURCES_DIR.rglob("rules.shacl"))
    vendored = sorted(SHAPES_DIR.rglob("rules.shacl")) if SHAPES_DIR.exists() else []
    graphs = {}
    for path in local + vendored:
        try:
            graph = Graph()
            graph.parse(path, format="turtle")
        except Exception as ex:
            print(f"  WARNING: unparsable shapes {path.name}: {ex}", file=sys.stderr)
            continue
        graphs[path] = graph
    return graphs, len(local), len(vendored)


def _refs_in(schema_path: Path):
    """Every $ref string in a schema file, fragments stripped."""
    try:
        text = schema_path.read_text(encoding="utf-8")
        doc = yaml.safe_load(text)
    except Exception:
        return
    stack = [doc]
    while stack:
        node = stack.pop()
        if isinstance(node, dict):
            for key, value in node.items():
                if key == "$ref" and isinstance(value, str):
                    yield value.split("#", 1)[0]
                else:
                    stack.append(value)
        elif isinstance(node, list):
            stack.extend(node)


def _ref_target(ref: str, from_schema: Path):
    """Local schema file a $ref points at, or None.

    A URL ref maps to its vendored copy under vendor/remote, so the walk follows
    a remote block's own relative refs the same way resolution does.
    """
    if not ref:
        return None
    if ref.startswith("//"):
        ref = "https:" + ref
    if ref.startswith(("http://", "https://")):
        from urllib.parse import urlparse
        parsed = urlparse(ref)
        return REPO_ROOT / "vendor" / "remote" / parsed.netloc / parsed.path.strip("/")
    return (from_schema.parent / ref).resolve()


def shape_closure(schema_path: Path, shapes: dict):
    """The rules.shacl files that apply to one block: its own plus every block
    reachable through its $refs.

    Scoped rather than "all shapes we have" because a register's shapes target
    types generically -- apply additionalProperty's rules to a block that never
    references it and you manufacture violations the published register does not
    report. bblocks-postprocess scopes the same way, so this keeps local output
    comparable with CI.
    """
    found, seen = [], set()
    stack = [schema_path.resolve()]
    while stack:
        current = stack.pop()
        if current in seen:
            continue
        seen.add(current)
        rules = current.parent / "rules.shacl"
        if rules in shapes and rules not in found:
            found.append(rules)
        # vendor/remote holds schemas; their shapes live in vendor/shapes
        if "vendor" in current.parts:
            mirrored = Path(str(current.parent).replace(
                str(REPO_ROOT / "vendor" / "remote"),
                str(SHAPES_DIR))) / "rules.shacl"
            if mirrored in shapes and mirrored not in found:
                found.append(mirrored)
        for ref in _refs_in(current):
            target = _ref_target(ref, current)
            if target and target.exists():
                stack.append(target)
    return found


def validate_shacl(example_path: Path, shapes, shape_files):
    """Validate one JSON-LD example against the shape graph.

    Returns {severity: [message, ...]}. A sh:Violation is a failure; Warning and
    Info are CDIF recommendations, reported but not fatal -- the postprocessor
    marks a report failed on any result at all, which buries the 20 findings
    that are actually wrong among the 26 that are advice.
    """
    from pyshacl import validate as shacl_validate
    from rdflib import Graph, RDF, Namespace

    SH = Namespace("http://www.w3.org/ns/shacl#")
    data = Graph()
    # An example with no inline @context needs the block's context.jsonld to
    # expand -- bblocks-postprocess calls this uplifting. Without it rdflib
    # keeps "schema:propertyID" as a RELATIVE IRI resolved against the file
    # path, the triple count looks healthy, and every shape targeting
    # http://schema.org/... matches nothing: SHACL reports a clean example that
    # the published register reports violations for.
    document = json.loads(example_path.read_text(encoding="utf-8"))
    if "@context" in document:
        data.parse(example_path, format="json-ld")
    else:
        context_file = example_path.parent / "context.jsonld"
        context = None
        if context_file.exists():
            context = json.loads(context_file.read_text(encoding="utf-8")).get("@context")
        data.parse(data=json.dumps(document), format="json-ld", context=context)

    found = {s: [] for s in SEVERITIES}
    for shape_path in shape_files:
        try:
            _conforms, results, _text = shacl_validate(
                data, shacl_graph=shapes[shape_path], advanced=True, inference="none")
        except Exception as ex:
            print(f"  WARNING: shapes {shape_path.parent.name} could not run: "
                  f"{type(ex).__name__}: {str(ex)[:90]}", file=sys.stderr)
            continue
        for result in results.subjects(RDF.type, SH.ValidationResult):
            name = str(results.value(result, SH.resultSeverity) or "").rsplit("#", 1)[-1]
            if name in found:
                message = results.value(result, SH.resultMessage)
                found[name].append(" ".join(str(message or "").split()))
    return found


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
    parser.add_argument("--no-shacl", action="store_true",
                        help="Skip the SHACL pass (JSON Schema only)")
    parser.add_argument("--refresh-shapes", action="store_true",
                        help="Fetch and pin the rules.shacl beside each "
                             "vendored schema, then exit")
    args = parser.parse_args()

    if args.refresh_shapes:
        return refresh_shapes()

    pairs = find_example_schema_pairs()
    if args.filter:
        pairs = [(e, s) for e, s in pairs if args.filter.lower() in str(e).lower()]

    passed = 0
    failed = 0
    errored = 0
    resolved_live = 0
    failures = []

    shapes, local_shapes, vendored_shapes = (None, 0, 0)
    shacl_totals = {s: 0 for s in SEVERITIES}
    shacl_failed = []
    if not args.no_shacl:
        shapes, local_shapes, vendored_shapes = load_shapes()
        if shapes is None:
            print("NOTE: rdflib/pyshacl not installed — SHACL pass skipped.",
                  file=sys.stderr)

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
                errors = validate_example(
                    example_path, _require_resolved(resolved, schema_path))
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

            if shapes is not None:
                sh = validate_shacl(example_path, shapes,
                                    shape_closure(schema_path, shapes))
                for sev in SEVERITIES:
                    shacl_totals[sev] += len(sh[sev])
                if sh["Violation"]:
                    shacl_failed.append((rel, sh["Violation"]))
                    if args.verbose:
                        print(f"  SHACL {len(sh['Violation'])} violation(s)")
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

    if shapes is not None:
        print(f"SHACL: {shacl_totals['Violation']} violation(s), "
              f"{shacl_totals['Warning']} warning(s), {shacl_totals['Info']} info "
              f"across {len(pairs)} example(s) "
              f"[{local_shapes} local + {vendored_shapes} vendored shape files]")
        if vendored_shapes == 0:
            print("       no vendored shapes — remote blocks' rules are not being "
                  "applied; run --refresh-shapes")
    print(f"{'='*60}")

    if shacl_failed:
        print("\nSHACL violations:")
        for rel, messages in shacl_failed:
            print(f"\n{rel}:")
            for m in sorted(set(messages))[:3]:
                print(f"  {m[:160]}")

    if failures:
        print("\nFailures:")
        for rel, errors in failures:
            print(f"\n{rel}:")
            for e in errors[:5]:
                print(e)
    if failures or shacl_failed:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
