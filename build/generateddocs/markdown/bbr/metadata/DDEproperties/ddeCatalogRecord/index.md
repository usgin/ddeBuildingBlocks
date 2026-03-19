
# DDE Catalog Record (Schema)

`dde.bbr.metadata.DDEproperties.ddeCatalogRecord` *v0.1*

Extends cdifCatalogRecord to require DDE conformance declaration. Adds dcterms:conformsTo constraint for ddeMandatory BB URI.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## DDE Catalog Record

Extends cdifCatalogRecord to require that `dcterms:conformsTo` includes the ddeMandatory building block URI (`https://w3id.org/cdif/bbr/metadata/DDEproperties/ddeMandatory`).

## Examples

### Example DDE catalog record conformance extension.
Import base cdifCatalogRecord, add requirement that dcterms:conformsTo has ddeMandatory BB URI.
#### json
```json
{
    "@context": {
        "schema": "http://schema.org/",
        "dde": "https://www.ddeworld.org/resource/",
        "cdif": "https://cdif.org/profile/",
        "dcterms": "http://purl.org/dc/terms/",
        "dcat": "http://www.w3.org/ns/dcat#"
    },
    "@id": "https://example.org/metadata/geo-dataset-001",
    "@type": ["schema:Dataset"],
    "schema:additionalType": ["dcat:CatalogRecord"],
    "schema:about": {"@id": "https://example.org/dataset/geo-dataset-001"},
    "schema:dateModified": "2026-02-28",
    "schema:creator": [
        {
            "@id": "https://orcid.org/0000-0002-7933-2154",
            "@type": "schema:Person",
            "schema:name": "Richard, Stephen M."
        }
    ],
    "schema:description": "Metadata record for a DDE geoscience dataset",
    "dcterms:conformsTo": [
        {"@id": "https://w3id.org/cdif/core/1.0/"},
        {"@id": "https://w3id.org/cdif/bbr/metadata/DDEproperties/ddeMandatory"}
    ]
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
      "cdif": "https://cdif.org/profile/",
      "dcterms": "http://purl.org/dc/terms/",
      "dcat": "http://www.w3.org/ns/dcat#"
    }
  ],
  "@id": "https://example.org/metadata/geo-dataset-001",
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
  "schema:creator": [
    {
      "@id": "https://orcid.org/0000-0002-7933-2154",
      "@type": "schema:Person",
      "schema:name": "Richard, Stephen M."
    }
  ],
  "schema:description": "Metadata record for a DDE geoscience dataset",
  "dcterms:conformsTo": [
    {
      "@id": "https://w3id.org/cdif/core/1.0/"
    },
    {
      "@id": "https://w3id.org/cdif/bbr/metadata/DDEproperties/ddeMandatory"
    }
  ]
}
```

#### ttl
```ttl
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix schema1: <http://schema.org/> .

<https://example.org/metadata/geo-dataset-001> a schema1:Dataset ;
    dcterms:conformsTo <https://w3id.org/cdif/bbr/metadata/DDEproperties/ddeMandatory>,
        <https://w3id.org/cdif/core/1.0/> ;
    schema1:about <https://example.org/dataset/geo-dataset-001> ;
    schema1:additionalType "dcat:CatalogRecord" ;
    schema1:creator <https://orcid.org/0000-0002-7933-2154> ;
    schema1:dateModified "2026-02-28" ;
    schema1:description "Metadata record for a DDE geoscience dataset" .

<https://orcid.org/0000-0002-7933-2154> a schema1:Person ;
    schema1:name "Richard, Stephen M." .


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
            const: https://w3id.org/cdif/bbr/metadata/DDEproperties/ddeMandatory
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

