
# DDE Geographic Dataset Properties (Schema)

`dde.bbr.metadata.DDEproperties.ddeGeographicDataset` *v0.1*

Conditional extension for geographic dataset resources. Implements MD_SpatialRepresentation (DDE spec Table 5): mandatory spatialCoverage, plus spatialRepresentationType, spatialResolution, referenceSystemType, and referenceSystemIdentifier. Defines properties: schema:spatialCoverage, schema:additionalProperty. Uses building blocks: spatialExtent (schemaorgProperties), additionalProperty (schemaorgProperties), identifier (schemaorgProperties).

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## DDE Geographic Dataset Properties

Conditional extension for geographic dataset resources. Implements MD_SpatialRepresentation from DDE spec Table 5 / XSD. This building block is composed into the DDEDataset profile when the resource type is `geographicDataset`.

### Required
- **`schema:spatialCoverage`**: Spatial extent of the geographic dataset. Mandatory for geographicDataset resource type.

### Optional (via `schema:additionalProperty`)

Each property is a `schema:PropertyValue` with a DDE `propertyID` and a value whose type is constrained per the XSD type definitions:

- **`dde:spatialRepresentationType`**: Value from `SpatialRepresentationTypeCode` enum: vector, grid, textTable, tin, stereoModel, video.
- **`dde:spatialResolution`**: Free text string (e.g., "1:1000000", "30m"). XSD type `CharacterString_Type`.
- **`dde:referenceSystemType`**: Value from `ReferenceSystemTypeCode` enum (28 values including geodeticGeographic2D, projected, vertical, etc.).
- **`dde:referenceSystemIdentifier`**: Follows `MD_Identifier` pattern — `schema:value` is the identifier code (e.g., "EPSG:4326"), with optional `schema:url` for the resolvable form. Requires either value or url.

## Examples

### Example DDE geographic dataset properties.
Shows spatialCoverage with GeoShape bounding box and additionalProperty entries for spatial representation type, resolution, reference system type, and reference system identifier.
#### json
```json
{
    "schema:spatialCoverage": {
        "@type": "schema:Place",
        "schema:geo": {
            "@type": "schema:GeoShape",
            "schema:box": "18.1609 73.499 53.5585 135.08"
        }
    },
    "schema:additionalProperty": [
        {
            "@type": "schema:PropertyValue",
            "schema:propertyID": ["dde:spatialRepresentationType"],
            "schema:name": "Spatial Representation Type",
            "schema:value": "vector"
        },
        {
            "@type": "schema:PropertyValue",
            "schema:propertyID": ["dde:spatialResolution"],
            "schema:name": "Spatial Resolution",
            "schema:value": "1:1000000"
        },
        {
            "@type": "schema:PropertyValue",
            "schema:propertyID": ["dde:referenceSystemType"],
            "schema:name": "Reference System Type",
            "schema:value": "geodeticGeographic2D"
        },
        {
            "@type": "schema:PropertyValue",
            "schema:propertyID": ["dde:referenceSystemIdentifier"],
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
      "dde": "https://www.ddeworld.org/resource/"
    },
    "https://usgin.github.io/ddeBuildingBlocks/build/annotated/bbr/metadata/DDEproperties/ddeGeographicDataset/context.jsonld"
  ],
  "schema:spatialCoverage": {
    "@type": "schema:Place",
    "schema:geo": {
      "@type": "schema:GeoShape",
      "schema:box": "18.1609 73.499 53.5585 135.08"
    }
  },
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
      "schema:value": "1:1000000"
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
@prefix schema1: <http://schema.org/> .

[] schema1:additionalProperty [ a schema1:PropertyValue ;
            schema1:name "Spatial Resolution" ;
            schema1:propertyID "dde:spatialResolution" ;
            schema1:value "1:1000000" ],
        [ a schema1:PropertyValue ;
            schema1:name "Reference System Type" ;
            schema1:propertyID "dde:referenceSystemType" ;
            schema1:value "geodeticGeographic2D" ],
        [ a schema1:PropertyValue ;
            schema1:name "Coordinate Reference System" ;
            schema1:propertyID "dde:referenceSystemIdentifier" ;
            schema1:url "https://epsg.io/4326" ;
            schema1:value "EPSG:4326" ],
        [ a schema1:PropertyValue ;
            schema1:name "Spatial Representation Type" ;
            schema1:propertyID "dde:spatialRepresentationType" ;
            schema1:value "vector" ] ;
    schema1:spatialCoverage [ a schema1:Place ;
            schema1:geo [ a schema1:GeoShape ;
                    schema1:box "18.1609 73.499 53.5585 135.08" ] ] .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: DDE Geographic Dataset properties
description: Conditional extension for geographic dataset resources. Implements MD_SpatialRepresentation
  entity (DDE spec Table 5) with spatialCoverage (mandatory), spatialRepresentationType
  (SpatialRepresentationTypeCode enum), spatialResolution (string), referenceSystemType
  (ReferenceSystemTypeCode enum), and referenceSystemIdentifier (MD_Identifier pattern).
type: object
properties:
  schema:spatialCoverage:
    description: Spatial extent of the geographic dataset. Mandatory for geographicDataset
      resource type.
    $ref: '#/$defs/SpatialExtent'
  schema:additionalProperty:
    type: array
    description: Spatial representation properties using DDE propertyIDs. Each item
      is a PropertyValue with a DDE propertyID and a value whose type depends on the
      property.
    items:
      anyOf:
      - $ref: '#/$defs/SpatialRepresentationTypePV'
      - $ref: '#/$defs/SpatialResolutionPV'
      - $ref: '#/$defs/ReferenceSystemTypePV'
      - $ref: '#/$defs/ReferenceSystemIdentifierPV'
      - $ref: '#/$defs/AdditionalProperty'
required:
- schema:spatialCoverage
$defs:
  SpatialExtent:
    $ref: https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/spatialExtent/schema.yaml
  AdditionalProperty:
    $ref: https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/additionalProperty/schema.yaml
  Identifier:
    $ref: https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/identifier/schema.yaml
  SpatialRepresentationTypePV:
    type: object
    description: Method used to represent geographic information in the resource.
      Value from SpatialRepresentationTypeCode (XSD).
    properties:
      '@type':
        const: schema:PropertyValue
      schema:propertyID:
        type: array
        contains:
          const: dde:spatialRepresentationType
        minItems: 1
      schema:name:
        type: string
      schema:value:
        type: string
        enum:
        - vector
        - grid
        - textTable
        - tin
        - stereoModel
        - video
    required:
    - schema:propertyID
    - schema:name
    - schema:value
  SpatialResolutionPV:
    type: object
    description: Spatial resolution of the dataset (free text, e.g. "1:1000000", "30m").
      Value is a string (CharacterString_Type in XSD).
    properties:
      '@type':
        const: schema:PropertyValue
      schema:propertyID:
        type: array
        contains:
          const: dde:spatialResolution
        minItems: 1
      schema:name:
        type: string
      schema:value:
        type: string
    required:
    - schema:propertyID
    - schema:name
    - schema:value
  ReferenceSystemTypePV:
    type: object
    description: Type of coordinate reference system. Value from ReferenceSystemTypeCode
      (XSD, 28 values).
    properties:
      '@type':
        const: schema:PropertyValue
      schema:propertyID:
        type: array
        contains:
          const: dde:referenceSystemType
        minItems: 1
      schema:name:
        type: string
      schema:value:
        type: string
        enum:
        - compoundEngineeringParametric
        - compoundEngineeringParametricTemporal
        - compoundEngineeringTemporal
        - compoundEngineeringVertical
        - compoundEngineeringVerticalTemporal
        - compoundGeographic2DParametric
        - compoundGeographic2DParametricTemporal
        - compoundGeographic2DTemporal
        - compoundGeographic2DVertical
        - compoundGeographicVerticalTemporal
        - compoundGeographic3DTemporal
        - compoundProjected2DParametric
        - compoundProjected2DParametricTemporal
        - compoundProjectedTemporal
        - compoundProjectedVertical
        - compoundProjectedVerticalTemporal
        - engineering
        - engineeringDesign
        - engineeringImage
        - geodeticGeocentric
        - geodeticGeographic2D
        - geodeticGeographic3D
        - geographicIdentifier
        - linear
        - parametric
        - projected
        - temporal
        - vertical
    required:
    - schema:propertyID
    - schema:name
    - schema:value
  ReferenceSystemIdentifierPV:
    type: object
    description: Identifier for the coordinate reference system. Follows the MD_Identifier
      pattern from the XSD (code + optional codeSpace, version, url). Value is the
      identifier code string (e.g. "EPSG:4326"), with optional schema:url for the
      resolvable form.
    properties:
      '@type':
        const: schema:PropertyValue
      schema:propertyID:
        type: array
        contains:
          const: dde:referenceSystemIdentifier
        minItems: 1
      schema:name:
        type: string
      schema:value:
        type: string
        description: The reference system identifier code (e.g. "EPSG:4326", "urn:ogc:def:crs:EPSG::4326").
      schema:url:
        type: string
        format: uri
        description: Resolvable URL for the reference system identifier (e.g. "https://epsg.io/4326").
    allOf:
    - required:
      - schema:propertyID
      - schema:name
    - anyOf:
      - required:
        - schema:value
      - required:
        - schema:url
x-jsonld-prefixes:
  schema: http://schema.org/
  dde: https://www.ddeworld.org/resource/

```

Links to the schema:

* YAML version: [schema.yaml](https://usgin.github.io/ddeBuildingBlocks/build/annotated/bbr/metadata/DDEproperties/ddeGeographicDataset/schema.json)
* JSON version: [schema.json](https://usgin.github.io/ddeBuildingBlocks/build/annotated/bbr/metadata/DDEproperties/ddeGeographicDataset/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "http://schema.org/",
    "dde": "https://www.ddeworld.org/resource/",
    "nxs": "http://purl.org/nexusformat/definitions/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://usgin.github.io/ddeBuildingBlocks/build/annotated/bbr/metadata/DDEproperties/ddeGeographicDataset/context.jsonld)

## Sources

* [DDE Metadata Standard](https://www.ddeworld.org)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/ddeBuildingBlocks](https://github.com/usgin/ddeBuildingBlocks)
* Path: `_sources/DDEproperties/ddeGeographicDataset`

