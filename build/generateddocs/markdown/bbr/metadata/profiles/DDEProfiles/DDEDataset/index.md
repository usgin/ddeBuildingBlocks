
# DDE Dataset profile (Schema)

`dde.bbr.metadata.profiles.DDEProfiles.DDEDataset` *v0.1*

DDE profile for dataset resources (dataset, dataCatalog, geographicDataset, nonGeographicDataset). Extends DDEDiscovery with resource type constraint. For geographicDataset, compose additionally with ddeGeographicDataset.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## DDE Dataset Profile

DDE profile for dataset resources. Extends DDEDiscovery with a resource type constraint requiring `schema:additionalType` to include a `schema:termCode` from: dataset, dataCatalog, geographicDataset, nonGeographicDataset.

### Composed building blocks

1. **DDEDiscovery** — Base DDE discovery profile (cdifCore + cdifOptional + ddeMandatory + ddeOptional)
2. **Resource type constraint** — `schema:termCode` must be one of the dataset group codes

### Sub-profile: geographicDataset

When the resource type is `geographicDataset`, additionally compose with **ddeGeographicDataset** building block for mandatory `schema:spatialCoverage` and optional spatial representation properties (spatialRepresentationType, spatialResolution, referenceSystemType, referenceSystemIdentifier).

## Examples

### DDE Dataset metadata example
DDE discovery metadata for a China 1:500K Hydrogeological Map as a geographic dataset with spatial representation and reference system properties.
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
  "@id": "urn:dde:example-hydrogeological-map",
  "@type": [
    "schema:Dataset"
  ],
  "schema:name": "China 1:500K Hydrogeological Map",
  "schema:description": "National-scale hydrogeological map of China at 1:500,000 scale, depicting aquifer types, groundwater flow systems, and hydrogeological units across all provinces. Compiled from regional geological survey data by the China Geological Survey.",
  "schema:identifier": "urn:cgs:hydrogeology-500k-2020",
  "schema:dateModified": "2020-11-15",
  "schema:inLanguage": "zho",
  "schema:license": [
    "licenceUnrestricted"
  ],
  "schema:url": "http://en.cgs.gov.cn/",
  "schema:subjectOf": {
    "@id": "urn:uuid:dde-dataset-catalog-record",
    "@type": [
      "schema:Dataset"
    ],
    "schema:additionalType": [
      "dcat:CatalogRecord"
    ],
    "schema:about": {
      "@id": "urn:dde:example-hydrogeological-map"
    },
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/core/1.0/"
      },
      {
        "@id": "https://w3id.org/cdif/discovery/1.0/"
      },
      {
        "@id": "https://w3id.org/cdif/bbr/metadata/profiles/DDEProfiles/DDEDataset"
      },
      {
        "@id": "https://w3id.org/cdif/bbr/metadata/DDEproperties/ddeMandatory"
      }
    ],
    "schema:sdDatePublished": "2020-11-15"
  },
  "schema:additionalType": [
    {
      "@type": "schema:DefinedTerm",
      "schema:name": "Geographic Dataset",
      "schema:termCode": "geographicDataset",
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
      "schema:name": "Geological Mapping",
      "schema:termCode": "geologicalMapping",
      "schema:inDefinedTermSet": "dde:codelist/AcquisitionTypeCode"
    },
    "hydrogeology",
    "groundwater",
    "aquifer",
    "China"
  ],
  "schema:image": [
    {
      "@type": "schema:ImageObject",
      "schema:contentUrl": "https://example.org/thumbnails/hydrogeological-map-500k.png",
      "schema:name": "thumbnail",
      "schema:encodingFormat": "image/png"
    }
  ],
  "schema:spatialCoverage": [
    {
      "@type": "schema:Place",
      "schema:geo": {
        "@type": "schema:GeoShape",
        "schema:box": "18.1609 73.499 53.5585 135.08"
      }
    }
  ],
  "schema:temporalCoverage": [
    {
      "@type": "time:ProperInterval",
      "time:hasBeginning": {
        "@type": "time:Instant",
        "time:inTimePosition": {
          "@type": "time:TimePosition",
          "time:hasTRS": {
            "@id": "http://www.opengis.net/def/uom/ISO-8601/0/Gregorian"
          },
          "time:numericPosition": 2015
        }
      },
      "time:hasEnd": {
        "@type": "time:Instant",
        "time:inTimePosition": {
          "@type": "time:TimePosition",
          "time:hasTRS": {
            "@id": "http://www.opengis.net/def/uom/ISO-8601/0/Gregorian"
          },
          "time:numericPosition": 2020
        }
      }
    }
  ],
  "schema:distribution": [
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:name": "Hydrogeological Map Shapefile",
      "schema:description": "Vector data in ESRI Shapefile format",
      "schema:contentUrl": "https://example.org/data/hydrogeology-500k.zip",
      "schema:encodingFormat": [
        "application/x-shapefile"
      ]
    }
  ],
  "schema:additionalProperty": [
    {
      "@type": "schema:PropertyValue",
      "schema:propertyID": [
        "dde:spatialRepresentationType"
      ],
      "schema:name": "Spatial Representation Type",
      "schema:value": "vector"
    },
    {
      "@type": "schema:PropertyValue",
      "schema:propertyID": [
        "dde:spatialResolution"
      ],
      "schema:name": "Spatial Resolution",
      "schema:value": "1:500000"
    },
    {
      "@type": "schema:PropertyValue",
      "schema:propertyID": [
        "dde:referenceSystemType"
      ],
      "schema:name": "Reference System Type",
      "schema:value": "geodeticGeographic2D"
    },
    {
      "@type": "schema:PropertyValue",
      "schema:propertyID": [
        "dde:referenceSystemIdentifier"
      ],
      "schema:name": "Coordinate Reference System",
      "schema:value": "EPSG:4326",
      "schema:url": "https://epsg.io/4326"
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
    "https://usgin.github.io/ddeBuildingBlocks/build/annotated/bbr/metadata/profiles/DDEProfiles/DDEDataset/context.jsonld",
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
  "@id": "urn:dde:example-hydrogeological-map",
  "@type": [
    "schema:Dataset"
  ],
  "schema:name": "China 1:500K Hydrogeological Map",
  "schema:description": "National-scale hydrogeological map of China at 1:500,000 scale, depicting aquifer types, groundwater flow systems, and hydrogeological units across all provinces. Compiled from regional geological survey data by the China Geological Survey.",
  "schema:identifier": "urn:cgs:hydrogeology-500k-2020",
  "schema:dateModified": "2020-11-15",
  "schema:inLanguage": "zho",
  "schema:license": [
    "licenceUnrestricted"
  ],
  "schema:url": "http://en.cgs.gov.cn/",
  "schema:subjectOf": {
    "@id": "urn:uuid:dde-dataset-catalog-record",
    "@type": [
      "schema:Dataset"
    ],
    "schema:additionalType": [
      "dcat:CatalogRecord"
    ],
    "schema:about": {
      "@id": "urn:dde:example-hydrogeological-map"
    },
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/core/1.0/"
      },
      {
        "@id": "https://w3id.org/cdif/discovery/1.0/"
      },
      {
        "@id": "https://w3id.org/cdif/bbr/metadata/profiles/DDEProfiles/DDEDataset"
      },
      {
        "@id": "https://w3id.org/cdif/bbr/metadata/DDEproperties/ddeMandatory"
      }
    ],
    "schema:sdDatePublished": "2020-11-15"
  },
  "schema:additionalType": [
    {
      "@type": "schema:DefinedTerm",
      "schema:name": "Geographic Dataset",
      "schema:termCode": "geographicDataset",
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
      "schema:name": "Geological Mapping",
      "schema:termCode": "geologicalMapping",
      "schema:inDefinedTermSet": "dde:codelist/AcquisitionTypeCode"
    },
    "hydrogeology",
    "groundwater",
    "aquifer",
    "China"
  ],
  "schema:image": [
    {
      "@type": "schema:ImageObject",
      "schema:contentUrl": "https://example.org/thumbnails/hydrogeological-map-500k.png",
      "schema:name": "thumbnail",
      "schema:encodingFormat": "image/png"
    }
  ],
  "schema:spatialCoverage": [
    {
      "@type": "schema:Place",
      "schema:geo": {
        "@type": "schema:GeoShape",
        "schema:box": "18.1609 73.499 53.5585 135.08"
      }
    }
  ],
  "schema:temporalCoverage": [
    {
      "@type": "time:ProperInterval",
      "time:hasBeginning": {
        "@type": "time:Instant",
        "time:inTimePosition": {
          "@type": "time:TimePosition",
          "time:hasTRS": {
            "@id": "http://www.opengis.net/def/uom/ISO-8601/0/Gregorian"
          },
          "time:numericPosition": 2015
        }
      },
      "time:hasEnd": {
        "@type": "time:Instant",
        "time:inTimePosition": {
          "@type": "time:TimePosition",
          "time:hasTRS": {
            "@id": "http://www.opengis.net/def/uom/ISO-8601/0/Gregorian"
          },
          "time:numericPosition": 2020
        }
      }
    }
  ],
  "schema:distribution": [
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:name": "Hydrogeological Map Shapefile",
      "schema:description": "Vector data in ESRI Shapefile format",
      "schema:contentUrl": "https://example.org/data/hydrogeology-500k.zip",
      "schema:encodingFormat": [
        "application/x-shapefile"
      ]
    }
  ],
  "schema:additionalProperty": [
    {
      "@type": "schema:PropertyValue",
      "schema:propertyID": [
        "dde:spatialRepresentationType"
      ],
      "schema:name": "Spatial Representation Type",
      "schema:value": "vector"
    },
    {
      "@type": "schema:PropertyValue",
      "schema:propertyID": [
        "dde:spatialResolution"
      ],
      "schema:name": "Spatial Resolution",
      "schema:value": "1:500000"
    },
    {
      "@type": "schema:PropertyValue",
      "schema:propertyID": [
        "dde:referenceSystemType"
      ],
      "schema:name": "Reference System Type",
      "schema:value": "geodeticGeographic2D"
    },
    {
      "@type": "schema:PropertyValue",
      "schema:propertyID": [
        "dde:referenceSystemIdentifier"
      ],
      "schema:name": "Coordinate Reference System",
      "schema:value": "EPSG:4326",
      "schema:url": "https://epsg.io/4326"
    }
  ]
}
```

#### ttl
```ttl
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix schema1: <http://schema.org/> .
@prefix time: <http://www.w3.org/2006/time#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<urn:dde:example-hydrogeological-map> a schema1:Dataset ;
    schema1:additionalProperty [ a schema1:PropertyValue ;
            schema1:name "Reference System Type" ;
            schema1:propertyID "dde:referenceSystemType" ;
            schema1:value "geodeticGeographic2D" ],
        [ a schema1:PropertyValue ;
            schema1:name "Spatial Resolution" ;
            schema1:propertyID "dde:spatialResolution" ;
            schema1:value "1:500000" ],
        [ a schema1:PropertyValue ;
            schema1:name "Coordinate Reference System" ;
            schema1:propertyID "dde:referenceSystemIdentifier" ;
            schema1:url "https://epsg.io/4326" ;
            schema1:value "EPSG:4326" ],
        [ a schema1:PropertyValue ;
            schema1:name "Spatial Representation Type" ;
            schema1:propertyID "dde:spatialRepresentationType" ;
            schema1:value "vector" ] ;
    schema1:additionalType [ a schema1:DefinedTerm ;
            schema1:inDefinedTermSet "dde:codelist/ResourceTypeCode" ;
            schema1:name "Geographic Dataset" ;
            schema1:termCode "geographicDataset" ] ;
    schema1:dateModified "2020-11-15" ;
    schema1:description "National-scale hydrogeological map of China at 1:500,000 scale, depicting aquifer types, groundwater flow systems, and hydrogeological units across all provinces. Compiled from regional geological survey data by the China Geological Survey." ;
    schema1:distribution [ a schema1:DataDownload ;
            schema1:contentUrl "https://example.org/data/hydrogeology-500k.zip" ;
            schema1:description "Vector data in ESRI Shapefile format" ;
            schema1:encodingFormat "application/x-shapefile" ;
            schema1:name "Hydrogeological Map Shapefile" ] ;
    schema1:identifier "urn:cgs:hydrogeology-500k-2020" ;
    schema1:image [ a schema1:ImageObject ;
            schema1:contentUrl "https://example.org/thumbnails/hydrogeological-map-500k.png" ;
            schema1:encodingFormat "image/png" ;
            schema1:name "thumbnail" ] ;
    schema1:inLanguage "zho" ;
    schema1:keywords [ a schema1:DefinedTerm ;
            schema1:inDefinedTermSet "dde:codelist/AcquisitionTypeCode" ;
            schema1:name "Geological Mapping" ;
            schema1:termCode "geologicalMapping" ],
        [ a schema1:DefinedTerm ;
            schema1:inDefinedTermSet "dde:codelist/TopicCategoryCode" ;
            schema1:name "Geoscientific Information" ;
            schema1:termCode "geoscientificInformation" ],
        "China",
        "aquifer",
        "groundwater",
        "hydrogeology" ;
    schema1:license "licenceUnrestricted" ;
    schema1:name "China 1:500K Hydrogeological Map" ;
    schema1:spatialCoverage [ a schema1:Place ;
            schema1:geo [ a schema1:GeoShape ;
                    schema1:box "18.1609 73.499 53.5585 135.08" ] ] ;
    schema1:subjectOf <urn:uuid:dde-dataset-catalog-record> ;
    schema1:temporalCoverage [ a time:ProperInterval ;
            time:hasBeginning [ a time:Instant ;
                    time:inTimePosition [ a time:TimePosition ;
                            time:hasTRS <http://www.opengis.net/def/uom/ISO-8601/0/Gregorian> ;
                            time:numericPosition 2015 ] ] ;
            time:hasEnd [ a time:Instant ;
                    time:inTimePosition [ a time:TimePosition ;
                            time:hasTRS <http://www.opengis.net/def/uom/ISO-8601/0/Gregorian> ;
                            time:numericPosition 2020 ] ] ] ;
    schema1:url "http://en.cgs.gov.cn/" .

<urn:uuid:dde-dataset-catalog-record> a schema1:Dataset ;
    dcterms:conformsTo <https://w3id.org/cdif/bbr/metadata/DDEproperties/ddeMandatory>,
        <https://w3id.org/cdif/bbr/metadata/profiles/DDEProfiles/DDEDataset>,
        <https://w3id.org/cdif/core/1.0/>,
        <https://w3id.org/cdif/discovery/1.0/> ;
    schema1:about <urn:dde:example-hydrogeological-map> ;
    schema1:additionalType "dcat:CatalogRecord" ;
    schema1:sdDatePublished "2020-11-15" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
type: object
title: DDE Dataset profile
description: DDE profile for dataset resources (dataset, dataCatalog, geographicDataset,
  nonGeographicDataset). Extends DDEDiscovery with resource type constraint. If additionalType
  termCode is geographicDataset, ddeGeographicDataset constraints are applied.
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
            - dataset
            - dataCatalog
            - geographicDataset
            - nonGeographicDataset
        required:
        - '@type'
        - schema:inDefinedTermSet
        - schema:termCode
      minContains: 1
- if:
    properties:
      schema:additionalType:
        contains:
          type: object
          properties:
            schema:termCode:
              const: geographicDataset
  then:
    $ref: https://usgin.github.io/ddeBuildingBlocks/build/annotated/bbr/metadata/DDEproperties/ddeGeographicDataset/schema.yaml
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

* YAML version: [schema.yaml](https://usgin.github.io/ddeBuildingBlocks/build/annotated/bbr/metadata/profiles/DDEProfiles/DDEDataset/schema.json)
* JSON version: [schema.json](https://usgin.github.io/ddeBuildingBlocks/build/annotated/bbr/metadata/profiles/DDEProfiles/DDEDataset/schema.yaml)


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
[context.jsonld](https://usgin.github.io/ddeBuildingBlocks/build/annotated/bbr/metadata/profiles/DDEProfiles/DDEDataset/context.jsonld)

## Sources

* [DDE Metadata Standard](https://www.ddeworld.org)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/ddeBuildingBlocks](https://github.com/usgin/ddeBuildingBlocks)
* Path: `_sources/profiles/DDEProfiles/DDEDataset`

