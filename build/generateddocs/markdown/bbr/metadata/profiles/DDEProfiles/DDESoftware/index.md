
# DDE Software profile (Schema)

`dde.bbr.metadata.profiles.DDEProfiles.DDESoftware` *v0.1*

DDE profile for software resources. Extends DDEDiscovery with resource type constraint.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## DDE Software Profile

DDE profile for software resources. Extends DDEDiscovery with a resource type constraint.

### Resource type codes
software

### Composed building blocks

1. **DDEDiscovery** — Base DDE discovery profile
2. **Resource type constraint** — `schema:termCode` must be `software`

## Examples

### DDE Software metadata example
DDE discovery metadata for GPlates plate reconstruction software with creator organization and download distribution.
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
  "@id": "urn:dde:example-gplates",
  "@type": [
    "schema:Dataset"
  ],
  "schema:name": "GPlates Plate Reconstruction Software",
  "schema:description": "Open-source desktop application for interactive visualization and manipulation of plate tectonic reconstructions. Enables users to load and combine digital plate models, create paleo-geographic maps, and export reconstructed geometries. Supports deep geological time reconstructions from the Archean to the present.",
  "schema:identifier": "urn:earthbyte:gplates-2.5",
  "schema:dateModified": "2024-01-20",
  "schema:version": "2.5",
  "schema:inLanguage": "eng",
  "schema:license": [
    {
      "@type": "schema:CreativeWork",
      "schema:name": "GNU General Public License v2.0",
      "schema:url": "https://www.gnu.org/licenses/old-licenses/gpl-2.0.html"
    }
  ],
  "schema:url": "https://www.gplates.org/",
  "schema:subjectOf": {
    "@id": "urn:uuid:dde-software-catalog-record",
    "@type": [
      "schema:Dataset"
    ],
    "schema:additionalType": [
      "dcat:CatalogRecord"
    ],
    "schema:about": {
      "@id": "urn:dde:example-gplates"
    },
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/core/1.0/"
      },
      {
        "@id": "https://w3id.org/cdif/discovery/1.0/"
      },
      {
        "@id": "https://w3id.org/cdif/bbr/metadata/profiles/DDEProfiles/DDESoftware"
      }
    ],
    "schema:sdDatePublished": "2024-01-20"
  },
  "schema:additionalType": [
    {
      "@type": "schema:DefinedTerm",
      "schema:name": "Software",
      "schema:termCode": "software",
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
    "plate tectonics",
    "plate reconstruction",
    "paleogeography",
    "GPlates"
  ],
  "schema:image": [
    {
      "@type": "schema:ImageObject",
      "schema:contentUrl": "https://www.gplates.org/images/gplates-screenshot.png",
      "schema:name": "GPlates application screenshot",
      "schema:encodingFormat": "image/png"
    }
  ],
  "schema:creator": {
    "@list": [
      {
        "@type": "schema:Organization",
        "schema:name": "EarthByte Group, University of Sydney",
        "schema:url": "https://www.earthbyte.org/"
      }
    ]
  },
  "schema:distribution": [
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:name": "GPlates Desktop Installer",
      "schema:description": "Platform-specific installers for Windows, macOS, and Linux",
      "schema:contentUrl": "https://www.gplates.org/download/",
      "schema:encodingFormat": [
        "application/octet-stream"
      ]
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
    "https://usgin.github.io/ddeBuildingBlocks/build/annotated/bbr/metadata/profiles/DDEProfiles/DDESoftware/context.jsonld",
    {
      "schema": "http://schema.org/",
      "dde": "https://www.ddeworld.org/resource/",
      "cdif": "https://cdif.org/profile/",
      "dcterms": "http://purl.org/dc/terms/",
      "dcat": "http://www.w3.org/ns/dcat#",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "urn:dde:example-gplates",
  "@type": [
    "schema:Dataset"
  ],
  "schema:name": "GPlates Plate Reconstruction Software",
  "schema:description": "Open-source desktop application for interactive visualization and manipulation of plate tectonic reconstructions. Enables users to load and combine digital plate models, create paleo-geographic maps, and export reconstructed geometries. Supports deep geological time reconstructions from the Archean to the present.",
  "schema:identifier": "urn:earthbyte:gplates-2.5",
  "schema:dateModified": "2024-01-20",
  "schema:version": "2.5",
  "schema:inLanguage": "eng",
  "schema:license": [
    {
      "@type": "schema:CreativeWork",
      "schema:name": "GNU General Public License v2.0",
      "schema:url": "https://www.gnu.org/licenses/old-licenses/gpl-2.0.html"
    }
  ],
  "schema:url": "https://www.gplates.org/",
  "schema:subjectOf": {
    "@id": "urn:uuid:dde-software-catalog-record",
    "@type": [
      "schema:Dataset"
    ],
    "schema:additionalType": [
      "dcat:CatalogRecord"
    ],
    "schema:about": {
      "@id": "urn:dde:example-gplates"
    },
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/core/1.0/"
      },
      {
        "@id": "https://w3id.org/cdif/discovery/1.0/"
      },
      {
        "@id": "https://w3id.org/cdif/bbr/metadata/profiles/DDEProfiles/DDESoftware"
      }
    ],
    "schema:sdDatePublished": "2024-01-20"
  },
  "schema:additionalType": [
    {
      "@type": "schema:DefinedTerm",
      "schema:name": "Software",
      "schema:termCode": "software",
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
    "plate tectonics",
    "plate reconstruction",
    "paleogeography",
    "GPlates"
  ],
  "schema:image": [
    {
      "@type": "schema:ImageObject",
      "schema:contentUrl": "https://www.gplates.org/images/gplates-screenshot.png",
      "schema:name": "GPlates application screenshot",
      "schema:encodingFormat": "image/png"
    }
  ],
  "schema:creator": {
    "@list": [
      {
        "@type": "schema:Organization",
        "schema:name": "EarthByte Group, University of Sydney",
        "schema:url": "https://www.earthbyte.org/"
      }
    ]
  },
  "schema:distribution": [
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:name": "GPlates Desktop Installer",
      "schema:description": "Platform-specific installers for Windows, macOS, and Linux",
      "schema:contentUrl": "https://www.gplates.org/download/",
      "schema:encodingFormat": [
        "application/octet-stream"
      ]
    }
  ]
}
```

#### ttl
```ttl
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix schema1: <http://schema.org/> .

<urn:dde:example-gplates> a schema1:Dataset ;
    schema1:additionalType [ a schema1:DefinedTerm ;
            schema1:inDefinedTermSet "dde:codelist/ResourceTypeCode" ;
            schema1:name "Software" ;
            schema1:termCode "software" ] ;
    schema1:creator ( [ a schema1:Organization ;
                schema1:name "EarthByte Group, University of Sydney" ;
                schema1:url "https://www.earthbyte.org/" ] ) ;
    schema1:dateModified "2024-01-20" ;
    schema1:description "Open-source desktop application for interactive visualization and manipulation of plate tectonic reconstructions. Enables users to load and combine digital plate models, create paleo-geographic maps, and export reconstructed geometries. Supports deep geological time reconstructions from the Archean to the present." ;
    schema1:distribution [ a schema1:DataDownload ;
            schema1:contentUrl "https://www.gplates.org/download/" ;
            schema1:description "Platform-specific installers for Windows, macOS, and Linux" ;
            schema1:encodingFormat "application/octet-stream" ;
            schema1:name "GPlates Desktop Installer" ] ;
    schema1:identifier "urn:earthbyte:gplates-2.5" ;
    schema1:image [ a schema1:ImageObject ;
            schema1:contentUrl "https://www.gplates.org/images/gplates-screenshot.png" ;
            schema1:encodingFormat "image/png" ;
            schema1:name "GPlates application screenshot" ] ;
    schema1:inLanguage "eng" ;
    schema1:keywords [ a schema1:DefinedTerm ;
            schema1:inDefinedTermSet "dde:codelist/TopicCategoryCode" ;
            schema1:name "Geoscientific Information" ;
            schema1:termCode "geoscientificInformation" ],
        [ a schema1:DefinedTerm ;
            schema1:inDefinedTermSet "dde:codelist/AcquisitionTypeCode" ;
            schema1:name "Data Integration Synthesis" ;
            schema1:termCode "dataIntegrationSynthesis" ],
        "GPlates",
        "paleogeography",
        "plate reconstruction",
        "plate tectonics" ;
    schema1:license [ a schema1:CreativeWork ;
            schema1:name "GNU General Public License v2.0" ;
            schema1:url "https://www.gnu.org/licenses/old-licenses/gpl-2.0.html" ] ;
    schema1:name "GPlates Plate Reconstruction Software" ;
    schema1:subjectOf <urn:uuid:dde-software-catalog-record> ;
    schema1:url "https://www.gplates.org/" ;
    schema1:version "2.5" .

<urn:uuid:dde-software-catalog-record> a schema1:Dataset ;
    dcterms:conformsTo <https://w3id.org/cdif/bbr/metadata/profiles/DDEProfiles/DDESoftware>,
        <https://w3id.org/cdif/core/1.0/>,
        <https://w3id.org/cdif/discovery/1.0/> ;
    schema1:about <urn:dde:example-gplates> ;
    schema1:additionalType "dcat:CatalogRecord" ;
    schema1:sdDatePublished "2024-01-20" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
type: object
title: DDE Software profile
description: DDE profile for software resources. Extends DDEDiscovery with resource
  type constraint.
allOf:
- $ref: https://usgin.github.io/ddeBuildingBlocks/build/annotated/bbr/metadata/profiles/DDEProfiles/DDEDiscovery/schema.yaml
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
            - software
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

* YAML version: [schema.yaml](https://usgin.github.io/ddeBuildingBlocks/build/annotated/bbr/metadata/profiles/DDEProfiles/DDESoftware/schema.json)
* JSON version: [schema.json](https://usgin.github.io/ddeBuildingBlocks/build/annotated/bbr/metadata/profiles/DDEProfiles/DDESoftware/schema.yaml)


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
[context.jsonld](https://usgin.github.io/ddeBuildingBlocks/build/annotated/bbr/metadata/profiles/DDEProfiles/DDESoftware/context.jsonld)

## Sources

* [DDE Metadata Standard](https://www.ddeworld.org)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/ddeBuildingBlocks](https://github.com/usgin/ddeBuildingBlocks)
* Path: `_sources/profiles/DDEProfiles/DDESoftware`

