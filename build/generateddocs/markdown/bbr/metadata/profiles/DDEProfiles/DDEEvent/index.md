
# DDE Event profile (Schema)

`dde.bbr.metadata.profiles.DDEProfiles.DDEEvent` *v0.1*

DDE profile for event resources (initiative, fieldSession). Extends DDEDiscovery with resource type constraint and requires schema:temporalCoverage.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## DDE Event Profile

DDE profile for event resources. Extends DDEDiscovery with a resource type constraint and requires `schema:temporalCoverage` (mandatory temporal extent for events).

### Resource type codes
initiative, fieldSession

### Composed building blocks

1. **DDEDiscovery** — Base DDE discovery profile
2. **Resource type constraint** — `schema:termCode` must be one of the event group codes
3. **`schema:temporalCoverage`** (required) — Temporal extent of the event

## Examples

### DDE Event metadata example
DDE discovery metadata for IODP Expedition 396 (mid-Norwegian margin) as a field session with temporal coverage for the expedition dates.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "dde": "https://www.ddeworld.org/resource/",
    "cdif": "https://cdif.org/profile/",
    "dcterms": "http://purl.org/dc/terms/",
    "dcat": "http://www.w3.org/ns/dcat#",
    "time": "http://www.w3.org/2006/time#",
    "prov": "http://www.w3.org/ns/prov#"
  },
  "@id": "urn:dde:example-iodp-expedition-396",
  "@type": [
    "schema:Dataset"
  ],
  "schema:name": "IODP Expedition 396: Mid-Norwegian Margin Magmatism and Paleoclimate Implications",
  "schema:description": "International Ocean Discovery Program Expedition 396 drilled volcanic and sedimentary sequences on the mid-Norwegian margin to investigate the causes and consequences of massive magmatism associated with the opening of the northeast Atlantic. The expedition occupied 8 sites and recovered over 1200 meters of core across the Voring and More margins.",
  "schema:identifier": "urn:iodp:expedition-396",
  "schema:dateModified": "2022-09-01",
  "schema:inLanguage": "eng",
  "schema:license": [
    {
      "@type": "schema:CreativeWork",
      "schema:name": "IODP Data Policy",
      "schema:url": "https://www.iodp.org/policies-and-guidelines/data-policy"
    }
  ],
  "schema:url": "https://www.iodp.org/expedition396",
  "schema:subjectOf": {
    "@id": "urn:uuid:dde-event-catalog-record",
    "@type": [
      "schema:Dataset"
    ],
    "schema:additionalType": [
      "dcat:CatalogRecord"
    ],
    "schema:about": {
      "@id": "urn:dde:example-iodp-expedition-396"
    },
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/core/1.0/"
      },
      {
        "@id": "https://w3id.org/cdif/discovery/1.0/"
      },
      {
        "@id": "https://w3id.org/cdif/bbr/metadata/profiles/DDEProfiles/DDEEvent"
      }
    ],
    "schema:sdDatePublished": "2022-09-01"
  },
  "schema:additionalType": [
    {
      "@type": "schema:DefinedTerm",
      "schema:name": "Field Session",
      "schema:termCode": "fieldSession",
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
      "schema:name": "Field Campaign Expedition",
      "schema:termCode": "fieldCampaignExpedition",
      "schema:inDefinedTermSet": "dde:codelist/AcquisitionTypeCode"
    },
    "IODP",
    "ocean drilling",
    "volcanic margin",
    "paleoclimate",
    "mid-Norwegian margin"
  ],
  "schema:image": [
    {
      "@type": "schema:ImageObject",
      "schema:contentUrl": "https://www.iodp.org/images/exp396-sites.png",
      "schema:name": "Expedition 396 drill site locations",
      "schema:encodingFormat": "image/png"
    }
  ],
  "schema:spatialCoverage": [
    {
      "@type": "schema:Place",
      "schema:geo": {
        "@type": "schema:GeoShape",
        "schema:box": "63.0 1.0 67.5 6.5"
      }
    }
  ],
  "schema:temporalCoverage": [
    {
      "@type": "time:ProperInterval",
      "time:hasBeginning": {
        "@type": "time:Instant",
        "time:inXSDDateTime": "2021-08-05"
      },
      "time:hasEnd": {
        "@type": "time:Instant",
        "time:inXSDDateTime": "2021-10-05"
      }
    }
  ],
  "schema:creator": {
    "@list": [
      {
        "@type": "schema:Organization",
        "schema:name": "International Ocean Discovery Program",
        "schema:url": "https://www.iodp.org/"
      }
    ]
  }
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
      "time": "http://www.w3.org/2006/time#",
      "prov": "http://www.w3.org/ns/prov#"
    },
    "https://usgin.github.io/ddeBuildingBlocks/build/annotated/bbr/metadata/profiles/DDEProfiles/DDEEvent/context.jsonld",
    {
      "schema": "http://schema.org/",
      "dde": "https://www.ddeworld.org/resource/",
      "cdif": "https://cdif.org/profile/",
      "dcterms": "http://purl.org/dc/terms/",
      "dcat": "http://www.w3.org/ns/dcat#",
      "time": "http://www.w3.org/2006/time#",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "urn:dde:example-iodp-expedition-396",
  "@type": [
    "schema:Dataset"
  ],
  "schema:name": "IODP Expedition 396: Mid-Norwegian Margin Magmatism and Paleoclimate Implications",
  "schema:description": "International Ocean Discovery Program Expedition 396 drilled volcanic and sedimentary sequences on the mid-Norwegian margin to investigate the causes and consequences of massive magmatism associated with the opening of the northeast Atlantic. The expedition occupied 8 sites and recovered over 1200 meters of core across the Voring and More margins.",
  "schema:identifier": "urn:iodp:expedition-396",
  "schema:dateModified": "2022-09-01",
  "schema:inLanguage": "eng",
  "schema:license": [
    {
      "@type": "schema:CreativeWork",
      "schema:name": "IODP Data Policy",
      "schema:url": "https://www.iodp.org/policies-and-guidelines/data-policy"
    }
  ],
  "schema:url": "https://www.iodp.org/expedition396",
  "schema:subjectOf": {
    "@id": "urn:uuid:dde-event-catalog-record",
    "@type": [
      "schema:Dataset"
    ],
    "schema:additionalType": [
      "dcat:CatalogRecord"
    ],
    "schema:about": {
      "@id": "urn:dde:example-iodp-expedition-396"
    },
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/core/1.0/"
      },
      {
        "@id": "https://w3id.org/cdif/discovery/1.0/"
      },
      {
        "@id": "https://w3id.org/cdif/bbr/metadata/profiles/DDEProfiles/DDEEvent"
      }
    ],
    "schema:sdDatePublished": "2022-09-01"
  },
  "schema:additionalType": [
    {
      "@type": "schema:DefinedTerm",
      "schema:name": "Field Session",
      "schema:termCode": "fieldSession",
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
      "schema:name": "Field Campaign Expedition",
      "schema:termCode": "fieldCampaignExpedition",
      "schema:inDefinedTermSet": "dde:codelist/AcquisitionTypeCode"
    },
    "IODP",
    "ocean drilling",
    "volcanic margin",
    "paleoclimate",
    "mid-Norwegian margin"
  ],
  "schema:image": [
    {
      "@type": "schema:ImageObject",
      "schema:contentUrl": "https://www.iodp.org/images/exp396-sites.png",
      "schema:name": "Expedition 396 drill site locations",
      "schema:encodingFormat": "image/png"
    }
  ],
  "schema:spatialCoverage": [
    {
      "@type": "schema:Place",
      "schema:geo": {
        "@type": "schema:GeoShape",
        "schema:box": "63.0 1.0 67.5 6.5"
      }
    }
  ],
  "schema:temporalCoverage": [
    {
      "@type": "time:ProperInterval",
      "time:hasBeginning": {
        "@type": "time:Instant",
        "time:inXSDDateTime": "2021-08-05"
      },
      "time:hasEnd": {
        "@type": "time:Instant",
        "time:inXSDDateTime": "2021-10-05"
      }
    }
  ],
  "schema:creator": {
    "@list": [
      {
        "@type": "schema:Organization",
        "schema:name": "International Ocean Discovery Program",
        "schema:url": "https://www.iodp.org/"
      }
    ]
  }
}
```

#### ttl
```ttl
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix schema1: <http://schema.org/> .
@prefix time: <http://www.w3.org/2006/time#> .

<urn:dde:example-iodp-expedition-396> a schema1:Dataset ;
    schema1:additionalType [ a schema1:DefinedTerm ;
            schema1:inDefinedTermSet "dde:codelist/ResourceTypeCode" ;
            schema1:name "Field Session" ;
            schema1:termCode "fieldSession" ] ;
    schema1:creator ( [ a schema1:Organization ;
                schema1:name "International Ocean Discovery Program" ;
                schema1:url "https://www.iodp.org/" ] ) ;
    schema1:dateModified "2022-09-01" ;
    schema1:description "International Ocean Discovery Program Expedition 396 drilled volcanic and sedimentary sequences on the mid-Norwegian margin to investigate the causes and consequences of massive magmatism associated with the opening of the northeast Atlantic. The expedition occupied 8 sites and recovered over 1200 meters of core across the Voring and More margins." ;
    schema1:identifier "urn:iodp:expedition-396" ;
    schema1:image [ a schema1:ImageObject ;
            schema1:contentUrl "https://www.iodp.org/images/exp396-sites.png" ;
            schema1:encodingFormat "image/png" ;
            schema1:name "Expedition 396 drill site locations" ] ;
    schema1:inLanguage "eng" ;
    schema1:keywords [ a schema1:DefinedTerm ;
            schema1:inDefinedTermSet "dde:codelist/AcquisitionTypeCode" ;
            schema1:name "Field Campaign Expedition" ;
            schema1:termCode "fieldCampaignExpedition" ],
        [ a schema1:DefinedTerm ;
            schema1:inDefinedTermSet "dde:codelist/TopicCategoryCode" ;
            schema1:name "Geoscientific Information" ;
            schema1:termCode "geoscientificInformation" ],
        "IODP",
        "mid-Norwegian margin",
        "ocean drilling",
        "paleoclimate",
        "volcanic margin" ;
    schema1:license [ a schema1:CreativeWork ;
            schema1:name "IODP Data Policy" ;
            schema1:url "https://www.iodp.org/policies-and-guidelines/data-policy" ] ;
    schema1:name "IODP Expedition 396: Mid-Norwegian Margin Magmatism and Paleoclimate Implications" ;
    schema1:spatialCoverage [ a schema1:Place ;
            schema1:geo [ a schema1:GeoShape ;
                    schema1:box "63.0 1.0 67.5 6.5" ] ] ;
    schema1:subjectOf <urn:uuid:dde-event-catalog-record> ;
    schema1:temporalCoverage [ a time:ProperInterval ;
            time:hasBeginning [ a time:Instant ;
                    time:inXSDDateTime "2021-08-05" ] ;
            time:hasEnd [ a time:Instant ;
                    time:inXSDDateTime "2021-10-05" ] ] ;
    schema1:url "https://www.iodp.org/expedition396" .

<urn:uuid:dde-event-catalog-record> a schema1:Dataset ;
    dcterms:conformsTo <https://w3id.org/cdif/bbr/metadata/profiles/DDEProfiles/DDEEvent>,
        <https://w3id.org/cdif/core/1.0/>,
        <https://w3id.org/cdif/discovery/1.0/> ;
    schema1:about <urn:dde:example-iodp-expedition-396> ;
    schema1:additionalType "dcat:CatalogRecord" ;
    schema1:sdDatePublished "2022-09-01" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
type: object
title: DDE Event profile
description: DDE profile for event resources (initiative, fieldSession). Extends DDEDiscovery
  with resource type constraint and requires schema:temporalCoverage (mandatory temporal
  extent for events).
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
            - initiative
            - fieldSession
        required:
        - '@type'
        - schema:inDefinedTermSet
        - schema:termCode
      minContains: 1
  required:
  - schema:temporalCoverage
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

* YAML version: [schema.yaml](https://usgin.github.io/ddeBuildingBlocks/build/annotated/bbr/metadata/profiles/DDEProfiles/DDEEvent/schema.json)
* JSON version: [schema.json](https://usgin.github.io/ddeBuildingBlocks/build/annotated/bbr/metadata/profiles/DDEProfiles/DDEEvent/schema.yaml)


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
[context.jsonld](https://usgin.github.io/ddeBuildingBlocks/build/annotated/bbr/metadata/profiles/DDEProfiles/DDEEvent/context.jsonld)

## Sources

* [DDE Metadata Standard](https://www.ddeworld.org)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/ddeBuildingBlocks](https://github.com/usgin/ddeBuildingBlocks)
* Path: `_sources/profiles/DDEProfiles/DDEEvent`

