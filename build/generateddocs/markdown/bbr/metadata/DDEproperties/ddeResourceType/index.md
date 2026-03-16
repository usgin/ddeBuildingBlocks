
# DDE Resource Type (Schema)

`dde.bbr.metadata.DDEproperties.ddeResourceType` *v0.1*

Constrains schema:additionalType to require at least one DefinedTerm from the DDE ResourceTypeCode codelist. The DDE resource type vocabulary includes 32 resource types from the DDE spec Table 18. Defines properties: schema:additionalType. Uses building blocks: definedTerm (schemaorgProperties).

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## DDE Resource Type

Constrains `schema:additionalType` to require at least one `schema:DefinedTerm` from the DDE `ResourceTypeCode` codelist (`dde:codelist/ResourceTypeCode`).

The DDE vocabulary defines 32 resource types from the DDE spec Table 18: aggregate, application, webApplication, collection, dataset, dataCatalog, geographicDataset, nonGeographicDataset, document, article, thesis, book, poster, webPage, image, map, photograph, explanatoryFigure, initiative, fieldSession, learningResource, guide, model, movie, repository, semanticResource, definedTermSet, series, service, webAPI, software, sound.

This building block is used by `ddeRequired` to enforce DDE resource typing on metadata records.

## Examples

### Example DDE Resource Type.
Shows a schema:additionalType with a DefinedTerm from the DDE ResourceTypeCode codelist.
#### json
```json
{
    "schema:additionalType": [
        {
            "@type": "schema:DefinedTerm",
            "schema:name": "Geographic Dataset",
            "schema:termCode": "geographicDataset",
            "schema:inDefinedTermSet": "dde:codelist/ResourceTypeCode"
        }
    ]
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "schema": "http://schema.org/",
      "dde": "https://www.ddeworld.org/resource/"
    },
    "https://usgin.github.io/ddeBuildingBlocks/build/annotated/bbr/metadata/DDEproperties/ddeResourceType/context.jsonld"
  ],
  "schema:additionalType": [
    {
      "@type": "schema:DefinedTerm",
      "schema:name": "Geographic Dataset",
      "schema:termCode": "geographicDataset",
      "schema:inDefinedTermSet": "dde:codelist/ResourceTypeCode"
    }
  ]
}
```

#### ttl
```ttl
@prefix schema1: <http://schema.org/> .

[] schema1:additionalType [ a schema1:DefinedTerm ;
            schema1:inDefinedTermSet "dde:codelist/ResourceTypeCode" ;
            schema1:name "Geographic Dataset" ;
            schema1:termCode "geographicDataset" ] .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: DDE Resource Type constraint
description: Constrains schema:additionalType to require at least one DefinedTerm
  from the DDE ResourceTypeCode codelist (32 resource types from DDE spec Table 18).
type: object
properties:
  schema:additionalType:
    type: array
    description: Must include at least one DefinedTerm from the DDE ResourceTypeCode
      codelist.
    minItems: 1
    items:
      anyOf:
      - type: string
      - $ref: '#/$defs/DefinedTerm'
    contains:
      type: object
      properties:
        '@type':
          const: schema:DefinedTerm
        schema:inDefinedTermSet:
          const: dde:codelist/ResourceTypeCode
        schema:termCode:
          type: string
          enum:
          - aggregate
          - application
          - webApplication
          - collection
          - dataset
          - dataCatalog
          - geographicDataset
          - nonGeographicDataset
          - document
          - article
          - thesis
          - book
          - poster
          - webPage
          - image
          - map
          - photograph
          - explanatoryFigure
          - initiative
          - fieldSession
          - learningResource
          - guide
          - model
          - movie
          - repository
          - semanticResource
          - definedTermSet
          - series
          - service
          - webAPI
          - software
          - sound
      required:
      - '@type'
      - schema:inDefinedTermSet
      - schema:termCode
    minContains: 1
$defs:
  DefinedTerm:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/_sources/schemaorgProperties/definedTerm/schema.yaml
x-jsonld-prefixes:
  schema: http://schema.org/
  dde: https://www.ddeworld.org/resource/

```

Links to the schema:

* YAML version: [schema.yaml](https://usgin.github.io/ddeBuildingBlocks/build/annotated/bbr/metadata/DDEproperties/ddeResourceType/schema.json)
* JSON version: [schema.json](https://usgin.github.io/ddeBuildingBlocks/build/annotated/bbr/metadata/DDEproperties/ddeResourceType/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "http://schema.org/",
    "dde": "https://www.ddeworld.org/resource/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://usgin.github.io/ddeBuildingBlocks/build/annotated/bbr/metadata/DDEproperties/ddeResourceType/context.jsonld)

## Sources

* [DDE Metadata Standard](https://www.ddeworld.org)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/ddeBuildingBlocks](https://github.com/usgin/ddeBuildingBlocks)
* Path: `_sources/DDEproperties/ddeResourceType`

