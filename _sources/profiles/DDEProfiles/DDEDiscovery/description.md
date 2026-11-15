## DDE Geoscience Discovery Metadata Profile

Composes CDIF discovery metadata building blocks with DDE-specific extensions to create a complete geoscience discovery metadata profile.

### Composed building blocks

1. **cdifCore** — Base CDIF mandatory fields: @id, @type, name, identifier, dateModified, subjectOf, license/conditionsOfAccess, url/distribution.
2. **cdifOptional** — CDIF optional fields: description, creator, contributor, publisher, provider, keywords, spatialCoverage, temporalCoverage, distribution, provenance, quality, funding, etc.
3. **ddeCore** — DDE mandatory extensions:
   - Resource type from `dde:codelist/ResourceTypeCode` (42 geoscience types)
   - Topic category keywords from `dde:codelist/TopicCategoryCode`
   - Acquisition type keywords from `dde:codelist/AcquisitionTypeCode`
   - Browse graphic images (`schema:ImageObject`)
4. **ddeOptional** — DDE optional extensions: alternate names.

### Resource-type profiles

The following profiles extend DDEDiscovery with resource-type-specific constraints:

- **DDEDataset** — Datasets; conditional ddeGeographicDataset for geographicDataset type.
- **DDEImage** — Imagery resources; includes ddeImagery; conditional ddeGeographicDataset for map type.
- **DDEWebAPI** — Service resources described as WebAPIs; composes CDIF webAPI building block with DDE ServiceTypeCode constraints.
- **DDECollection**, **DDEDocument**, **DDEEvent**, **DDESoftware**, etc. — Resource-type-specific additionalType constraints.

### Conformance

A document instance claiming this profile declares it on the catalog record:

```json
"schema:subjectOf": {
    "dcterms:conformsTo": [
        {"@id": "https://w3id.org/cdif/core/1.1"},
        {"@id": "https://w3id.org/cdif/dde/1.0/DDEDiscovery"}
    ]
}
```

`https://w3id.org/cdif/dde/1.0/DDEDiscovery` is required by this profile's schema, as a
`contains` over `schema:subjectOf`/`dcterms:conformsTo`. The URI is on the profile
because DDE profiles are what document instances conform to; the property building
blocks they compose, `ddeCore` among them, declare none of their own.
