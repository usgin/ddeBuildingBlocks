
# DDE Geographic Dataset Properties (Schema)

`dde.bbr.metadata.DDEproperties.ddeGeographicDataset` *v0.1*

Conditional extension for geographic dataset resources. Implements MD_SpatialRepresentation (DDE spec Table 5): mandatory spatialCoverage, plus spatialRepresentationType, spatialResolution, referenceSystemType, referenceSystemIdentifier, and verticalExtent (EX_VerticalExtent). Defines properties: schema:spatialCoverage, schema:additionalProperty. Uses building blocks: spatialExtent (schemaorgProperties), additionalProperty (schemaorgProperties), identifier (schemaorgProperties).

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
- **`dde:verticalExtent`**: The `EX_VerticalExtent` of the dataset (DDE elevation). `schema:value` is a `schema:QuantitativeValue` whose `schema:minValue` and `schema:maxValue` are numbers, the lowest and highest vertical coordinates; at least one is required, so an open-ended range gives only the other. Its `schema:unitCode` gives their unit as a UCUM code (e.g. "m"). The PropertyValue's `schema:valueReference` names the vertical CRS as a `schema:DefinedTerm` with the identifier code in `schema:termCode` (e.g. "EPSG:5714", MSL height) and/or `schema:url`. Depths are negative in a height CRS, or positive in a depth CRS such as EPSG:5715. Unlike the other four, this shape is enforced: a PropertyValue with this propertyID whose value is not such a range fails, rather than passing as a generic additional property.

## Examples

### Example DDE geographic dataset properties.
Shows spatialCoverage with GeoShape bounding box and additionalProperty entries for spatial representation type, resolution, reference system type, reference system identifier, and vertical extent.
#### json
```json
{
  "schema:spatialCoverage": [
    {
      "@type": [
        "schema:Place"
      ],
      "schema:geo": {
        "@type": [
          "schema:GeoShape"
        ],
        "schema:box": "18.1609 73.499 53.5585 135.08"
      }
    }
  ],
  "schema:additionalProperty": [
    {
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "dde:spatialRepresentationType"
        }
      ],
      "schema:name": "Spatial Representation Type",
      "schema:value": "vector"
    },
    {
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "dde:spatialResolution"
        }
      ],
      "schema:name": "Spatial Resolution",
      "schema:value": "1:1000000"
    },
    {
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "dde:referenceSystemType"
        }
      ],
      "schema:name": "Reference System Type",
      "schema:value": "geodeticGeographic2D"
    },
    {
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "dde:referenceSystemIdentifier"
        }
      ],
      "schema:name": "Coordinate Reference System",
      "schema:value": "EPSG:4326",
      "schema:url": "https://epsg.io/4326"
    },
    {
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "dde:verticalExtent"
        }
      ],
      "schema:name": "Vertical Extent",
      "schema:value": {
        "@type": [
          "schema:QuantitativeValue"
        ],
        "schema:minValue": -154,
        "schema:maxValue": 8848,
        "schema:unitCode": "m"
      },
      "schema:valueReference": {
        "@type": [
          "schema:DefinedTerm"
        ],
        "schema:name": "MSL height",
        "schema:termCode": "EPSG:5714",
        "schema:url": "https://epsg.io/5714"
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
      "dde": "https://www.ddeworld.org/resource/"
    },
    "https://usgin.github.io/ddeBuildingBlocks/build/annotated/bbr/metadata/DDEproperties/ddeGeographicDataset/context.jsonld"
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
        "schema:box": "18.1609 73.499 53.5585 135.08"
      }
    }
  ],
  "schema:additionalProperty": [
    {
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "dde:spatialRepresentationType"
        }
      ],
      "schema:name": "Spatial Representation Type",
      "schema:value": "vector"
    },
    {
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "dde:spatialResolution"
        }
      ],
      "schema:name": "Spatial Resolution",
      "schema:value": "1:1000000"
    },
    {
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "dde:referenceSystemType"
        }
      ],
      "schema:name": "Reference System Type",
      "schema:value": "geodeticGeographic2D"
    },
    {
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "dde:referenceSystemIdentifier"
        }
      ],
      "schema:name": "Coordinate Reference System",
      "schema:value": "EPSG:4326",
      "schema:url": "https://epsg.io/4326"
    },
    {
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "dde:verticalExtent"
        }
      ],
      "schema:name": "Vertical Extent",
      "schema:value": {
        "@type": [
          "schema:QuantitativeValue"
        ],
        "schema:minValue": -154,
        "schema:maxValue": 8848,
        "schema:unitCode": "m"
      },
      "schema:valueReference": {
        "@type": [
          "schema:DefinedTerm"
        ],
        "schema:name": "MSL height",
        "schema:termCode": "EPSG:5714",
        "schema:url": "https://epsg.io/5714"
      }
    }
  ]
}
```

#### ttl
```ttl
@prefix dde: <https://www.ddeworld.org/resource/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

[] schema1:additionalProperty [ a schema1:PropertyValue ;
            schema1:name "Spatial Resolution" ;
            schema1:propertyID dde:spatialResolution ;
            schema1:value "1:1000000" ],
        [ a schema1:PropertyValue ;
            schema1:name "Spatial Representation Type" ;
            schema1:propertyID dde:spatialRepresentationType ;
            schema1:value "vector" ],
        [ a schema1:PropertyValue ;
            schema1:name "Vertical Extent" ;
            schema1:propertyID dde:verticalExtent ;
            schema1:value [ a schema1:QuantitativeValue ;
                    schema1:maxValue 8848 ;
                    schema1:minValue -154 ;
                    schema1:unitCode "m" ] ;
            schema1:valueReference [ a schema1:DefinedTerm ;
                    schema1:name "MSL height" ;
                    schema1:termCode "EPSG:5714" ;
                    schema1:url "https://epsg.io/5714" ] ],
        [ a schema1:PropertyValue ;
            schema1:name "Coordinate Reference System" ;
            schema1:propertyID dde:referenceSystemIdentifier ;
            schema1:url "https://epsg.io/4326" ;
            schema1:value "EPSG:4326" ],
        [ a schema1:PropertyValue ;
            schema1:name "Reference System Type" ;
            schema1:propertyID dde:referenceSystemType ;
            schema1:value "geodeticGeographic2D" ] ;
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
  (ReferenceSystemTypeCode enum), referenceSystemIdentifier (MD_Identifier pattern),
  and verticalExtent (EX_VerticalExtent - minimum and maximum value, units, vertical
  CRS).
type: object
properties:
  schema:spatialCoverage:
    description: Spatial extent of the geographic dataset. Mandatory for geographicDataset
      resource type.
    type: array
    items:
      $ref: '#/$defs/SpatialExtent'
    minItems: 1
    x-jsonld-id: http://schema.org/spatialCoverage
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
      - $ref: '#/$defs/VerticalExtentPV'
      - $ref: '#/$defs/AdditionalProperty'
      if:
        type: object
        properties:
          schema:propertyID:
            type: array
            contains:
              $ref: '#/$defs/VerticalExtentID'
        required:
        - schema:propertyID
      then:
        $ref: '#/$defs/VerticalExtentPV'
    x-jsonld-id: http://schema.org/additionalProperty
required:
- schema:spatialCoverage
$defs:
  SpatialExtent:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/spatialExtent/schema.yaml
  AdditionalProperty:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/additionalProperty/schema.yaml
  Identifier:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/identifier/schema.yaml
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
        x-jsonld-id: http://schema.org/propertyID
      schema:name:
        type: string
        x-jsonld-id: http://schema.org/name
      schema:value:
        type: string
        enum:
        - vector
        - grid
        - textTable
        - tin
        - stereoModel
        - video
        x-jsonld-id: http://schema.org/value
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
        x-jsonld-id: http://schema.org/propertyID
      schema:name:
        type: string
        x-jsonld-id: http://schema.org/name
      schema:value:
        type: string
        x-jsonld-id: http://schema.org/value
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
        x-jsonld-id: http://schema.org/propertyID
      schema:name:
        type: string
        x-jsonld-id: http://schema.org/name
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
        x-jsonld-id: http://schema.org/value
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
        x-jsonld-id: http://schema.org/propertyID
      schema:name:
        type: string
        x-jsonld-id: http://schema.org/name
      schema:value:
        type: string
        description: The reference system identifier code (e.g. "EPSG:4326", "urn:ogc:def:crs:EPSG::4326").
        x-jsonld-id: http://schema.org/value
      schema:url:
        type: string
        format: uri
        description: Resolvable URL for the reference system identifier (e.g. "https://epsg.io/4326").
        x-jsonld-id: http://schema.org/url
    allOf:
    - required:
      - schema:propertyID
      - schema:name
    - anyOf:
      - required:
        - schema:value
      - required:
        - schema:url
  VerticalExtentID:
    description: The dde:verticalExtent propertyID, as a string or an @id reference.
    anyOf:
    - const: dde:verticalExtent
    - type: object
      properties:
        '@id':
          const: dde:verticalExtent
      required:
      - '@id'
  VerticalExtentPV:
    type: object
    description: Vertical extent of the dataset (ISO 19115-3 EX_VerticalExtent; DDE
      elevation). schema:value is a schema:QuantitativeValue whose schema:minValue
      and schema:maxValue are the lowest and highest vertical coordinates, in the
      unit of its schema:unitCode (UCUM, e.g. "m"). schema:valueReference names the
      vertical coordinate reference system. Depths below a datum are negative values
      in a height CRS, or positive values in a depth CRS such as EPSG:5715. Give at
      least one bound; an open-ended range gives only the other. A PropertyValue whose
      propertyID is dde:verticalExtent must have this shape.
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: schema:PropertyValue
      schema:propertyID:
        type: array
        contains:
          $ref: '#/$defs/VerticalExtentID'
        minItems: 1
        x-jsonld-id: http://schema.org/propertyID
      schema:name:
        type: string
        x-jsonld-id: http://schema.org/name
      schema:value:
        type: object
        description: The vertical range.
        properties:
          '@type':
            type: array
            items:
              type: string
            contains:
              const: schema:QuantitativeValue
          schema:minValue:
            type: number
            description: Lowest vertical coordinate (EX_VerticalExtent/minimumValue).
            x-jsonld-id: http://schema.org/minValue
          schema:maxValue:
            type: number
            description: Highest vertical coordinate (EX_VerticalExtent/maximumValue).
            x-jsonld-id: http://schema.org/maxValue
          schema:unitCode:
            type: string
            description: Unit of the bounds, as a UCUM code (e.g. "m", "km", "[ft_i]").
            x-jsonld-id: http://schema.org/unitCode
          schema:unitText:
            type: string
            description: Unit of the bounds as text, where there is no code.
            x-jsonld-id: http://schema.org/unitText
        allOf:
        - required:
          - '@type'
        - anyOf:
          - required:
            - schema:minValue
          - required:
            - schema:maxValue
        x-jsonld-id: http://schema.org/value
      schema:valueReference:
        type: object
        description: The vertical coordinate reference system (EX_VerticalExtent/verticalCRSId),
          as a DefinedTerm whose termCode is the identifier code (e.g. "EPSG:5714")
          and whose schema:url is its resolvable form.
        properties:
          '@type':
            type: array
            items:
              type: string
            contains:
              const: schema:DefinedTerm
          schema:name:
            type: string
            x-jsonld-id: http://schema.org/name
          schema:termCode:
            type: string
            x-jsonld-id: http://schema.org/termCode
          schema:url:
            type: string
            format: uri
            x-jsonld-id: http://schema.org/url
        anyOf:
        - required:
          - schema:termCode
        - required:
          - schema:url
        x-jsonld-id: http://schema.org/valueReference
    required:
    - schema:propertyID
    - schema:name
    - schema:value
x-jsonld-prefixes:
  schema: http://schema.org/
  dde: https://www.ddeworld.org/resource/
x-bblocks-metadata:
  itemIdentifier: dde.bbr.metadata.DDEproperties.ddeGeographicDataset
  register: https://usgin.github.io/ddeBuildingBlocks/build/register.json
  version: '0.1'
  dateOfLastChange: '2026-11-20'

```

Links to the schema:

* YAML version: [schema.yaml](https://usgin.github.io/ddeBuildingBlocks/build/annotated/bbr/metadata/DDEproperties/ddeGeographicDataset/schema.json)
* JSON version: [schema.json](https://usgin.github.io/ddeBuildingBlocks/build/annotated/bbr/metadata/DDEproperties/ddeGeographicDataset/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "http://schema.org/",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "dde": "https://www.ddeworld.org/resource/",
    "nxs": "https://manual.nexusformat.org/classes/",
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

