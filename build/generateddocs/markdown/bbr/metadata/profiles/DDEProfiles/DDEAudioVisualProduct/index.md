
# DDE AudioVisual Product profile (Schema)

`dde.bbr.metadata.profiles.DDEProfiles.DDEAudioVisualProduct` *v0.1*

DDE profile for audiovisual resources (movie, sound). Extends DDEDiscovery with resource type constraint and schema:duration.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## DDE AudioVisual Product Profile

DDE profile for audiovisual resources. Extends DDEDiscovery with a resource type constraint and adds `schema:duration`.

### Resource type codes
movie, sound

### Composed building blocks

1. **DDEDiscovery** — Base DDE discovery profile
2. **Resource type constraint** — `schema:termCode` must be one of the audiovisual group codes
3. **`schema:duration`** (optional) — Duration in ISO 8601 format (e.g., PT1H30M, PT45S)

## Examples

### DDE AudioVisual Product metadata example
DDE discovery metadata for an educational video on plate tectonics with ISO 8601 duration (PT25M) and MP4 distribution.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "dde": "https://www.ddeworld.org/resource/",
    "cdif": "https://cdif.org/profile/",
    "dcterms": "http://purl.org/dc/terms/",
    "dcat": "http://www.w3.org/ns/dcat#",
    "prov": "http://www.w3.org/ns/prov#"
  },
  "@id": "urn:dde:example-plate-tectonics-video",
  "@type": [
    "schema:Dataset"
  ],
  "schema:name": "Plate Tectonics Explained: Earth's Dynamic Surface",
  "schema:description": "Educational video explaining the fundamentals of plate tectonics, including continental drift, seafloor spreading, subduction zones, and transform boundaries. Features animations of plate reconstructions from 250 Ma to present day, mid-ocean ridge processes, and earthquake/volcano distributions along plate boundaries. Produced for university-level Earth science courses.",
  "schema:identifier": "urn:dde:video-plate-tectonics-edu",
  "schema:dateModified": "2023-09-15",
  "schema:inLanguage": "eng",
  "schema:license": [
    {
      "@type": "schema:CreativeWork",
      "schema:name": "Creative Commons Attribution-NonCommercial 4.0",
      "schema:url": "https://creativecommons.org/licenses/by-nc/4.0/"
    }
  ],
  "schema:url": "https://example.org/videos/plate-tectonics-explained",
  "schema:subjectOf": {
    "@id": "urn:uuid:dde-audiovisual-catalog-record",
    "@type": [
      "schema:Dataset"
    ],
    "schema:additionalType": [
      "dcat:CatalogRecord"
    ],
    "schema:about": {
      "@id": "urn:dde:example-plate-tectonics-video"
    },
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/core/1.0/"
      },
      {
        "@id": "https://w3id.org/cdif/discovery/1.0/"
      },
      {
        "@id": "https://w3id.org/cdif/bbr/metadata/profiles/DDEProfiles/DDEAudioVisualProduct"
      }
    ],
    "schema:sdDatePublished": "2023-09-15"
  },
  "schema:additionalType": [
    {
      "@type": "schema:DefinedTerm",
      "schema:name": "Product",
      "schema:termCode": "product",
      "schema:inDefinedTermSet": "dde:codelist/ResourceTypeCode"
    },
    {
      "@type": "schema:DefinedTerm",
      "schema:name": "Movie",
      "schema:termCode": "movie",
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
      "schema:name": "Data Integration Synthesis",
      "schema:termCode": "dataIntegrationSynthesis",
      "schema:inDefinedTermSet": "dde:codelist/AcquisitionTypeCode"
    },
    "plate tectonics",
    "educational video",
    "continental drift",
    "earth science"
  ],
  "schema:image": [
    {
      "@type": "schema:ImageObject",
      "schema:contentUrl": "https://example.org/thumbnails/plate-tectonics-video-thumb.jpg",
      "schema:name": "video thumbnail",
      "schema:encodingFormat": "image/jpeg"
    }
  ],
  "schema:creator": {
    "@list": [
      {
        "@type": "schema:Organization",
        "schema:name": "Deep-time Digital Earth (DDE)",
        "schema:url": "https://www.ddeworld.org/"
      }
    ]
  },
  "schema:duration": "PT25M",
  "schema:distribution": [
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:name": "Video MP4",
      "schema:description": "Full HD video file",
      "schema:contentUrl": "https://example.org/videos/plate-tectonics-explained.mp4",
      "schema:encodingFormat": [
        "video/mp4"
      ]
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
      "cdif": "https://cdif.org/profile/",
      "dcterms": "http://purl.org/dc/terms/",
      "dcat": "http://www.w3.org/ns/dcat#",
      "prov": "http://www.w3.org/ns/prov#"
    },
    "https://usgin.github.io/ddeBuildingBlocks/build/annotated/bbr/metadata/profiles/DDEProfiles/DDEAudioVisualProduct/context.jsonld",
    {
      "schema": "http://schema.org/",
      "dde": "https://www.ddeworld.org/resource/",
      "cdif": "https://cdif.org/profile/",
      "dcterms": "http://purl.org/dc/terms/",
      "dcat": "http://www.w3.org/ns/dcat#",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "urn:dde:example-plate-tectonics-video",
  "@type": [
    "schema:Dataset"
  ],
  "schema:name": "Plate Tectonics Explained: Earth's Dynamic Surface",
  "schema:description": "Educational video explaining the fundamentals of plate tectonics, including continental drift, seafloor spreading, subduction zones, and transform boundaries. Features animations of plate reconstructions from 250 Ma to present day, mid-ocean ridge processes, and earthquake/volcano distributions along plate boundaries. Produced for university-level Earth science courses.",
  "schema:identifier": "urn:dde:video-plate-tectonics-edu",
  "schema:dateModified": "2023-09-15",
  "schema:inLanguage": "eng",
  "schema:license": [
    {
      "@type": "schema:CreativeWork",
      "schema:name": "Creative Commons Attribution-NonCommercial 4.0",
      "schema:url": "https://creativecommons.org/licenses/by-nc/4.0/"
    }
  ],
  "schema:url": "https://example.org/videos/plate-tectonics-explained",
  "schema:subjectOf": {
    "@id": "urn:uuid:dde-audiovisual-catalog-record",
    "@type": [
      "schema:Dataset"
    ],
    "schema:additionalType": [
      "dcat:CatalogRecord"
    ],
    "schema:about": {
      "@id": "urn:dde:example-plate-tectonics-video"
    },
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/core/1.0/"
      },
      {
        "@id": "https://w3id.org/cdif/discovery/1.0/"
      },
      {
        "@id": "https://w3id.org/cdif/bbr/metadata/profiles/DDEProfiles/DDEAudioVisualProduct"
      }
    ],
    "schema:sdDatePublished": "2023-09-15"
  },
  "schema:additionalType": [
    {
      "@type": "schema:DefinedTerm",
      "schema:name": "Product",
      "schema:termCode": "product",
      "schema:inDefinedTermSet": "dde:codelist/ResourceTypeCode"
    },
    {
      "@type": "schema:DefinedTerm",
      "schema:name": "Movie",
      "schema:termCode": "movie",
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
      "schema:name": "Data Integration Synthesis",
      "schema:termCode": "dataIntegrationSynthesis",
      "schema:inDefinedTermSet": "dde:codelist/AcquisitionTypeCode"
    },
    "plate tectonics",
    "educational video",
    "continental drift",
    "earth science"
  ],
  "schema:image": [
    {
      "@type": "schema:ImageObject",
      "schema:contentUrl": "https://example.org/thumbnails/plate-tectonics-video-thumb.jpg",
      "schema:name": "video thumbnail",
      "schema:encodingFormat": "image/jpeg"
    }
  ],
  "schema:creator": {
    "@list": [
      {
        "@type": "schema:Organization",
        "schema:name": "Deep-time Digital Earth (DDE)",
        "schema:url": "https://www.ddeworld.org/"
      }
    ]
  },
  "schema:duration": "PT25M",
  "schema:distribution": [
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:name": "Video MP4",
      "schema:description": "Full HD video file",
      "schema:contentUrl": "https://example.org/videos/plate-tectonics-explained.mp4",
      "schema:encodingFormat": [
        "video/mp4"
      ]
    }
  ]
}
```

#### ttl
```ttl
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix schema1: <http://schema.org/> .

<urn:dde:example-plate-tectonics-video> a schema1:Dataset ;
    schema1:additionalType [ a schema1:DefinedTerm ;
            schema1:inDefinedTermSet "dde:codelist/ResourceTypeCode" ;
            schema1:name "Movie" ;
            schema1:termCode "movie" ],
        [ a schema1:DefinedTerm ;
            schema1:inDefinedTermSet "dde:codelist/ResourceTypeCode" ;
            schema1:name "Product" ;
            schema1:termCode "product" ] ;
    schema1:creator ( [ a schema1:Organization ;
                schema1:name "Deep-time Digital Earth (DDE)" ;
                schema1:url "https://www.ddeworld.org/" ] ) ;
    schema1:dateModified "2023-09-15" ;
    schema1:description "Educational video explaining the fundamentals of plate tectonics, including continental drift, seafloor spreading, subduction zones, and transform boundaries. Features animations of plate reconstructions from 250 Ma to present day, mid-ocean ridge processes, and earthquake/volcano distributions along plate boundaries. Produced for university-level Earth science courses." ;
    schema1:distribution [ a schema1:DataDownload ;
            schema1:contentUrl "https://example.org/videos/plate-tectonics-explained.mp4" ;
            schema1:description "Full HD video file" ;
            schema1:encodingFormat "video/mp4" ;
            schema1:name "Video MP4" ] ;
    schema1:duration "PT25M" ;
    schema1:identifier "urn:dde:video-plate-tectonics-edu" ;
    schema1:image [ a schema1:ImageObject ;
            schema1:contentUrl "https://example.org/thumbnails/plate-tectonics-video-thumb.jpg" ;
            schema1:encodingFormat "image/jpeg" ;
            schema1:name "video thumbnail" ] ;
    schema1:inLanguage "eng" ;
    schema1:keywords [ a schema1:DefinedTerm ;
            schema1:inDefinedTermSet "dde:codelist/TopicCategoryCode" ;
            schema1:name "Geoscientific Information" ;
            schema1:termCode "geoscientificInformation" ],
        [ a schema1:DefinedTerm ;
            schema1:inDefinedTermSet "dde:codelist/AcquisitionTypeCode" ;
            schema1:name "Data Integration Synthesis" ;
            schema1:termCode "dataIntegrationSynthesis" ],
        "continental drift",
        "earth science",
        "educational video",
        "plate tectonics" ;
    schema1:license [ a schema1:CreativeWork ;
            schema1:name "Creative Commons Attribution-NonCommercial 4.0" ;
            schema1:url "https://creativecommons.org/licenses/by-nc/4.0/" ] ;
    schema1:name "Plate Tectonics Explained: Earth's Dynamic Surface" ;
    schema1:subjectOf <urn:uuid:dde-audiovisual-catalog-record> ;
    schema1:url "https://example.org/videos/plate-tectonics-explained" .

<urn:uuid:dde-audiovisual-catalog-record> a schema1:Dataset ;
    dcterms:conformsTo <https://w3id.org/cdif/bbr/metadata/profiles/DDEProfiles/DDEAudioVisualProduct>,
        <https://w3id.org/cdif/core/1.0/>,
        <https://w3id.org/cdif/discovery/1.0/> ;
    schema1:about <urn:dde:example-plate-tectonics-video> ;
    schema1:additionalType "dcat:CatalogRecord" ;
    schema1:sdDatePublished "2023-09-15" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
type: object
title: DDE AudioVisual Product profile
description: DDE profile for audiovisual resources (movie, sound). Extends DDEDiscovery
  with resource type constraint and schema:duration.
allOf:
- $ref: https://usgin.github.io/ddeBuildingBlocks/build/annotated/bbr/metadata/profiles/DDEProfiles/DDEDiscovery/schema.yaml
- properties:
    schema:additionalType:
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
            - movie
            - sound
        required:
        - '@type'
        - schema:inDefinedTermSet
        - schema:termCode
      minContains: 1
    schema:duration:
      type: string
      description: Duration in ISO 8601 format (e.g., PT1H30M, PT45S).
x-jsonld-prefixes:
  schema: http://schema.org/
  cdi: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/
  dcterms: http://purl.org/dc/terms/
  geosparql: http://www.opengis.net/ont/geosparql#
  spdx: http://spdx.org/rdf/terms#
  time: http://www.w3.org/2006/time#
  dde: https://www.ddeworld.org/resource/
  dcat: http://www.w3.org/ns/dcat#
  prov: http://www.w3.org/ns/prov#
  dqv: http://www.w3.org/ns/dqv#

```

Links to the schema:

* YAML version: [schema.yaml](https://usgin.github.io/ddeBuildingBlocks/build/annotated/bbr/metadata/profiles/DDEProfiles/DDEAudioVisualProduct/schema.json)
* JSON version: [schema.json](https://usgin.github.io/ddeBuildingBlocks/build/annotated/bbr/metadata/profiles/DDEProfiles/DDEAudioVisualProduct/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "http://schema.org/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "dcterms": "http://purl.org/dc/terms/",
    "geosparql": "http://www.opengis.net/ont/geosparql#",
    "spdx": "http://spdx.org/rdf/terms#",
    "time": "http://www.w3.org/2006/time#",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "dde": "https://www.ddeworld.org/resource/",
    "dcat": "http://www.w3.org/ns/dcat#",
    "prov": "http://www.w3.org/ns/prov#",
    "dqv": "http://www.w3.org/ns/dqv#",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://usgin.github.io/ddeBuildingBlocks/build/annotated/bbr/metadata/profiles/DDEProfiles/DDEAudioVisualProduct/context.jsonld)

## Sources

* [DDE Metadata Standard](https://www.ddeworld.org)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/ddeBuildingBlocks](https://github.com/usgin/ddeBuildingBlocks)
* Path: `_sources/profiles/DDEProfiles/DDEAudioVisualProduct`

