## DDE Software Profile

DDE profile for software resources. Extends `ddeCore` with a resource type constraint.

### Resource type codes
software

### Composed building blocks

1. **ddeCore** — DDE core properties: resource type from `dde:codelist/ResourceTypeCode`, topic category and acquisition type keywords, alternate names, optional browse graphics. `ddeCore` composes `cdifCore`, so CDIF's mandatory fields come in with it.
2. **Resource type constraint** — `schema:termCode` must be `software`

### Conformance

A document instance claiming this profile declares it on the catalog record:

```json
"schema:subjectOf": {
    "dcterms:conformsTo": [
        {"@id": "https://w3id.org/cdif/core/1.1"},
        {"@id": "https://w3id.org/cdif/dde/1.0/DDESoftware"}
    ]
}
```

`https://w3id.org/cdif/dde/1.0/DDESoftware` is required by this profile's schema, as a
`contains` over `schema:subjectOf`/`dcterms:conformsTo`. The URI is on the profile
because DDE profiles are what document instances conform to; the property building
blocks they compose, `ddeCore` among them, declare none of their own.
