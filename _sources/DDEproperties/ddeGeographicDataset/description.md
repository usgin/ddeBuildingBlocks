## DDE Geographic Dataset Properties

Conditional extension for geographic dataset resources. Implements MD_SpatialRepresentation from DDE spec Table 5 / XSD. This building block is composed into the DDEDataset profile when the resource type is `geographicDataset`.

### Required
- **`schema:spatialCoverage`**: Spatial extent of the geographic dataset. Mandatory for geographicDataset resource type.

### Optional (via `schema:additionalProperty`)

Each property is a `schema:PropertyValue` with a DDE `propertyID` and a value whose type is constrained per the XSD type definitions:

- **`dde:spatialRepresentationType`**: Value from `SpatialRepresentationTypeCode` enum: vector, grid, textTable, tin, stereoModel, video.
- **`dde:spatialResolution`**: Free text string (e.g., "1:1000000", "30m"). XSD type `CharacterString_Type`.
- **`dde:referenceSystemType`**: Value from `ReferenceSystemTypeCode` enum (28 values including geodeticGeographic2D, projected, vertical, etc.).
- **`dde:referenceSystemIdentifier`**: Follows `MD_Identifier` pattern — `schema:value` is the identifier code (e.g., "EPSG:4326"), with optional `schema:url` for the resolvable form. Requires either value or url.
- **`dde:verticalExtent`**: The `EX_VerticalExtent` of the dataset (DDE elevation). `schema:value` is a `schema:QuantitativeValue` whose `schema:minValue` and `schema:maxValue` are numbers, the lowest and highest vertical coordinates; at least one is required, so an open-ended range gives only the other. Its `schema:unitCode` gives their unit as a UCUM code (e.g. "m"). The PropertyValue's `schema:valueReference` names the vertical CRS as a `schema:DefinedTerm` with the identifier code in `schema:termCode` (e.g. "EPSG:5714", MSL height) and/or `schema:url`. Depths are negative in a height CRS, or positive in a depth CRS such as EPSG:5715. Unlike the other four, this shape is enforced: a PropertyValue with this propertyID whose value is not such a range fails, rather than passing as a generic additional property.
