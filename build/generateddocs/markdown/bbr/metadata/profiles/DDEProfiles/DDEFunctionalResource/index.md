
# DDE Functional Resource profile (Schema)

`dde.bbr.metadata.profiles.DDEProfiles.DDEFunctionalResource` *v0.1*

DDE profile for functional resources (application, webApplication, model). Extends DDEDiscovery with resource type constraint and requires a relatedLink with implementationSoftware linkRelationship.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## DDE Functional Resource Profile

DDE profile for functional resources. Extends DDEDiscovery with a resource type constraint and requires a `schema:relatedLink` with `schema:linkRelationship` of `implementationSoftware`.

### Resource type codes
application, webApplication, model

### Composed building blocks

1. **DDEDiscovery** — Base DDE discovery profile
2. **Resource type constraint** — `schema:termCode` must be one of the functional resource group codes
3. **`schema:relatedLink`** — Must contain at least one link with `schema:linkRelationship: "implementationSoftware"` pointing to the software that implements the functional resource

## Examples

### DDE Functional Resource metadata example
DDE discovery metadata for a DDE Geological Time visualization web application with required implementationSoftware relatedLink.
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
  "@id": "urn:dde:example-geological-time-viewer",
  "@type": [
    "schema:Dataset"
  ],
  "schema:name": "DDE Geological Time Visualization Application",
  "schema:description": "Interactive web application for exploring the International Chronostratigraphic Chart. Enables browsing of geological time divisions from Eons to Ages, viewing boundary ages, color codes, and correlations between regional and global stratigraphic schemes. Built on the DDE knowledge graph with data from the International Commission on Stratigraphy.",
  "schema:identifier": "urn:dde:geol-time-viewer-v2",
  "schema:dateModified": "2024-09-01",
  "schema:inLanguage": "eng",
  "schema:license": [
    {
      "@type": "schema:CreativeWork",
      "schema:name": "Creative Commons Attribution 4.0",
      "schema:url": "https://creativecommons.org/licenses/by/4.0/"
    }
  ],
  "schema:url": "https://deep-time.org/geological-time/",
  "schema:subjectOf": {
    "@id": "urn:uuid:dde-funcres-catalog-record",
    "@type": [
      "schema:Dataset"
    ],
    "schema:additionalType": [
      "dcat:CatalogRecord"
    ],
    "schema:about": {
      "@id": "urn:dde:example-geological-time-viewer"
    },
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/core/1.0/"
      },
      {
        "@id": "https://w3id.org/cdif/discovery/1.0/"
      },
      {
        "@id": "https://w3id.org/cdif/bbr/metadata/profiles/DDEProfiles/DDEFunctionalResource"
      }
    ],
    "schema:sdDatePublished": "2024-09-01"
  },
  "schema:additionalType": [
    {
      "@type": "schema:DefinedTerm",
      "schema:name": "Software",
      "schema:termCode": "software",
      "schema:inDefinedTermSet": "dde:codelist/ResourceTypeCode"
    },
    {
      "@type": "schema:DefinedTerm",
      "schema:name": "Web Application",
      "schema:termCode": "webApplication",
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
    "geological time",
    "stratigraphy",
    "chronostratigraphy",
    "ICS"
  ],
  "schema:image": [
    {
      "@type": "schema:ImageObject",
      "schema:contentUrl": "https://deep-time.org/images/geol-time-viewer-screenshot.png",
      "schema:name": "Geological Time Viewer screenshot",
      "schema:encodingFormat": "image/png"
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
  "schema:relatedLink": [
    {
      "@type": "schema:LinkRole",
      "schema:linkRelationship": "implementationSoftware",
      "target": {
        "@type": "schema:EntryPoint",
        "schema:name": "DDE Geological Time Viewer Web Application",
        "schema:url": "https://deep-time.org/geological-time/"
      }
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
    "https://usgin.github.io/ddeBuildingBlocks/build/annotated/bbr/metadata/profiles/DDEProfiles/DDEFunctionalResource/context.jsonld",
    {
      "schema": "http://schema.org/",
      "dde": "https://www.ddeworld.org/resource/",
      "cdif": "https://cdif.org/profile/",
      "dcterms": "http://purl.org/dc/terms/",
      "dcat": "http://www.w3.org/ns/dcat#",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "urn:dde:example-geological-time-viewer",
  "@type": [
    "schema:Dataset"
  ],
  "schema:name": "DDE Geological Time Visualization Application",
  "schema:description": "Interactive web application for exploring the International Chronostratigraphic Chart. Enables browsing of geological time divisions from Eons to Ages, viewing boundary ages, color codes, and correlations between regional and global stratigraphic schemes. Built on the DDE knowledge graph with data from the International Commission on Stratigraphy.",
  "schema:identifier": "urn:dde:geol-time-viewer-v2",
  "schema:dateModified": "2024-09-01",
  "schema:inLanguage": "eng",
  "schema:license": [
    {
      "@type": "schema:CreativeWork",
      "schema:name": "Creative Commons Attribution 4.0",
      "schema:url": "https://creativecommons.org/licenses/by/4.0/"
    }
  ],
  "schema:url": "https://deep-time.org/geological-time/",
  "schema:subjectOf": {
    "@id": "urn:uuid:dde-funcres-catalog-record",
    "@type": [
      "schema:Dataset"
    ],
    "schema:additionalType": [
      "dcat:CatalogRecord"
    ],
    "schema:about": {
      "@id": "urn:dde:example-geological-time-viewer"
    },
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/core/1.0/"
      },
      {
        "@id": "https://w3id.org/cdif/discovery/1.0/"
      },
      {
        "@id": "https://w3id.org/cdif/bbr/metadata/profiles/DDEProfiles/DDEFunctionalResource"
      }
    ],
    "schema:sdDatePublished": "2024-09-01"
  },
  "schema:additionalType": [
    {
      "@type": "schema:DefinedTerm",
      "schema:name": "Software",
      "schema:termCode": "software",
      "schema:inDefinedTermSet": "dde:codelist/ResourceTypeCode"
    },
    {
      "@type": "schema:DefinedTerm",
      "schema:name": "Web Application",
      "schema:termCode": "webApplication",
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
    "geological time",
    "stratigraphy",
    "chronostratigraphy",
    "ICS"
  ],
  "schema:image": [
    {
      "@type": "schema:ImageObject",
      "schema:contentUrl": "https://deep-time.org/images/geol-time-viewer-screenshot.png",
      "schema:name": "Geological Time Viewer screenshot",
      "schema:encodingFormat": "image/png"
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
  "schema:relatedLink": [
    {
      "@type": "schema:LinkRole",
      "schema:linkRelationship": "implementationSoftware",
      "target": {
        "@type": "schema:EntryPoint",
        "schema:name": "DDE Geological Time Viewer Web Application",
        "schema:url": "https://deep-time.org/geological-time/"
      }
    }
  ]
}
```

#### ttl
```ttl
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix schema1: <http://schema.org/> .

<urn:dde:example-geological-time-viewer> a schema1:Dataset ;
    schema1:additionalType [ a schema1:DefinedTerm ;
            schema1:inDefinedTermSet "dde:codelist/ResourceTypeCode" ;
            schema1:name "Software" ;
            schema1:termCode "software" ],
        [ a schema1:DefinedTerm ;
            schema1:inDefinedTermSet "dde:codelist/ResourceTypeCode" ;
            schema1:name "Web Application" ;
            schema1:termCode "webApplication" ] ;
    schema1:creator ( [ a schema1:Organization ;
                schema1:name "Deep-time Digital Earth (DDE)" ;
                schema1:url "https://www.ddeworld.org/" ] ) ;
    schema1:dateModified "2024-09-01" ;
    schema1:description "Interactive web application for exploring the International Chronostratigraphic Chart. Enables browsing of geological time divisions from Eons to Ages, viewing boundary ages, color codes, and correlations between regional and global stratigraphic schemes. Built on the DDE knowledge graph with data from the International Commission on Stratigraphy." ;
    schema1:identifier "urn:dde:geol-time-viewer-v2" ;
    schema1:image [ a schema1:ImageObject ;
            schema1:contentUrl "https://deep-time.org/images/geol-time-viewer-screenshot.png" ;
            schema1:encodingFormat "image/png" ;
            schema1:name "Geological Time Viewer screenshot" ] ;
    schema1:inLanguage "eng" ;
    schema1:keywords [ a schema1:DefinedTerm ;
            schema1:inDefinedTermSet "dde:codelist/AcquisitionTypeCode" ;
            schema1:name "Data Integration Synthesis" ;
            schema1:termCode "dataIntegrationSynthesis" ],
        [ a schema1:DefinedTerm ;
            schema1:inDefinedTermSet "dde:codelist/TopicCategoryCode" ;
            schema1:name "Geoscientific Information" ;
            schema1:termCode "geoscientificInformation" ],
        "ICS",
        "chronostratigraphy",
        "geological time",
        "stratigraphy" ;
    schema1:license [ a schema1:CreativeWork ;
            schema1:name "Creative Commons Attribution 4.0" ;
            schema1:url "https://creativecommons.org/licenses/by/4.0/" ] ;
    schema1:name "DDE Geological Time Visualization Application" ;
    schema1:relatedLink [ a schema1:LinkRole ;
            schema1:linkRelationship "implementationSoftware" ] ;
    schema1:subjectOf <urn:uuid:dde-funcres-catalog-record> ;
    schema1:url "https://deep-time.org/geological-time/" .

<urn:uuid:dde-funcres-catalog-record> a schema1:Dataset ;
    dcterms:conformsTo <https://w3id.org/cdif/bbr/metadata/profiles/DDEProfiles/DDEFunctionalResource>,
        <https://w3id.org/cdif/core/1.0/>,
        <https://w3id.org/cdif/discovery/1.0/> ;
    schema1:about <urn:dde:example-geological-time-viewer> ;
    schema1:additionalType "dcat:CatalogRecord" ;
    schema1:sdDatePublished "2024-09-01" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
type: object
title: DDE Functional Resource profile
description: DDE profile for functional resources (application, webApplication, model).
  Extends DDEDiscovery with resource type constraint and requires a schema:relatedLink
  with linkRelationship "implementationSoftware".
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
            - application
            - webApplication
            - model
        required:
        - '@type'
        - schema:inDefinedTermSet
        - schema:termCode
      minContains: 1
    schema:relatedLink:
      type: array
      contains:
        type: object
        properties:
          schema:linkRelationship:
            const: implementationSoftware
        required:
        - schema:linkRelationship
      minContains: 1
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

* YAML version: [schema.yaml](https://usgin.github.io/ddeBuildingBlocks/build/annotated/bbr/metadata/profiles/DDEProfiles/DDEFunctionalResource/schema.json)
* JSON version: [schema.json](https://usgin.github.io/ddeBuildingBlocks/build/annotated/bbr/metadata/profiles/DDEProfiles/DDEFunctionalResource/schema.yaml)


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
[context.jsonld](https://usgin.github.io/ddeBuildingBlocks/build/annotated/bbr/metadata/profiles/DDEProfiles/DDEFunctionalResource/context.jsonld)

## Sources

* [DDE Metadata Standard](https://www.ddeworld.org)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/ddeBuildingBlocks](https://github.com/usgin/ddeBuildingBlocks)
* Path: `_sources/profiles/DDEProfiles/DDEFunctionalResource`

