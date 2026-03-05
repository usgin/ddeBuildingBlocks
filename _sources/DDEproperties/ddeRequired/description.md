## DDE Required Metadata Properties

Extends CDIF mandatory metadata with DDE-specific required fields:

- **Resource type** (`schema:additionalType`): At least one `schema:DefinedTerm` from the DDE `ResourceTypeCode` codelist, which defines 42 geoscience-specific resource types.
- **Topic category keywords** (`schema:keywords`): At least one `schema:DefinedTerm` from the DDE `TopicCategoryCode` codelist.
- **Acquisition type keywords** (`schema:keywords`): At least one `schema:DefinedTerm` from the DDE `AcquisitionTypeCode` codelist.
- **Browse graphics** (`schema:image`): At least one `schema:ImageObject` with a `schema:contentUrl`.
- **Profile conformance** (`schema:subjectOf`): The catalog record must declare conformance with `cdif:profile_ddeCDIF` via the ddeSubject extension.

This building block uses `allOf` to compose the CDIF mandatory base schema with the DDE-specific constraints.
