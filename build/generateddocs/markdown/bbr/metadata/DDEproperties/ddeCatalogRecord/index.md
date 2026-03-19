
# DDE Catalog Record (Schema)

`dde.bbr.metadata.DDEproperties.ddeCatalogRecord` *v0.1*

Extends cdifCatalogRecord to require DDE conformance declaration. Adds dcterms:conformsTo constraint for ddeCore BB URI.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## DDE Catalog Record

Extends cdifCatalogRecord to require that `dcterms:conformsTo` includes the ddeCore building block URI (`https://w3id.org/cdif/bbr/metadata/DDEproperties/ddeCore`).

## Examples

### Example DDE catalog record conformance extension.
Import base cdifCatalogRecord, add requirement that dcterms:conformsTo has ddeCore BB URI.
#### json
```json
{
    "@context": {
        "schema": "http://schema.org/",
        "dde": "https://www.ddeworld.org/resource/",
        "dcterms": "http://purl.org/dc/terms/",
        "dcat": "http://www.w3.org/ns/dcat#"
    },
    "@id": "urn:uuid:example-dde-catalog-record",
    "@type": ["schema:Dataset"],
    "schema:additionalType": ["dcat:CatalogRecord"],
    "schema:about": {"@id": "https://example.org/dataset/geo-dataset-001"},
    "schema:dateModified": "2026-02-28",
    "dcterms:conformsTo": [
        {"@id": "https://w3id.org/cdif/core/1.0/"},
        {"@id": "https://w3id.org/cdif/bbr/metadata/DDEproperties/ddeCore"}
    ],
    "schema:sdDatePublished": "2026-02-28"
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "schema": "http://schema.org/"
    },
    "https://usgin.github.io/ddeBuildingBlocks/build/annotated/bbr/metadata/DDEproperties/ddeCatalogRecord/context.jsonld",
    {
      "schema": "http://schema.org/",
      "dde": "https://www.ddeworld.org/resource/",
      "dcterms": "http://purl.org/dc/terms/",
      "dcat": "http://www.w3.org/ns/dcat#"
    }
  ],
  "@id": "urn:uuid:example-dde-catalog-record",
  "@type": [
    "schema:Dataset"
  ],
  "schema:additionalType": [
    "dcat:CatalogRecord"
  ],
  "schema:about": {
    "@id": "https://example.org/dataset/geo-dataset-001"
  },
  "schema:dateModified": "2026-02-28",
  "dcterms:conformsTo": [
    {
      "@id": "https://w3id.org/cdif/core/1.0/"
    },
    {
      "@id": "https://w3id.org/cdif/bbr/metadata/DDEproperties/ddeCore"
    }
  ],
  "schema:sdDatePublished": "2026-02-28"
}
```

#### ttl
```ttl
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix schema1: <http://schema.org/> .

<urn:uuid:example-dde-catalog-record> a schema1:Dataset ;
    dcterms:conformsTo <https://w3id.org/cdif/bbr/metadata/DDEproperties/ddeCore>,
        <https://w3id.org/cdif/core/1.0/> ;
    schema1:about <https://example.org/dataset/geo-dataset-001> ;
    schema1:additionalType "dcat:CatalogRecord" ;
    schema1:dateModified "2026-02-28" ;
    schema1:sdDatePublished "2026-02-28" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
type: object
allOf:
- $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/_sources/cdifProperties/cdifCatalogRecord/schema.yaml
- properties:
    dcterms:conformsTo:
      type: array
      items:
        type: object
        properties:
          '@id':
            type: string
      minItems: 1
      contains:
        type: object
        properties:
          '@id':
            const: https://w3id.org/cdif/bbr/metadata/DDEproperties/ddeCore
        required:
        - '@id'
      minContains: 1
x-jsonld-prefixes:
  schema: http://schema.org/

```

Links to the schema:

* YAML version: [schema.yaml](https://usgin.github.io/ddeBuildingBlocks/build/annotated/bbr/metadata/DDEproperties/ddeCatalogRecord/schema.json)
* JSON version: [schema.json](https://usgin.github.io/ddeBuildingBlocks/build/annotated/bbr/metadata/DDEproperties/ddeCatalogRecord/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "http://schema.org/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://usgin.github.io/ddeBuildingBlocks/build/annotated/bbr/metadata/DDEproperties/ddeCatalogRecord/context.jsonld)

## Sources

* [DDE Metadata Standard](https://www.ddeworld.org)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/ddeBuildingBlocks](https://github.com/usgin/ddeBuildingBlocks)
* Path: `_sources/DDEproperties/ddeCatalogRecord`

