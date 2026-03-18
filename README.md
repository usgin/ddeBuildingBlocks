# DDE Building Blocks

Modular metadata schema components for [Deep-time Digital Earth (DDE)](https://www.ddeworld.org/), built using the [OGC Building Blocks](https://opengeospatial.github.io/bblocks/) pattern.

## Structure

### DDEproperties (6 schema components)

Property building blocks that define DDE-specific metadata elements:

- **ddeMandatory** — DDE mandatory fields: resource type (ResourceTypeCode), topic/acquisition keywords, browse graphics, conformance declaration. Composes cdifCore + ddeResourceType.
- **ddeOptional** — DDE optional fields: alternate names. Composes cdifOptional.
- **ddeResourceType** — Constrains schema:additionalType to require a DefinedTerm from the DDE ResourceTypeCode codelist.
- **ddeSubject** — DDE catalog record conformance declaration.
- **ddeGeographicDataset** — Geographic extent, CRS, and resolution for geographic resources.
- **ddeImagery** — Imagery acquisition metadata: sensor, platform, wavelength, signal generator, processing level.

### DDEProfiles (11 resource type profiles)

Metadata profiles that compose property building blocks for specific resource types:

- **DDEDiscovery** — base DDE discovery profile (ddeMandatory + ddeOptional)
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

- `tools/regenerate_schema_json.py` — Generate *Schema.json from schema.yaml sources
- `tools/resolve_schema.py` — Resolve all $ref into single resolvedSchema.json files

## Cross-repo imports

This repository imports shared schema.org and CDIF property building blocks from [metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks) via the OGC Building Blocks import mechanism.

## Viewer

Browse the building blocks at: https://usgin.github.io/ddeBuildingBlocks/

## License

[Apache 2.0](LICENSE)
