# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

An [OGC Building Blocks](https://opengeospatial.github.io/bblocks/) register publishing modular
JSON Schema components for Deep-time Digital Earth (DDE) metadata. There is no application code —
the deliverables are schemas, JSON-LD contexts, and the generated register at
https://usgin.github.io/ddeBuildingBlocks/. Everything is JSON Schema 2020-12 over schema.org terms
in JSON-LD.

## Two-layer architecture

The whole repo is one composition pattern, and understanding it explains every file:

- **`_sources/DDEproperties/`** — *property* building blocks. Each defines a slice of DDE-specific
  constraints (`ddeCore`, `ddeResourceType`, `ddeCatalogRecord`, `ddeGeographicDataset`, `ddeImagery`).
- **`_sources/profiles/DDEProfiles/`** — *profile* building blocks, one per DDE resource type. Each
  composes property blocks and pins `schema:additionalType` to the codelist terms valid for that type.

Composition is plain JSON Schema: `allOf` with a relative `$ref` to another block's `schema.yaml`,
plus `$defs` entries holding absolute URL `$ref`s to the CDIF repo. Conditional composition uses
`if`/`then` on a codelist term — e.g. `DDEDataset` pulls in `ddeGeographicDataset` only when
`schema:termCode` is `geographicDataset`. `DDEImage` does the same for `map`.

Constraints are expressed almost entirely as `contains` + `minContains` over arrays of
`schema:DefinedTerm`, keyed on `schema:inDefinedTermSet` naming a DDE codelist:
`dde:codelist/{ResourceTypeCode, TopicCategoryCode, AcquisitionTypeCode, ServiceTypeCode}`. When
adding a resource-type profile, copy an existing one and change the `enum` of allowed `termCode`s —
the surrounding boilerplate is deliberately uniform.

`archive/deprecated/` holds superseded blocks (`DDEService`, `ddeServiceInfo`); it is outside
`_sources/` so the postprocessor ignores it.

## Source of truth and the generated chain

Each block directory holds hand-edited and generated files side by side. **Only `schema.yaml` and
the `.md`/`.jsonld`/example files are edited by hand:**

| File | Status | Produced by |
|---|---|---|
| `schema.yaml` | **source of truth** | hand-edited |
| `bblock.json`, `description.md`, `context.jsonld`, `examples.yaml`, `example*.json`, `rules.shacl` | source | hand-edited |
| `{blockName}Schema.json` | generated | `tools/regenerate_schema_json.py` |
| `resolvedSchema.json` | generated | `tools/resolve_schema.py` |
| `vendor/remote/`, `vendor/remote-lock.json` | generated | `tools/resolve_schema.py --refresh-remote` |
| `vendor/shapes/`, `vendor/shapes-lock.json` | generated | `tools/validate_examples.py --refresh-shapes` |
| `build/` | generated | CI (`bblocks-postprocess`), committed back to `main` |

The two vendor trees have separate locks on purpose: `resolve_schema.py --refresh-remote` rewrites
`vendor/remote-lock.json` from whatever it fetched, so shape pins kept in the same file would be
dropped the next time anyone re-pinned the schemas.

After editing any `schema.yaml`, regenerate both derived files or the published register goes stale
against the source.

`validate_examples.py` validates against the committed `resolvedSchema.json` by default, so a run is
deterministic and offline. `--live` re-resolves `schema.yaml` instead. Either way it refuses to
validate against a schema containing unresolved `$ref` placeholders — see below. It runs **two
layers**: JSON Schema and SHACL. The register checks both, so a change that satisfies the schemas can
still be wrong.

Do not hand-edit anything under `build/`. The CI postprocess job rewrites it and commits over your
changes ("Building blocks postprocessing" commits on `main` are the bot).

## Commands

```bash
python tools/regenerate_schema_json.py
```

Rewrites every `{blockName}Schema.json` from its `schema.yaml` (YAML→JSON plus `$ref` path rewriting).

```bash
python tools/resolve_schema.py --all
```

Re-inlines every `resolvedSchema.json`. Single block: `python tools/resolve_schema.py ddeCore`
(profiles only — a property block needs `--file _sources/DDEproperties/<name>/schema.yaml`). Writing
in place is the default; `--stdout` prints instead. **No network:** remote `$ref`s are read from
`vendor/remote/`, so this works offline and refuses to write a schema whose refs did not resolve —
a degraded artifact must not replace a good one.

```bash
python tools/resolve_schema.py --all --refresh-remote
```

The only command that touches the network. Fetches each remote `$ref`, rewrites `vendor/remote/`,
re-pins `vendor/remote-lock.json`, and prints `CHANGED upstream:` for anything that moved. Run it
deliberately; the diff to `vendor/` is the record of what upstream did.

```bash
python tools/validate_examples.py
```

Validates every `example*.json` against its block's **committed `resolvedSchema.json`** — this repo's
closest thing to a test suite, and offline. `--live` re-resolves from `schema.yaml` instead (still
offline, via `vendor/`); both should agree. `--verbose` for per-file results, `--filter ddeCore` to
narrow to one block (the filter matches on path, and is the way to "run a single test" here).

An unresolved `$ref` becomes `{"$comment": "failed to fetch URL: …"}`, which is an empty schema that
accepts anything. The suite therefore reports `UnresolvedRefs` as an **error** rather than a pass —
if you see that, `vendor/` is missing or incomplete and the fix is `--refresh-remote`.

Two cliffs make older green runs meaningless: a run before **2026-10-09** predates the
`UnresolvedRefs` check, and one before **2026-10-10** did not check SHACL at all.

### The SHACL pass

Every run ends with a line like:

```
SHACL: 0 violation(s), 19 warning(s), 7 info across 17 example(s) [15 local + 24 vendored shape files]
```

`sh:Violation` fails the run; `sh:Warning` and `sh:Info` are CDIF recommendations, reported but not
fatal. `--no-shacl` skips the pass; `--refresh-shapes` re-fetches and re-pins the shapes (the URL set
is derived from `vendor/remote-lock.json` — the `rules.shacl` beside each vendored schema — so
vendoring a new remote block brings its shapes along; 4 of the 28 blocks have none).

**It needs `rdflib` and `pyshacl`, and this repo has no dependency manifest.** Without them the pass
prints a notice and is **skipped**, so `17 passed` can be read as a clean bill of health for a layer
that never ran. Check the `SHACL:` line is present before believing a green run; if the shape count
reads `0 vendored`, remote blocks' rules are not being applied either.

Three details in the implementation are load-bearing and look like candidates for simplification.
They are not:

- **One graph per `rules.shacl`, never a union.** The registers reuse shape URIs across files, so a
  merged graph lands two `sh:path` on one `PropertyShape` and pyshacl rejects the whole graph with a
  `ShapeLoadError`.
- **Shapes scoped to each block's `$ref` closure**, not every file available. Unscoped,
  `additionalProperty`'s rules fire on blocks that never reference it and manufacture violations the
  published register does not report — `ddeCore` went from 0 to 2 violations and 2 to 22 warnings.
- **An example with no inline `@context` is uplifted with the block's `context.jsonld`.** Without it
  rdflib keeps `schema:propertyID` as a *relative* IRI: the triple count looks healthy, every shape
  targeting `http://schema.org/…` matches nothing, and two examples report clean while the register
  fails them.

Local output matches `bblocks-postprocess` exactly on this register, which is the test that these
three are right. If a change makes local and CI disagree, suspect one of them.

```bash
python tools/augment_register.py
```

Adds `resolvedSchema` URLs to `build/register.json`. Run after a CI build, not before.

Local full build (matches CI, needs Docker):

```bash
docker run --pull=always --rm --workdir /workspace -v "$(pwd):/workspace" ghcr.io/opengeospatial/bblocks-postprocess --clean true --base-url http://localhost:9090/register/
```

`.gitignore` already covers `build-local/` and `.volumes` for this pattern.

## Cross-repo dependency on CDIF

DDE blocks extend CDIF ones. `bblocks-config.yaml` imports the CDIF register
(`cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/register.json`), and
`$defs` reference CDIF schemas by **published GitHub Pages URL**, not by relative path:

```yaml
$defs:
  CdifMandatory:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/_sources/profiles/cdifProfile/cdifCore/schema.yaml
```

Those URLs are **vendored and pinned**: a copy of each lives under `vendor/remote/` (28 schemas — the
transitive closure, since CDIF's blocks `$ref` each other) with its SHA-256 in
`vendor/remote-lock.json`. Resolution reads the vendored copy, so an upstream restructure no longer
breaks a build silently; it shows up the next time someone runs `--refresh-remote`, as a lock diff.

Consequences worth knowing before debugging a resolution failure:

- If resolution fails with `failed to fetch URL`, the ref is **not vendored**, not necessarily moved.
  Run `--refresh-remote` before hunting for a rename.
- Editing `vendor/` by hand is reported: the digest check prints `does not match remote-lock.json`.
- A local clone of CDIF sits at `../metadataBuildingBlocks`. Since 2026-10-22 its single remote
  `origin` is CDIF itself (`Cross-Domain-Interoperability-Framework/metadataBuildingBlocks`): the
  `usgin` fork it used to point at was archived and so read-only, and the duplicate `cdif` and
  `upstream` remotes were removed. Use `git -C ../metadataBuildingBlocks fetch origin` — older notes
  and commit messages in this repo say `cdif/main`, which no longer exists as a ref. It was level
  with `origin/main` and 4 commits ahead on 2026-10-22. Prefer the vendored copies in this repo,
  which are what resolution actually uses.
- **Those 4 commits are the only copy of the current tools.** Snapshot validation, the UTF-8 fix, the
  `UnresolvedRefs` check and the SHACL pass are unpushed and absent from upstream, so a tool sync run
  from anywhere else reverts them. They belong in a PR to CDIF.
- **`tools/resolve_schema.py`, `tools/regenerate_schema_json.py` and `tools/validate_examples.py` are
  copies, not originals.** The canonical versions live in `../metadataBuildingBlocks/tools/`. Fix
  them there and run `python tools/sync_resolve_schema.py --apply` **from that repo**; editing them
  locally means the next sync overwrites your fix.
- **Only sync from an up-to-date canonical clone.** The sync overwrites all three files, so running
  it from a stale clone downgrades them — in September it silently reverted a drift-check flag, and
  in October a sync from the then-343-behind clone would have removed vendoring support entirely.
  The clone was brought level on 2026-10-22, so a sync is safe again; check `fetch origin` first, and
  when it is behind, copy the single intended file by hand and say so in the commit message.
- `sync_resolve_schema.py`'s `TARGETS` also lists `geochemBuildingBlocks`, whose GitHub repo is
  **archived** — tool changes synced there cannot be pushed.

## Conventions

- **Identifier prefix** `dde.bbr.metadata.` (from `bblocks-config.yaml`) maps to source paths —
  `dde.bbr.metadata.profiles.DDEProfiles.DDEDiscovery` ⇄ `_sources/profiles/DDEProfiles/DDEDiscovery`.
- **`@type` values are arrays**, so schemas test them with `contains`, never `const` directly.
- **JSON-LD prefixes** are declared per block in `context.jsonld` and repeated in `examples.yaml`:
  `schema:` → `http://schema.org/`, `dde:` → `https://www.ddeworld.org/resource/`, plus `dcterms:`.
- `schema-oas30-downcompile: True` is set, so schemas must stay expressible in OpenAPI 3.0.
- `tests.yaml` exists in each block but is empty (`[]`); example validation carries the load.

## CI

`.github/workflows/process-bblocks.yml` calls the shared OGC
`bblocks-postprocess/validate-and-process.yml` on every push to `main`, which validates the register
and commits regenerated `build/` output back. `deploy-viewer.yml` then publishes the custom viewer to
GitHub Pages on that workflow's success.

## Current state (2026-10-22)

Working tree clean. `python tools/validate_examples.py` reports **17 passed, 0 failed** with
**0 SHACL violations** (19 warnings, 7 info — all advisory), and `--live` agrees. The published
register reports the same: 0 violations, same 19 warnings and 7 info. Keep it there: run the suite
before and after any change.

**The register's 12 `build/tests/**/example_1_1.validation_failed.txt` files are expected.**
`bblocks-postprocess` marks a report failed on *any* SHACL result, advisory ones included, so 12
reports are "failed" on nothing but warnings and info. Do not read them as breakage, and do not chase
them as bugs — check the severities inside before acting.

Four URI-valued literals must **stay** literals, and two CDIF shape files disagree about why.
`schema:propertyID` in `ddeCore`, `DDEDiscovery`, `DDEDocument` and `DDESemanticResource` matches the
URI/CURIE pattern that `additionalProperty/rules.shacl` says must be serialized `{"@id": …}`, but
those four sit inside `schema:identifier`, which `cdifCore`'s `cdifd:resourceIdentifierProperty`
constrains with an `sh:or` whose PropertyValue branch requires `schema:propertyID` to be
`sh:datatype xsd:string`. The `sh:severity sh:Warning` on that inner shape softens only a direct
report — inside an `sh:or` it still decides conformance — so an IRI `propertyID` fails the branch,
the whole `or` fails, and the outer `sh:Violation` fires with "An identifier for the documented
resource must be provided".

**So converting them trades zero violations for one.** This was tried on 2026-10-22 and reverted;
the two rules cannot both be satisfied for an identifier whose scheme is a registry URI, and it is
worth raising upstream. The four are only unflagged by the first rule because `additionalProperty`'s
shapes are outside their `$ref` closure — that is luck, not design.

Separately, `DDEDiscovery`'s `schema:propertyID` value `"Wikidata"` is a free label, does **not**
match the pattern, and must not be converted either.

Aligned with CDIF as of 2026-10-22, pinned in `vendor/remote-lock.json` and `vendor/shapes-lock.json`.
The 2026-10 resolve picked up an upstream refactor of the reference and concept types — every
block's `$defs` changed name even where constraints did not:

| was | now |
|---|---|
| `cdifConcept` | `Concept` |
| `Relation` | `DcatRole` |
| `cdifConceptOrTermOrString` | `LabeledLink_cdifConceptOrTermOrString` |
| `cdifDataType/cdifReference` | retired 2026-09-23, folded into `labeledLink` |

### Shapes CDIF changed, worth knowing before writing an example

These broke every example at once and will break the next one written from an old template:

- `@context` must declare `schema`, `dcterms`, `dcat`, **and `prov`**, each with an exact const value.
- `schema:subjectOf.schema:additionalType` takes `[{"@id": "dcat:CatalogRecord"}]` — an object, not
  the bare string.
- `schema:subjectOf.dcterms:conformsTo` must contain `https://w3id.org/cdif/core/1.1` (no trailing
  slash). The current DDE pair is that plus `https://w3id.org/cdif/discovery/1.1`.
- **Labelled links are valid again — do not "fix" them into bare `@id`s.** For about three weeks
  `cdifReference` required `dcat:Relationship` *and* `schema:CreativeWork` in `@type` under an
  `allOf`, which made every labeled link unsatisfiable; upstream removed that mandate on 2026-09-08
  (their note: it "broke every schema:license example that followed schema.org's own advice") and
  retired `cdifReference` into `labeledLink` on 2026-09-23, where the two co-types are now an
  `anyOf`. So `{"@type": ["schema:CreativeWork"], "schema:name": …, "schema:url": …}` validates for
  `schema:license`, `schema:conditionsOfAccess` and `schema:documentation`, and carrying the name is
  what schema.org and `cdifCore`'s own description recommend. `schema:url` is required when `@type`
  includes `schema:CreativeWork`. A plain string or `{"@id": <uri>}` is still valid.
- `time:hasTRS` is a string URI, not `{"@id": …}`.
- `prov:wasDerivedFrom` items are a string or `{"@id"}` only — `additionalProperties: false`, so no
  `@type`/`schema:name` alongside.
- `schema:instrument` inside `prov:used` is an **array**, and each instrument's `@type` must contain
  both `schema:Product` and `schema:Thing` (`minItems: 2`) with `schema:additionalType` as an array.

### Checking against CDIF

To read what a DDE schema actually resolves against, read the vendored copy — it is the same bytes
resolution uses, and needs no network:

```bash
cat vendor/remote/cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/_sources/profiles/cdifProfile/cdifCore/schema.yaml
```

To ask what upstream serves *today* — a different question, and the one to ask before re-pinning:

```bash
curl -sS https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/_sources/profiles/cdifProfile/cdifCore/schema.yaml
```

CDIF's `exampleCdifCoreComplete.json` beside it is the best reference for what a valid instance looks
like. The CDIF schemas carry unusually long comments explaining *why* a constraint is shaped as it is,
often naming the date and the breakage that prompted it — read them before working around a
constraint, because the workaround may already be obsolete.
