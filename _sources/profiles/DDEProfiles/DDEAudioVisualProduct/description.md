## DDE AudioVisual Product Profile

DDE profile for audiovisual resources. Extends `ddeCore` with a resource type constraint and adds `schema:duration`.

### Resource type codes
movie, sound

### Composed building blocks

1. **ddeCore** — DDE core properties: resource type from `dde:codelist/ResourceTypeCode`, topic category and acquisition type keywords, alternate names, optional browse graphics. `ddeCore` composes `cdifCore`, so CDIF's mandatory fields come in with it.
2. **Resource type constraint** — `schema:termCode` must be one of the audiovisual group codes
3. **`schema:duration`** (optional) — Duration in ISO 8601 format (e.g., PT1H30M, PT45S)

### Conformance

A document instance claiming this profile declares it on the catalog record:

```json
"schema:subjectOf": {
    "dcterms:conformsTo": [
        {"@id": "https://w3id.org/cdif/core/2.0"},
        {"@id": "https://w3id.org/cdif/dde/1.0/DDEAudioVisualProduct"}
    ]
}
```

`https://w3id.org/cdif/dde/1.0/DDEAudioVisualProduct` is required by this profile's schema, as a
`contains` over `schema:subjectOf`/`dcterms:conformsTo`. The URI is on the profile
because DDE profiles are what document instances conform to; the property building
blocks they compose, `ddeCore` among them, declare none of their own.
