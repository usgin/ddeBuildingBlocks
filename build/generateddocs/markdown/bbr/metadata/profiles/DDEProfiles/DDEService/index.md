
# DDE Service profile (Schema)

`dde.bbr.metadata.profiles.DDEProfiles.DDEService` *v0.1*

DDE profile for service resources (repository, service, webAPI). Extends DDEDiscovery with resource type constraint and ddeServiceInfo conditional properties (serviceType, containsOperations, accessProperties, etc.).

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## DDE Service Profile

DDE profile for service resources. Extends DDEDiscovery with a resource type constraint and the ddeServiceInfo building block for service-specific properties.

### Resource type codes
repository, service, webAPI

### Composed building blocks

1. **DDEDiscovery** — Base DDE discovery profile
2. **ddeServiceInfo** — Service properties: serviceType (mandatory), containsOperations, accessProperties, operatedDataset, endpointDescription
3. **Resource type constraint** — `schema:termCode` must be one of the service group codes

## Examples

### DDE Service metadata example
DDE discovery metadata for the OneGeology WFS data access service with DDE ServiceTypeCode, potentialAction operations, and operated dataset references.
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
  "@id": "urn:dde:example-onegeology-wfs",
  "@type": [
    "schema:Dataset"
  ],
  "schema:name": "DDE OneGeology WFS Data Access Service",
  "schema:description": "OGC Web Feature Service providing vector feature access to harmonized geological unit data from participating OneGeology geological surveys. Supports WFS 2.0 GetCapabilities, DescribeFeatureType, and GetFeature operations with GeoSciML Portrayal output.",
  "schema:identifier": "urn:onegeology:wfs-global-2024",
  "schema:dateModified": "2024-03-15",
  "schema:inLanguage": "eng",
  "schema:license": [
    {
      "@type": "schema:CreativeWork",
      "schema:name": "Creative Commons Attribution 4.0",
      "schema:url": "https://creativecommons.org/licenses/by/4.0/"
    }
  ],
  "schema:url": "https://onegeology.org/technical_implementation/",
  "schema:subjectOf": {
    "@id": "urn:uuid:dde-service-catalog-record",
    "@type": [
      "schema:Dataset"
    ],
    "schema:additionalType": [
      "dcat:CatalogRecord"
    ],
    "schema:about": {
      "@id": "urn:dde:example-onegeology-wfs"
    },
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/core/1.0/"
      },
      {
        "@id": "https://w3id.org/cdif/discovery/1.0/"
      },
      {
        "@id": "https://w3id.org/cdif/bbr/metadata/profiles/DDEProfiles/DDEService"
      }
    ],
    "schema:sdDatePublished": "2024-03-15"
  },
  "schema:additionalType": [
    {
      "@type": "schema:DefinedTerm",
      "schema:name": "Service",
      "schema:termCode": "service",
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
    "OneGeology",
    "WFS",
    "geological map",
    "GeoSciML"
  ],
  "schema:image": [
    {
      "@type": "schema:ImageObject",
      "schema:contentUrl": "https://onegeology.org/images/wfs-service-preview.png",
      "schema:name": "service preview",
      "schema:encodingFormat": "image/png"
    }
  ],
  "schema:distribution": [
    {
      "@type": [
        "schema:WebAPI"
      ],
      "schema:name": "OneGeology Global WFS",
      "schema:description": "OGC WFS 2.0 service for harmonized geological unit features",
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
            "schema:urlTemplate": "https://onegeology.org/wfs?service=WFS&request=GetCapabilities",
            "schema:httpMethod": [
              "GET"
            ]
          }
        },
        {
          "@type": "schema:SearchAction",
          "schema:name": "GetFeature",
          "schema:description": "Retrieve geological unit features by bounding box",
          "schema:target": {
            "@type": "schema:EntryPoint",
            "schema:urlTemplate": "https://onegeology.org/wfs?service=WFS&request=GetFeature&typeName={typeName}&bbox={bbox}",
            "schema:httpMethod": [
              "GET"
            ]
          }
        }
      ],
      "schema:documentation": {
        "@type": "schema:CreativeWork",
        "schema:name": "WFS Capabilities Document",
        "schema:url": "https://onegeology.org/wfs?service=WFS&request=GetCapabilities",
        "schema:encodingFormat": [
          "application/xml"
        ]
      }
    }
  ],
  "schema:dataset": [
    {
      "@type": "schema:PropertyValue",
      "schema:propertyID": "schema:identifier",
      "schema:name": "OneGeology Global Geological Map Data",
      "schema:url": "https://onegeology.org/data/"
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
    "https://usgin.github.io/ddeBuildingBlocks/build/annotated/bbr/metadata/profiles/DDEProfiles/DDEService/context.jsonld",
    {
      "schema": "http://schema.org/",
      "dde": "https://www.ddeworld.org/resource/",
      "cdif": "https://cdif.org/profile/",
      "dcterms": "http://purl.org/dc/terms/",
      "dcat": "http://www.w3.org/ns/dcat#",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "urn:dde:example-onegeology-wfs",
  "@type": [
    "schema:Dataset"
  ],
  "schema:name": "DDE OneGeology WFS Data Access Service",
  "schema:description": "OGC Web Feature Service providing vector feature access to harmonized geological unit data from participating OneGeology geological surveys. Supports WFS 2.0 GetCapabilities, DescribeFeatureType, and GetFeature operations with GeoSciML Portrayal output.",
  "schema:identifier": "urn:onegeology:wfs-global-2024",
  "schema:dateModified": "2024-03-15",
  "schema:inLanguage": "eng",
  "schema:license": [
    {
      "@type": "schema:CreativeWork",
      "schema:name": "Creative Commons Attribution 4.0",
      "schema:url": "https://creativecommons.org/licenses/by/4.0/"
    }
  ],
  "schema:url": "https://onegeology.org/technical_implementation/",
  "schema:subjectOf": {
    "@id": "urn:uuid:dde-service-catalog-record",
    "@type": [
      "schema:Dataset"
    ],
    "schema:additionalType": [
      "dcat:CatalogRecord"
    ],
    "schema:about": {
      "@id": "urn:dde:example-onegeology-wfs"
    },
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/core/1.0/"
      },
      {
        "@id": "https://w3id.org/cdif/discovery/1.0/"
      },
      {
        "@id": "https://w3id.org/cdif/bbr/metadata/profiles/DDEProfiles/DDEService"
      }
    ],
    "schema:sdDatePublished": "2024-03-15"
  },
  "schema:additionalType": [
    {
      "@type": "schema:DefinedTerm",
      "schema:name": "Service",
      "schema:termCode": "service",
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
    "OneGeology",
    "WFS",
    "geological map",
    "GeoSciML"
  ],
  "schema:image": [
    {
      "@type": "schema:ImageObject",
      "schema:contentUrl": "https://onegeology.org/images/wfs-service-preview.png",
      "schema:name": "service preview",
      "schema:encodingFormat": "image/png"
    }
  ],
  "schema:distribution": [
    {
      "@type": [
        "schema:WebAPI"
      ],
      "schema:name": "OneGeology Global WFS",
      "schema:description": "OGC WFS 2.0 service for harmonized geological unit features",
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
            "schema:urlTemplate": "https://onegeology.org/wfs?service=WFS&request=GetCapabilities",
            "schema:httpMethod": [
              "GET"
            ]
          }
        },
        {
          "@type": "schema:SearchAction",
          "schema:name": "GetFeature",
          "schema:description": "Retrieve geological unit features by bounding box",
          "schema:target": {
            "@type": "schema:EntryPoint",
            "schema:urlTemplate": "https://onegeology.org/wfs?service=WFS&request=GetFeature&typeName={typeName}&bbox={bbox}",
            "schema:httpMethod": [
              "GET"
            ]
          }
        }
      ],
      "schema:documentation": {
        "@type": "schema:CreativeWork",
        "schema:name": "WFS Capabilities Document",
        "schema:url": "https://onegeology.org/wfs?service=WFS&request=GetCapabilities",
        "schema:encodingFormat": [
          "application/xml"
        ]
      }
    }
  ],
  "schema:dataset": [
    {
      "@type": "schema:PropertyValue",
      "schema:propertyID": "schema:identifier",
      "schema:name": "OneGeology Global Geological Map Data",
      "schema:url": "https://onegeology.org/data/"
    }
  ]
}
```

#### ttl
```ttl
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix schema1: <http://schema.org/> .

<urn:dde:example-onegeology-wfs> a schema1:Dataset ;
    schema1:additionalType [ a schema1:DefinedTerm ;
            schema1:inDefinedTermSet "dde:codelist/ResourceTypeCode" ;
            schema1:name "Service" ;
            schema1:termCode "service" ] ;
    schema1:dataset [ a schema1:PropertyValue ;
            schema1:name "OneGeology Global Geological Map Data" ;
            schema1:propertyID "schema:identifier" ;
            schema1:url "https://onegeology.org/data/" ] ;
    schema1:dateModified "2024-03-15" ;
    schema1:description "OGC Web Feature Service providing vector feature access to harmonized geological unit data from participating OneGeology geological surveys. Supports WFS 2.0 GetCapabilities, DescribeFeatureType, and GetFeature operations with GeoSciML Portrayal output." ;
    schema1:distribution [ a schema1:WebAPI ;
            schema1:description "OGC WFS 2.0 service for harmonized geological unit features" ;
            schema1:documentation [ a schema1:CreativeWork ;
                    schema1:encodingFormat "application/xml" ;
                    schema1:name "WFS Capabilities Document" ;
                    schema1:url "https://onegeology.org/wfs?service=WFS&request=GetCapabilities" ] ;
            schema1:name "OneGeology Global WFS" ;
            schema1:potentialAction [ a schema1:SearchAction ;
                    schema1:name "GetCapabilities" ;
                    schema1:target [ a schema1:EntryPoint ;
                            schema1:httpMethod "GET" ;
                            schema1:urlTemplate "https://onegeology.org/wfs?service=WFS&request=GetCapabilities" ] ],
                [ a schema1:SearchAction ;
                    schema1:description "Retrieve geological unit features by bounding box" ;
                    schema1:name "GetFeature" ;
                    schema1:target [ a schema1:EntryPoint ;
                            schema1:httpMethod "GET" ;
                            schema1:urlTemplate "https://onegeology.org/wfs?service=WFS&request=GetFeature&typeName={typeName}&bbox={bbox}" ] ] ;
            schema1:serviceType [ a schema1:DefinedTerm ;
                    schema1:inDefinedTermSet "dde:codelist/ServiceTypeCode" ;
                    schema1:name "Data Access Service" ;
                    schema1:termCode "DataService>DataAccess" ] ] ;
    schema1:identifier "urn:onegeology:wfs-global-2024" ;
    schema1:image [ a schema1:ImageObject ;
            schema1:contentUrl "https://onegeology.org/images/wfs-service-preview.png" ;
            schema1:encodingFormat "image/png" ;
            schema1:name "service preview" ] ;
    schema1:inLanguage "eng" ;
    schema1:keywords [ a schema1:DefinedTerm ;
            schema1:inDefinedTermSet "dde:codelist/TopicCategoryCode" ;
            schema1:name "Geoscientific Information" ;
            schema1:termCode "geoscientificInformation" ],
        [ a schema1:DefinedTerm ;
            schema1:inDefinedTermSet "dde:codelist/AcquisitionTypeCode" ;
            schema1:name "Data Integration Synthesis" ;
            schema1:termCode "dataIntegrationSynthesis" ],
        "GeoSciML",
        "OneGeology",
        "WFS",
        "geological map" ;
    schema1:license [ a schema1:CreativeWork ;
            schema1:name "Creative Commons Attribution 4.0" ;
            schema1:url "https://creativecommons.org/licenses/by/4.0/" ] ;
    schema1:name "DDE OneGeology WFS Data Access Service" ;
    schema1:subjectOf <urn:uuid:dde-service-catalog-record> ;
    schema1:url "https://onegeology.org/technical_implementation/" .

<urn:uuid:dde-service-catalog-record> a schema1:Dataset ;
    dcterms:conformsTo <https://w3id.org/cdif/bbr/metadata/profiles/DDEProfiles/DDEService>,
        <https://w3id.org/cdif/core/1.0/>,
        <https://w3id.org/cdif/discovery/1.0/> ;
    schema1:about <urn:dde:example-onegeology-wfs> ;
    schema1:additionalType "dcat:CatalogRecord" ;
    schema1:sdDatePublished "2024-03-15" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
type: object
title: DDE Service profile
description: DDE profile for service resources (repository, service, webAPI). Extends
  DDEDiscovery with resource type constraint and ddeServiceInfo conditional properties.
allOf:
- $ref: https://usgin.github.io/ddeBuildingBlocks/build/annotated/bbr/metadata/profiles/DDEProfiles/DDEDiscovery/schema.yaml
- $ref: https://usgin.github.io/ddeBuildingBlocks/build/annotated/bbr/metadata/DDEproperties/ddeServiceInfo/schema.yaml
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
            - repository
            - service
            - webAPI
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

* YAML version: [schema.yaml](https://usgin.github.io/ddeBuildingBlocks/build/annotated/bbr/metadata/profiles/DDEProfiles/DDEService/schema.json)
* JSON version: [schema.json](https://usgin.github.io/ddeBuildingBlocks/build/annotated/bbr/metadata/profiles/DDEProfiles/DDEService/schema.yaml)


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
[context.jsonld](https://usgin.github.io/ddeBuildingBlocks/build/annotated/bbr/metadata/profiles/DDEProfiles/DDEService/context.jsonld)

## Sources

* [DDE Metadata Standard](https://www.ddeworld.org)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/ddeBuildingBlocks](https://github.com/usgin/ddeBuildingBlocks)
* Path: `_sources/profiles/DDEProfiles/DDEService`

