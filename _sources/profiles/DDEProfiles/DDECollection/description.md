## DDE Collection Profile

DDE profile for collection resources. Extends `ddeCore` with a resource type constraint and requires `schema:hasPart` to describe collection members.

### Resource type codes
aggregate, collection, series, learningResource, guide

### Composed building blocks

1. **ddeCore** — DDE core properties: resource type from `dde:codelist/ResourceTypeCode`, topic category and acquisition type keywords, alternate names, optional browse graphics. `ddeCore` composes `cdifCore`, so CDIF's mandatory fields come in with it.
2. **Resource type constraint** — `schema:termCode` must be one of the collection group codes
3. **cdifManifest** — `schema:hasPart` on the Dataset, for members retrievable at their own addresses, and on a `schema:distribution` item, for component files inside an archive
4. **`schema:hasPart`** (required) — at least one member, each classified with a DDE resource type

### Collection member structure

The member shape comes from **cdifManifest**'s `resourcePartItem`: `@id`, `@type`,
`schema:name`, `schema:description`, `schema:encodingFormat`, `schema:url` and
`schema:about`. On top of that, every member carries a DDE resource type
(`ddeResourceType`) — `items`, not `contains`, so each member is classified rather than
just one of them.

Before 2026-11-15 this block defined its own member shape, with `schema:name` required and
no way to say where a member could be retrieved, which is the one thing a manifest exists
to express.

### Conformance

A document instance claiming this profile declares it on the catalog record:

```json
"schema:subjectOf": {
    "dcterms:conformsTo": [
        {"@id": "https://w3id.org/cdif/core/1.1"},
        {"@id": "https://w3id.org/cdif/dde/1.0/DDECollection"}
    ]
}
```

`https://w3id.org/cdif/dde/1.0/DDECollection` is required by this profile's schema, as a
`contains` over `schema:subjectOf`/`dcterms:conformsTo`. The URI is on the profile
because DDE profiles are what document instances conform to; the property building
blocks they compose, `ddeCore` among them, declare none of their own.
