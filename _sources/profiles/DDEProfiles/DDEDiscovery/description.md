## DDE Geoscience Discovery Metadata Profile

Composes `ddeCore` with a temporal extent and quality measurements, to give a DDE discovery metadata profile that is not tied to one resource type.

**This is a sibling of the resource-type profiles, not their base.** Every DDE profile `$ref`s `ddeCore` directly; none `$ref`s DDEDiscovery. Each profile's description said it "extends DDEDiscovery" until 2026-11-15, which no schema ever did.

### Composed building blocks

1. **ddeCore** — DDE core properties:
   - Resource type from `dde:codelist/ResourceTypeCode`, required
   - Topic category keywords from `dde:codelist/TopicCategoryCode`, required
   - Acquisition type keywords from `dde:codelist/AcquisitionTypeCode`, required
   - Alternate names, optional
   - Browse graphic images (`schema:ImageObject`), optional, matching the DDE XSD
   `ddeCore` composes `cdifCore`, which brings in CDIF's mandatory fields: `@id`, `@type`,
   `@context`, `schema:name`, `schema:identifier`, `schema:dateModified`,
   `schema:subjectOf`, one of license or conditionsOfAccess, and one of url or distribution.
2. **`schema:temporalCoverage`** (optional) — temporal extent of the resource content.
3. **`dqv:hasQualityMeasurement`** (optional) — quality measurements reported for the resource.

There are no `cdifOptional` or `ddeOptional` building blocks. This list named both until
2026-11-15; CDIF's optional discovery properties live in `cdifCore` and `cdifDiscovery`,
and DDE's alternate names in `ddeCore`.

### Resource-type profiles

The following profiles extend DDEDiscovery with resource-type-specific constraints:

- **DDEDataset** — Datasets; conditional ddeGeographicDataset for geographicDataset type.
- **DDEImage** — Imagery resources; includes ddeImagery; conditional ddeGeographicDataset for map type.
- **DDEWebAPI** — Service resources described as WebAPIs; composes CDIF webAPI building block with DDE ServiceTypeCode constraints.
- **DDECollection** — Collections; composes `cdifManifest` for `schema:hasPart`.
- **DDEAudioVisualProduct**, **DDEDocument**, **DDEEvent**, **DDEFunctionalResource**,
  **DDESemanticResource**, **DDESoftware** — resource-type `additionalType` constraints,
  each adding the few properties its type needs.

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
