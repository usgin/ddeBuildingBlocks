
# DDE Service Information Properties (Schema)

`dde.bbr.metadata.DDEproperties.ddeServiceInfo` *v0.1*

Conditional extension for service resources. Implements SV_ServiceIdentification (DDE spec Table 2): serviceType (mandatory), containsOperations, accessProperties, operatedDataset, and endpointDescription. Defines properties: schema:distribution, schema:dataset, schema:additionalProperty. Uses building blocks: additionalProperty (schemaorgProperties), definedTerm (schemaorgProperties), identifier (schemaorgProperties).

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## DDE Service Information Properties

Conditional extension for service resources. Implements SV_ServiceIdentification from DDE spec Table 2. This building block is not included in the base DDEDiscovery profile — it is composed into the DDEService profile when describing web services.

### Required
- **`schema:serviceType`** (on WebAPI in `schema:distribution`): Service type specified as a `schema:DefinedTerm` from the DDE `ServiceTypeCode` codelist (`dde:codelist/ServiceTypeCode`). 35 codes in 9 categories from the DDE specification (Table 21):
  1. **Data services** (5): DataService>DataAccess, DataWorkflow, DataProcessing, MapView, Other
  2. **Knowledge services** (6): DDE_GeoscienceKnowledgeDirectory, DDE_GeoscienceKnowledgeContent, DDE_KnowledgeReasoning, DDE_DeepShovel, DDE_Scholar, DDE_OtherKnowledge
  3. **Platform services** (10): DDE_PlatformCatalogue, DDE_PlatformRegistry, DDE_PlatformModel, DDE_PlatformCloudComputing, DDE_PlatformAnnotation, DDE_API_Information, DDE_EarthExplorer, DDE_Platform>DataEvaluation, DDE_Platform>DataIdentifier, DDE_Platform>Other
  4. **Thematic services** (9): Theme>MineralResourceAssessment, GeologicMapping, GeologicalTime, GeologicalOccurrence, Dinosaur, GeographicName, GeomorphologyMapping, GeoscienceStandard, Other
  5-9. **Generic services** (5): VocabularyService, RegistryService, DiscoveryService, ViewService, OtherService

### Optional
- **`schema:potentialAction`** (on WebAPI): Operations available on the service (containsOperations). Array of Action objects with name and description.
- **`schema:termsOfService`** (on WebAPI): Access properties and constraints for the service. String or CreativeWork.
- **`schema:documentation`** (on WebAPI): Endpoint description document URL or CreativeWork reference.
- **`schema:dataset`** (on root): Datasets operated on by the service (operatedDataset). Array of URIs or Dataset references.
- **`schema:additionalProperty`**: Additional properties for service resources.

## Examples

### Example DDE service information.
Shows a distribution with a WebAPI using a DDE ServiceTypeCode and an optional operated dataset property.
#### json
```json
{
    "schema:distribution": [
        {
            "@type": ["schema:WebAPI"],
            "schema:name": "Arizona Geologic Unit View WFS",
            "schema:description": "OGC WFS service providing vector feature access to Arizona geologic unit data",
            "schema:serviceType": {
                "@type": "schema:DefinedTerm",
                "schema:name": "Data Access Service",
                "schema:termCode": "DataService>DataAccess",
                "schema:inDefinedTermSet": "dde:codelist/ServiceTypeCode"
            },
            "schema:potentialAction": [
                {
                    "@type": "schema:SearchAction",
                    "schema:name": "GetCapabilities",
                    "schema:target": {
                        "@type": "schema:EntryPoint",
                        "schema:urlTemplate": "http://services.azgs.az.gov/ArcGIS/services/OneGeology/AZGS_Arizona_Geology_WFS/MapServer/WFSServer?service=WFS&request=GetCapabilities",
                        "schema:httpMethod": "GET"
                    }
                },
                {
                    "@type": "schema:SearchAction",
                    "schema:name": "GetFeature",
                    "schema:description": "Retrieve geologic unit features by bounding box or attribute filter",
                    "schema:target": {
                        "@type": "schema:EntryPoint",
                        "schema:urlTemplate": "http://services.azgs.az.gov/ArcGIS/services/OneGeology/AZGS_Arizona_Geology_WFS/MapServer/WFSServer?service=WFS&request=GetFeature&typeName={typeName}&bbox={bbox}",
                        "schema:httpMethod": "GET"
                    }
                }
            ],
            "schema:documentation": {
                "@type": "schema:CreativeWork",
                "schema:name": "WFS Capabilities Document",
                "schema:url": "http://services.azgs.az.gov/ArcGIS/services/OneGeology/AZGS_Arizona_Geology_WFS/MapServer/WFSServer?service=WFS&request=GetCapabilities",
                "schema:encodingFormat": ["application/xml"]
            }
        },
        {
            "@type": ["schema:WebAPI"],
            "schema:name": "Arizona Lithostratigraphy WMS",
            "schema:description": "OGC WMS service providing map tile views of Arizona lithostratigraphy",
            "schema:serviceType": {
                "@type": "schema:DefinedTerm",
                "schema:name": "Map View Service",
                "schema:termCode": "DataService>MapView",
                "schema:inDefinedTermSet": "dde:codelist/ServiceTypeCode"
            },
            "schema:potentialAction": [
                {
                    "@type": "schema:SearchAction",
                    "schema:name": "GetMap",
                    "schema:description": "Retrieve rendered map tiles for a given bounding box and layers",
                    "schema:target": {
                        "@type": "schema:EntryPoint",
                        "schema:urlTemplate": "http://services.azgs.az.gov/ArcGIS/services/OneGeology/AZGS_Arizona_Geology/MapServer/WMSServer?service=WMS&request=GetMap&layers={layers}&bbox={bbox}&width={width}&height={height}&srs={srs}&format={format}",
                        "schema:httpMethod": "GET"
                    }
                }
            ]
        }
    ],
    "schema:dataset": [
        {
            "@type": "schema:PropertyValue",
            "schema:propertyID": "schema:identifier",
            "schema:name": "Arizona Geologic Units (Shapefile)",
            "schema:value": "urn:azgs:geologic-units-shp"
        },
        {
            "@type": "schema:PropertyValue",
            "schema:propertyID": "schema:identifier",
            "schema:name": "Arizona Geologic Units (GeoJSON)",
            "schema:url": "https://data.azgs.az.gov/geologic-units.geojson"
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
    "https://usgin.github.io/ddeBuildingBlocks/build/annotated/bbr/metadata/DDEproperties/ddeServiceInfo/context.jsonld"
  ],
  "schema:distribution": [
    {
      "@type": [
        "schema:WebAPI"
      ],
      "schema:name": "Arizona Geologic Unit View WFS",
      "schema:description": "OGC WFS service providing vector feature access to Arizona geologic unit data",
      "schema:serviceType": {
        "@type": "schema:DefinedTerm",
        "schema:name": "Data Access Service",
        "schema:termCode": "DataService>DataAccess",
        "schema:inDefinedTermSet": "dde:codelist/ServiceTypeCode"
      },
      "schema:potentialAction": [
        {
          "@type": "schema:SearchAction",
          "schema:name": "GetCapabilities",
          "schema:target": {
            "@type": "schema:EntryPoint",
            "schema:urlTemplate": "http://services.azgs.az.gov/ArcGIS/services/OneGeology/AZGS_Arizona_Geology_WFS/MapServer/WFSServer?service=WFS&request=GetCapabilities",
            "schema:httpMethod": "GET"
          }
        },
        {
          "@type": "schema:SearchAction",
          "schema:name": "GetFeature",
          "schema:description": "Retrieve geologic unit features by bounding box or attribute filter",
          "schema:target": {
            "@type": "schema:EntryPoint",
            "schema:urlTemplate": "http://services.azgs.az.gov/ArcGIS/services/OneGeology/AZGS_Arizona_Geology_WFS/MapServer/WFSServer?service=WFS&request=GetFeature&typeName={typeName}&bbox={bbox}",
            "schema:httpMethod": "GET"
          }
        }
      ],
      "schema:documentation": {
        "@type": "schema:CreativeWork",
        "schema:name": "WFS Capabilities Document",
        "schema:url": "http://services.azgs.az.gov/ArcGIS/services/OneGeology/AZGS_Arizona_Geology_WFS/MapServer/WFSServer?service=WFS&request=GetCapabilities",
        "schema:encodingFormat": [
          "application/xml"
        ]
      }
    },
    {
      "@type": [
        "schema:WebAPI"
      ],
      "schema:name": "Arizona Lithostratigraphy WMS",
      "schema:description": "OGC WMS service providing map tile views of Arizona lithostratigraphy",
      "schema:serviceType": {
        "@type": "schema:DefinedTerm",
        "schema:name": "Map View Service",
        "schema:termCode": "DataService>MapView",
        "schema:inDefinedTermSet": "dde:codelist/ServiceTypeCode"
      },
      "schema:potentialAction": [
        {
          "@type": "schema:SearchAction",
          "schema:name": "GetMap",
          "schema:description": "Retrieve rendered map tiles for a given bounding box and layers",
          "schema:target": {
            "@type": "schema:EntryPoint",
            "schema:urlTemplate": "http://services.azgs.az.gov/ArcGIS/services/OneGeology/AZGS_Arizona_Geology/MapServer/WMSServer?service=WMS&request=GetMap&layers={layers}&bbox={bbox}&width={width}&height={height}&srs={srs}&format={format}",
            "schema:httpMethod": "GET"
          }
        }
      ]
    }
  ],
  "schema:dataset": [
    {
      "@type": "schema:PropertyValue",
      "schema:propertyID": "schema:identifier",
      "schema:name": "Arizona Geologic Units (Shapefile)",
      "schema:value": "urn:azgs:geologic-units-shp"
    },
    {
      "@type": "schema:PropertyValue",
      "schema:propertyID": "schema:identifier",
      "schema:name": "Arizona Geologic Units (GeoJSON)",
      "schema:url": "https://data.azgs.az.gov/geologic-units.geojson"
    }
  ]
}
```

#### ttl
```ttl
@prefix schema1: <http://schema.org/> .

[] schema1:dataset [ a schema1:PropertyValue ;
            schema1:name "Arizona Geologic Units (GeoJSON)" ;
            schema1:propertyID "schema:identifier" ;
            schema1:url "https://data.azgs.az.gov/geologic-units.geojson" ],
        [ a schema1:PropertyValue ;
            schema1:name "Arizona Geologic Units (Shapefile)" ;
            schema1:propertyID "schema:identifier" ;
            schema1:value "urn:azgs:geologic-units-shp" ] ;
    schema1:distribution [ a schema1:WebAPI ;
            schema1:description "OGC WFS service providing vector feature access to Arizona geologic unit data" ;
            schema1:documentation [ a schema1:CreativeWork ;
                    schema1:encodingFormat "application/xml" ;
                    schema1:name "WFS Capabilities Document" ;
                    schema1:url "http://services.azgs.az.gov/ArcGIS/services/OneGeology/AZGS_Arizona_Geology_WFS/MapServer/WFSServer?service=WFS&request=GetCapabilities" ] ;
            schema1:name "Arizona Geologic Unit View WFS" ;
            schema1:potentialAction [ a schema1:SearchAction ;
                    schema1:description "Retrieve geologic unit features by bounding box or attribute filter" ;
                    schema1:name "GetFeature" ;
                    schema1:target [ a schema1:EntryPoint ;
                            schema1:httpMethod "GET" ;
                            schema1:urlTemplate "http://services.azgs.az.gov/ArcGIS/services/OneGeology/AZGS_Arizona_Geology_WFS/MapServer/WFSServer?service=WFS&request=GetFeature&typeName={typeName}&bbox={bbox}" ] ],
                [ a schema1:SearchAction ;
                    schema1:name "GetCapabilities" ;
                    schema1:target [ a schema1:EntryPoint ;
                            schema1:httpMethod "GET" ;
                            schema1:urlTemplate "http://services.azgs.az.gov/ArcGIS/services/OneGeology/AZGS_Arizona_Geology_WFS/MapServer/WFSServer?service=WFS&request=GetCapabilities" ] ] ;
            schema1:serviceType [ a schema1:DefinedTerm ;
                    schema1:inDefinedTermSet "dde:codelist/ServiceTypeCode" ;
                    schema1:name "Data Access Service" ;
                    schema1:termCode "DataService>DataAccess" ] ],
        [ a schema1:WebAPI ;
            schema1:description "OGC WMS service providing map tile views of Arizona lithostratigraphy" ;
            schema1:name "Arizona Lithostratigraphy WMS" ;
            schema1:potentialAction [ a schema1:SearchAction ;
                    schema1:description "Retrieve rendered map tiles for a given bounding box and layers" ;
                    schema1:name "GetMap" ;
                    schema1:target [ a schema1:EntryPoint ;
                            schema1:httpMethod "GET" ;
                            schema1:urlTemplate "http://services.azgs.az.gov/ArcGIS/services/OneGeology/AZGS_Arizona_Geology/MapServer/WMSServer?service=WMS&request=GetMap&layers={layers}&bbox={bbox}&width={width}&height={height}&srs={srs}&format={format}" ] ] ;
            schema1:serviceType [ a schema1:DefinedTerm ;
                    schema1:inDefinedTermSet "dde:codelist/ServiceTypeCode" ;
                    schema1:name "Map View Service" ;
                    schema1:termCode "DataService>MapView" ] ] .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: DDE Service Information properties
description: Conditional extension for service resources with DDE service type constraints.
  Implements SV_ServiceIdentification entity (DDE spec Table 2) with serviceType,
  containsOperations, accessProperties, operatedDataset, and endpointDescription.
type: object
properties:
  schema:distribution:
    type: array
    description: Must contain at least one WebAPI with a serviceType from the DDE
      ServiceTypeCode codelist.
    contains:
      type: object
      properties:
        '@type':
          type: array
          items:
            type: string
          contains:
            const: schema:WebAPI
          minItems: 1
        schema:serviceType:
          type: object
          properties:
            '@type':
              const: schema:DefinedTerm
            schema:inDefinedTermSet:
              const: dde:codelist/ServiceTypeCode
            schema:termCode:
              type: string
              enum:
              - DataService>DataAccess
              - DataService>DataWorkflow
              - DataService>DataProcessing
              - DataService>MapView
              - DataService>Other
              - DDE_GeoscienceKnowledgeDirectory
              - DDE_GeoscienceKnowledgeContent
              - DDE_KnowledgeReasoning
              - DDE_DeepShovel
              - DDE_Scholar
              - DDE_OtherKnowledge
              - DDE_PlatformCatalogue
              - DDE_PlatformRegistry
              - DDE_PlatformModel
              - DDE_PlatformCloudComputing
              - DDE_PlatformAnnotation
              - DDE_API_Information
              - DDE_EarthExplorer
              - DDE_Platform>DataEvaluation
              - DDE_Platform>DataIdentifier
              - DDE_Platform>Other
              - Theme>MineralResourceAssessment
              - Theme>GeologicMapping
              - Theme>GeologicalTime
              - Theme>GeologicalOccurrence
              - Theme>Dinosaur
              - Theme>GeographicName
              - Theme>GeomorphologyMapping
              - Theme>GeoscienceStandard
              - Theme>Other
              - VocabularyService
              - RegistryService
              - DiscoveryService
              - ViewService
              - OtherService
          required:
          - '@type'
          - schema:inDefinedTermSet
          - schema:termCode
        schema:potentialAction:
          type: array
          description: Operations available on the service (containsOperations).
          items:
            type: object
            properties:
              '@type':
                type: string
              schema:name:
                type: string
              schema:description:
                type: string
            required:
            - schema:name
        schema:termsOfService:
          description: Access properties and constraints for the service.
          anyOf:
          - type: string
          - type: object
            properties:
              '@type':
                const: schema:CreativeWork
              schema:name:
                type: string
              schema:url:
                type: string
                format: uri
        schema:documentation:
          description: Endpoint description document URL or reference.
          anyOf:
          - type: string
            format: uri
          - type: object
            properties:
              '@type':
                const: schema:CreativeWork
              schema:name:
                type: string
              schema:url:
                type: string
                format: uri
      required:
      - '@type'
      - schema:serviceType
    minContains: 1
  schema:dataset:
    type: array
    description: Datasets operated on by the service (operatedDataset). XSD type is
      MD_Identifier (code + codeSpace + version). Mapped to Identifier PropertyValue
      pattern (value or url required).
    items:
      anyOf:
      - type: string
        format: uri
      - $ref: '#/$defs/Identifier'
  schema:additionalProperty:
    type: array
    description: Optional properties for service resources.
    items:
      $ref: '#/$defs/AdditionalProperty'
required:
- schema:distribution
$defs:
  AdditionalProperty:
    $ref: https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/additionalProperty/schema.yaml
  DefinedTerm:
    $ref: https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/definedTerm/schema.yaml
  Identifier:
    $ref: https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/identifier/schema.yaml
x-jsonld-prefixes:
  schema: http://schema.org/
  dde: https://www.ddeworld.org/resource/

```

Links to the schema:

* YAML version: [schema.yaml](https://usgin.github.io/ddeBuildingBlocks/build/annotated/bbr/metadata/DDEproperties/ddeServiceInfo/schema.json)
* JSON version: [schema.json](https://usgin.github.io/ddeBuildingBlocks/build/annotated/bbr/metadata/DDEproperties/ddeServiceInfo/schema.yaml)


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
[context.jsonld](https://usgin.github.io/ddeBuildingBlocks/build/annotated/bbr/metadata/DDEproperties/ddeServiceInfo/context.jsonld)

## Sources

* [DDE Metadata Standard](https://www.ddeworld.org)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/ddeBuildingBlocks](https://github.com/usgin/ddeBuildingBlocks)
* Path: `_sources/DDEproperties/ddeServiceInfo`

