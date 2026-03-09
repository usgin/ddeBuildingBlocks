
# DDE Document profile (Schema)

`dde.bbr.metadata.profiles.DDEProfiles.DDEDocument` *v0.1*

DDE profile for document resources (document, article, thesis, book, poster, webPage). Extends DDEDiscovery with resource type constraint.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## DDE Document Profile

DDE profile for document resources. Extends DDEDiscovery with a resource type constraint.

### Resource type codes
document, article, thesis, book, poster, webPage

### Composed building blocks

1. **DDEDiscovery** — Base DDE discovery profile
2. **Resource type constraint** — `schema:termCode` must be one of the document group codes

## Examples

### DDE Document metadata example
DDE discovery metadata for a published research article on global plate tectonics and paleogeography with DOI identifier and creator.
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
    "@id": "urn:dde:example-plate-tectonics-article",
    "@type": [
        "schema:Dataset"
    ],
    "schema:name": "Global Plate Tectonics and Paleogeography Since the Late Paleozoic",
    "schema:description": "Published research article presenting a comprehensive plate tectonic and paleogeographic model for the Earth from the Late Paleozoic to the present day (410 Ma to 0 Ma). Includes digital reconstructions of continental configurations, ocean basins, and major tectonic boundaries through geological time.",
    "schema:identifier": {
        "@type": "schema:PropertyValue",
        "schema:propertyID": "schema:identifier",
        "schema:name": "DOI",
        "schema:value": "10.1016/j.earscirev.2021.103477",
        "schema:url": "https://doi.org/10.1016/j.earscirev.2021.103477"
    },
    "schema:dateModified": "2021-02-15",
    "schema:datePublished": "2021-02-15",
    "schema:inLanguage": "eng",
    "schema:license": [
        {
            "@type": "schema:CreativeWork",
            "schema:name": "Elsevier User License",
            "schema:url": "https://www.elsevier.com/about/policies/open-access-licenses"
        }
    ],
    "schema:subjectOf": {
        "@id": "urn:uuid:dde-document-catalog-record",
        "@type": [
            "schema:Dataset"
        ],
        "schema:additionalType": [
            "dcat:CatalogRecord"
        ],
        "schema:about": {
            "@id": "urn:dde:example-plate-tectonics-article"
        },
        "dcterms:conformsTo": [
            {
                "@id": "https://w3id.org/cdif/bbr/metadata/profiles/DDEProfiles/DDEDocument"
            }
        ],
        "schema:sdDatePublished": "2021-02-15"
    },
    "schema:additionalType": [
        {
            "@type": "schema:DefinedTerm",
            "schema:name": "Document",
            "schema:termCode": "document",
            "schema:inDefinedTermSet": "dde:codelist/ResourceTypeCode"
        },
        {
            "@type": "schema:DefinedTerm",
            "schema:name": "Article",
            "schema:termCode": "article",
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
        "paleogeography",
        "Pangaea",
        "continental drift"
    ],
    "schema:image": [
        {
            "@type": "schema:ImageObject",
            "schema:contentUrl": "https://doi.org/10.1016/j.earscirev.2021.103477/thumbnail.jpg",
            "schema:name": "article thumbnail",
            "schema:encodingFormat": "image/jpeg"
        }
    ],
    "schema:creator": {
        "@list": [
            {
                "@type": "schema:Person",
                "schema:name": "Dietmar Muller",
                "schema:identifier": "https://orcid.org/0000-0002-3334-5764",
                "schema:affiliation": {
                    "@type": "schema:Organization",
                    "schema:name": "University of Sydney"
                }
            }
        ]
    },
    "schema:distribution": [
        {
            "@type": [
                "schema:DataDownload"
            ],
            "schema:name": "Article PDF",
            "schema:contentUrl": "https://doi.org/10.1016/j.earscirev.2021.103477",
            "schema:encodingFormat": [
                "application/pdf"
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
    "https://usgin.github.io/ddeBuildingBlocks/build/annotated/bbr/metadata/profiles/DDEProfiles/DDEDocument/context.jsonld",
    {
      "schema": "http://schema.org/",
      "dde": "https://www.ddeworld.org/resource/",
      "cdif": "https://cdif.org/profile/",
      "dcterms": "http://purl.org/dc/terms/",
      "dcat": "http://www.w3.org/ns/dcat#",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "urn:dde:example-plate-tectonics-article",
  "@type": [
    "schema:Dataset"
  ],
  "schema:name": "Global Plate Tectonics and Paleogeography Since the Late Paleozoic",
  "schema:description": "Published research article presenting a comprehensive plate tectonic and paleogeographic model for the Earth from the Late Paleozoic to the present day (410 Ma to 0 Ma). Includes digital reconstructions of continental configurations, ocean basins, and major tectonic boundaries through geological time.",
  "schema:identifier": {
    "@type": "schema:PropertyValue",
    "schema:propertyID": "schema:identifier",
    "schema:name": "DOI",
    "schema:value": "10.1016/j.earscirev.2021.103477",
    "schema:url": "https://doi.org/10.1016/j.earscirev.2021.103477"
  },
  "schema:dateModified": "2021-02-15",
  "schema:datePublished": "2021-02-15",
  "schema:inLanguage": "eng",
  "schema:license": [
    {
      "@type": "schema:CreativeWork",
      "schema:name": "Elsevier User License",
      "schema:url": "https://www.elsevier.com/about/policies/open-access-licenses"
    }
  ],
  "schema:subjectOf": {
    "@id": "urn:uuid:dde-document-catalog-record",
    "@type": [
      "schema:Dataset"
    ],
    "schema:additionalType": [
      "dcat:CatalogRecord"
    ],
    "schema:about": {
      "@id": "urn:dde:example-plate-tectonics-article"
    },
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/bbr/metadata/profiles/DDEProfiles/DDEDocument"
      }
    ],
    "schema:sdDatePublished": "2021-02-15"
  },
  "schema:additionalType": [
    {
      "@type": "schema:DefinedTerm",
      "schema:name": "Document",
      "schema:termCode": "document",
      "schema:inDefinedTermSet": "dde:codelist/ResourceTypeCode"
    },
    {
      "@type": "schema:DefinedTerm",
      "schema:name": "Article",
      "schema:termCode": "article",
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
    "paleogeography",
    "Pangaea",
    "continental drift"
  ],
  "schema:image": [
    {
      "@type": "schema:ImageObject",
      "schema:contentUrl": "https://doi.org/10.1016/j.earscirev.2021.103477/thumbnail.jpg",
      "schema:name": "article thumbnail",
      "schema:encodingFormat": "image/jpeg"
    }
  ],
  "schema:creator": {
    "@list": [
      {
        "@type": "schema:Person",
        "schema:name": "Dietmar Muller",
        "schema:identifier": "https://orcid.org/0000-0002-3334-5764",
        "schema:affiliation": {
          "@type": "schema:Organization",
          "schema:name": "University of Sydney"
        }
      }
    ]
  },
  "schema:distribution": [
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:name": "Article PDF",
      "schema:contentUrl": "https://doi.org/10.1016/j.earscirev.2021.103477",
      "schema:encodingFormat": [
        "application/pdf"
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

<urn:dde:example-plate-tectonics-article> a schema1:Dataset ;
    schema1:additionalType [ a schema1:DefinedTerm ;
            schema1:inDefinedTermSet "dde:codelist/ResourceTypeCode" ;
            schema1:name "Article" ;
            schema1:termCode "article" ],
        [ a schema1:DefinedTerm ;
            schema1:inDefinedTermSet "dde:codelist/ResourceTypeCode" ;
            schema1:name "Document" ;
            schema1:termCode "document" ] ;
    schema1:creator ( [ a schema1:Person ;
                schema1:affiliation [ a schema1:Organization ;
                        schema1:name "University of Sydney" ] ;
                schema1:identifier "https://orcid.org/0000-0002-3334-5764" ;
                schema1:name "Dietmar Muller" ] ) ;
    schema1:dateModified "2021-02-15" ;
    schema1:datePublished "2021-02-15" ;
    schema1:description "Published research article presenting a comprehensive plate tectonic and paleogeographic model for the Earth from the Late Paleozoic to the present day (410 Ma to 0 Ma). Includes digital reconstructions of continental configurations, ocean basins, and major tectonic boundaries through geological time." ;
    schema1:distribution [ a schema1:DataDownload ;
            schema1:contentUrl "https://doi.org/10.1016/j.earscirev.2021.103477" ;
            schema1:encodingFormat "application/pdf" ;
            schema1:name "Article PDF" ] ;
    schema1:identifier [ a schema1:PropertyValue ;
            schema1:name "DOI" ;
            schema1:propertyID "schema:identifier" ;
            schema1:url "https://doi.org/10.1016/j.earscirev.2021.103477" ;
            schema1:value "10.1016/j.earscirev.2021.103477" ] ;
    schema1:image [ a schema1:ImageObject ;
            schema1:contentUrl "https://doi.org/10.1016/j.earscirev.2021.103477/thumbnail.jpg" ;
            schema1:encodingFormat "image/jpeg" ;
            schema1:name "article thumbnail" ] ;
    schema1:inLanguage "eng" ;
    schema1:keywords [ a schema1:DefinedTerm ;
            schema1:inDefinedTermSet "dde:codelist/AcquisitionTypeCode" ;
            schema1:name "Data Integration Synthesis" ;
            schema1:termCode "dataIntegrationSynthesis" ],
        [ a schema1:DefinedTerm ;
            schema1:inDefinedTermSet "dde:codelist/TopicCategoryCode" ;
            schema1:name "Geoscientific Information" ;
            schema1:termCode "geoscientificInformation" ],
        "Pangaea",
        "continental drift",
        "paleogeography",
        "plate tectonics" ;
    schema1:license [ a schema1:CreativeWork ;
            schema1:name "Elsevier User License" ;
            schema1:url "https://www.elsevier.com/about/policies/open-access-licenses" ] ;
    schema1:name "Global Plate Tectonics and Paleogeography Since the Late Paleozoic" ;
    schema1:subjectOf <urn:uuid:dde-document-catalog-record> .

<urn:uuid:dde-document-catalog-record> a schema1:Dataset ;
    dcterms:conformsTo <https://w3id.org/cdif/bbr/metadata/profiles/DDEProfiles/DDEDocument> ;
    schema1:about <urn:dde:example-plate-tectonics-article> ;
    schema1:additionalType "dcat:CatalogRecord" ;
    schema1:sdDatePublished "2021-02-15" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
type: object
title: DDE Document profile
description: DDE profile for document resources (document, article, thesis, book,
  poster, webPage). Extends DDEDiscovery with resource type constraint.
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
            - document
            - article
            - thesis
            - book
            - poster
            - webPage
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

* YAML version: [schema.yaml](https://usgin.github.io/ddeBuildingBlocks/build/annotated/bbr/metadata/profiles/DDEProfiles/DDEDocument/schema.json)
* JSON version: [schema.json](https://usgin.github.io/ddeBuildingBlocks/build/annotated/bbr/metadata/profiles/DDEProfiles/DDEDocument/schema.yaml)


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
[context.jsonld](https://usgin.github.io/ddeBuildingBlocks/build/annotated/bbr/metadata/profiles/DDEProfiles/DDEDocument/context.jsonld)

## Sources

* [DDE Metadata Standard](https://www.ddeworld.org)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/ddeBuildingBlocks](https://github.com/usgin/ddeBuildingBlocks)
* Path: `_sources/profiles/DDEProfiles/DDEDocument`

