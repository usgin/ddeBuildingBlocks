## DDE Geoscience Discovery Metadata Profile

Composes CDIF discovery metadata building blocks with DDE-specific extensions to create a complete geoscience discovery metadata profile.

### Composed building blocks

1. **cdifMandatory** — Base CDIF mandatory fields: @id, @type, name, identifier, dateModified, subjectOf, license/conditionsOfAccess, url/distribution.
2. **cdifOptional** — CDIF optional fields: description, creator, contributor, publisher, provider, keywords, spatialCoverage, temporalCoverage, distribution, provenance, quality, funding, etc.
3. **ddeRequired** — DDE mandatory extensions:
   - Resource type from `dde:codelist/ResourceTypeCode` (42 geoscience types)
   - Topic category keywords from `dde:codelist/TopicCategoryCode`
   - Acquisition type keywords from `dde:codelist/AcquisitionTypeCode`
   - Browse graphic images (`schema:ImageObject`)
   - DDE profile conformance (`cdif:profile_ddeCDIF`)
4. **ddeOptional** — DDE optional extensions: alternate names, measurement techniques, additional keywords and types.

### Conditional extensions (NOT included)

The following building blocks are conditional and should be composed into separate sub-profiles:

- **ddeImagery** — For imagery resources: sensor type, platform, wavelength range, signal generator, processing level.
- **ddeServiceInfo** — For service resources: DDE service type from `dde:codelist/ServiceTypeCode`, operated datasets.
