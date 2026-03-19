
# DDE WebAPI profile (Schema)

`dde.bbr.metadata.profiles.DDEProfiles.DDEWebAPI` *v0.1*

DDE profile for resources that are web services. Composes ddeMandatory, ddeOptional, and the CDIF webAPI building block. Narrows serviceType to the DDE ServiceTypeCode codelist. Includes dataset references for operated datasets.

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### Example DDE WebAPI metadata record
DDE discovery metadata for a geological map WMS/WFS service. The resource itself
is a WebAPI with DDE service type classification, operations (GetMap, GetFeature),
terms of service, and capability document reference.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "dcterms": "http://purl.org/dc/terms/",
    "dcat": "http://www.w3.org/ns/dcat#",
    "dde": "https://www.ddeworld.org/resource/",
    "ex": "https://example.org/"
  },
  "@id": "ex:dde-webapi-001",
  "@type": [
    "schema:Dataset",
    "schema:WebAPI",
    "schema:Product"
  ],
  "schema:name": "DDE Global Geological Map Service",
  "schema:identifier": "https://doi.org/10.1234/dde-geomap-api",
  "schema:description": "A WMS/WFS service providing access to the DDE Global Geological Map, offering tiled map views and vector feature queries for geological units, faults, and contacts at 1:5M scale.",
  "schema:url": "https://example.org/services/dde-geomap",
  "schema:dateModified": "2026-02-15",
  "schema:license": [
    "https://creativecommons.org/licenses/by/4.0/"
  ],
  "schema:additionalType": [
    {
      "@type": "schema:DefinedTerm",
      "schema:inDefinedTermSet": "dde:codelist/ResourceTypeCode",
      "schema:termCode": "webAPI",
      "schema:name": "Web API"
    }
  ],
  "schema:keywords": [
    {
      "@type": "schema:DefinedTerm",
      "schema:inDefinedTermSet": "dde:codelist/TopicCategoryCode",
      "schema:termCode": "GeologicMapping",
      "schema:name": "Geologic Mapping"
    },
    {
      "@type": "schema:DefinedTerm",
      "schema:inDefinedTermSet": "dde:codelist/AcquisitionTypeCode",
      "schema:termCode": "Compilation",
      "schema:name": "Compilation"
    }
  ],
  "schema:image": [
    {
      "@type": "schema:ImageObject",
      "schema:contentUrl": "https://example.org/services/dde-geomap/preview.png",
      "schema:name": "Service preview showing geological map tiles"
    }
  ],
  "schema:serviceType": {
    "@type": "schema:DefinedTerm",
    "schema:inDefinedTermSet": "dde:codelist/ServiceTypeCode",
    "schema:termCode": "DataService>MapView",
    "schema:name": "Map View Data Service"
  },
  "schema:termsOfService": "Open access, no authentication required. Rate limit: 1000 requests/hour.",
  "schema:documentation": {
    "@type": "schema:CreativeWork",
    "schema:name": "OGC WMS GetCapabilities",
    "schema:url": "https://example.org/services/dde-geomap/wms?service=WMS&request=GetCapabilities"
  },
  "schema:potentialAction": [
    {
      "@type": "schema:Action",
      "schema:name": "GetMap",
      "schema:description": "Request a rendered map image for a geographic extent",
      "schema:target": {
        "@type": "schema:EntryPoint",
        "schema:urlTemplate": "https://example.org/services/dde-geomap/wms?service=WMS&request=GetMap&layers={layer}&bbox={bbox}&width={width}&height={height}&format={format}",
        "schema:httpMethod": "GET",
        "schema:encodingFormat": "image/png"
      }
    },
    {
      "@type": "schema:Action",
      "schema:name": "GetFeature",
      "schema:description": "Query vector features for geological units within a bounding box",
      "schema:target": {
        "@type": "schema:EntryPoint",
        "schema:urlTemplate": "https://example.org/services/dde-geomap/wfs?service=WFS&request=GetFeature&typeName={typeName}&bbox={bbox}&outputFormat={format}",
        "schema:httpMethod": "GET",
        "schema:encodingFormat": "application/json"
      }
    }
  ],
  "schema:dataset": [
    "https://doi.org/10.1234/dde-global-geomap-v1"
  ],
  "schema:subjectOf": {
    "@id": "urn:uuid:dde-webapi-catalog-record",
    "@type": [
      "schema:Dataset"
    ],
    "schema:additionalType": [
      "dcat:CatalogRecord"
    ],
    "schema:about": {
      "@id": "ex:dde-webapi-001"
    },
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/core/1.0/"
      },
      {
        "@id": "https://w3id.org/cdif/discovery/1.0/"
      },
      {
        "@id": "https://w3id.org/cdif/bbr/metadata/profiles/DDEProfiles/DDEWebAPI"
      },
      {
        "@id": "https://w3id.org/cdif/bbr/metadata/DDEproperties/ddeMandatory"
      }
    ]
  }
}

```

#### jsonld
```jsonld
{
  "@context": [
    "https://usgin.github.io/ddeBuildingBlocks/build/annotated/bbr/metadata/profiles/DDEProfiles/DDEWebAPI/context.jsonld",
    {
      "schema": "http://schema.org/",
      "dcterms": "http://purl.org/dc/terms/",
      "dcat": "http://www.w3.org/ns/dcat#",
      "dde": "https://www.ddeworld.org/resource/",
      "ex": "https://example.org/"
    }
  ],
  "@id": "ex:dde-webapi-001",
  "@type": [
    "schema:Dataset",
    "schema:WebAPI",
    "schema:Product"
  ],
  "schema:name": "DDE Global Geological Map Service",
  "schema:identifier": "https://doi.org/10.1234/dde-geomap-api",
  "schema:description": "A WMS/WFS service providing access to the DDE Global Geological Map, offering tiled map views and vector feature queries for geological units, faults, and contacts at 1:5M scale.",
  "schema:url": "https://example.org/services/dde-geomap",
  "schema:dateModified": "2026-02-15",
  "schema:license": [
    "https://creativecommons.org/licenses/by/4.0/"
  ],
  "schema:additionalType": [
    {
      "@type": "schema:DefinedTerm",
      "schema:inDefinedTermSet": "dde:codelist/ResourceTypeCode",
      "schema:termCode": "webAPI",
      "schema:name": "Web API"
    }
  ],
  "schema:keywords": [
    {
      "@type": "schema:DefinedTerm",
      "schema:inDefinedTermSet": "dde:codelist/TopicCategoryCode",
      "schema:termCode": "GeologicMapping",
      "schema:name": "Geologic Mapping"
    },
    {
      "@type": "schema:DefinedTerm",
      "schema:inDefinedTermSet": "dde:codelist/AcquisitionTypeCode",
      "schema:termCode": "Compilation",
      "schema:name": "Compilation"
    }
  ],
  "schema:image": [
    {
      "@type": "schema:ImageObject",
      "schema:contentUrl": "https://example.org/services/dde-geomap/preview.png",
      "schema:name": "Service preview showing geological map tiles"
    }
  ],
  "schema:serviceType": {
    "@type": "schema:DefinedTerm",
    "schema:inDefinedTermSet": "dde:codelist/ServiceTypeCode",
    "schema:termCode": "DataService>MapView",
    "schema:name": "Map View Data Service"
  },
  "schema:termsOfService": "Open access, no authentication required. Rate limit: 1000 requests/hour.",
  "schema:documentation": {
    "@type": "schema:CreativeWork",
    "schema:name": "OGC WMS GetCapabilities",
    "schema:url": "https://example.org/services/dde-geomap/wms?service=WMS&request=GetCapabilities"
  },
  "schema:potentialAction": [
    {
      "@type": "schema:Action",
      "schema:name": "GetMap",
      "schema:description": "Request a rendered map image for a geographic extent",
      "schema:target": {
        "@type": "schema:EntryPoint",
        "schema:urlTemplate": "https://example.org/services/dde-geomap/wms?service=WMS&request=GetMap&layers={layer}&bbox={bbox}&width={width}&height={height}&format={format}",
        "schema:httpMethod": "GET",
        "schema:encodingFormat": "image/png"
      }
    },
    {
      "@type": "schema:Action",
      "schema:name": "GetFeature",
      "schema:description": "Query vector features for geological units within a bounding box",
      "schema:target": {
        "@type": "schema:EntryPoint",
        "schema:urlTemplate": "https://example.org/services/dde-geomap/wfs?service=WFS&request=GetFeature&typeName={typeName}&bbox={bbox}&outputFormat={format}",
        "schema:httpMethod": "GET",
        "schema:encodingFormat": "application/json"
      }
    }
  ],
  "schema:dataset": [
    "https://doi.org/10.1234/dde-global-geomap-v1"
  ],
  "schema:subjectOf": {
    "@id": "urn:uuid:dde-webapi-catalog-record",
    "@type": [
      "schema:Dataset"
    ],
    "schema:additionalType": [
      "dcat:CatalogRecord"
    ],
    "schema:about": {
      "@id": "ex:dde-webapi-001"
    },
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/core/1.0/"
      },
      {
        "@id": "https://w3id.org/cdif/discovery/1.0/"
      },
      {
        "@id": "https://w3id.org/cdif/bbr/metadata/profiles/DDEProfiles/DDEWebAPI"
      },
      {
        "@id": "https://w3id.org/cdif/bbr/metadata/DDEproperties/ddeMandatory"
      }
    ]
  }
}
```

#### ttl
```ttl
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .

ex:dde-webapi-001 a schema1:Dataset,
        schema1:Product,
        schema1:WebAPI ;
    schema1:additionalType [ a schema1:DefinedTerm ;
            schema1:inDefinedTermSet "dde:codelist/ResourceTypeCode" ;
            schema1:name "Web API" ;
            schema1:termCode "webAPI" ] ;
    schema1:dataset "https://doi.org/10.1234/dde-global-geomap-v1" ;
    schema1:dateModified "2026-02-15" ;
    schema1:description "A WMS/WFS service providing access to the DDE Global Geological Map, offering tiled map views and vector feature queries for geological units, faults, and contacts at 1:5M scale." ;
    schema1:documentation [ a schema1:CreativeWork ;
            schema1:name "OGC WMS GetCapabilities" ;
            schema1:url "https://example.org/services/dde-geomap/wms?service=WMS&request=GetCapabilities" ] ;
    schema1:identifier "https://doi.org/10.1234/dde-geomap-api" ;
    schema1:image [ a schema1:ImageObject ;
            schema1:contentUrl "https://example.org/services/dde-geomap/preview.png" ;
            schema1:name "Service preview showing geological map tiles" ] ;
    schema1:keywords [ a schema1:DefinedTerm ;
            schema1:inDefinedTermSet "dde:codelist/TopicCategoryCode" ;
            schema1:name "Geologic Mapping" ;
            schema1:termCode "GeologicMapping" ],
        [ a schema1:DefinedTerm ;
            schema1:inDefinedTermSet "dde:codelist/AcquisitionTypeCode" ;
            schema1:name "Compilation" ;
            schema1:termCode "Compilation" ] ;
    schema1:license "https://creativecommons.org/licenses/by/4.0/" ;
    schema1:name "DDE Global Geological Map Service" ;
    schema1:potentialAction [ a schema1:Action ;
            schema1:description "Request a rendered map image for a geographic extent" ;
            schema1:name "GetMap" ;
            schema1:target [ a schema1:EntryPoint ;
                    schema1:encodingFormat "image/png" ;
                    schema1:httpMethod "GET" ;
                    schema1:urlTemplate "https://example.org/services/dde-geomap/wms?service=WMS&request=GetMap&layers={layer}&bbox={bbox}&width={width}&height={height}&format={format}" ] ],
        [ a schema1:Action ;
            schema1:description "Query vector features for geological units within a bounding box" ;
            schema1:name "GetFeature" ;
            schema1:target [ a schema1:EntryPoint ;
                    schema1:encodingFormat "application/json" ;
                    schema1:httpMethod "GET" ;
                    schema1:urlTemplate "https://example.org/services/dde-geomap/wfs?service=WFS&request=GetFeature&typeName={typeName}&bbox={bbox}&outputFormat={format}" ] ] ;
    schema1:serviceType [ a schema1:DefinedTerm ;
            schema1:inDefinedTermSet "dde:codelist/ServiceTypeCode" ;
            schema1:name "Map View Data Service" ;
            schema1:termCode "DataService>MapView" ] ;
    schema1:subjectOf <urn:uuid:dde-webapi-catalog-record> ;
    schema1:termsOfService "Open access, no authentication required. Rate limit: 1000 requests/hour." ;
    schema1:url "https://example.org/services/dde-geomap" .

<urn:uuid:dde-webapi-catalog-record> a schema1:Dataset ;
    dcterms:conformsTo <https://w3id.org/cdif/bbr/metadata/DDEproperties/ddeMandatory>,
        <https://w3id.org/cdif/bbr/metadata/profiles/DDEProfiles/DDEWebAPI>,
        <https://w3id.org/cdif/core/1.0/>,
        <https://w3id.org/cdif/discovery/1.0/> ;
    schema1:about ex:dde-webapi-001 ;
    schema1:additionalType "dcat:CatalogRecord" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
type: object
title: DDE WebAPI profile
description: DDE profile for resources that ARE web services. The resource itself
  is described as a WebAPI with service type, operations, terms of service, and documentation.
  Composes ddeMandatory + ddeOptional for discovery metadata, and the CDIF webAPI
  building block for service-specific properties (serviceType, potentialAction, termsOfService,
  documentation). DDE narrows serviceType to require a term from the DDE ServiceTypeCode
  codelist. schema:dataset identifies datasets operated on by the service.
allOf:
- $ref: https://usgin.github.io/ddeBuildingBlocks/build/annotated/bbr/metadata/DDEproperties/ddeMandatory/schema.yaml
- $ref: https://usgin.github.io/ddeBuildingBlocks/build/annotated/bbr/metadata/DDEproperties/ddeOptional/schema.yaml
- $ref: '#/$defs/CdifWebAPI'
- type: object
  properties:
    '@type':
      type: array
      items:
        type: string
      contains:
        const: schema:WebAPI
      description: Must include schema:WebAPI since the resource itself is a service.
    schema:serviceType:
      description: DDE service type classification from the ServiceTypeCode codelist.
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
    schema:dataset:
      type: array
      description: Datasets operated on by the service (DDE operatedDataset).
      items:
        anyOf:
        - type: string
          format: uri
        - $ref: '#/$defs/Identifier'
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
            - service
            - webAPI
            - repository
        required:
        - '@type'
        - schema:inDefinedTermSet
        - schema:termCode
      minContains: 1
  required:
  - '@type'
$defs:
  CdifWebAPI:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/_sources/schemaorgProperties/webAPI/schema.yaml
  Identifier:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/_sources/schemaorgProperties/identifier/schema.yaml

```

Links to the schema:

* YAML version: [schema.yaml](https://usgin.github.io/ddeBuildingBlocks/build/annotated/bbr/metadata/profiles/DDEProfiles/DDEWebAPI/schema.json)
* JSON version: [schema.json](https://usgin.github.io/ddeBuildingBlocks/build/annotated/bbr/metadata/profiles/DDEProfiles/DDEWebAPI/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "http://schema.org/",
    "dde": "https://www.ddeworld.org/resource/",
    "dcterms": "http://purl.org/dc/terms/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://usgin.github.io/ddeBuildingBlocks/build/annotated/bbr/metadata/profiles/DDEProfiles/DDEWebAPI/context.jsonld)

## Sources

* [DDE Metadata Standard](https://www.ddeworld.org)
* [schema.org WebAPI](https://schema.org/WebAPI)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/ddeBuildingBlocks](https://github.com/usgin/ddeBuildingBlocks)
* Path: `_sources/profiles/DDEProfiles/DDEWebAPI`

