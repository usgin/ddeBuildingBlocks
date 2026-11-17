
# DDE Acquisition Activity (Schema)

`dde.bbr.metadata.DDEproperties.ddeActivity` *v0.1*

Narrows cdifProvActivity for DDE acquisition. Requires at least one instrument typed with a DDE acquisition category (dde:sensorType, dde:platform, dde:equipment, dde:signalGenerator) alongside the Wikidata measuring-instrument term cdifProvActivity already requires. A DataCollector participant is permitted but not required, because the DDE XSD has no collector element. Defines properties: schema:instrument, schema:participant. Uses building blocks: cdifProvActivity (cdifDataType).

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# DDE acquisition activity

Narrows [cdifProvActivity](../../../cdifDataType/cdifProvActivity) for DDE
acquisition. It adds two things and inherits everything else.

## What it requires

**At least one instrument typed with a DDE acquisition category.** The four
categories are:

| category | DDE element |
|---|---|
| `dde:sensorType` | `sensor` |
| `dde:platform` | `platform` |
| `dde:equipment` | `equipment` |
| `dde:signalGenerator` | `signalGenerator` |

`cdifProvActivity` already requires an instrument described in place to carry the
Wikidata measuring-instrument term, so a DDE instrument's `schema:additionalType`
carries both:

```json
"schema:additionalType": [
  { "@id": "dde:sensorType" },
  { "@id": "https://www.wikidata.org/entity/Q3099911" }
]
```

The constraint uses `contains`, not `items`: an acquisition may list instruments
that are not DDE-categorised beside the ones that are, and `items` would reject
them. The four categories are separate `anyOf` branches rather than one `enum`, so
each can be extended independently and a failure names which was expected.

## What it does not require

**A data collector.** The DDE XSD has no collector element — `MD_Imagery` is
`sensor` [0..*], `platform`, `equipment`, `signalGenerator`, `wavelength` and
`processingLevel`, every one `minOccurs="0"` — so a `DataCollector` participant is
a convention rather than an obligation. `DataCollectorRole` in `$defs` records the
shape DDE imagery conventionally uses, a `schema:Role` with `roleName`
`DataCollector` wrapping a Person or an Organization, without imposing it.
Participants of any other shape `cdifProvActivity` permits remain valid.

## What it inherits

`schema:startTime`, `schema:endTime`, `schema:agent`, `schema:object`,
`schema:result`, `schema:location`, `schema:actionProcess`,
`schema:additionalProperty` and the rest come from `cdifProvActivity` unchanged,
including its requirement that an activity carry at least one of
`schema:instrument`, `schema:object` or `schema:actionProcess`.

## Examples

### DDE acquisition activity.
An imagery acquisition with two DDE-categorised instruments -- a sensor and a
platform -- each carrying the Wikidata measuring-instrument term that
cdifProvActivity requires, plus the conventional DataCollector participant and
temporal bounds. The participant is optional: the DDE XSD has no collector
element.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "dde": "https://www.ddeworld.org/resource/",
    "prov": "http://www.w3.org/ns/prov#"
  },
  "@type": [
    "schema:Action",
    "prov:Activity"
  ],
  "schema:name": "Landsat 8 OLI multispectral acquisition",
  "schema:startTime": "2024-03-01T10:15:00Z",
  "schema:endTime": "2024-03-01T10:17:00Z",
  "schema:instrument": [
    {
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "schema:name": "Multispectral",
      "schema:additionalType": [
        {
          "@id": "dde:sensorType"
        },
        {
          "@id": "https://www.wikidata.org/entity/Q3099911"
        }
      ]
    },
    {
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "schema:name": "Landsat 8",
      "schema:additionalType": [
        {
          "@id": "dde:platform"
        },
        {
          "@id": "https://www.wikidata.org/entity/Q3099911"
        }
      ]
    }
  ],
  "schema:participant": [
    {
      "@type": [
        "schema:Role"
      ],
      "schema:roleName": "DataCollector",
      "schema:contributor": {
        "@type": [
          "schema:Organization"
        ],
        "schema:name": "USGS / NASA"
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
      "prov": "http://www.w3.org/ns/prov#"
    },
    "https://usgin.github.io/ddeBuildingBlocks/build/annotated/bbr/metadata/DDEproperties/ddeActivity/context.jsonld",
    {
      "schema": "http://schema.org/",
      "dde": "https://www.ddeworld.org/resource/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@type": [
    "schema:Action",
    "prov:Activity"
  ],
  "schema:name": "Landsat 8 OLI multispectral acquisition",
  "schema:startTime": "2024-03-01T10:15:00Z",
  "schema:endTime": "2024-03-01T10:17:00Z",
  "schema:instrument": [
    {
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "schema:name": "Multispectral",
      "schema:additionalType": [
        {
          "@id": "dde:sensorType"
        },
        {
          "@id": "https://www.wikidata.org/entity/Q3099911"
        }
      ]
    },
    {
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "schema:name": "Landsat 8",
      "schema:additionalType": [
        {
          "@id": "dde:platform"
        },
        {
          "@id": "https://www.wikidata.org/entity/Q3099911"
        }
      ]
    }
  ],
  "schema:participant": [
    {
      "@type": [
        "schema:Role"
      ],
      "schema:roleName": "DataCollector",
      "schema:contributor": {
        "@type": [
          "schema:Organization"
        ],
        "schema:name": "USGS / NASA"
      }
    }
  ]
}
```

#### ttl
```ttl
@prefix dde: <https://www.ddeworld.org/resource/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix wd: <https://www.wikidata.org/entity/> .

[] a schema1:Action,
        prov:Activity ;
    schema1:endTime "2024-03-01T10:17:00Z" ;
    schema1:instrument [ a schema1:Product,
                schema1:Thing ;
            schema1:additionalType dde:sensorType,
                wd:Q3099911 ;
            schema1:name "Multispectral" ],
        [ a schema1:Product,
                schema1:Thing ;
            schema1:additionalType dde:platform,
                wd:Q3099911 ;
            schema1:name "Landsat 8" ] ;
    schema1:name "Landsat 8 OLI multispectral acquisition" ;
    schema1:participant [ a schema1:Role ;
            schema1:contributor [ a schema1:Organization ;
                    schema1:name "USGS / NASA" ] ;
            schema1:roleName "DataCollector" ] ;
    schema1:startTime "2024-03-01T10:15:00Z" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
type: object
title: DDE acquisition activity
description: 'Narrows cdifProvActivity for DDE acquisition. Everything an acquisition
  activity may carry -- schema:instrument, schema:participant, schema:startTime, schema:endTime,
  schema:agent and the rest -- is inherited from cdifProvActivity rather than restated
  here; this block adds only what is DDE-specific.

  What it adds: at least one instrument typed with a DDE acquisition category. cdifProvActivity
  already requires each described-in-place instrument to carry the Wikidata measuring-instrument
  term, so a DDE instrument''s schema:additionalType carries both, for example [{"@id":
  "dde:sensorType"}, {"@id": "https://www.wikidata.org/entity/Q3099911"}].

  What it does not add: a required data collector. The DDE XSD has no collector element
  -- MD_Imagery is sensor, platform, equipment, signalGenerator, wavelength and processingLevel,
  all optional -- so a DataCollector participant is a convention, not an obligation.
  DataCollectorRole below documents the shape without requiring it, and participants
  of any other shape cdifProvActivity allows remain valid.'
allOf:
- $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifProvActivity/schema.yaml
- type: object
  properties:
    schema:instrument:
      description: 'At least one instrument carries a DDE acquisition category. "contains"
        rather than "items" on purpose: an acquisition may legitimately list instruments
        that are not DDE-categorised alongside the ones that are, and constraining
        every item would reject them.'
      contains:
        $ref: '#/$defs/DdeTypedInstrument'
      x-jsonld-id: http://schema.org/instrument
    schema:participant:
      description: Unconstrained beyond cdifProvActivity. DataCollectorRole records
        the shape DDE imagery conventionally uses for the collecting agent; it is
        referenced here only so the definition travels with the block, and imposes
        nothing.
      x-jsonld-id: http://schema.org/participant
$defs:
  DdeTypedInstrument:
    type: object
    description: An instrument whose schema:additionalType names a DDE acquisition
      category. The four categories are listed as separate anyOf branches rather than
      one enum so each can be extended independently later, and so a validation failure
      names which category was expected.
    properties:
      schema:additionalType:
        type: array
        anyOf:
        - contains:
            type: object
            required:
            - '@id'
            properties:
              '@id':
                const: dde:sensorType
        - contains:
            type: object
            required:
            - '@id'
            properties:
              '@id':
                const: dde:platform
        - contains:
            type: object
            required:
            - '@id'
            properties:
              '@id':
                const: dde:equipment
        - contains:
            type: object
            required:
            - '@id'
            properties:
              '@id':
                const: dde:signalGenerator
        x-jsonld-id: http://schema.org/additionalType
    required:
    - schema:additionalType
  DataCollectorRole:
    type: object
    description: 'The conventional shape for the collecting agent: a schema:Role with
      roleName DataCollector wrapping a Person or an Organization. Documented, not
      required -- see the block description.'
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: schema:Role
      schema:roleName:
        const: DataCollector
        x-jsonld-id: http://schema.org/roleName
      schema:contributor:
        anyOf:
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/person/schema.yaml
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/organization/schema.yaml
        x-jsonld-id: http://schema.org/contributor
    required:
    - '@type'
    - schema:roleName
x-jsonld-prefixes:
  schema: http://schema.org/
  dde: https://www.ddeworld.org/resource/
  prov: http://www.w3.org/ns/prov#
x-bblocks-metadata:
  itemIdentifier: dde.bbr.metadata.DDEproperties.ddeActivity
  register: https://usgin.github.io/ddeBuildingBlocks/build/register.json
  version: '0.1'
  dateOfLastChange: '2026-11-17'

```

Links to the schema:

* YAML version: [schema.yaml](https://usgin.github.io/ddeBuildingBlocks/build/annotated/bbr/metadata/DDEproperties/ddeActivity/schema.json)
* JSON version: [schema.json](https://usgin.github.io/ddeBuildingBlocks/build/annotated/bbr/metadata/DDEproperties/ddeActivity/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "http://schema.org/",
    "prov": "http://www.w3.org/ns/prov#",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "wd": "https://www.wikidata.org/entity/",
    "nxs": "https://manual.nexusformat.org/classes/",
    "dde": "https://www.ddeworld.org/resource/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://usgin.github.io/ddeBuildingBlocks/build/annotated/bbr/metadata/DDEproperties/ddeActivity/context.jsonld)

## Sources

* [DDE Metadata Standard](https://www.ddeworld.org)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/ddeBuildingBlocks](https://github.com/usgin/ddeBuildingBlocks)
* Path: `_sources/DDEproperties/ddeActivity`

