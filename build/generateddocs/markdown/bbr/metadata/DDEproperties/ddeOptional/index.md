
# Optional Fields for DDE Geoscience Metadata (Schema)

`dde.bbr.metadata.DDEproperties.ddeOptional` *v0.1*

DDE profile optional properties beyond CDIF optional: alternate names, measurement techniques, and additional unconstrained keywords and types. Defines properties: schema:alternateName, schema:measurementTechnique, schema:keywords, schema:additionalType. Uses building blocks: definedTerm (schemaorgProperties).

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## DDE Optional Metadata Properties

Non-required DDE-specific properties that complement the base CDIF optional metadata:

- **`schema:alternateName`**: Alternative names or aliases for the resource. Can be a single string or an array of strings.
- **`schema:measurementTechnique`**: Techniques, methods, or instruments used in the measurement or creation of the data. Can be plain text descriptions or `schema:DefinedTerm` values from controlled vocabularies.
- **`schema:keywords`**: Additional keywords beyond the DDE-required vocabulary-constrained keywords. Allows free-text or DefinedTerms from any vocabulary.
- **`schema:additionalType`**: Additional type classifications beyond the required DDE resource type. Can include identifiers from other vocabularies (e.g., schema.org types, Wikidata entities).

## Examples

### Example DDE optional metadata properties.
Shows optional DDE properties including alternate names, measurement techniques, free-text keywords, and additional type classifications.
#### json
```json
{
    "schema:alternateName": [
        "OJP Cenozoic Geology",
        "Greater Ontong Java Plateau Geological Survey"
    ],
    "schema:measurementTechnique": [
        "Field mapping with GPS waypoint collection",
        {
            "@type": "schema:DefinedTerm",
            "schema:name": "Thin Section Petrography",
            "schema:termCode": "thinSectionPetrography",
            "schema:inDefinedTermSet": "https://example.org/methods/geology"
        }
    ],
    "schema:keywords": [
        "Pacific Ocean",
        {
            "@type": "schema:DefinedTerm",
            "schema:name": "Basalt",
            "schema:identifier": "https://example.org/lithology/basalt",
            "schema:inDefinedTermSet": "https://example.org/lithology"
        }
    ],
    "schema:additionalType": [
        "schema:CreativeWork",
        {
            "@type": "schema:DefinedTerm",
            "schema:name": "geological map",
            "schema:identifier": "http://www.wikidata.org/entity/Q4884234",
            "schema:inDefinedTermSet": "https://www.wikidata.org"
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
    "https://usgin.github.io/ddeBuildingBlocks/build/annotated/bbr/metadata/DDEproperties/ddeOptional/context.jsonld"
  ],
  "schema:alternateName": [
    "OJP Cenozoic Geology",
    "Greater Ontong Java Plateau Geological Survey"
  ],
  "schema:measurementTechnique": [
    "Field mapping with GPS waypoint collection",
    {
      "@type": "schema:DefinedTerm",
      "schema:name": "Thin Section Petrography",
      "schema:termCode": "thinSectionPetrography",
      "schema:inDefinedTermSet": "https://example.org/methods/geology"
    }
  ],
  "schema:keywords": [
    "Pacific Ocean",
    {
      "@type": "schema:DefinedTerm",
      "schema:name": "Basalt",
      "schema:identifier": "https://example.org/lithology/basalt",
      "schema:inDefinedTermSet": "https://example.org/lithology"
    }
  ],
  "schema:additionalType": [
    "schema:CreativeWork",
    {
      "@type": "schema:DefinedTerm",
      "schema:name": "geological map",
      "schema:identifier": "http://www.wikidata.org/entity/Q4884234",
      "schema:inDefinedTermSet": "https://www.wikidata.org"
    }
  ]
}
```

#### ttl
```ttl
@prefix schema1: <http://schema.org/> .

[] schema1:additionalType [ a schema1:DefinedTerm ;
            schema1:identifier "http://www.wikidata.org/entity/Q4884234" ;
            schema1:inDefinedTermSet "https://www.wikidata.org" ;
            schema1:name "geological map" ],
        "schema:CreativeWork" ;
    schema1:alternateName "Greater Ontong Java Plateau Geological Survey",
        "OJP Cenozoic Geology" ;
    schema1:keywords [ a schema1:DefinedTerm ;
            schema1:identifier "https://example.org/lithology/basalt" ;
            schema1:inDefinedTermSet "https://example.org/lithology" ;
            schema1:name "Basalt" ],
        "Pacific Ocean" ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:inDefinedTermSet "https://example.org/methods/geology" ;
            schema1:name "Thin Section Petrography" ;
            schema1:termCode "thinSectionPetrography" ],
        "Field mapping with GPS waypoint collection" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
type: object
title: DDE Optional metadata properties
description: Optional DDE-specific properties that extend CDIF optional metadata.
properties:
  schema:alternateName:
    description: Alternative names or aliases for the resource.
    anyOf:
    - type: string
    - type: array
      items:
        type: string
  schema:measurementTechnique:
    description: Techniques, methods, or instruments used in the measurement or creation
      of the data.
    type: array
    items:
      anyOf:
      - type: string
      - $ref: '#/$defs/DefinedTerm'
  schema:keywords:
    description: Additional keywords beyond the required DDE vocabulary-constrained
      keywords.
    type: array
    items:
      anyOf:
      - $ref: '#/$defs/DefinedTerm'
      - type: string
  schema:additionalType:
    description: Additional type classifications beyond the required DDE resource
      type.
    type: array
    items:
      anyOf:
      - type: string
      - $ref: '#/$defs/DefinedTerm'
$defs:
  DefinedTerm:
    $ref: https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/definedTerm/schema.yaml
x-jsonld-prefixes:
  schema: http://schema.org/
  dde: https://www.ddeworld.org/resource/

```

Links to the schema:

* YAML version: [schema.yaml](https://usgin.github.io/ddeBuildingBlocks/build/annotated/bbr/metadata/DDEproperties/ddeOptional/schema.json)
* JSON version: [schema.json](https://usgin.github.io/ddeBuildingBlocks/build/annotated/bbr/metadata/DDEproperties/ddeOptional/schema.yaml)


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
[context.jsonld](https://usgin.github.io/ddeBuildingBlocks/build/annotated/bbr/metadata/DDEproperties/ddeOptional/context.jsonld)

## Sources

* [DDE Metadata Standard](https://www.ddeworld.org)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/ddeBuildingBlocks](https://github.com/usgin/ddeBuildingBlocks)
* Path: `_sources/DDEproperties/ddeOptional`

