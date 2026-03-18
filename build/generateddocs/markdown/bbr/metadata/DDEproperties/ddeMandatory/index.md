
# DDE Mandatory metadata properties (Schema)

`dde.bbr.metadata.DDEproperties.ddeMandatory` *v0.1*

DDE profile extensions that add mandatory fields beyond CDIF discovery: DDE resource type (from ResourceTypeCode), topic category keywords (from TopicCategoryCode), acquisition type keywords (from AcquisitionTypeCode), browse graphic images, and DDE profile conformance declaration. Defines properties: schema:subjectOf, schema:additionalType, schema:keywords, schema:image. Uses building blocks: cdifMandatory (cdifProperties), definedTerm (schemaorgProperties), ddeSubject (DDEproperties), ddeResourceType (DDEproperties).

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## DDE Required Metadata Properties

Extends CDIF mandatory metadata with DDE-specific required fields:

- **Resource type** (`schema:additionalType`): At least one `schema:DefinedTerm` from the DDE `ResourceTypeCode` codelist, which defines 42 geoscience-specific resource types.
- **Topic category keywords** (`schema:keywords`): At least one `schema:DefinedTerm` from the DDE `TopicCategoryCode` codelist.
- **Acquisition type keywords** (`schema:keywords`): At least one `schema:DefinedTerm` from the DDE `AcquisitionTypeCode` codelist.
- **Browse graphics** (`schema:image`): At least one `schema:ImageObject` with a `schema:contentUrl`.
- **Profile conformance** (`schema:subjectOf`): The catalog record must declare conformance with `cdif:profile_ddeCDIF` via the ddeSubject extension.

This building block uses `allOf` to compose the CDIF mandatory base schema with the DDE-specific constraints.

## Examples

### Example DDE mandatory metadata record.
Shows a DDE geoscience metadata record with all mandatory DDE fields: resource type, topic category, acquisition type, browse graphic, and DDE profile conformance.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "dde": "https://www.ddeworld.org/resource/",
    "cdif": "https://cdif.org/profile/",
    "dcterms": "http://purl.org/dc/terms/",
    "dcat": "http://www.w3.org/ns/dcat#",
    "spdx": "http://spdx.org/rdf/terms#"
  },
  "@id": "https://doi.org/23609/53w7klh",
  "@type": [
    "schema:Dataset"
  ],
  "schema:name": "US-AZ_AZGS_1M_Lithostratigraphy",
  "schema:identifier": {
    "@type": "schema:PropertyValue",
    "schema:propertyID": "https://registry.identifiers.org/registry/doi",
    "schema:value": "doi:23609/53w7klh",
    "schema:url": "https://doi.org/23609/53w7klh"
  },
  "schema:dateModified": "2016-04-14",
  "schema:license": [
    {
      "@type": "schema:CreativeWork",
      "schema:name": "Creative Commons CC0 1.0 Universal",
      "schema:url": "https://creativecommons.org/publicdomain/zero/1.0/"
    }
  ],
  "schema:url": "https://hdl.handle.net/10150/630741",
  "schema:subjectOf": {
    "@id": "urn:uuid:c98705ae-058a-43fb-85a2-7b5209d9a4b3",
    "@type": [
      "schema:Dataset"
    ],
    "schema:additionalType": [
      "dcat:CatalogRecord"
    ],
    "schema:about": {
      "@id": "https://doi.org/23609/53w7klh"
    },
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/core/1.0/"
      },
      {
        "@id": "https://w3id.org/cdif/discovery/1.0/"
      },
      {
        "@id": "https://w3id.org/cdif/bbr/metadata/DDEproperties/ddeMandatory"
      }
    ],
    "schema:sdDatePublished": "2017-04-24"
  },
  "schema:additionalType": [
    {
      "@type": "schema:DefinedTerm",
      "schema:name": "Dataset",
      "schema:termCode": "dataset",
      "schema:inDefinedTermSet": "dde:codelist/ResourceTypeCode"
    }
  ],
  "schema:keywords": [
    {
      "@type": "schema:DefinedTerm",
      "schema:name": "Geoscientific Information",
      "schema:termCode": "geoscientificInformation",
      "schema:inDefinedTermSet": "dde:codelist/TopicCategoryCode"
    },
    {
      "@type": "schema:DefinedTerm",
      "schema:name": "Digital Conversion from Published Source",
      "schema:termCode": "digitalConversionFromPublishedSource",
      "schema:inDefinedTermSet": "dde:codelist/AcquisitionTypeCode"
    },
    {
      "@type": "schema:DefinedTerm",
      "schema:name": "Synthesis from Multiple Sources",
      "schema:termCode": "synthesisFromMultipleSources",
      "schema:inDefinedTermSet": "dde:codelist/AcquisitionTypeCode"
    },
    "United States",
    "Arizona",
    "Geology",
    "Geologic Map"
  ],
  "schema:image": [
    {
      "@type": "schema:ImageObject",
      "schema:contentUrl": "http://azgs.az.gov/repository/browse/3757.jpg",
      "schema:name": "Quick view lithostratigraphic map of Arizona",
      "schema:encodingFormat": "application/xml"
    },
    {
      "@type": "schema:ImageObject",
      "schema:contentUrl": "http://azgs.az.gov/repository/browse/2222.jpg",
      "schema:name": "Another map of Arizona",
      "schema:encodingFormat": "image/png"
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
      "dde": "https://www.ddeworld.org/resource/",
      "dcterms": "http://purl.org/dc/terms/"
    },
    "https://usgin.github.io/ddeBuildingBlocks/build/annotated/bbr/metadata/DDEproperties/ddeMandatory/context.jsonld",
    {
      "schema": "http://schema.org/",
      "dde": "https://www.ddeworld.org/resource/",
      "cdif": "https://cdif.org/profile/",
      "dcterms": "http://purl.org/dc/terms/",
      "dcat": "http://www.w3.org/ns/dcat#",
      "spdx": "http://spdx.org/rdf/terms#"
    }
  ],
  "@id": "https://doi.org/23609/53w7klh",
  "@type": [
    "schema:Dataset"
  ],
  "schema:name": "US-AZ_AZGS_1M_Lithostratigraphy",
  "schema:identifier": {
    "@type": "schema:PropertyValue",
    "schema:propertyID": "https://registry.identifiers.org/registry/doi",
    "schema:value": "doi:23609/53w7klh",
    "schema:url": "https://doi.org/23609/53w7klh"
  },
  "schema:dateModified": "2016-04-14",
  "schema:license": [
    {
      "@type": "schema:CreativeWork",
      "schema:name": "Creative Commons CC0 1.0 Universal",
      "schema:url": "https://creativecommons.org/publicdomain/zero/1.0/"
    }
  ],
  "schema:url": "https://hdl.handle.net/10150/630741",
  "schema:subjectOf": {
    "@id": "urn:uuid:c98705ae-058a-43fb-85a2-7b5209d9a4b3",
    "@type": [
      "schema:Dataset"
    ],
    "schema:additionalType": [
      "dcat:CatalogRecord"
    ],
    "schema:about": {
      "@id": "https://doi.org/23609/53w7klh"
    },
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/core/1.0/"
      },
      {
        "@id": "https://w3id.org/cdif/discovery/1.0/"
      },
      {
        "@id": "https://w3id.org/cdif/bbr/metadata/DDEproperties/ddeMandatory"
      }
    ],
    "schema:sdDatePublished": "2017-04-24"
  },
  "schema:additionalType": [
    {
      "@type": "schema:DefinedTerm",
      "schema:name": "Dataset",
      "schema:termCode": "dataset",
      "schema:inDefinedTermSet": "dde:codelist/ResourceTypeCode"
    }
  ],
  "schema:keywords": [
    {
      "@type": "schema:DefinedTerm",
      "schema:name": "Geoscientific Information",
      "schema:termCode": "geoscientificInformation",
      "schema:inDefinedTermSet": "dde:codelist/TopicCategoryCode"
    },
    {
      "@type": "schema:DefinedTerm",
      "schema:name": "Digital Conversion from Published Source",
      "schema:termCode": "digitalConversionFromPublishedSource",
      "schema:inDefinedTermSet": "dde:codelist/AcquisitionTypeCode"
    },
    {
      "@type": "schema:DefinedTerm",
      "schema:name": "Synthesis from Multiple Sources",
      "schema:termCode": "synthesisFromMultipleSources",
      "schema:inDefinedTermSet": "dde:codelist/AcquisitionTypeCode"
    },
    "United States",
    "Arizona",
    "Geology",
    "Geologic Map"
  ],
  "schema:image": [
    {
      "@type": "schema:ImageObject",
      "schema:contentUrl": "http://azgs.az.gov/repository/browse/3757.jpg",
      "schema:name": "Quick view lithostratigraphic map of Arizona",
      "schema:encodingFormat": "application/xml"
    },
    {
      "@type": "schema:ImageObject",
      "schema:contentUrl": "http://azgs.az.gov/repository/browse/2222.jpg",
      "schema:name": "Another map of Arizona",
      "schema:encodingFormat": "image/png"
    }
  ]
}
```

#### ttl
```ttl
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix schema1: <http://schema.org/> .

<https://doi.org/23609/53w7klh> a schema1:Dataset ;
    schema1:additionalType [ a schema1:DefinedTerm ;
            schema1:inDefinedTermSet "dde:codelist/ResourceTypeCode" ;
            schema1:name "Dataset" ;
            schema1:termCode "dataset" ] ;
    schema1:dateModified "2016-04-14" ;
    schema1:identifier [ a schema1:PropertyValue ;
            schema1:propertyID "https://registry.identifiers.org/registry/doi" ;
            schema1:url "https://doi.org/23609/53w7klh" ;
            schema1:value "doi:23609/53w7klh" ] ;
    schema1:image [ a schema1:ImageObject ;
            schema1:contentUrl "http://azgs.az.gov/repository/browse/2222.jpg" ;
            schema1:encodingFormat "image/png" ;
            schema1:name "Another map of Arizona" ],
        [ a schema1:ImageObject ;
            schema1:contentUrl "http://azgs.az.gov/repository/browse/3757.jpg" ;
            schema1:encodingFormat "application/xml" ;
            schema1:name "Quick view lithostratigraphic map of Arizona" ] ;
    schema1:keywords [ a schema1:DefinedTerm ;
            schema1:inDefinedTermSet "dde:codelist/TopicCategoryCode" ;
            schema1:name "Geoscientific Information" ;
            schema1:termCode "geoscientificInformation" ],
        [ a schema1:DefinedTerm ;
            schema1:inDefinedTermSet "dde:codelist/AcquisitionTypeCode" ;
            schema1:name "Synthesis from Multiple Sources" ;
            schema1:termCode "synthesisFromMultipleSources" ],
        [ a schema1:DefinedTerm ;
            schema1:inDefinedTermSet "dde:codelist/AcquisitionTypeCode" ;
            schema1:name "Digital Conversion from Published Source" ;
            schema1:termCode "digitalConversionFromPublishedSource" ],
        "Arizona",
        "Geologic Map",
        "Geology",
        "United States" ;
    schema1:license [ a schema1:CreativeWork ;
            schema1:name "Creative Commons CC0 1.0 Universal" ;
            schema1:url "https://creativecommons.org/publicdomain/zero/1.0/" ] ;
    schema1:name "US-AZ_AZGS_1M_Lithostratigraphy" ;
    schema1:subjectOf <urn:uuid:c98705ae-058a-43fb-85a2-7b5209d9a4b3> ;
    schema1:url "https://hdl.handle.net/10150/630741" .

<urn:uuid:c98705ae-058a-43fb-85a2-7b5209d9a4b3> a schema1:Dataset ;
    dcterms:conformsTo <https://w3id.org/cdif/bbr/metadata/DDEproperties/ddeMandatory>,
        <https://w3id.org/cdif/core/1.0/>,
        <https://w3id.org/cdif/discovery/1.0/> ;
    schema1:about <https://doi.org/23609/53w7klh> ;
    schema1:additionalType "dcat:CatalogRecord" ;
    schema1:sdDatePublished "2017-04-24" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: DDE Mandatory metadata properties
description: Extends CDIF mandatory metadata with DDE-specific mandatory fields.
allOf:
- $ref: '#/$defs/CdifMandatory'
- $ref: https://usgin.github.io/ddeBuildingBlocks/build/annotated/bbr/metadata/DDEproperties/ddeResourceType/schema.yaml
- type: object
  properties:
    schema:subjectOf:
      $ref: '#/$defs/DdeSubject'
    schema:keywords:
      type: array
      description: Extends base CDIF keyword schema to require DefinedTerms from both
        the DDE TopicCategoryCode and AcquisitionTypeCode codelists.
      minItems: 2
      items:
        anyOf:
        - $ref: '#/$defs/DefinedTerm'
        - type: string
      allOf:
      - contains:
          type: object
          properties:
            '@type':
              const: schema:DefinedTerm
            schema:inDefinedTermSet:
              const: dde:codelist/TopicCategoryCode
          required:
          - '@type'
          - schema:inDefinedTermSet
        minContains: 1
      - contains:
          type: object
          properties:
            '@type':
              const: schema:DefinedTerm
            schema:inDefinedTermSet:
              const: dde:codelist/AcquisitionTypeCode
          required:
          - '@type'
          - schema:inDefinedTermSet
        minContains: 1
    schema:image:
      type: array
      description: Browse graphics for the resource. At least one ImageObject is required
        for DDE metadata.
      minItems: 1
      items:
        type: object
        properties:
          '@type':
            const: schema:ImageObject
          schema:contentUrl:
            type: string
            format: uri
            description: URL to the image file
          schema:name:
            type: string
            description: Caption or title for the browse graphic
          schema:encodingFormat:
            type: string
            description: MIME type of the image
        required:
        - '@type'
        - schema:contentUrl
  required:
  - schema:additionalType
  - schema:keywords
  - schema:image
$defs:
  CdifMandatory:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/_sources/cdifProperties/cdifMandatory/schema.yaml
  DefinedTerm:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/_sources/schemaorgProperties/definedTerm/schema.yaml
  DdeSubject:
    $ref: https://usgin.github.io/ddeBuildingBlocks/build/annotated/bbr/metadata/DDEproperties/ddeSubject/schema.yaml
x-jsonld-prefixes:
  schema: http://schema.org/
  dde: https://www.ddeworld.org/resource/
  dcterms: http://purl.org/dc/terms/

```

Links to the schema:

* YAML version: [schema.yaml](https://usgin.github.io/ddeBuildingBlocks/build/annotated/bbr/metadata/DDEproperties/ddeMandatory/schema.json)
* JSON version: [schema.json](https://usgin.github.io/ddeBuildingBlocks/build/annotated/bbr/metadata/DDEproperties/ddeMandatory/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "http://schema.org/",
    "dde": "https://www.ddeworld.org/resource/",
    "dcterms": "http://purl.org/dc/terms/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://usgin.github.io/ddeBuildingBlocks/build/annotated/bbr/metadata/DDEproperties/ddeMandatory/context.jsonld)

## Sources

* [DDE Metadata Standard](https://www.ddeworld.org)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/ddeBuildingBlocks](https://github.com/usgin/ddeBuildingBlocks)
* Path: `_sources/DDEproperties/ddeMandatory`

