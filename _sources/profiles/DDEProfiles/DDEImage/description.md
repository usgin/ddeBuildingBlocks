## DDE Image Profile

DDE profile for image resources. Extends `ddeCore` with a resource type constraint and the ddeImagery building block for imagery-specific properties.

### Resource type codes
image, photograph, explanatoryFigure, map

### Composed building blocks

1. **ddeCore** — DDE core properties: resource type from `dde:codelist/ResourceTypeCode`, topic category and acquisition type keywords, alternate names, optional browse graphics. `ddeCore` composes `cdifCore`, so CDIF's mandatory fields come in with it.
2. **ddeImagery** — Optional imagery properties: sensor type, platform, equipment, collector, startTime, endTime, signalGenerator, wavelength, processingLevel
3. **Resource type constraint** — `schema:termCode` must be one of the image group codes

### Conformance

A document instance claiming this profile declares it on the catalog record:

```json
"schema:subjectOf": {
    "dcterms:conformsTo": [
        {"@id": "https://w3id.org/cdif/core/2.0"},
        {"@id": "https://w3id.org/cdif/dde/1.0/DDEImage"}
    ]
}
```

`https://w3id.org/cdif/dde/1.0/DDEImage` is required by this profile's schema, as a
`contains` over `schema:subjectOf`/`dcterms:conformsTo`. The URI is on the profile
because DDE profiles are what document instances conform to; the property building
blocks they compose, `ddeCore` among them, declare none of their own.
