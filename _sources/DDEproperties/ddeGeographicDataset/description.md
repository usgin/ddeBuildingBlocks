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
