## DDE Required Metadata Properties

Extends CDIF mandatory metadata with DDE-specific required fields:

- **Resource type** (`schema:additionalType`): At least one `schema:DefinedTerm` from the DDE `ResourceTypeCode` codelist, which defines 42 geoscience-specific resource types.
- **Topic category keywords** (`schema:keywords`): At least one `schema:DefinedTerm` from the DDE `TopicCategoryCode` codelist.
- **Acquisition type keywords** (`schema:keywords`): At least one `schema:DefinedTerm` from the DDE `AcquisitionTypeCode` codelist.
- **Browse graphics** (`schema:image`): Optional. Any number of `schema:ImageObject`, each with a `schema:contentUrl`, matching the DDE XSD where `browseGraphic` is `minOccurs="0" maxOccurs="unbounded"`.
- **Profile conformance**: none declared here. In DDE the profiles under `profiles/DDEProfiles` are what a document instance conforms to, so each pins its own `https://w3id.org/cdif/dde/1.0/{profileName}`. `schema:subjectOf` is inherited from `cdifCore`, which requires it and refs `cdifCatalogRecord` for its shape. Until 2026-11-15 this block pinned a `ddeCore` register path with no version, through a `ddeCatalogRecord` wrapper now in `archive/deprecated/`.

This building block uses `allOf` to compose the CDIF mandatory base schema with the DDE-specific constraints.
