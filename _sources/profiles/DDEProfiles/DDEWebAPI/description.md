## DDE WebAPI Profile

DDE profile for resources that **are** web services. Unlike the other profiles, where
`schema:distribution` may offer an API as one way to reach a dataset, here the described
resource is itself the service, so `@type` must include `schema:WebAPI`.

### Resource type codes
service, webAPI, repository

### Composed building blocks

1. **ddeCore** — DDE core properties: resource type from `dde:codelist/ResourceTypeCode`,
   topic category and acquisition type keywords, alternate names, optional browse graphics.
   `ddeCore` composes `cdifCore`, so CDIF's mandatory fields come in with it.
2. **webAPI** (CDIF `schemaorgProperties/webAPI`) — service-specific properties:
   `schema:potentialAction`, `schema:termsOfService`, `schema:documentation`.
3. **`@type`** (required) — must contain `schema:WebAPI`.
4. **Resource type constraint** — `schema:termCode` must be one of the service group codes.
5. **`schema:serviceType`** — a `schema:DefinedTerm` from `dde:codelist/ServiceTypeCode`,
   narrowing CDIF's open service typing to the 37 DDE codes. Requires `@type`,
   `schema:inDefinedTermSet` and `schema:termCode`.
6. **`schema:dataset`** (optional) — datasets operated on by the service, the DDE
   `operatedDataset` element. Each entry is a URI or a `schema:PropertyValue` identifier.

### DDE ServiceTypeCode groups

The codelist covers nine categories: data services (`DataService>DataAccess`,
`DataService>MapView`, …), knowledge services (`DDE_GeoscienceKnowledgeDirectory`,
`DDE_DeepShovel`, `DDE_Scholar`, …), platform services (`DDE_PlatformCatalogue`,
`DDE_PlatformRegistry`, `DDE_EarthExplorer`, …), thematic services
(`Theme>MineralResourceAssessment`, `Theme>GeologicMapping`, `Theme>Dinosaur`, …), and the
generic `VocabularyService`, `RegistryService`, `DiscoveryService`, `ViewService` and
`OtherService`. See `schema.yaml` for the full enumeration.

### Validation

`rules.shacl` reports, at warning severity: the missing conformance URI, a `@type` without
`schema:WebAPI`, a missing or wrongly-scoped `schema:serviceType`, and an
`schema:additionalType` outside the service group. The `schema:serviceType` term shape is
scoped with `sh:targetObjectsOf`, not `sh:targetClass schema:DefinedTerm`, so it does not
fire on every keyword in the record.

### Conformance

A document instance claiming this profile declares it on the catalog record:

```json
"schema:subjectOf": {
    "dcterms:conformsTo": [
        {"@id": "https://w3id.org/cdif/core/1.1"},
        {"@id": "https://w3id.org/cdif/dde/1.0/DDEWebAPI"}
    ]
}
```

`https://w3id.org/cdif/dde/1.0/DDEWebAPI` is required by this profile's schema, as a
`contains` over `schema:subjectOf`/`dcterms:conformsTo`. The URI is on the profile
because DDE profiles are what document instances conform to; the property building
blocks they compose, `ddeCore` among them, declare none of their own.
