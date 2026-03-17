
# DDE Imagery Properties (Schema)

`dde.bbr.metadata.DDEproperties.ddeImagery` *v0.1*

Conditional extension for imagery resources using the CDIF provenance pattern (cdifProv). Maps DDE imagery acquisition metadata into prov:wasGeneratedBy activities: sensor, platform, equipment, and signalGenerator become typed instruments; collector becomes a participant with DataCollector role; startTime and endTime are activity temporal bounds. Wavelength and processedLevel remain as dataset-level schema:additionalProperty values. Defines properties: prov:wasGeneratedBy, schema:additionalProperty. Uses building blocks: instrument, agentInRole, person, organization, additionalProperty (schemaorgProperties).

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## DDE Imagery Properties

Conditional extension for imagery resources. Maps DDE imagery acquisition metadata into the CDIF provenance pattern (cdifProv). This building block is composed into the DDEImage profile when describing remote sensing or other imagery datasets.

All properties are optional.

### Imagery acquisition via `prov:wasGeneratedBy`

Each imagery acquisition event is represented as a provenance activity following the cdifProv pattern. The activity captures:

- **Instruments** (`prov:used` with `schema:instrument`): Each instrument is typed via `schema:additionalType` with a DDE category:
  - `dde:sensorType` — Type of sensor (e.g., "Multispectral", "SAR", "LiDAR")
  - `dde:platform` — Platform carrying the sensor (e.g., "Landsat-8", "Sentinel-2A")
  - `dde:equipment` — Equipment used for acquisition (e.g., "Operational Land Imager")
  - `dde:signalGenerator` — Type of signal used (e.g., "Passive solar", "Active radar")
- **Participants** (`schema:participant`): The data collector as an agentInRole with `schema:roleName: "DataCollector"`
- **Temporal bounds**: `schema:startTime` and `schema:endTime` on the activity (ISO 8601)

### Dataset-level properties via `schema:additionalProperty`

Properties that describe the image product itself (not the acquisition activity):

- **`dde:wavelength`** — Wavelength range (e.g., "0.43-2.29 micrometers"). Value: string.
- **`dde:processedLevel`** — Processing level. Value from `ProcessingLevelCode` enum: Level0, Level1, Level2, Level3, Level4.

## Examples

### Example DDE imagery properties.
Shows additionalProperty entries with DDE propertyIDs for sensor type, platform, wavelength range, signal generator, and processing level.
#### json
```json
{
    "prov:wasGeneratedBy": [
        {
            "@type": ["schema:Action", "prov:Activity"],
            "schema:name": "Landsat-8 OLI imagery acquisition",
            "schema:startTime": "2023-06-15T03:45:00Z",
            "schema:endTime": "2023-06-15T03:45:12Z",
            "prov:used": [
                {
                    "schema:instrument": {
                        "@type": ["schema:Thing"],
                        "schema:name": "Multispectral",
                        "schema:additionalType": "dde:sensorType"
                    }
                },
                {
                    "schema:instrument": {
                        "@type": ["schema:Thing"],
                        "schema:name": "Landsat-8",
                        "schema:additionalType": "dde:platform"
                    }
                },
                {
                    "schema:instrument": {
                        "@type": ["schema:Thing"],
                        "schema:name": "Operational Land Imager (OLI)",
                        "schema:additionalType": "dde:equipment"
                    }
                },
                {
                    "schema:instrument": {
                        "@type": ["schema:Thing"],
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
            "schema:propertyID": ["dde:wavelength"],
            "schema:name": "Wavelength Range",
            "schema:value": "0.43-2.29 micrometers"
        },
        {
            "@type": "schema:PropertyValue",
            "schema:propertyID": ["dde:processedLevel"],
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
      "dde": "https://www.ddeworld.org/resource/"
    },
    "https://usgin.github.io/ddeBuildingBlocks/build/annotated/bbr/metadata/DDEproperties/ddeImagery/context.jsonld"
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
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .

[] schema1:additionalProperty [ a schema1:PropertyValue ;
            schema1:name "Wavelength Range" ;
            schema1:propertyID "dde:wavelength" ;
            schema1:value "0.43-2.29 micrometers" ],
        [ a schema1:PropertyValue ;
            schema1:name "Processing Level" ;
            schema1:propertyID "dde:processedLevel" ;
            schema1:value "Level2" ] ;
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
                            schema1:additionalType "dde:equipment" ;
                            schema1:name "Operational Land Imager (OLI)" ] ],
                [ schema1:instrument [ a schema1:Thing ;
                            schema1:additionalType "dde:signalGenerator" ;
                            schema1:name "Passive solar" ] ],
                [ schema1:instrument [ a schema1:Thing ;
                            schema1:additionalType "dde:platform" ;
                            schema1:name "Landsat-8" ] ],
                [ schema1:instrument [ a schema1:Thing ;
                            schema1:additionalType "dde:sensorType" ;
                            schema1:name "Multispectral" ] ] ] .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: DDE Imagery properties
description: Conditional extension for imagery resources. Maps DDE imagery acquisition
  metadata into the CDIF provenance pattern (cdifProv). Sensor, platform, equipment,
  and signalGenerator become typed instruments (via schema:additionalType) under prov:wasGeneratedBy
  activities; collector becomes a schema:participant with DataCollector role; startTime
  and endTime are temporal bounds on the activity. Wavelength and processedLevel remain
  as dataset-level additionalProperty values. All properties are optional.
type: object
properties:
  prov:wasGeneratedBy:
    type: array
    description: Imagery acquisition activities following the cdifProv pattern. Each
      activity can include instruments typed with DDE categories (dde:sensorType,
      dde:platform, dde:equipment, dde:signalGenerator) via prov:used/schema:instrument,
      a data collector via schema:participant as an agentInRole, and temporal bounds
      via schema:startTime/schema:endTime.
    items:
      $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/_sources/cdifProperties/cdifProvActivity/schema.yaml
  schema:additionalProperty:
    type: array
    description: Dataset-level additional properties for imagery resources. Wavelength
      and processedLevel describe the image product itself rather than the acquisition
      activity.
    items:
      anyOf:
      - $ref: '#/$defs/WavelengthPV'
      - $ref: '#/$defs/ProcessedLevelPV'
      - $ref: '#/$defs/AdditionalProperty'
$defs:
  AdditionalProperty:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/_sources/schemaorgProperties/additionalProperty/schema.yaml
  WavelengthPV:
    type: object
    description: Wavelength range of the imagery (e.g. "0.45-0.52 micrometers"). XSD
      type CharacterString_Type.
    properties:
      '@type':
        const: schema:PropertyValue
      schema:propertyID:
        type: array
        contains:
          const: dde:wavelength
        minItems: 1
      schema:name:
        type: string
      schema:value:
        type: string
    required:
    - schema:propertyID
    - schema:name
    - schema:value
  ProcessedLevelPV:
    type: object
    description: Processing level of the imagery. Value from ProcessingLevelCode (XSD).
    properties:
      '@type':
        const: schema:PropertyValue
      schema:propertyID:
        type: array
        contains:
          const: dde:processedLevel
        minItems: 1
      schema:name:
        type: string
      schema:value:
        type: string
        enum:
        - Level0
        - Level1
        - Level2
        - Level3
        - Level4
    required:
    - schema:propertyID
    - schema:name
    - schema:value
x-jsonld-prefixes:
  schema: http://schema.org/
  dde: https://www.ddeworld.org/resource/
  prov: http://www.w3.org/ns/prov#

```

Links to the schema:

* YAML version: [schema.yaml](https://usgin.github.io/ddeBuildingBlocks/build/annotated/bbr/metadata/DDEproperties/ddeImagery/schema.json)
* JSON version: [schema.json](https://usgin.github.io/ddeBuildingBlocks/build/annotated/bbr/metadata/DDEproperties/ddeImagery/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "http://schema.org/",
    "dde": "https://www.ddeworld.org/resource/",
    "prov": "http://www.w3.org/ns/prov#",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://usgin.github.io/ddeBuildingBlocks/build/annotated/bbr/metadata/DDEproperties/ddeImagery/context.jsonld)

## Sources

* [DDE Metadata Standard](https://www.ddeworld.org)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/ddeBuildingBlocks](https://github.com/usgin/ddeBuildingBlocks)
* Path: `_sources/DDEproperties/ddeImagery`

