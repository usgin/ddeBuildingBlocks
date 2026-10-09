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
| `build/` | generated | CI (`bblocks-postprocess`), committed back to `main` |

After editing any `schema.yaml`, regenerate both derived files or the published register goes stale
against the source.

`validate_examples.py` validates against the committed `resolvedSchema.json` by default, so a run is
deterministic and offline. `--live` re-resolves `schema.yaml` instead. Either way it refuses to
validate against a schema containing unresolved `$ref` placeholders — see below.

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
if you see that, `vendor/` is missing or incomplete and the fix is `--refresh-remote`. Do not read a
green run from before 2026-10-09 as meaningful: it predates that check.

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
- A local clone of CDIF sits at `../metadataBuildingBlocks` (remote named `cdif`). It is a **fork**
  (`origin` is `usgin/metadataBuildingBlocks`) and was **334 commits behind `cdif/main`** on
  2026-10-09 — `git -C ../metadataBuildingBlocks fetch cdif` before trusting it. Prefer the vendored
  copies in this repo, which are what resolution actually uses.
- **`tools/resolve_schema.py`, `tools/regenerate_schema_json.py` and `tools/validate_examples.py` are
  copies, not originals.** The canonical versions live in `../metadataBuildingBlocks/tools/`. Fix
  them there and run `python tools/sync_resolve_schema.py --apply` **from that repo**; editing them
  locally means the next sync overwrites your fix.
- **Only sync from an up-to-date canonical clone.** The sync overwrites all three files, so running
  it from a stale clone downgrades them — in September it silently reverted a drift-check flag, and
  from that clone today it would remove vendoring support entirely. When the clone is behind, copy
  the single intended file by hand and say so in the commit message.

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

## Current state (2026-10-09)

Working tree clean. `python tools/validate_examples.py` reports **17 passed, 0 failed**, and
`--live` agrees — both genuine, since the suite now errors rather than passing on unresolved refs.
Keep it there: run it before and after any change.

Aligned with CDIF as of 2026-10-09, pinned in `vendor/remote-lock.json`. The last resolve picked up
an upstream refactor of the reference and concept types — every block's `$defs` changed name even
where constraints did not:

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
