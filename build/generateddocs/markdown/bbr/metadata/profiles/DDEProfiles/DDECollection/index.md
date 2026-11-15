
# DDE Collection profile (Schema)

`dde.bbr.metadata.profiles.DDEProfiles.DDECollection` *v0.1*

DDE profile for collection resources (aggregate, collection, series, learningResource, guide). Extends ddeCore with resource type constraint and requires schema:hasPart for collection members.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## DDE Collection Profile

DDE profile for collection resources. Extends `ddeCore` with a resource type constraint and requires `schema:hasPart` to describe collection members.

### Resource type codes
aggregate, collection, series, learningResource, guide

### Composed building blocks

1. **ddeCore** — DDE core properties: resource type from `dde:codelist/ResourceTypeCode`, topic category and acquisition type keywords, alternate names, optional browse graphics. `ddeCore` composes `cdifCore`, so CDIF's mandatory fields come in with it.
2. **Resource type constraint** — `schema:termCode` must be one of the collection group codes
3. **cdifManifest** — `schema:hasPart` on the Dataset, for members retrievable at their own addresses, and on a `schema:distribution` item, for component files inside an archive
4. **`schema:hasPart`** (required) — at least one member, each classified with a DDE resource type

### Collection member structure

The member shape comes from **cdifManifest**'s `resourcePartItem`: `@id`, `@type`,
`schema:name`, `schema:description`, `schema:encodingFormat`, `schema:url` and
`schema:about`. On top of that, every member carries a DDE resource type
(`ddeResourceType`) — `items`, not `contains`, so each member is classified rather than
just one of them.

Before 2026-11-15 this block defined its own member shape, with `schema:name` required and
no way to say where a member could be retrieved, which is the one thing a manifest exists
to express.

### Conformance

A document instance claiming this profile declares it on the catalog record:

```json
"schema:subjectOf": {
    "dcterms:conformsTo": [
        {"@id": "https://w3id.org/cdif/core/1.1"},
        {"@id": "https://w3id.org/cdif/dde/1.0/DDECollection"}
    ]
}
```

`https://w3id.org/cdif/dde/1.0/DDECollection` is required by this profile's schema, as a
`contains` over `schema:subjectOf`/`dcterms:conformsTo`. The URI is on the profile
because DDE profiles are what document instances conform to; the property building
blocks they compose, `ddeCore` among them, declare none of their own.

## Examples

### DDE Collection metadata example
DDE discovery metadata for the OneGeology Global Geological Map Collection with three hasPart member maps (China, Australia, UK).
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
    "@id": "urn:dde:example-onegeology-collection",
    "@type": [
        "schema:Dataset"
    ],
    "schema:name": "OneGeology Global Geological Map Collection",
    "schema:description": "A curated collection of 1:1M scale geological maps contributed by national geological surveys through the OneGeology initiative. Each member map covers a single country or territory and uses harmonized symbology based on the GeoSciML Portrayal schema.",
    "schema:identifier": "urn:onegeology:global-collection-2024",
    "schema:dateModified": "2024-06-01",
    "schema:inLanguage": "eng",
    "schema:license": [
        {
            "@type": [
                "schema:CreativeWork"
            ],
            "schema:name": "Creative Commons Attribution 4.0",
            "schema:url": "https://creativecommons.org/licenses/by/4.0/"
        }
    ],
    "schema:url": "https://onegeology.org/",
    "schema:subjectOf": {
        "@id": "urn:uuid:dde-collection-catalog-record",
        "@type": [
            "schema:Dataset"
        ],
        "schema:additionalType": [
            {
                "@id": "dcat:CatalogRecord"
            }
        ],
        "schema:about": {
            "@id": "urn:dde:example-onegeology-collection"
        },
        "dcterms:conformsTo": [
            {
                "@id": "https://w3id.org/cdif/core/1.1"
            },
            {
                "@id": "https://w3id.org/cdif/discovery/1.1"
            },
            {
                "@id": "https://w3id.org/cdif/dde/1.0/DDECollection"
            },
            {
                "@id": "https://w3id.org/cdif/manifest/1.1"
            }
        ],
        "schema:sdDatePublished": "2024-06-01"
    },
    "schema:additionalType": [
        {
            "@type": [
                "schema:DefinedTerm"
            ],
            "schema:name": "Series",
            "schema:termCode": "series",
            "schema:inDefinedTermSet": "dde:codelist/ResourceTypeCode"
        },
        {
            "@type": [
                "schema:DefinedTerm"
            ],
            "schema:name": "Collection",
            "schema:termCode": "collection",
            "schema:inDefinedTermSet": "dde:codelist/ResourceTypeCode"
        }
    ],
    "schema:keywords": [
        {
            "@type": [
                "schema:DefinedTerm"
            ],
            "schema:name": "Geoscientific Information",
            "schema:termCode": "geoscientificInformation",
            "schema:inDefinedTermSet": "dde:codelist/TopicCategoryCode"
        },
        {
            "@type": [
                "schema:DefinedTerm"
            ],
            "schema:name": "Geological Mapping",
            "schema:termCode": "geologicalMapping",
            "schema:inDefinedTermSet": "dde:codelist/AcquisitionTypeCode"
        },
        "OneGeology",
        "geology",
        "geological map",
        "global"
    ],
    "schema:image": [
        {
            "@type": [
                "schema:ImageObject"
            ],
            "schema:contentUrl": "https://onegeology.org/images/global-map-preview.png",
            "schema:name": "thumbnail",
            "schema:encodingFormat": "image/png"
        }
    ],
    "schema:spatialCoverage": [
        {
            "@type": [
                "schema:Place"
            ],
            "schema:geo": {
                "@type": [
                    "schema:GeoShape"
                ],
                "schema:box": "-90 -180 90 180"
            }
        }
    ],
    "schema:hasPart": [
        {
            "@type": [
                "schema:CreativeWork"
            ],
            "schema:name": "China 1:1M Bedrock Lithostratigraphy",
            "schema:description": "Geological map of China compiled from 63 separate survey sheets",
            "schema:url": "http://en.cgs.gov.cn/"
        },
        {
            "@type": [
                "schema:CreativeWork"
            ],
            "schema:name": "Australia 1:1M Surface Geology",
            "schema:description": "National-scale surface geology map of Australia by Geoscience Australia",
            "schema:url": "https://www.ga.gov.au/data-pubs/data-and-publications-search/datasets"
        },
        {
            "@type": [
                "schema:CreativeWork"
            ],
            "schema:name": "United Kingdom 1:625K Bedrock Geology",
            "schema:description": "Bedrock geological map of the United Kingdom by the British Geological Survey",
            "schema:url": "https://www.bgs.ac.uk/geological-data/"
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
      "time": "http://www.w3.org/2006/time#",
      "prov": "http://www.w3.org/ns/prov#"
    },
    "https://usgin.github.io/ddeBuildingBlocks/build/annotated/bbr/metadata/profiles/DDEProfiles/DDECollection/context.jsonld",
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
  "@id": "urn:dde:example-onegeology-collection",
  "@type": [
    "schema:Dataset"
  ],
  "schema:name": "OneGeology Global Geological Map Collection",
  "schema:description": "A curated collection of 1:1M scale geological maps contributed by national geological surveys through the OneGeology initiative. Each member map covers a single country or territory and uses harmonized symbology based on the GeoSciML Portrayal schema.",
  "schema:identifier": "urn:onegeology:global-collection-2024",
  "schema:dateModified": "2024-06-01",
  "schema:inLanguage": "eng",
  "schema:license": [
    {
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:name": "Creative Commons Attribution 4.0",
      "schema:url": "https://creativecommons.org/licenses/by/4.0/"
    }
  ],
  "schema:url": "https://onegeology.org/",
  "schema:subjectOf": {
    "@id": "urn:uuid:dde-collection-catalog-record",
    "@type": [
      "schema:Dataset"
    ],
    "schema:additionalType": [
      {
        "@id": "dcat:CatalogRecord"
      }
    ],
    "schema:about": {
      "@id": "urn:dde:example-onegeology-collection"
    },
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/core/1.1"
      },
      {
        "@id": "https://w3id.org/cdif/discovery/1.1"
      },
      {
        "@id": "https://w3id.org/cdif/dde/1.0/DDECollection"
      },
      {
        "@id": "https://w3id.org/cdif/manifest/1.1"
      }
    ],
    "schema:sdDatePublished": "2024-06-01"
  },
  "schema:additionalType": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "Series",
      "schema:termCode": "series",
      "schema:inDefinedTermSet": "dde:codelist/ResourceTypeCode"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "Collection",
      "schema:termCode": "collection",
      "schema:inDefinedTermSet": "dde:codelist/ResourceTypeCode"
    }
  ],
  "schema:keywords": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "Geoscientific Information",
      "schema:termCode": "geoscientificInformation",
      "schema:inDefinedTermSet": "dde:codelist/TopicCategoryCode"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "Geological Mapping",
      "schema:termCode": "geologicalMapping",
      "schema:inDefinedTermSet": "dde:codelist/AcquisitionTypeCode"
    },
    "OneGeology",
    "geology",
    "geological map",
    "global"
  ],
  "schema:image": [
    {
      "@type": [
        "schema:ImageObject"
      ],
      "schema:contentUrl": "https://onegeology.org/images/global-map-preview.png",
      "schema:name": "thumbnail",
      "schema:encodingFormat": "image/png"
    }
  ],
  "schema:spatialCoverage": [
    {
      "@type": [
        "schema:Place"
      ],
      "schema:geo": {
        "@type": [
          "schema:GeoShape"
        ],
        "schema:box": "-90 -180 90 180"
      }
    }
  ],
  "schema:hasPart": [
    {
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:name": "China 1:1M Bedrock Lithostratigraphy",
      "schema:description": "Geological map of China compiled from 63 separate survey sheets",
      "schema:url": "http://en.cgs.gov.cn/"
    },
    {
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:name": "Australia 1:1M Surface Geology",
      "schema:description": "National-scale surface geology map of Australia by Geoscience Australia",
      "schema:url": "https://www.ga.gov.au/data-pubs/data-and-publications-search/datasets"
    },
    {
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:name": "United Kingdom 1:625K Bedrock Geology",
      "schema:description": "Bedrock geological map of the United Kingdom by the British Geological Survey",
      "schema:url": "https://www.bgs.ac.uk/geological-data/"
    }
  ]
}
```

#### ttl
```ttl
@prefix dcat: <http://www.w3.org/ns/dcat#> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix schema1: <http://schema.org/> .

<urn:dde:example-onegeology-collection> a schema1:Dataset ;
    schema1:additionalType [ a schema1:DefinedTerm ;
            schema1:inDefinedTermSet "dde:codelist/ResourceTypeCode" ;
            schema1:name "Series" ;
            schema1:termCode "series" ],
        [ a schema1:DefinedTerm ;
            schema1:inDefinedTermSet "dde:codelist/ResourceTypeCode" ;
            schema1:name "Collection" ;
            schema1:termCode "collection" ] ;
    schema1:dateModified "2024-06-01" ;
    schema1:description "A curated collection of 1:1M scale geological maps contributed by national geological surveys through the OneGeology initiative. Each member map covers a single country or territory and uses harmonized symbology based on the GeoSciML Portrayal schema." ;
    schema1:hasPart [ a schema1:CreativeWork ;
            schema1:description "Bedrock geological map of the United Kingdom by the British Geological Survey" ;
            schema1:name "United Kingdom 1:625K Bedrock Geology" ;
            schema1:url "https://www.bgs.ac.uk/geological-data/" ],
        [ a schema1:CreativeWork ;
            schema1:description "National-scale surface geology map of Australia by Geoscience Australia" ;
            schema1:name "Australia 1:1M Surface Geology" ;
            schema1:url "https://www.ga.gov.au/data-pubs/data-and-publications-search/datasets" ],
        [ a schema1:CreativeWork ;
            schema1:description "Geological map of China compiled from 63 separate survey sheets" ;
            schema1:name "China 1:1M Bedrock Lithostratigraphy" ;
            schema1:url "http://en.cgs.gov.cn/" ] ;
    schema1:identifier "urn:onegeology:global-collection-2024" ;
    schema1:image [ a schema1:ImageObject ;
            schema1:contentUrl "https://onegeology.org/images/global-map-preview.png" ;
            schema1:encodingFormat "image/png" ;
            schema1:name "thumbnail" ] ;
    schema1:inLanguage "eng" ;
    schema1:keywords [ a schema1:DefinedTerm ;
            schema1:inDefinedTermSet "dde:codelist/TopicCategoryCode" ;
            schema1:name "Geoscientific Information" ;
            schema1:termCode "geoscientificInformation" ],
        [ a schema1:DefinedTerm ;
            schema1:inDefinedTermSet "dde:codelist/AcquisitionTypeCode" ;
            schema1:name "Geological Mapping" ;
            schema1:termCode "geologicalMapping" ],
        "OneGeology",
        "geological map",
        "geology",
        "global" ;
    schema1:license [ a schema1:CreativeWork ;
            schema1:name "Creative Commons Attribution 4.0" ;
            schema1:url "https://creativecommons.org/licenses/by/4.0/" ] ;
    schema1:name "OneGeology Global Geological Map Collection" ;
    schema1:spatialCoverage [ a schema1:Place ;
            schema1:geo [ a schema1:GeoShape ;
                    schema1:box "-90 -180 90 180" ] ] ;
    schema1:subjectOf <urn:uuid:dde-collection-catalog-record> ;
    schema1:url "https://onegeology.org/" .

<urn:uuid:dde-collection-catalog-record> a schema1:Dataset ;
    dcterms:conformsTo <https://w3id.org/cdif/core/1.1>,
        <https://w3id.org/cdif/dde/1.0/DDECollection>,
        <https://w3id.org/cdif/discovery/1.1>,
        <https://w3id.org/cdif/manifest/1.1> ;
    schema1:about <urn:dde:example-onegeology-collection> ;
    schema1:additionalType dcat:CatalogRecord ;
    schema1:sdDatePublished "2024-06-01" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
type: object
title: DDE Collection profile
description: 'DDE profile for collection resources (aggregate, collection, series,
  learningResource, guide). Composes ddeCore with the CDIF manifest profile and adds
  the DDE-specific constraints: the collection''s own resource type, a DDE resource
  type on every member, and a temporal extent.

  schema:hasPart comes from cdifManifest, so a member carries that profile''s resourcePartItem
  shape -- @id, @type, schema:name, schema:description, schema:encodingFormat, schema:url,
  schema:about -- and a DDE resource type in addition, the two composing through the
  allOf below. Before this the block defined its own member shape with no way to say
  where a member could be retrieved, which is the one thing a manifest exists to express.

  Three conformance URIs land on the catalog record, each a separate "contains" over
  the same dcterms:conformsTo array: cdif/core/1.1 from cdifCore, cdif/manifest/1.1
  from cdifManifest, and this profile''s own cdif/dde/1.0/DDECollection. Manifest
  conformance is against 1.1, matching what this repository vendors. Nothing here
  restates that the array is required -- cdifCore requires schema:subjectOf and cdifCatalogRecord
  requires dcterms:conformsTo, so a branch doing that by hand was removed 2026-11-15.'
allOf:
- $ref: https://usgin.github.io/ddeBuildingBlocks/build/annotated/bbr/metadata/DDEproperties/ddeCore/schema.yaml
- properties:
    schema:subjectOf:
      properties:
        dcterms:conformsTo:
          contains:
            type: object
            required:
            - '@id'
            additionalProperties: false
            properties:
              '@id':
                const: https://w3id.org/cdif/dde/1.0/DDECollection
          x-jsonld-id: http://purl.org/dc/terms/conformsTo
      x-jsonld-id: http://schema.org/subjectOf
- $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/cdifProfile/cdifManifest/schema.yaml
- properties:
    schema:additionalType:
      contains:
        type: object
        properties:
          '@type':
            contains:
              const: schema:DefinedTerm
          schema:inDefinedTermSet:
            const: dde:codelist/ResourceTypeCode
          schema:termCode:
            type: string
            enum:
            - aggregate
            - collection
            - series
            - learningResource
            - guide
        required:
        - '@type'
        - schema:inDefinedTermSet
        - schema:termCode
      minContains: 1
      x-jsonld-id: http://schema.org/additionalType
    schema:hasPart:
      type: array
      description: 'Members of the collection. The item shape comes from cdifManifest''s
        resourcePartItem via the allOf above; this branch adds the DDE resource type
        every member must carry. items, not contains: each member is classified, not
        merely one of them.'
      minItems: 1
      items:
        $ref: https://usgin.github.io/ddeBuildingBlocks/build/annotated/bbr/metadata/DDEproperties/ddeResourceType/schema.yaml
      x-jsonld-id: http://schema.org/hasPart
    schema:temporalCoverage:
      description: Temporal extent of resource content.
      type: array
      items:
        $ref: '#/$defs/TemporalExtent'
      x-jsonld-id: http://schema.org/temporalCoverage
  required:
  - schema:hasPart
$defs:
  TemporalExtent:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/temporalExtent/schema.yaml
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
x-bblocks-metadata:
  itemIdentifier: dde.bbr.metadata.profiles.DDEProfiles.DDECollection
  register: https://usgin.github.io/ddeBuildingBlocks/build/register.json
  version: '0.1'
  dateOfLastChange: '2026-11-15'

```

Links to the schema:

* YAML version: [schema.yaml](https://usgin.github.io/ddeBuildingBlocks/build/annotated/bbr/metadata/profiles/DDEProfiles/DDECollection/schema.json)
* JSON version: [schema.json](https://usgin.github.io/ddeBuildingBlocks/build/annotated/bbr/metadata/profiles/DDEProfiles/DDECollection/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "http://schema.org/",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "dcterms": "http://purl.org/dc/terms/",
    "dcat": "http://www.w3.org/ns/dcat#",
    "cdif": "https://w3id.org/cdif/",
    "prov": "http://www.w3.org/ns/prov#",
    "ex": "https://example.org/",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "dde": "https://www.ddeworld.org/resource/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "geosparql": "http://www.opengis.net/ont/geosparql#",
    "spdx": "http://spdx.org/rdf/terms#",
    "time": "http://www.w3.org/2006/time#",
    "dqv": "http://www.w3.org/ns/dqv#",
    "ada": "https://ada.astromat.org/metadata/",
    "nxs": "https://manual.nexusformat.org/classes/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://usgin.github.io/ddeBuildingBlocks/build/annotated/bbr/metadata/profiles/DDEProfiles/DDECollection/context.jsonld)

## Sources

* [DDE Metadata Standard](https://www.ddeworld.org)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/ddeBuildingBlocks](https://github.com/usgin/ddeBuildingBlocks)
* Path: `_sources/profiles/DDEProfiles/DDECollection`

