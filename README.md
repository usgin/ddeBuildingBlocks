# DDE Building Blocks

Modular metadata schema components for [Deep-time Digital Earth (DDE)](https://www.ddeworld.org/), built using the [OGC Building Blocks](https://opengeospatial.github.io/bblocks/) pattern.

## Structure

### DDEproperties (7 schema components)

Property building blocks that define DDE-specific metadata elements: geographic dataset, imagery, optional/required fields, resource types, service info, and subject classification.

### DDEProfiles (11 resource type profiles)

Metadata profiles that compose property building blocks with CDIF base schemas:

- **DDEDiscovery** — base DDE discovery profile (composes cdifMandatory + cdifOptional + DDE properties)
- **10 resource type profiles** — DDEAudioVisualProduct, DDECollection, DDEDataset, DDEDocument, DDEEvent, DDEFunctionalResource, DDEImage, DDESemanticResource, DDEService, DDESoftware

## Cross-repo imports

This repository imports shared schema.org and CDIF property building blocks from [metadataBuildingBlocks](https://github.com/usgin/metadataBuildingBlocks) via the OGC Building Blocks import mechanism.

## Viewer

Browse the building blocks at: https://usgin.github.io/ddeBuildingBlocks/

## License

[Apache 2.0](LICENSE)
