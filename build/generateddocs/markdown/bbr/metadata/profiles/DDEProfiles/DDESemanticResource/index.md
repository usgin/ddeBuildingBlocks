
# DDE Semantic Resource profile (Schema)

`dde.bbr.metadata.profiles.DDEProfiles.DDESemanticResource` *v0.1*

DDE profile for semantic resources (semanticResource, definedTermSet). Extends DDEDiscovery with resource type constraint.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## DDE Semantic Resource Profile

DDE profile for semantic resources. Extends DDEDiscovery with a resource type constraint.

### Resource type codes
semanticResource, definedTermSet

### Composed building blocks

1. **DDEDiscovery** — Base DDE discovery profile
2. **Resource type constraint** — `schema:termCode` must be one of the semantic resource group codes

## Examples

### DDE Semantic Resource metadata example
DDE discovery metadata for the International Chronostratigraphic Chart (ICS) vocabulary with SKOS and PDF distributions.
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
  "@id": "urn:dde:example-chronostrat-chart",
  "@type": [
    "schema:Dataset"
  ],
  "schema:name": "International Chronostratigraphic Chart v2024/12",
  "schema:description": "The International Chronostratigraphic Chart maintained by the International Commission on Stratigraphy (ICS). Defines the global standard nomenclature and boundary ages for geological time divisions (Eonothems/Eons, Erathems/Eras, Systems/Periods, Series/Epochs, Stages/Ages). Published as a controlled vocabulary with SKOS concept scheme encoding.",
  "schema:identifier": {
    "@type": "schema:PropertyValue",
    "schema:propertyID": "schema:identifier",
    "schema:name": "DOI",
    "schema:value": "10.25504/FAIRsharing.c82b6h",
    "schema:url": "https://doi.org/10.25504/FAIRsharing.c82b6h"
  },
  "schema:dateModified": "2024-12-01",
  "schema:version": "2024/12",
  "schema:inLanguage": "eng",
  "schema:license": [
    {
      "@type": "schema:CreativeWork",
      "schema:name": "Creative Commons Attribution 4.0",
      "schema:url": "https://creativecommons.org/licenses/by/4.0/"
    }
  ],
  "schema:url": "https://stratigraphy.org/chart",
  "schema:subjectOf": {
    "@id": "urn:uuid:dde-semres-catalog-record",
    "@type": [
      "schema:Dataset"
    ],
    "schema:additionalType": [
      "dcat:CatalogRecord"
    ],
    "schema:about": {
      "@id": "urn:dde:example-chronostrat-chart"
    },
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/core/1.0/"
      },
      {
        "@id": "https://w3id.org/cdif/discovery/1.0/"
      },
      {
        "@id": "https://w3id.org/cdif/bbr/metadata/profiles/DDEProfiles/DDESemanticResource"
      },
      {
        "@id": "https://w3id.org/cdif/bbr/metadata/DDEproperties/ddeMandatory"
      }
    ],
    "schema:sdDatePublished": "2024-12-01"
  },
  "schema:additionalType": [
    {
      "@type": "schema:DefinedTerm",
      "schema:name": "Vocabulary",
      "schema:termCode": "vocabulary",
      "schema:inDefinedTermSet": "dde:codelist/ResourceTypeCode"
    },
    {
      "@type": "schema:DefinedTerm",
      "schema:name": "Defined Term Set",
      "schema:termCode": "definedTermSet",
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
    "stratigraphy",
    "geological time",
    "chronostratigraphy",
    "ICS",
    "vocabulary"
  ],
  "schema:image": [
    {
      "@type": "schema:ImageObject",
      "schema:contentUrl": "https://stratigraphy.org/ICSchart/ChronostratChart2024-12-thumb.png",
      "schema:name": "chart thumbnail",
      "schema:encodingFormat": "image/png"
    }
  ],
  "schema:creator": {
    "@list": [
      {
        "@type": "schema:Organization",
        "schema:name": "International Commission on Stratigraphy",
        "schema:url": "https://stratigraphy.org/"
      }
    ]
  },
  "schema:distribution": [
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:name": "Chronostratigraphic Chart PDF",
      "schema:contentUrl": "https://stratigraphy.org/ICSchart/ChronostratChart2024-12.pdf",
      "schema:encodingFormat": [
        "application/pdf"
      ],
      "dcterms:conformsTo": [
        {
          "@id": "http://www.opengis.net/def/nil/OGC/0/missing"
        }
      ]
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:name": "Geological Time Scale RDF/SKOS",
      "schema:description": "Machine-readable SKOS concept scheme for geological time divisions",
      "schema:contentUrl": "https://resource.geosciml.org/classifierscheme/ics/ischart",
      "schema:encodingFormat": [
        "application/rdf+xml"
      ],
      "dcterms:conformsTo": [
        {
          "@id": "http://www.opengis.net/def/nil/OGC/0/missing"
        }
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
    "https://usgin.github.io/ddeBuildingBlocks/build/annotated/bbr/metadata/profiles/DDEProfiles/DDESemanticResource/context.jsonld",
    {
      "schema": "http://schema.org/",
      "dde": "https://www.ddeworld.org/resource/",
      "cdif": "https://cdif.org/profile/",
      "dcterms": "http://purl.org/dc/terms/",
      "dcat": "http://www.w3.org/ns/dcat#",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "urn:dde:example-chronostrat-chart",
  "@type": [
    "schema:Dataset"
  ],
  "schema:name": "International Chronostratigraphic Chart v2024/12",
  "schema:description": "The International Chronostratigraphic Chart maintained by the International Commission on Stratigraphy (ICS). Defines the global standard nomenclature and boundary ages for geological time divisions (Eonothems/Eons, Erathems/Eras, Systems/Periods, Series/Epochs, Stages/Ages). Published as a controlled vocabulary with SKOS concept scheme encoding.",
  "schema:identifier": {
    "@type": "schema:PropertyValue",
    "schema:propertyID": "schema:identifier",
    "schema:name": "DOI",
    "schema:value": "10.25504/FAIRsharing.c82b6h",
    "schema:url": "https://doi.org/10.25504/FAIRsharing.c82b6h"
  },
  "schema:dateModified": "2024-12-01",
  "schema:version": "2024/12",
  "schema:inLanguage": "eng",
  "schema:license": [
    {
      "@type": "schema:CreativeWork",
      "schema:name": "Creative Commons Attribution 4.0",
      "schema:url": "https://creativecommons.org/licenses/by/4.0/"
    }
  ],
  "schema:url": "https://stratigraphy.org/chart",
  "schema:subjectOf": {
    "@id": "urn:uuid:dde-semres-catalog-record",
    "@type": [
      "schema:Dataset"
    ],
    "schema:additionalType": [
      "dcat:CatalogRecord"
    ],
    "schema:about": {
      "@id": "urn:dde:example-chronostrat-chart"
    },
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/core/1.0/"
      },
      {
        "@id": "https://w3id.org/cdif/discovery/1.0/"
      },
      {
        "@id": "https://w3id.org/cdif/bbr/metadata/profiles/DDEProfiles/DDESemanticResource"
      },
      {
        "@id": "https://w3id.org/cdif/bbr/metadata/DDEproperties/ddeMandatory"
      }
    ],
    "schema:sdDatePublished": "2024-12-01"
  },
  "schema:additionalType": [
    {
      "@type": "schema:DefinedTerm",
      "schema:name": "Vocabulary",
      "schema:termCode": "vocabulary",
      "schema:inDefinedTermSet": "dde:codelist/ResourceTypeCode"
    },
    {
      "@type": "schema:DefinedTerm",
      "schema:name": "Defined Term Set",
      "schema:termCode": "definedTermSet",
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
    "stratigraphy",
    "geological time",
    "chronostratigraphy",
    "ICS",
    "vocabulary"
  ],
  "schema:image": [
    {
      "@type": "schema:ImageObject",
      "schema:contentUrl": "https://stratigraphy.org/ICSchart/ChronostratChart2024-12-thumb.png",
      "schema:name": "chart thumbnail",
      "schema:encodingFormat": "image/png"
    }
  ],
  "schema:creator": {
    "@list": [
      {
        "@type": "schema:Organization",
        "schema:name": "International Commission on Stratigraphy",
        "schema:url": "https://stratigraphy.org/"
      }
    ]
  },
  "schema:distribution": [
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:name": "Chronostratigraphic Chart PDF",
      "schema:contentUrl": "https://stratigraphy.org/ICSchart/ChronostratChart2024-12.pdf",
      "schema:encodingFormat": [
        "application/pdf"
      ],
      "dcterms:conformsTo": [
        {
          "@id": "http://www.opengis.net/def/nil/OGC/0/missing"
        }
      ]
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:name": "Geological Time Scale RDF/SKOS",
      "schema:description": "Machine-readable SKOS concept scheme for geological time divisions",
      "schema:contentUrl": "https://resource.geosciml.org/classifierscheme/ics/ischart",
      "schema:encodingFormat": [
        "application/rdf+xml"
      ],
      "dcterms:conformsTo": [
        {
          "@id": "http://www.opengis.net/def/nil/OGC/0/missing"
        }
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

<urn:dde:example-chronostrat-chart> a schema1:Dataset ;
    schema1:additionalType [ a schema1:DefinedTerm ;
            schema1:inDefinedTermSet "dde:codelist/ResourceTypeCode" ;
            schema1:name "Defined Term Set" ;
            schema1:termCode "definedTermSet" ],
        [ a schema1:DefinedTerm ;
            schema1:inDefinedTermSet "dde:codelist/ResourceTypeCode" ;
            schema1:name "Vocabulary" ;
            schema1:termCode "vocabulary" ] ;
    schema1:creator ( [ a schema1:Organization ;
                schema1:name "International Commission on Stratigraphy" ;
                schema1:url "https://stratigraphy.org/" ] ) ;
    schema1:dateModified "2024-12-01" ;
    schema1:description "The International Chronostratigraphic Chart maintained by the International Commission on Stratigraphy (ICS). Defines the global standard nomenclature and boundary ages for geological time divisions (Eonothems/Eons, Erathems/Eras, Systems/Periods, Series/Epochs, Stages/Ages). Published as a controlled vocabulary with SKOS concept scheme encoding." ;
    schema1:distribution [ a schema1:DataDownload ;
            dcterms:conformsTo <http://www.opengis.net/def/nil/OGC/0/missing> ;
            schema1:contentUrl "https://resource.geosciml.org/classifierscheme/ics/ischart" ;
            schema1:description "Machine-readable SKOS concept scheme for geological time divisions" ;
            schema1:encodingFormat "application/rdf+xml" ;
            schema1:name "Geological Time Scale RDF/SKOS" ],
        [ a schema1:DataDownload ;
            dcterms:conformsTo <http://www.opengis.net/def/nil/OGC/0/missing> ;
            schema1:contentUrl "https://stratigraphy.org/ICSchart/ChronostratChart2024-12.pdf" ;
            schema1:encodingFormat "application/pdf" ;
            schema1:name "Chronostratigraphic Chart PDF" ] ;
    schema1:identifier [ a schema1:PropertyValue ;
            schema1:name "DOI" ;
            schema1:propertyID "schema:identifier" ;
            schema1:url "https://doi.org/10.25504/FAIRsharing.c82b6h" ;
            schema1:value "10.25504/FAIRsharing.c82b6h" ] ;
    schema1:image [ a schema1:ImageObject ;
            schema1:contentUrl "https://stratigraphy.org/ICSchart/ChronostratChart2024-12-thumb.png" ;
            schema1:encodingFormat "image/png" ;
            schema1:name "chart thumbnail" ] ;
    schema1:inLanguage "eng" ;
    schema1:keywords [ a schema1:DefinedTerm ;
            schema1:inDefinedTermSet "dde:codelist/TopicCategoryCode" ;
            schema1:name "Geoscientific Information" ;
            schema1:termCode "geoscientificInformation" ],
        [ a schema1:DefinedTerm ;
            schema1:inDefinedTermSet "dde:codelist/AcquisitionTypeCode" ;
            schema1:name "Data Integration Synthesis" ;
            schema1:termCode "dataIntegrationSynthesis" ],
        "ICS",
        "chronostratigraphy",
        "geological time",
        "stratigraphy",
        "vocabulary" ;
    schema1:license [ a schema1:CreativeWork ;
            schema1:name "Creative Commons Attribution 4.0" ;
            schema1:url "https://creativecommons.org/licenses/by/4.0/" ] ;
    schema1:name "International Chronostratigraphic Chart v2024/12" ;
    schema1:subjectOf <urn:uuid:dde-semres-catalog-record> ;
    schema1:url "https://stratigraphy.org/chart" ;
    schema1:version "2024/12" .

<urn:uuid:dde-semres-catalog-record> a schema1:Dataset ;
    dcterms:conformsTo <https://w3id.org/cdif/bbr/metadata/DDEproperties/ddeMandatory>,
        <https://w3id.org/cdif/bbr/metadata/profiles/DDEProfiles/DDESemanticResource>,
        <https://w3id.org/cdif/core/1.0/>,
        <https://w3id.org/cdif/discovery/1.0/> ;
    schema1:about <urn:dde:example-chronostrat-chart> ;
    schema1:additionalType "dcat:CatalogRecord" ;
    schema1:sdDatePublished "2024-12-01" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
type: object
title: DDE Semantic Resource profile
description: DDE profile for semantic resources (semanticResource, definedTermSet).
  Extends DDEDiscovery with resource type constraint.
allOf:
- $ref: https://usgin.github.io/ddeBuildingBlocks/build/annotated/bbr/metadata/DDEproperties/ddeMandatory/schema.yaml
- $ref: https://usgin.github.io/ddeBuildingBlocks/build/annotated/bbr/metadata/DDEproperties/ddeOptional/schema.yaml
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
            - semanticResource
            - definedTermSet
        required:
        - '@type'
        - schema:inDefinedTermSet
        - schema:termCode
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

* YAML version: [schema.yaml](https://usgin.github.io/ddeBuildingBlocks/build/annotated/bbr/metadata/profiles/DDEProfiles/DDESemanticResource/schema.json)
* JSON version: [schema.json](https://usgin.github.io/ddeBuildingBlocks/build/annotated/bbr/metadata/profiles/DDEProfiles/DDESemanticResource/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "http://schema.org/",
    "dde": "https://www.ddeworld.org/resource/",
    "dcterms": "http://purl.org/dc/terms/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "geosparql": "http://www.opengis.net/ont/geosparql#",
    "spdx": "http://spdx.org/rdf/terms#",
    "time": "http://www.w3.org/2006/time#",
    "dcat": "http://www.w3.org/ns/dcat#",
    "prov": "http://www.w3.org/ns/prov#",
    "dqv": "http://www.w3.org/ns/dqv#",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://usgin.github.io/ddeBuildingBlocks/build/annotated/bbr/metadata/profiles/DDEProfiles/DDESemanticResource/context.jsonld)

## Sources

* [DDE Metadata Standard](https://www.ddeworld.org)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/ddeBuildingBlocks](https://github.com/usgin/ddeBuildingBlocks)
* Path: `_sources/profiles/DDEProfiles/DDESemanticResource`

