## DDE Dataset Profile

DDE profile for dataset resources. Extends DDEDiscovery with a resource type constraint requiring `schema:additionalType` to include a `schema:termCode` from: dataset, dataCatalog, geographicDataset, nonGeographicDataset.

### Composed building blocks

1. **DDEDiscovery** — Base DDE discovery profile (cdifMandatory + cdifOptional + ddeRequired + ddeOptional)
2. **Resource type constraint** — `schema:termCode` must be one of the dataset group codes

### Sub-profile: geographicDataset

When the resource type is `geographicDataset`, additionally compose with **ddeGeographicDataset** building block for mandatory `schema:spatialCoverage` and optional spatial representation properties (spatialRepresentationType, spatialResolution, referenceSystemType, referenceSystemIdentifier).
