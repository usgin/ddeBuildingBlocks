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
| `build/` | generated | CI (`bblocks-postprocess`), committed back to `main` |

After editing any `schema.yaml`, regenerate both derived files or the register and validators go
stale against the source. `resolvedSchema.json` is the fully-inlined schema — it is what
`validate_examples.py` validates against, so a change that lands only in `schema.yaml` is a change
nothing checks.

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

Re-inlines every `resolvedSchema.json`. Single block: `python tools/resolve_schema.py ddeCore`, or
`--file path/to/schema.yaml`. Writing in place is the default; `--stdout` prints instead. Resolution
fetches the CDIF `$ref` URLs over the network, so this needs connectivity.

```bash
python tools/validate_examples.py
```

Validates every `example*.json` against its block's resolved schema — this repo's closest thing to a
test suite. `--verbose` for per-file results, `--filter ddeCore` to narrow to one block (the filter
matches on path, and is the way to "run a single test" here).

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

Consequences worth knowing before debugging a resolution failure:

- A restructure in the CDIF repo silently breaks these URLs; there is no local fallback. The current
  working-tree changes are exactly that — `cdifProperties/cdifCore` moved to
  `profiles/cdifProfile/cdifCore`.
- A local clone of that repo sits at `../metadataBuildingBlocks` (remote named `cdif`), useful for
  checking what a URL *should* resolve to.
- **`tools/resolve_schema.py` and `tools/regenerate_schema_json.py` are copies, not originals.** The
  canonical versions live in `../metadataBuildingBlocks/tools/`. Fix them there and run
  `python tools/sync_resolve_schema.py --apply` **from that repo** to push the copy here; editing
  them locally means the next sync overwrites your fix.

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

## Current state (2026-09-04)

`python tools/validate_examples.py` reports **17 passed, 0 failed**. Keep it there — run it before
and after any change.

Uncommitted: the CDIF `$ref` migration (`cdifProperties/cdifCore` → `profiles/cdifProfile/cdifCore`),
regenerated `*Schema.json` and `resolvedSchema.json`, the two synced tools, and 15 examples updated to
the shapes current CDIF now requires.

### Shapes CDIF changed, worth knowing before writing an example

These broke every example at once and will break the next one written from an old template:

- `@context` must declare `schema`, `dcterms`, `dcat`, **and `prov`**, each with an exact const value.
- `schema:subjectOf.schema:additionalType` takes `[{"@id": "dcat:CatalogRecord"}]` — an object, not
  the bare string.
- `schema:subjectOf.dcterms:conformsTo` must contain `https://w3id.org/cdif/core/1.1` (no trailing
  slash). The current DDE pair is that plus `https://w3id.org/cdif/discovery/1.1`.
- **`cdifReference` now requires `dcat:Relationship` in `@type`** (it composes `labeledLink` with a
  DCAT `Relation` overlay). A `{"@type": ["schema:CreativeWork"], "schema:name": …, "schema:url": …}`
  link therefore no longer validates as a reference. For `schema:license`,
  `schema:conditionsOfAccess`, and `schema:documentation`, CDIF's own examples use a plain string or
  `{"@id": <uri>}` — do that rather than adding `dcat:Relationship` to something that is not a
  relationship.
- `time:hasTRS` is a string URI, not `{"@id": …}`.
- `prov:wasDerivedFrom` items are a string or `{"@id"}` only — `additionalProperties: false`, so no
  `@type`/`schema:name` alongside.
- `schema:instrument` inside `prov:used` is an **array**, and each instrument's `@type` must contain
  both `schema:Product` and `schema:Thing` (`minItems: 2`) with `schema:additionalType` as an array.

### Checking against CDIF

The local clone at `../metadataBuildingBlocks` was **700 commits behind** `cdif/main` as of
2026-09-04 and still had the pre-restructure `cdifProperties/` layout — do not trust it without
`git -C ../metadataBuildingBlocks fetch cdif` first. What `resolve_schema.py` actually fetches is the
published GitHub Pages copy, so `curl` that when in doubt:

```bash
curl -sS https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/_sources/profiles/cdifProfile/cdifCore/schema.yaml
```

CDIF's own `exampleCdifCoreComplete.json` beside it is the best reference for what a valid instance
looks like.
