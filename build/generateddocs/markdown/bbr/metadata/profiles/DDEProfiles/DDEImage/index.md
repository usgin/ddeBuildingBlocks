
# DDE Image profile (Schema)

`dde.bbr.metadata.profiles.DDEProfiles.DDEImage` *v0.1*

DDE profile for image resources (image, photograph, explanatoryFigure, map). Extends DDEDiscovery with resource type constraint and ddeImagery conditional properties (sensor, platform, equipment, etc.).

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## DDE Image Profile

DDE profile for image resources. Extends DDEDiscovery with a resource type constraint and the ddeImagery building block for imagery-specific properties.

### Resource type codes
image, photograph, explanatoryFigure, map

### Composed building blocks

1. **DDEDiscovery** — Base DDE discovery profile
2. **ddeImagery** — Optional imagery properties: sensor type, platform, equipment, collector, startTime, endTime, signalGenerator, wavelength, processedLevel
3. **Resource type constraint** — `schema:termCode` must be one of the image group codes

## Examples

### DDE Image metadata example
DDE discovery metadata for a Landsat-8 multispectral scene of the Tibetan Plateau. Imagery acquisition metadata (sensor, platform, equipment, signalGenerator, collector, temporal bounds) is represented as a prov:wasGeneratedBy activity following the cdifProv pattern. Wavelength and processing level remain as dataset-level additionalProperty values.
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
  "@id": "urn:dde:example-landsat8-tibet",
  "@type": [
    "schema:Dataset"
  ],
  "schema:name": "Landsat-8 Multispectral Scene of the Tibetan Plateau",
  "schema:description": "Level-2 surface reflectance product from Landsat-8 OLI sensor covering the central Tibetan Plateau. Scene acquired on 2023-06-15, path 138 row 037. Nine spectral bands from coastal aerosol (0.43 um) to shortwave infrared (2.29 um) at 30m spatial resolution, plus 15m panchromatic band.",
  "schema:identifier": "LC08_L2SP_138037_20230615",
  "schema:dateModified": "2023-07-01",
  "schema:inLanguage": "eng",
  "schema:license": [
    "licenceUnrestricted"
  ],
  "schema:url": "https://earthexplorer.usgs.gov/",
  "schema:subjectOf": {
    "@id": "urn:uuid:dde-image-catalog-record",
    "@type": [
      "schema:Dataset"
    ],
    "schema:additionalType": [
      "dcat:CatalogRecord"
    ],
    "schema:about": {
      "@id": "urn:dde:example-landsat8-tibet"
    },
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/core/1.0/"
      },
      {
        "@id": "https://w3id.org/cdif/discovery/1.0/"
      },
      {
        "@id": "https://w3id.org/cdif/bbr/metadata/profiles/DDEProfiles/DDEImage"
      },
      {
        "@id": "https://w3id.org/cdif/bbr/metadata/DDEproperties/ddeMandatory"
      }
    ],
    "schema:sdDatePublished": "2023-07-01"
  },
  "schema:additionalType": [
    {
      "@type": "schema:DefinedTerm",
      "schema:name": "Image",
      "schema:termCode": "image",
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
      "schema:name": "Remote Sensing",
      "schema:termCode": "remoteSensing",
      "schema:inDefinedTermSet": "dde:codelist/AcquisitionTypeCode"
    },
    "Landsat-8",
    "multispectral",
    "Tibetan Plateau",
    "remote sensing"
  ],
  "schema:image": [
    {
      "@type": "schema:ImageObject",
      "schema:contentUrl": "https://example.org/thumbnails/landsat8-tibet-preview.png",
      "schema:name": "browse image",
      "schema:encodingFormat": "image/png"
    }
  ],
  "schema:spatialCoverage": [
    {
      "@type": "schema:Place",
      "schema:geo": {
        "@type": "schema:GeoShape",
        "schema:box": "29.5 88.0 31.5 90.5"
      }
    }
  ],
  "schema:distribution": [
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:name": "Landsat-8 L2SP GeoTIFF Bundle",
      "schema:description": "Surface reflectance bands in GeoTIFF format",
      "schema:contentUrl": "https://earthexplorer.usgs.gov/download/external/options/landsat_ot_c2_l2/LC08_L2SP_138037_20230615/",
      "schema:encodingFormat": [
        "image/tiff"
      ]
    }
  ],
  "prov:wasGeneratedBy": [
    {
      "@type": [
        "schema:Action",
        "prov:Activity"
      ],
      "schema:name": "Landsat-8 OLI imagery acquisition",
      "schema:startTime": "2023-06-15T03:45:00Z",
      "schema:endTime": "2023-06-15T03:45:12Z",
      "prov:used": [
        {
          "schema:instrument": {
            "@type": [
              "schema:Thing"
            ],
            "schema:name": "Multispectral",
            "schema:additionalType": "dde:sensorType"
          }
        },
        {
          "schema:instrument": {
            "@type": [
              "schema:Thing"
            ],
            "schema:name": "Landsat-8",
            "schema:additionalType": "dde:platform"
          }
        },
        {
          "schema:instrument": {
            "@type": [
              "schema:Thing"
            ],
            "schema:name": "Operational Land Imager (OLI)",
            "schema:additionalType": "dde:equipment"
          }
        },
        {
          "schema:instrument": {
            "@type": [
              "schema:Thing"
            ],
            "schema:name": "Passive solar",
            "schema:additionalType": "dde:signalGenerator"
          }
        }
      ],
      "schema:participant": [
        {
          "@type": "schema:Role",
          "schema:roleName": "DataCollector",
          "schema:contributor": {
            "@type": "schema:Organization",
            "schema:name": "USGS / NASA"
          }
        }
      ]
    }
  ],
  "schema:additionalProperty": [
    {
      "@type": "schema:PropertyValue",
      "schema:propertyID": [
        "dde:wavelength"
      ],
      "schema:name": "Wavelength Range",
      "schema:value": "0.43-2.29 micrometers"
    },
    {
      "@type": "schema:PropertyValue",
      "schema:propertyID": [
        "dde:processedLevel"
      ],
      "schema:name": "Processing Level",
      "schema:value": "Level2"
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
    "https://usgin.github.io/ddeBuildingBlocks/build/annotated/bbr/metadata/profiles/DDEProfiles/DDEImage/context.jsonld",
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
  "@id": "urn:dde:example-landsat8-tibet",
  "@type": [
    "schema:Dataset"
  ],
  "schema:name": "Landsat-8 Multispectral Scene of the Tibetan Plateau",
  "schema:description": "Level-2 surface reflectance product from Landsat-8 OLI sensor covering the central Tibetan Plateau. Scene acquired on 2023-06-15, path 138 row 037. Nine spectral bands from coastal aerosol (0.43 um) to shortwave infrared (2.29 um) at 30m spatial resolution, plus 15m panchromatic band.",
  "schema:identifier": "LC08_L2SP_138037_20230615",
  "schema:dateModified": "2023-07-01",
  "schema:inLanguage": "eng",
  "schema:license": [
    "licenceUnrestricted"
  ],
  "schema:url": "https://earthexplorer.usgs.gov/",
  "schema:subjectOf": {
    "@id": "urn:uuid:dde-image-catalog-record",
    "@type": [
      "schema:Dataset"
    ],
    "schema:additionalType": [
      "dcat:CatalogRecord"
    ],
    "schema:about": {
      "@id": "urn:dde:example-landsat8-tibet"
    },
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/core/1.0/"
      },
      {
        "@id": "https://w3id.org/cdif/discovery/1.0/"
      },
      {
        "@id": "https://w3id.org/cdif/bbr/metadata/profiles/DDEProfiles/DDEImage"
      },
      {
        "@id": "https://w3id.org/cdif/bbr/metadata/DDEproperties/ddeMandatory"
      }
    ],
    "schema:sdDatePublished": "2023-07-01"
  },
  "schema:additionalType": [
    {
      "@type": "schema:DefinedTerm",
      "schema:name": "Image",
      "schema:termCode": "image",
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
      "schema:name": "Remote Sensing",
      "schema:termCode": "remoteSensing",
      "schema:inDefinedTermSet": "dde:codelist/AcquisitionTypeCode"
    },
    "Landsat-8",
    "multispectral",
    "Tibetan Plateau",
    "remote sensing"
  ],
  "schema:image": [
    {
      "@type": "schema:ImageObject",
      "schema:contentUrl": "https://example.org/thumbnails/landsat8-tibet-preview.png",
      "schema:name": "browse image",
      "schema:encodingFormat": "image/png"
    }
  ],
  "schema:spatialCoverage": [
    {
      "@type": "schema:Place",
      "schema:geo": {
        "@type": "schema:GeoShape",
        "schema:box": "29.5 88.0 31.5 90.5"
      }
    }
  ],
  "schema:distribution": [
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:name": "Landsat-8 L2SP GeoTIFF Bundle",
      "schema:description": "Surface reflectance bands in GeoTIFF format",
      "schema:contentUrl": "https://earthexplorer.usgs.gov/download/external/options/landsat_ot_c2_l2/LC08_L2SP_138037_20230615/",
      "schema:encodingFormat": [
        "image/tiff"
      ]
    }
  ],
  "prov:wasGeneratedBy": [
    {
      "@type": [
        "schema:Action",
        "prov:Activity"
      ],
      "schema:name": "Landsat-8 OLI imagery acquisition",
      "schema:startTime": "2023-06-15T03:45:00Z",
      "schema:endTime": "2023-06-15T03:45:12Z",
      "prov:used": [
        {
          "schema:instrument": {
            "@type": [
              "schema:Thing"
            ],
            "schema:name": "Multispectral",
            "schema:additionalType": "dde:sensorType"
          }
        },
        {
          "schema:instrument": {
            "@type": [
              "schema:Thing"
            ],
            "schema:name": "Landsat-8",
            "schema:additionalType": "dde:platform"
          }
        },
        {
          "schema:instrument": {
            "@type": [
              "schema:Thing"
            ],
            "schema:name": "Operational Land Imager (OLI)",
            "schema:additionalType": "dde:equipment"
          }
        },
        {
          "schema:instrument": {
            "@type": [
              "schema:Thing"
            ],
            "schema:name": "Passive solar",
            "schema:additionalType": "dde:signalGenerator"
          }
        }
      ],
      "schema:participant": [
        {
          "@type": "schema:Role",
          "schema:roleName": "DataCollector",
          "schema:contributor": {
            "@type": "schema:Organization",
            "schema:name": "USGS / NASA"
          }
        }
      ]
    }
  ],
  "schema:additionalProperty": [
    {
      "@type": "schema:PropertyValue",
      "schema:propertyID": [
        "dde:wavelength"
      ],
      "schema:name": "Wavelength Range",
      "schema:value": "0.43-2.29 micrometers"
    },
    {
      "@type": "schema:PropertyValue",
      "schema:propertyID": [
        "dde:processedLevel"
      ],
      "schema:name": "Processing Level",
      "schema:value": "Level2"
    }
  ]
}
```

#### ttl
```ttl
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .

<urn:dde:example-landsat8-tibet> a schema1:Dataset ;
    schema1:additionalProperty [ a schema1:PropertyValue ;
            schema1:name "Processing Level" ;
            schema1:propertyID "dde:processedLevel" ;
            schema1:value "Level2" ],
        [ a schema1:PropertyValue ;
            schema1:name "Wavelength Range" ;
            schema1:propertyID "dde:wavelength" ;
            schema1:value "0.43-2.29 micrometers" ] ;
    schema1:additionalType [ a schema1:DefinedTerm ;
            schema1:inDefinedTermSet "dde:codelist/ResourceTypeCode" ;
            schema1:name "Image" ;
            schema1:termCode "image" ] ;
    schema1:dateModified "2023-07-01" ;
    schema1:description "Level-2 surface reflectance product from Landsat-8 OLI sensor covering the central Tibetan Plateau. Scene acquired on 2023-06-15, path 138 row 037. Nine spectral bands from coastal aerosol (0.43 um) to shortwave infrared (2.29 um) at 30m spatial resolution, plus 15m panchromatic band." ;
    schema1:distribution [ a schema1:DataDownload ;
            schema1:contentUrl "https://earthexplorer.usgs.gov/download/external/options/landsat_ot_c2_l2/LC08_L2SP_138037_20230615/" ;
            schema1:description "Surface reflectance bands in GeoTIFF format" ;
            schema1:encodingFormat "image/tiff" ;
            schema1:name "Landsat-8 L2SP GeoTIFF Bundle" ] ;
    schema1:identifier "LC08_L2SP_138037_20230615" ;
    schema1:image [ a schema1:ImageObject ;
            schema1:contentUrl "https://example.org/thumbnails/landsat8-tibet-preview.png" ;
            schema1:encodingFormat "image/png" ;
            schema1:name "browse image" ] ;
    schema1:inLanguage "eng" ;
    schema1:keywords [ a schema1:DefinedTerm ;
            schema1:inDefinedTermSet "dde:codelist/TopicCategoryCode" ;
            schema1:name "Geoscientific Information" ;
            schema1:termCode "geoscientificInformation" ],
        [ a schema1:DefinedTerm ;
            schema1:inDefinedTermSet "dde:codelist/AcquisitionTypeCode" ;
            schema1:name "Remote Sensing" ;
            schema1:termCode "remoteSensing" ],
        "Landsat-8",
        "Tibetan Plateau",
        "multispectral",
        "remote sensing" ;
    schema1:license "licenceUnrestricted" ;
    schema1:name "Landsat-8 Multispectral Scene of the Tibetan Plateau" ;
    schema1:spatialCoverage [ a schema1:Place ;
            schema1:geo [ a schema1:GeoShape ;
                    schema1:box "29.5 88.0 31.5 90.5" ] ] ;
    schema1:subjectOf <urn:uuid:dde-image-catalog-record> ;
    schema1:url "https://earthexplorer.usgs.gov/" ;
    prov:wasGeneratedBy [ a schema1:Action,
                prov:Activity ;
            schema1:endTime "2023-06-15T03:45:12Z" ;
            schema1:name "Landsat-8 OLI imagery acquisition" ;
            schema1:participant [ a schema1:Role ;
                    schema1:contributor [ a schema1:Organization ;
                            schema1:name "USGS / NASA" ] ;
                    schema1:roleName "DataCollector" ] ;
            schema1:startTime "2023-06-15T03:45:00Z" ;
            prov:used [ schema1:instrument [ a schema1:Thing ;
                            schema1:additionalType "dde:signalGenerator" ;
                            schema1:name "Passive solar" ] ],
                [ schema1:instrument [ a schema1:Thing ;
                            schema1:additionalType "dde:equipment" ;
                            schema1:name "Operational Land Imager (OLI)" ] ],
                [ schema1:instrument [ a schema1:Thing ;
                            schema1:additionalType "dde:platform" ;
                            schema1:name "Landsat-8" ] ],
                [ schema1:instrument [ a schema1:Thing ;
                            schema1:additionalType "dde:sensorType" ;
                            schema1:name "Multispectral" ] ] ] .

<urn:uuid:dde-image-catalog-record> a schema1:Dataset ;
    dcterms:conformsTo <https://w3id.org/cdif/bbr/metadata/DDEproperties/ddeMandatory>,
        <https://w3id.org/cdif/bbr/metadata/profiles/DDEProfiles/DDEImage>,
        <https://w3id.org/cdif/core/1.0/>,
        <https://w3id.org/cdif/discovery/1.0/> ;
    schema1:about <urn:dde:example-landsat8-tibet> ;
    schema1:additionalType "dcat:CatalogRecord" ;
    schema1:sdDatePublished "2023-07-01" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
type: object
title: DDE Image profile
description: DDE profile for image resources (image, photograph, explanatoryFigure,
  map). Extends DDEDiscovery with resource type constraint and ddeImagery properties.
  If additionalType termCode is map, ddeGeographicDataset constraints are also applied.
allOf:
- $ref: https://usgin.github.io/ddeBuildingBlocks/build/annotated/bbr/metadata/DDEproperties/ddeMandatory/schema.yaml
- $ref: https://usgin.github.io/ddeBuildingBlocks/build/annotated/bbr/metadata/DDEproperties/ddeOptional/schema.yaml
- $ref: https://usgin.github.io/ddeBuildingBlocks/build/annotated/bbr/metadata/DDEproperties/ddeImagery/schema.yaml
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
            - image
            - map
            - photograph
            - explanatoryFigure
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
              const: map
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

* YAML version: [schema.yaml](https://usgin.github.io/ddeBuildingBlocks/build/annotated/bbr/metadata/profiles/DDEProfiles/DDEImage/schema.json)
* JSON version: [schema.json](https://usgin.github.io/ddeBuildingBlocks/build/annotated/bbr/metadata/profiles/DDEProfiles/DDEImage/schema.yaml)


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
[context.jsonld](https://usgin.github.io/ddeBuildingBlocks/build/annotated/bbr/metadata/profiles/DDEProfiles/DDEImage/context.jsonld)

## Sources

* [DDE Metadata Standard](https://www.ddeworld.org)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/ddeBuildingBlocks](https://github.com/usgin/ddeBuildingBlocks)
* Path: `_sources/profiles/DDEProfiles/DDEImage`

