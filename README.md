# DDE Building Blocks

Modular metadata schema components for [Deep-time Digital Earth (DDE)](https://www.ddeworld.org/), built using the [OGC Building Blocks](https://opengeospatial.github.io/bblocks/) pattern.

## Structure

### DDEproperties (5 schema components)

Property building blocks that define DDE-specific metadata elements:

- **ddeCore** — DDE mandatory fields: resource type (ResourceTypeCode), topic/acquisition keywords, browse graphics, conformance declaration. Composes cdifCore + ddeResourceType.
- **ddeResourceType** — Constrains schema:additionalType to require a DefinedTerm from the DDE ResourceTypeCode codelist.
- **ddeCatalogRecord** — DDE catalog record conformance declaration (extends cdifCatalogRecord to require ddeCore BB URI).
- **ddeGeographicDataset** — Geographic extent, CRS, and resolution for geographic resources.
- **ddeImagery** — Imagery acquisition metadata: sensor, platform, wavelength, signal generator, processing level.

### DDEProfiles (11 resource type profiles)

Metadata profiles that compose property building blocks for specific resource types:

- **DDEDiscovery** — base DDE discovery profile (ddeCore)
- **DDEDataset** — datasets; conditional ddeGeographicDataset for geographicDataset type
- **DDEImage** — imagery; includes ddeImagery; conditional ddeGeographicDataset for map type
- **DDEWebAPI** — service resources; composes CDIF webAPI BB with DDE ServiceTypeCode constraints
- **DDECollection** — collections; hasPart items require DDE resource type classification
- **DDEDocument**, **DDEEvent**, **DDESoftware**, **DDEFunctionalResource**, **DDEAudioVisualProduct**, **DDESemanticResource** — resource-type-specific additionalType constraints

### archive/deprecated

Superseded building blocks retained for reference:

- **DDEService** — replaced by DDEWebAPI
- **ddeServiceInfo** — service properties now inherited from CDIF webAPI building block

## Tools

- `tools/resolve_schema.py` — Resolve all `$ref` into single resolvedSchema.json files
- `tools/regenerate_schema_json.py` — Generate *Schema.json from schema.yaml sources (YAML→JSON + ref rewrite)
- `tools/validate_examples.py` — Validate every example against its block's resolved schema

These tools are synced from the canonical copies in [metadataBuildingBlocks/tools/](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks/tree/main/tools). Do not edit locally — update the canonical copy and run `python tools/sync_resolve_schema.py --apply` from the metadataBuildingBlocks repo. Run that sync only from an up-to-date clone of that repo: it overwrites all three files, so syncing from a stale clone silently downgrades them.

## Cross-repo imports

This repository imports shared schema.org and CDIF property building blocks from [metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks) via the OGC Building Blocks import mechanism.

Those blocks are `$ref`d by published URL, and a copy of each is vendored under `vendor/remote/` with its SHA-256 digest recorded in `vendor/remote-lock.json`. Resolution reads the vendored copies, so builds are reproducible and offline; nothing is fetched unless you ask for it:

```bash
python tools/resolve_schema.py --all --refresh-remote   # re-fetch upstream and re-pin
```

The diff to `vendor/` is then the record of what upstream changed.

## Viewer

Browse the building blocks at: https://usgin.github.io/ddeBuildingBlocks/

## License

[Apache 2.0](LICENSE)
