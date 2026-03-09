
# DDE Geoscience Discovery metadata (Schema)

`dde.bbr.metadata.profiles.DDEProfiles.DDEDiscovery` *v0.1*

Gather building blocks to generate a DDE Geoscience Discovery record. Composes CDIF mandatory and optional properties with DDE required and optional extensions for geoscience metadata.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## DDE Geoscience Discovery Metadata Profile

Composes CDIF discovery metadata building blocks with DDE-specific extensions to create a complete geoscience discovery metadata profile.

### Composed building blocks

1. **cdifMandatory** — Base CDIF mandatory fields: @id, @type, name, identifier, dateModified, subjectOf, license/conditionsOfAccess, url/distribution.
2. **cdifOptional** — CDIF optional fields: description, creator, contributor, publisher, provider, keywords, spatialCoverage, temporalCoverage, distribution, provenance, quality, funding, etc.
3. **ddeRequired** — DDE mandatory extensions:
   - Resource type from `dde:codelist/ResourceTypeCode` (42 geoscience types)
   - Topic category keywords from `dde:codelist/TopicCategoryCode`
   - Acquisition type keywords from `dde:codelist/AcquisitionTypeCode`
   - Browse graphic images (`schema:ImageObject`)
   - DDE profile conformance (`cdif:profile_ddeCDIF`)
4. **ddeOptional** — DDE optional extensions: alternate names, measurement techniques, additional keywords and types.

### Conditional extensions (NOT included)

The following building blocks are conditional and should be composed into separate sub-profiles:

- **ddeImagery** — For imagery resources: sensor type, platform, wavelength range, signal generator, processing level.
- **ddeServiceInfo** — For service resources: DDE service type from `dde:codelist/ServiceTypeCode`, operated datasets.

## Examples

### China Bedrock Lithostratigraphy DDE discovery record.
DDE discovery metadata for the China 1:1M Bedrock Lithostratigraphy dataset from the China Geological Survey (CGS). Derived from CHN-CGS-EN-BedrockLithostratigraphyDDE.xml.
#### json
```json
{
    "@context": {
        "schema": "http://schema.org/",
        "dde": "https://www.ddeworld.org/resource/",
        "cdif": "https://cdif.org/profile/",
        "dcterms": "http://purl.org/dc/terms/",
        "dcat": "http://www.w3.org/ns/dcat#",
        "spdx": "http://spdx.org/rdf/terms#",
        "geosparql": "http://www.opengis.net/ont/geosparql#",
        "time": "http://www.w3.org/2006/time#",
        "prov": "http://www.w3.org/ns/prov#"
    },
    "@id": "urn:cgs:22e1d1ca752a7bc3ff4e90014e760e8a08947654",
    "@type": [
        "schema:Dataset"
    ],
    "schema:name": "CHN CGS EN 1:1M Bedrock Lithostratigraphy",
    "schema:alternateName": [
        "Bedrock lithostratigraphic map of China",
        "中国基岩地层图"
    ],
    "schema:description": "China 1:1M Bedrock Geology layer are composed by 63 sheets separate geological layers and information about sedimentary strata, quaternary strata, Igneous and metamorphic rocks. Sedimentary strata are be mapped by chronostratigraphic units and the rock formations. Intrusive rocks are be showed by the rock plus years, Pliocene strata are expressed by lithology and volcanic pattern. The layer includes more than 5,000 lithostratigraphic units and more than 1700 intrusive unit. Each geological units have attributes. For more information about China geological maps that are available please visit http://en.cgs.gov.cn/",
    "schema:identifier": "urn:cgs:22e1d1ca752a7bc3ff4e90014e760e8a08947654",
    "schema:dateModified": "2018-09-07",
    "schema:inLanguage": "zho",
    "schema:license": [
        "licenceUnrestricted"
    ],
    "schema:url": "http://en.cgs.gov.cn/",
    "schema:subjectOf": {
        "@id": "urn:uuid:22e1d1ca752a7bc3ff4e90014e760e8a08947654",
        "@type": [
            "schema:Dataset"
        ],
        "schema:additionalType": [
            "dcat:CatalogRecord"
        ],
        "schema:about": {
            "@id": "urn:cgs:22e1d1ca752a7bc3ff4e90014e760e8a08947654"
        },
        "dcterms:conformsTo": [
            {
                "@id": "https://w3id.org/cdif/bbr/metadata/profiles/DDEProfiles/DDEDiscovery"
            }
        ],
        "schema:sdDatePublished": "2018-09-07",
        "schema:maintainer": {
            "@type": "schema:Person",
            "schema:name": "Yang Tiantian",
            "schema:identifier": "http://orcid.org/q34r2675427",
            "schema:contactPoint": {
                "@type": "schema:ContactPoint",
                "schema:email": "ytiantian@mail.cgs.gov.cn"
            }
        }
    },
    "schema:additionalType": [
        {
            "@type": "schema:DefinedTerm",
            "schema:name": "Geographic Dataset",
            "schema:termCode": "geographicDataset",
            "schema:inDefinedTermSet": "dde:codelist/ResourceTypeCode"
        },
        {
            "@type": "schema:DefinedTerm",
            "schema:name": "Map",
            "schema:termCode": "map",
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
        {
            "@type": "schema:DefinedTerm",
            "schema:name": "Data Integration Synthesis",
            "schema:termCode": "dataIntegrationSynthesis",
            "schema:inDefinedTermSet": "dde:codelist/AcquisitionTypeCode"
        },
        "OneGeology",
        "geology",
        "Asia",
        "China"
    ],
    "schema:image": [
        {
            "@type": "schema:ImageObject",
            "schema:contentUrl": "http://onegeology-geonetwork.brgm.fr/geonetwork3/srv/eng//resources.get?uuid=22e1d1ca752a7bc3ff4e90014e760e8a08947654&fname=22e1d1ca752a7bc3ff4e90014e760e8a08947654_s.png",
            "schema:name": "thumbnail",
            "schema:encodingFormat": "image/png"
        },
        {
            "@type": "schema:ImageObject",
            "schema:contentUrl": "http://onegeology-geonetwork.brgm.fr/geonetwork3/srv/eng//resources.get?uuid=22e1d1ca752a7bc3ff4e90014e760e8a08947654&fname=22e1d1ca752a7bc3ff4e90014e760e8a08947654.png",
            "schema:name": "large thumbnail",
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
                        "@id": "https://example.org/trs/ma-before-present"
                    },
                    "time:numericPosition": 3804
                }
            },
            "time:hasEnd": {
                "@type": "time:Instant",
                "time:inTimePosition": {
                    "@type": "time:TimePosition",
                    "time:hasTRS": {
                        "@id": "https://example.org/trs/ma-before-present"
                    },
                    "time:numericPosition": 0
                }
            }
        }
    ],
    "schema:distribution": [
        {
            "@type": [
                "schema:DataDownload"
            ],
            "schema:name": "CHN_CGS_EN_1M_BLS",
            "schema:description": "CHN CGS EN 1:1M Bedrock Lithostratigraphy",
            "schema:contentUrl": "http://onegeologychina.cgs.gov.cn/cgi-bin/mapserv.exe?map=C:/ms4w/apps/CHINAGEOLOGY/CHINAMMAP_ENGLISH.map&",
            "schema:encodingFormat": [
                "image/jpg",
                "image/png",
                "image/tif"
            ]
        }
    ],
    "schema:relatedLink": [
        {
            "@type": "schema:LinkRole",
            "schema:linkRelationship": "order",
            "target": {
                "@type": "schema:EntryPoint",
                "schema:name": "China geological maps that are available",
                "schema:url": "http://en.cgs.gov.cn/"
            }
        }
    ],
    "prov:wasDerivedFrom": [
        {
            "@type": "prov:Entity",
            "schema:description": "Paleoarchean through Holocene geological mapping data from 63 separate geological survey sheets"
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
    "https://usgin.github.io/ddeBuildingBlocks/build/annotated/bbr/metadata/profiles/DDEProfiles/DDEDiscovery/context.jsonld",
    {
      "schema": "http://schema.org/",
      "dde": "https://www.ddeworld.org/resource/",
      "cdif": "https://cdif.org/profile/",
      "dcterms": "http://purl.org/dc/terms/",
      "dcat": "http://www.w3.org/ns/dcat#",
      "spdx": "http://spdx.org/rdf/terms#",
      "geosparql": "http://www.opengis.net/ont/geosparql#",
      "time": "http://www.w3.org/2006/time#",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "urn:cgs:22e1d1ca752a7bc3ff4e90014e760e8a08947654",
  "@type": [
    "schema:Dataset"
  ],
  "schema:name": "CHN CGS EN 1:1M Bedrock Lithostratigraphy",
  "schema:alternateName": [
    "Bedrock lithostratigraphic map of China",
    "\u4e2d\u56fd\u57fa\u5ca9\u5730\u5c42\u56fe"
  ],
  "schema:description": "China 1:1M Bedrock Geology layer are composed by 63 sheets separate geological layers and information about sedimentary strata, quaternary strata, Igneous and metamorphic rocks. Sedimentary strata are be mapped by chronostratigraphic units and the rock formations. Intrusive rocks are be showed by the rock plus years, Pliocene strata are expressed by lithology and volcanic pattern. The layer includes more than 5,000 lithostratigraphic units and more than 1700 intrusive unit. Each geological units have attributes. For more information about China geological maps that are available please visit http://en.cgs.gov.cn/",
  "schema:identifier": "urn:cgs:22e1d1ca752a7bc3ff4e90014e760e8a08947654",
  "schema:dateModified": "2018-09-07",
  "schema:inLanguage": "zho",
  "schema:license": [
    "licenceUnrestricted"
  ],
  "schema:url": "http://en.cgs.gov.cn/",
  "schema:subjectOf": {
    "@id": "urn:uuid:22e1d1ca752a7bc3ff4e90014e760e8a08947654",
    "@type": [
      "schema:Dataset"
    ],
    "schema:additionalType": [
      "dcat:CatalogRecord"
    ],
    "schema:about": {
      "@id": "urn:cgs:22e1d1ca752a7bc3ff4e90014e760e8a08947654"
    },
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/bbr/metadata/profiles/DDEProfiles/DDEDiscovery"
      }
    ],
    "schema:sdDatePublished": "2018-09-07",
    "schema:maintainer": {
      "@type": "schema:Person",
      "schema:name": "Yang Tiantian",
      "schema:identifier": "http://orcid.org/q34r2675427",
      "schema:contactPoint": {
        "@type": "schema:ContactPoint",
        "schema:email": "ytiantian@mail.cgs.gov.cn"
      }
    }
  },
  "schema:additionalType": [
    {
      "@type": "schema:DefinedTerm",
      "schema:name": "Geographic Dataset",
      "schema:termCode": "geographicDataset",
      "schema:inDefinedTermSet": "dde:codelist/ResourceTypeCode"
    },
    {
      "@type": "schema:DefinedTerm",
      "schema:name": "Map",
      "schema:termCode": "map",
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
    {
      "@type": "schema:DefinedTerm",
      "schema:name": "Data Integration Synthesis",
      "schema:termCode": "dataIntegrationSynthesis",
      "schema:inDefinedTermSet": "dde:codelist/AcquisitionTypeCode"
    },
    "OneGeology",
    "geology",
    "Asia",
    "China"
  ],
  "schema:image": [
    {
      "@type": "schema:ImageObject",
      "schema:contentUrl": "http://onegeology-geonetwork.brgm.fr/geonetwork3/srv/eng//resources.get?uuid=22e1d1ca752a7bc3ff4e90014e760e8a08947654&fname=22e1d1ca752a7bc3ff4e90014e760e8a08947654_s.png",
      "schema:name": "thumbnail",
      "schema:encodingFormat": "image/png"
    },
    {
      "@type": "schema:ImageObject",
      "schema:contentUrl": "http://onegeology-geonetwork.brgm.fr/geonetwork3/srv/eng//resources.get?uuid=22e1d1ca752a7bc3ff4e90014e760e8a08947654&fname=22e1d1ca752a7bc3ff4e90014e760e8a08947654.png",
      "schema:name": "large thumbnail",
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
            "@id": "https://example.org/trs/ma-before-present"
          },
          "time:numericPosition": 3804
        }
      },
      "time:hasEnd": {
        "@type": "time:Instant",
        "time:inTimePosition": {
          "@type": "time:TimePosition",
          "time:hasTRS": {
            "@id": "https://example.org/trs/ma-before-present"
          },
          "time:numericPosition": 0
        }
      }
    }
  ],
  "schema:distribution": [
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:name": "CHN_CGS_EN_1M_BLS",
      "schema:description": "CHN CGS EN 1:1M Bedrock Lithostratigraphy",
      "schema:contentUrl": "http://onegeologychina.cgs.gov.cn/cgi-bin/mapserv.exe?map=C:/ms4w/apps/CHINAGEOLOGY/CHINAMMAP_ENGLISH.map&",
      "schema:encodingFormat": [
        "image/jpg",
        "image/png",
        "image/tif"
      ]
    }
  ],
  "schema:relatedLink": [
    {
      "@type": "schema:LinkRole",
      "schema:linkRelationship": "order",
      "target": {
        "@type": "schema:EntryPoint",
        "schema:name": "China geological maps that are available",
        "schema:url": "http://en.cgs.gov.cn/"
      }
    }
  ],
  "prov:wasDerivedFrom": [
    {
      "@type": "prov:Entity",
      "schema:description": "Paleoarchean through Holocene geological mapping data from 63 separate geological survey sheets"
    }
  ]
}
```

#### ttl
```ttl
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix time: <http://www.w3.org/2006/time#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<urn:cgs:22e1d1ca752a7bc3ff4e90014e760e8a08947654> a schema1:Dataset ;
    schema1:additionalType [ a schema1:DefinedTerm ;
            schema1:inDefinedTermSet "dde:codelist/ResourceTypeCode" ;
            schema1:name "Map" ;
            schema1:termCode "map" ],
        [ a schema1:DefinedTerm ;
            schema1:inDefinedTermSet "dde:codelist/ResourceTypeCode" ;
            schema1:name "Geographic Dataset" ;
            schema1:termCode "geographicDataset" ] ;
    schema1:alternateName "Bedrock lithostratigraphic map of China",
        "中国基岩地层图" ;
    schema1:dateModified "2018-09-07" ;
    schema1:description "China 1:1M Bedrock Geology layer are composed by 63 sheets separate geological layers and information about sedimentary strata, quaternary strata, Igneous and metamorphic rocks. Sedimentary strata are be mapped by chronostratigraphic units and the rock formations. Intrusive rocks are be showed by the rock plus years, Pliocene strata are expressed by lithology and volcanic pattern. The layer includes more than 5,000 lithostratigraphic units and more than 1700 intrusive unit. Each geological units have attributes. For more information about China geological maps that are available please visit http://en.cgs.gov.cn/" ;
    schema1:distribution [ a schema1:DataDownload ;
            schema1:contentUrl "http://onegeologychina.cgs.gov.cn/cgi-bin/mapserv.exe?map=C:/ms4w/apps/CHINAGEOLOGY/CHINAMMAP_ENGLISH.map&" ;
            schema1:description "CHN CGS EN 1:1M Bedrock Lithostratigraphy" ;
            schema1:encodingFormat "image/jpg",
                "image/png",
                "image/tif" ;
            schema1:name "CHN_CGS_EN_1M_BLS" ] ;
    schema1:identifier "urn:cgs:22e1d1ca752a7bc3ff4e90014e760e8a08947654" ;
    schema1:image [ a schema1:ImageObject ;
            schema1:contentUrl "http://onegeology-geonetwork.brgm.fr/geonetwork3/srv/eng//resources.get?uuid=22e1d1ca752a7bc3ff4e90014e760e8a08947654&fname=22e1d1ca752a7bc3ff4e90014e760e8a08947654_s.png" ;
            schema1:encodingFormat "image/png" ;
            schema1:name "thumbnail" ],
        [ a schema1:ImageObject ;
            schema1:contentUrl "http://onegeology-geonetwork.brgm.fr/geonetwork3/srv/eng//resources.get?uuid=22e1d1ca752a7bc3ff4e90014e760e8a08947654&fname=22e1d1ca752a7bc3ff4e90014e760e8a08947654.png" ;
            schema1:encodingFormat "image/png" ;
            schema1:name "large thumbnail" ] ;
    schema1:inLanguage "zho" ;
    schema1:keywords [ a schema1:DefinedTerm ;
            schema1:inDefinedTermSet "dde:codelist/AcquisitionTypeCode" ;
            schema1:name "Geological Mapping" ;
            schema1:termCode "geologicalMapping" ],
        [ a schema1:DefinedTerm ;
            schema1:inDefinedTermSet "dde:codelist/TopicCategoryCode" ;
            schema1:name "Geoscientific Information" ;
            schema1:termCode "geoscientificInformation" ],
        [ a schema1:DefinedTerm ;
            schema1:inDefinedTermSet "dde:codelist/AcquisitionTypeCode" ;
            schema1:name "Data Integration Synthesis" ;
            schema1:termCode "dataIntegrationSynthesis" ],
        "Asia",
        "China",
        "OneGeology",
        "geology" ;
    schema1:license "licenceUnrestricted" ;
    schema1:name "CHN CGS EN 1:1M Bedrock Lithostratigraphy" ;
    schema1:relatedLink [ a schema1:LinkRole ;
            schema1:linkRelationship "order" ] ;
    schema1:spatialCoverage [ a schema1:Place ;
            schema1:geo [ a schema1:GeoShape ;
                    schema1:box "18.1609 73.499 53.5585 135.08" ] ] ;
    schema1:subjectOf <urn:uuid:22e1d1ca752a7bc3ff4e90014e760e8a08947654> ;
    schema1:temporalCoverage [ a time:ProperInterval ;
            time:hasBeginning [ a time:Instant ;
                    time:inTimePosition [ a time:TimePosition ;
                            time:hasTRS <https://example.org/trs/ma-before-present> ;
                            time:numericPosition 3804 ] ] ;
            time:hasEnd [ a time:Instant ;
                    time:inTimePosition [ a time:TimePosition ;
                            time:hasTRS <https://example.org/trs/ma-before-present> ;
                            time:numericPosition 0 ] ] ] ;
    schema1:url "http://en.cgs.gov.cn/" ;
    prov:wasDerivedFrom [ a prov:Entity ;
            schema1:description "Paleoarchean through Holocene geological mapping data from 63 separate geological survey sheets" ] .

<urn:uuid:22e1d1ca752a7bc3ff4e90014e760e8a08947654> a schema1:Dataset ;
    dcterms:conformsTo <https://w3id.org/cdif/bbr/metadata/profiles/DDEProfiles/DDEDiscovery> ;
    schema1:about <urn:cgs:22e1d1ca752a7bc3ff4e90014e760e8a08947654> ;
    schema1:additionalType "dcat:CatalogRecord" ;
    schema1:maintainer [ a schema1:Person ;
            schema1:contactPoint [ a schema1:ContactPoint ;
                    schema1:email "ytiantian@mail.cgs.gov.cn" ] ;
            schema1:identifier "http://orcid.org/q34r2675427" ;
            schema1:name "Yang Tiantian" ] ;
    schema1:sdDatePublished "2018-09-07" .


```


### Arizona Lithostratigraphy DDE discovery record.
DDE discovery metadata for the Arizona 1:1M Lithostratigraphy dataset from the Arizona Geological Survey. Derived from ArizonaLithostratigraphyOneGeologyDDE.xml. Demonstrates all CDIF mandatory/optional and DDE required/optional fields.
#### json
```json
{
    "@context": {
        "schema": "http://schema.org/",
        "dde": "https://www.ddeworld.org/resource/",
        "cdif": "https://cdif.org/profile/",
        "dcterms": "http://purl.org/dc/terms/",
        "dcat": "http://www.w3.org/ns/dcat#",
        "spdx": "http://spdx.org/rdf/terms#",
        "geosparql": "http://www.opengis.net/ont/geosparql#",
        "time": "http://www.w3.org/2006/time#",
        "prov": "http://www.w3.org/ns/prov#",
        "dqv": "http://www.w3.org/ns/dqv#"
    },
    "@id": "https://doi.org/23609/53w7klh",
    "@type": [
        "schema:Dataset"
    ],
    "schema:name": "US-AZ_AZGS_1M_Lithostratigraphy",
    "schema:alternateName": "Arizona 1:1000000 Lithostratigraphic map",
    "schema:description": "Lithostratigraphic unit distribution for the Geologic Map of Arizona at 1:1,000,000-scale. Shows entire state with map units defined broadly by age and lithologic type. The map was compiled by modifying the previous 1:1000000 statemap version with more recent mapping.",
    "schema:identifier": {
        "@type": "schema:PropertyValue",
        "schema:propertyID": "https://registry.identifiers.org/registry/doi",
        "schema:value": "doi:23609/53w7klh",
        "schema:url": "https://doi.org/23609/53w7klh"
    },
    "schema:dateModified": "2016-04-14",
    "schema:datePublished": "2006-05-04",
    "schema:version": "4",
    "schema:inLanguage": "eng",
    "schema:license": [
        {
            "@type": "schema:CreativeWork",
            "schema:name": "Creative Commons CC0 1.0 Universal",
            "schema:url": "https://creativecommons.org/publicdomain/zero/1.0/"
        }
    ],
    "schema:conditionsOfAccess": [
        {
            "@type": "schema:CreativeWork",
            "schema:name": "other license test",
            "schema:url": "https://test.org/otherlicense/zero/1.0/"
        }
    ],
    "schema:url": "https://hdl.handle.net/10150/630741",
    "schema:subjectOf": {
        "@id": "urn:uuid:c98705ae-058a-43fb-85a2-7b5209d9a4b3",
        "@type": [
            "schema:Dataset"
        ],
        "schema:additionalType": [
            "dcat:CatalogRecord"
        ],
        "schema:about": {
            "@id": "https://doi.org/23609/53w7klh"
        },
        "dcterms:conformsTo": [
            {
                "@id": "https://w3id.org/cdif/bbr/metadata/profiles/DDEProfiles/DDEDiscovery"
            }
        ],
        "schema:sdDatePublished": "2017-04-24",
        "schema:maintainer": {
            "@type": "schema:Person",
            "schema:name": "publications manager",
            "schema:identifier": "https://orcid.org/0000-0041-6041-6309",
            "schema:contactPoint": {
                "@type": "schema:ContactPoint",
                "schema:email": "metadata@azgs.az.gov"
            }
        }
    },
    "schema:additionalType": [
        {
            "@type": "schema:DefinedTerm",
            "schema:name": "Dataset",
            "schema:termCode": "dataset",
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
            "schema:name": "Paleontology",
            "schema:termCode": "GI_PO_paleontology",
            "schema:inDefinedTermSet": "dde:codelist/TopicCategoryCode"
        },
        {
            "@type": "schema:DefinedTerm",
            "schema:name": "Hydrogeology",
            "schema:termCode": "GI_HG_hydrogeology",
            "schema:inDefinedTermSet": "dde:codelist/TopicCategoryCode"
        },
        {
            "@type": "schema:DefinedTerm",
            "schema:name": "Environment",
            "schema:termCode": "environment",
            "schema:inDefinedTermSet": "dde:codelist/TopicCategoryCode"
        },
        {
            "@type": "schema:DefinedTerm",
            "schema:name": "Digital Conversion from Published Source",
            "schema:termCode": "digitalConversionFromPublishedSource",
            "schema:inDefinedTermSet": "dde:codelist/AcquisitionTypeCode"
        },
        {
            "@type": "schema:DefinedTerm",
            "schema:name": "Synthesis from Multiple Sources",
            "schema:termCode": "synthesisFromMultipleSources",
            "schema:inDefinedTermSet": "dde:codelist/AcquisitionTypeCode"
        },
        "United States",
        {
            "@type": "schema:DefinedTerm",
            "schema:name": "Arizona",
            "schema:identifier": "https://edits.nationalmap.gov/apps/gaz-domestic/public/gaz-record/1779777"
        },
        "Geology",
        "Geologic Map"
    ],
    "schema:image": [
        {
            "@type": "schema:ImageObject",
            "schema:contentUrl": "http://azgs.az.gov/repository/browse/3757.jpg",
            "schema:name": "Quick view lithostratigraphic map of Arizona",
            "schema:description": "description of the browse image"
        },
        {
            "@type": "schema:ImageObject",
            "schema:contentUrl": "http://azgs.az.gov/repository/browse/2222.jpg",
            "schema:name": "Another map of Arizona",
            "schema:description": "description of the browse image2",
            "schema:encodingFormat": "image/png"
        }
    ],
    "schema:creator": {
        "@list": [
            {
                "@type": "schema:Person",
                "schema:name": "Stephen Richard",
                "schema:identifier": "https://orcid.org/0000-0001-6041-5302",
                "schema:contactPoint": {
                    "@type": "schema:ContactPoint",
                    "schema:email": "richards@azgs.az.gov"
                }
            }
        ]
    },
    "schema:contributor": [
        {
            "@type": "schema:Role",
            "schema:roleName": "pointOfContact",
            "schema:contributor": {
                "@type": "schema:Person",
                "schema:name": "Ryan Clark",
                "schema:identifier": "https://orcid.org/0000-0041-6041-6309",
                "schema:contactPoint": {
                    "@type": "schema:ContactPoint",
                    "schema:email": "clarkr@azgs.az.gov"
                }
            }
        }
    ],
    "schema:provider": [
        {
            "@type": "schema:Organization",
            "schema:name": "Arizona Geological Survey",
            "schema:identifier": "https://ror.org/00vcszp55",
            "schema:contactPoint": {
                "@type": "schema:ContactPoint",
                "schema:email": "info@azgs.az.gov"
            }
        }
    ],
    "schema:spatialCoverage": [
        {
            "@type": "schema:Place",
            "schema:name": [
                "Arizona"
            ],
            "schema:identifier": {
                "@type": "schema:PropertyValue",
                "schema:propertyID": "Wikidata",
                "schema:value": "https://www.wikidata.org/wiki/Q816"
            },
            "schema:geo": {
                "@type": "schema:GeoShape",
                "schema:box": "31.332177 -114.81651 37.00426 -109.045223"
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
                        "@id": "https://example.org/trs/ma-before-present"
                    },
                    "time:numericPosition": 1870
                },
                "schema:name": "Early Proterozoic",
                "schema:identifier": "http://resource.geosciml.org/classifier/ics/ischart/Paleoproterozoic"
            },
            "time:hasEnd": {
                "@type": "time:Instant",
                "schema:name": "Holocene",
                "schema:identifier": "http://resource.geosciml.org/classifier/ics/ischart/Holocene"
            }
        }
    ],
    "schema:distribution": [
        {
            "@type": [
                "schema:DataDownload"
            ],
            "schema:name": "gsmlp:GeologicUnitView",
            "schema:description": "OGC get capabilities URL",
            "schema:contentUrl": "http://services.azgs.az.gov/ArcGIS/services/OneGeology/AZGS_Arizona_Geology_WFS/MapServer/WFSServer?",
            "schema:encodingFormat": [
                "application/xml"
            ],
            "schema:provider": [
                {
                    "@type": "schema:Organization",
                    "schema:name": "Arizona Geological Survey",
                    "schema:identifier": "https://ror.org/00vcszp55"
                }
            ]
        },
        {
            "@type": [
                "schema:DataDownload"
            ],
            "schema:name": "US-AZ_AZGS_1M_Lithostratigraphy",
            "schema:description": "OGC get map URL",
            "schema:contentUrl": "http://services.azgs.az.gov/ArcGIS/services/OneGeology/AZGS_Arizona_Geology/MapServer/WMSServer?",
            "schema:encodingFormat": [
                "image/jpg",
                "image/png",
                "image/tif"
            ]
        }
    ],
    "dqv:hasQualityMeasurement": [
        {
            "@type": "dqv:QualityMeasurement",
            "schema:description": "Line work reviewed for consistency with source maps",
            "dqv:isMeasurementOf": "completeness",
            "dqv:value": "Line work reviewed for consistency with source maps"
        }
    ],
    "prov:wasDerivedFrom": [
        {
            "@type": "prov:Entity",
            "@id": "https://doi.org/24596/tehou246",
            "schema:name": "source0"
        },
        {
            "@type": "prov:Entity",
            "@id": "https://doi.org/24596/h35wp59y",
            "schema:name": "source1"
        }
    ],
    "schema:relatedLink": [
        {
            "@type": "schema:LinkRole",
            "schema:linkRelationship": "information",
            "target": {
                "@type": "schema:EntryPoint",
                "schema:name": "Geologic Map of Arizona",
                "schema:url": "https://hdl.handle.net/10150/630741"
            }
        },
        {
            "@type": "schema:LinkRole",
            "schema:linkRelationship": "completeMetadata",
            "target": {
                "@type": "schema:EntryPoint",
                "schema:name": "ISO19115 metadata record",
                "schema:url": "http://repository.stategeothermaldata.org/metadata/record/4e6b8f72f7d6c3856f092c6b850180eb.iso.xml",
                "schema:encodingType": "INSPIRE 19115"
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
      "cdif": "https://cdif.org/profile/",
      "dcterms": "http://purl.org/dc/terms/",
      "dcat": "http://www.w3.org/ns/dcat#",
      "time": "http://www.w3.org/2006/time#",
      "prov": "http://www.w3.org/ns/prov#",
      "dqv": "http://www.w3.org/ns/dqv#"
    },
    "https://usgin.github.io/ddeBuildingBlocks/build/annotated/bbr/metadata/profiles/DDEProfiles/DDEDiscovery/context.jsonld",
    {
      "schema": "http://schema.org/",
      "dde": "https://www.ddeworld.org/resource/",
      "cdif": "https://cdif.org/profile/",
      "dcterms": "http://purl.org/dc/terms/",
      "dcat": "http://www.w3.org/ns/dcat#",
      "spdx": "http://spdx.org/rdf/terms#",
      "geosparql": "http://www.opengis.net/ont/geosparql#",
      "time": "http://www.w3.org/2006/time#",
      "prov": "http://www.w3.org/ns/prov#",
      "dqv": "http://www.w3.org/ns/dqv#"
    }
  ],
  "@id": "https://doi.org/23609/53w7klh",
  "@type": [
    "schema:Dataset"
  ],
  "schema:name": "US-AZ_AZGS_1M_Lithostratigraphy",
  "schema:alternateName": "Arizona 1:1000000 Lithostratigraphic map",
  "schema:description": "Lithostratigraphic unit distribution for the Geologic Map of Arizona at 1:1,000,000-scale. Shows entire state with map units defined broadly by age and lithologic type. The map was compiled by modifying the previous 1:1000000 statemap version with more recent mapping.",
  "schema:identifier": {
    "@type": "schema:PropertyValue",
    "schema:propertyID": "https://registry.identifiers.org/registry/doi",
    "schema:value": "doi:23609/53w7klh",
    "schema:url": "https://doi.org/23609/53w7klh"
  },
  "schema:dateModified": "2016-04-14",
  "schema:datePublished": "2006-05-04",
  "schema:version": "4",
  "schema:inLanguage": "eng",
  "schema:license": [
    {
      "@type": "schema:CreativeWork",
      "schema:name": "Creative Commons CC0 1.0 Universal",
      "schema:url": "https://creativecommons.org/publicdomain/zero/1.0/"
    }
  ],
  "schema:conditionsOfAccess": [
    {
      "@type": "schema:CreativeWork",
      "schema:name": "other license test",
      "schema:url": "https://test.org/otherlicense/zero/1.0/"
    }
  ],
  "schema:url": "https://hdl.handle.net/10150/630741",
  "schema:subjectOf": {
    "@id": "urn:uuid:c98705ae-058a-43fb-85a2-7b5209d9a4b3",
    "@type": [
      "schema:Dataset"
    ],
    "schema:additionalType": [
      "dcat:CatalogRecord"
    ],
    "schema:about": {
      "@id": "https://doi.org/23609/53w7klh"
    },
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/bbr/metadata/profiles/DDEProfiles/DDEDiscovery"
      }
    ],
    "schema:sdDatePublished": "2017-04-24",
    "schema:maintainer": {
      "@type": "schema:Person",
      "schema:name": "publications manager",
      "schema:identifier": "https://orcid.org/0000-0041-6041-6309",
      "schema:contactPoint": {
        "@type": "schema:ContactPoint",
        "schema:email": "metadata@azgs.az.gov"
      }
    }
  },
  "schema:additionalType": [
    {
      "@type": "schema:DefinedTerm",
      "schema:name": "Dataset",
      "schema:termCode": "dataset",
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
      "schema:name": "Paleontology",
      "schema:termCode": "GI_PO_paleontology",
      "schema:inDefinedTermSet": "dde:codelist/TopicCategoryCode"
    },
    {
      "@type": "schema:DefinedTerm",
      "schema:name": "Hydrogeology",
      "schema:termCode": "GI_HG_hydrogeology",
      "schema:inDefinedTermSet": "dde:codelist/TopicCategoryCode"
    },
    {
      "@type": "schema:DefinedTerm",
      "schema:name": "Environment",
      "schema:termCode": "environment",
      "schema:inDefinedTermSet": "dde:codelist/TopicCategoryCode"
    },
    {
      "@type": "schema:DefinedTerm",
      "schema:name": "Digital Conversion from Published Source",
      "schema:termCode": "digitalConversionFromPublishedSource",
      "schema:inDefinedTermSet": "dde:codelist/AcquisitionTypeCode"
    },
    {
      "@type": "schema:DefinedTerm",
      "schema:name": "Synthesis from Multiple Sources",
      "schema:termCode": "synthesisFromMultipleSources",
      "schema:inDefinedTermSet": "dde:codelist/AcquisitionTypeCode"
    },
    "United States",
    {
      "@type": "schema:DefinedTerm",
      "schema:name": "Arizona",
      "schema:identifier": "https://edits.nationalmap.gov/apps/gaz-domestic/public/gaz-record/1779777"
    },
    "Geology",
    "Geologic Map"
  ],
  "schema:image": [
    {
      "@type": "schema:ImageObject",
      "schema:contentUrl": "http://azgs.az.gov/repository/browse/3757.jpg",
      "schema:name": "Quick view lithostratigraphic map of Arizona",
      "schema:description": "description of the browse image"
    },
    {
      "@type": "schema:ImageObject",
      "schema:contentUrl": "http://azgs.az.gov/repository/browse/2222.jpg",
      "schema:name": "Another map of Arizona",
      "schema:description": "description of the browse image2",
      "schema:encodingFormat": "image/png"
    }
  ],
  "schema:creator": {
    "@list": [
      {
        "@type": "schema:Person",
        "schema:name": "Stephen Richard",
        "schema:identifier": "https://orcid.org/0000-0001-6041-5302",
        "schema:contactPoint": {
          "@type": "schema:ContactPoint",
          "schema:email": "richards@azgs.az.gov"
        }
      }
    ]
  },
  "schema:contributor": [
    {
      "@type": "schema:Role",
      "schema:roleName": "pointOfContact",
      "schema:contributor": {
        "@type": "schema:Person",
        "schema:name": "Ryan Clark",
        "schema:identifier": "https://orcid.org/0000-0041-6041-6309",
        "schema:contactPoint": {
          "@type": "schema:ContactPoint",
          "schema:email": "clarkr@azgs.az.gov"
        }
      }
    }
  ],
  "schema:provider": [
    {
      "@type": "schema:Organization",
      "schema:name": "Arizona Geological Survey",
      "schema:identifier": "https://ror.org/00vcszp55",
      "schema:contactPoint": {
        "@type": "schema:ContactPoint",
        "schema:email": "info@azgs.az.gov"
      }
    }
  ],
  "schema:spatialCoverage": [
    {
      "@type": "schema:Place",
      "schema:name": [
        "Arizona"
      ],
      "schema:identifier": {
        "@type": "schema:PropertyValue",
        "schema:propertyID": "Wikidata",
        "schema:value": "https://www.wikidata.org/wiki/Q816"
      },
      "schema:geo": {
        "@type": "schema:GeoShape",
        "schema:box": "31.332177 -114.81651 37.00426 -109.045223"
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
            "@id": "https://example.org/trs/ma-before-present"
          },
          "time:numericPosition": 1870
        },
        "schema:name": "Early Proterozoic",
        "schema:identifier": "http://resource.geosciml.org/classifier/ics/ischart/Paleoproterozoic"
      },
      "time:hasEnd": {
        "@type": "time:Instant",
        "schema:name": "Holocene",
        "schema:identifier": "http://resource.geosciml.org/classifier/ics/ischart/Holocene"
      }
    }
  ],
  "schema:distribution": [
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:name": "gsmlp:GeologicUnitView",
      "schema:description": "OGC get capabilities URL",
      "schema:contentUrl": "http://services.azgs.az.gov/ArcGIS/services/OneGeology/AZGS_Arizona_Geology_WFS/MapServer/WFSServer?",
      "schema:encodingFormat": [
        "application/xml"
      ],
      "schema:provider": [
        {
          "@type": "schema:Organization",
          "schema:name": "Arizona Geological Survey",
          "schema:identifier": "https://ror.org/00vcszp55"
        }
      ]
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:name": "US-AZ_AZGS_1M_Lithostratigraphy",
      "schema:description": "OGC get map URL",
      "schema:contentUrl": "http://services.azgs.az.gov/ArcGIS/services/OneGeology/AZGS_Arizona_Geology/MapServer/WMSServer?",
      "schema:encodingFormat": [
        "image/jpg",
        "image/png",
        "image/tif"
      ]
    }
  ],
  "dqv:hasQualityMeasurement": [
    {
      "@type": "dqv:QualityMeasurement",
      "schema:description": "Line work reviewed for consistency with source maps",
      "dqv:isMeasurementOf": "completeness",
      "dqv:value": "Line work reviewed for consistency with source maps"
    }
  ],
  "prov:wasDerivedFrom": [
    {
      "@type": "prov:Entity",
      "@id": "https://doi.org/24596/tehou246",
      "schema:name": "source0"
    },
    {
      "@type": "prov:Entity",
      "@id": "https://doi.org/24596/h35wp59y",
      "schema:name": "source1"
    }
  ],
  "schema:relatedLink": [
    {
      "@type": "schema:LinkRole",
      "schema:linkRelationship": "information",
      "target": {
        "@type": "schema:EntryPoint",
        "schema:name": "Geologic Map of Arizona",
        "schema:url": "https://hdl.handle.net/10150/630741"
      }
    },
    {
      "@type": "schema:LinkRole",
      "schema:linkRelationship": "completeMetadata",
      "target": {
        "@type": "schema:EntryPoint",
        "schema:name": "ISO19115 metadata record",
        "schema:url": "http://repository.stategeothermaldata.org/metadata/record/4e6b8f72f7d6c3856f092c6b850180eb.iso.xml",
        "schema:encodingType": "INSPIRE 19115"
      }
    }
  ]
}
```

#### ttl
```ttl
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix dqv: <http://www.w3.org/ns/dqv#> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix schema1: <http://schema.org/> .
@prefix time: <http://www.w3.org/2006/time#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://doi.org/23609/53w7klh> a schema1:Dataset ;
    schema1:additionalType [ a schema1:DefinedTerm ;
            schema1:inDefinedTermSet "dde:codelist/ResourceTypeCode" ;
            schema1:name "Dataset" ;
            schema1:termCode "dataset" ] ;
    schema1:alternateName "Arizona 1:1000000 Lithostratigraphic map" ;
    schema1:conditionsOfAccess [ a schema1:CreativeWork ;
            schema1:name "other license test" ;
            schema1:url "https://test.org/otherlicense/zero/1.0/" ] ;
    schema1:contributor [ a schema1:Role ;
            schema1:contributor [ a schema1:Person ;
                    schema1:contactPoint [ a schema1:ContactPoint ;
                            schema1:email "clarkr@azgs.az.gov" ] ;
                    schema1:identifier "https://orcid.org/0000-0041-6041-6309" ;
                    schema1:name "Ryan Clark" ] ;
            schema1:roleName "pointOfContact" ] ;
    schema1:creator ( [ a schema1:Person ;
                schema1:contactPoint [ a schema1:ContactPoint ;
                        schema1:email "richards@azgs.az.gov" ] ;
                schema1:identifier "https://orcid.org/0000-0001-6041-5302" ;
                schema1:name "Stephen Richard" ] ) ;
    schema1:dateModified "2016-04-14" ;
    schema1:datePublished "2006-05-04" ;
    schema1:description "Lithostratigraphic unit distribution for the Geologic Map of Arizona at 1:1,000,000-scale. Shows entire state with map units defined broadly by age and lithologic type. The map was compiled by modifying the previous 1:1000000 statemap version with more recent mapping." ;
    schema1:distribution [ a schema1:DataDownload ;
            schema1:contentUrl "http://services.azgs.az.gov/ArcGIS/services/OneGeology/AZGS_Arizona_Geology/MapServer/WMSServer?" ;
            schema1:description "OGC get map URL" ;
            schema1:encodingFormat "image/jpg",
                "image/png",
                "image/tif" ;
            schema1:name "US-AZ_AZGS_1M_Lithostratigraphy" ],
        [ a schema1:DataDownload ;
            schema1:contentUrl "http://services.azgs.az.gov/ArcGIS/services/OneGeology/AZGS_Arizona_Geology_WFS/MapServer/WFSServer?" ;
            schema1:description "OGC get capabilities URL" ;
            schema1:encodingFormat "application/xml" ;
            schema1:name "gsmlp:GeologicUnitView" ;
            schema1:provider [ a schema1:Organization ;
                    schema1:identifier "https://ror.org/00vcszp55" ;
                    schema1:name "Arizona Geological Survey" ] ] ;
    schema1:identifier [ a schema1:PropertyValue ;
            schema1:propertyID "https://registry.identifiers.org/registry/doi" ;
            schema1:url "https://doi.org/23609/53w7klh" ;
            schema1:value "doi:23609/53w7klh" ] ;
    schema1:image [ a schema1:ImageObject ;
            schema1:contentUrl "http://azgs.az.gov/repository/browse/2222.jpg" ;
            schema1:description "description of the browse image2" ;
            schema1:encodingFormat "image/png" ;
            schema1:name "Another map of Arizona" ],
        [ a schema1:ImageObject ;
            schema1:contentUrl "http://azgs.az.gov/repository/browse/3757.jpg" ;
            schema1:description "description of the browse image" ;
            schema1:name "Quick view lithostratigraphic map of Arizona" ] ;
    schema1:inLanguage "eng" ;
    schema1:keywords [ a schema1:DefinedTerm ;
            schema1:inDefinedTermSet "dde:codelist/TopicCategoryCode" ;
            schema1:name "Paleontology" ;
            schema1:termCode "GI_PO_paleontology" ],
        [ a schema1:DefinedTerm ;
            schema1:identifier "https://edits.nationalmap.gov/apps/gaz-domestic/public/gaz-record/1779777" ;
            schema1:name "Arizona" ],
        [ a schema1:DefinedTerm ;
            schema1:inDefinedTermSet "dde:codelist/TopicCategoryCode" ;
            schema1:name "Environment" ;
            schema1:termCode "environment" ],
        [ a schema1:DefinedTerm ;
            schema1:inDefinedTermSet "dde:codelist/AcquisitionTypeCode" ;
            schema1:name "Digital Conversion from Published Source" ;
            schema1:termCode "digitalConversionFromPublishedSource" ],
        [ a schema1:DefinedTerm ;
            schema1:inDefinedTermSet "dde:codelist/TopicCategoryCode" ;
            schema1:name "Geoscientific Information" ;
            schema1:termCode "geoscientificInformation" ],
        [ a schema1:DefinedTerm ;
            schema1:inDefinedTermSet "dde:codelist/AcquisitionTypeCode" ;
            schema1:name "Synthesis from Multiple Sources" ;
            schema1:termCode "synthesisFromMultipleSources" ],
        [ a schema1:DefinedTerm ;
            schema1:inDefinedTermSet "dde:codelist/TopicCategoryCode" ;
            schema1:name "Hydrogeology" ;
            schema1:termCode "GI_HG_hydrogeology" ],
        "Geologic Map",
        "Geology",
        "United States" ;
    schema1:license [ a schema1:CreativeWork ;
            schema1:name "Creative Commons CC0 1.0 Universal" ;
            schema1:url "https://creativecommons.org/publicdomain/zero/1.0/" ] ;
    schema1:name "US-AZ_AZGS_1M_Lithostratigraphy" ;
    schema1:provider [ a schema1:Organization ;
            schema1:contactPoint [ a schema1:ContactPoint ;
                    schema1:email "info@azgs.az.gov" ] ;
            schema1:identifier "https://ror.org/00vcszp55" ;
            schema1:name "Arizona Geological Survey" ] ;
    schema1:relatedLink [ a schema1:LinkRole ;
            schema1:linkRelationship "information" ],
        [ a schema1:LinkRole ;
            schema1:linkRelationship "completeMetadata" ] ;
    schema1:spatialCoverage [ a schema1:Place ;
            schema1:geo [ a schema1:GeoShape ;
                    schema1:box "31.332177 -114.81651 37.00426 -109.045223" ] ;
            schema1:identifier [ a schema1:PropertyValue ;
                    schema1:propertyID "Wikidata" ;
                    schema1:value "https://www.wikidata.org/wiki/Q816" ] ;
            schema1:name "Arizona" ] ;
    schema1:subjectOf <urn:uuid:c98705ae-058a-43fb-85a2-7b5209d9a4b3> ;
    schema1:temporalCoverage [ a time:ProperInterval ;
            time:hasBeginning [ a time:Instant ;
                    schema1:identifier "http://resource.geosciml.org/classifier/ics/ischart/Paleoproterozoic" ;
                    schema1:name "Early Proterozoic" ;
                    time:inTimePosition [ a time:TimePosition ;
                            time:hasTRS <https://example.org/trs/ma-before-present> ;
                            time:numericPosition 1870 ] ] ;
            time:hasEnd [ a time:Instant ;
                    schema1:identifier "http://resource.geosciml.org/classifier/ics/ischart/Holocene" ;
                    schema1:name "Holocene" ] ] ;
    schema1:url "https://hdl.handle.net/10150/630741" ;
    schema1:version "4" ;
    dqv:hasQualityMeasurement [ a dqv:QualityMeasurement ;
            schema1:description "Line work reviewed for consistency with source maps" ;
            dqv:isMeasurementOf "completeness" ;
            dqv:value "Line work reviewed for consistency with source maps" ] ;
    prov:wasDerivedFrom <https://doi.org/24596/h35wp59y>,
        <https://doi.org/24596/tehou246> .

<https://doi.org/24596/h35wp59y> a prov:Entity ;
    schema1:name "source1" .

<https://doi.org/24596/tehou246> a prov:Entity ;
    schema1:name "source0" .

<urn:uuid:c98705ae-058a-43fb-85a2-7b5209d9a4b3> a schema1:Dataset ;
    dcterms:conformsTo <https://w3id.org/cdif/bbr/metadata/profiles/DDEProfiles/DDEDiscovery> ;
    schema1:about <https://doi.org/23609/53w7klh> ;
    schema1:additionalType "dcat:CatalogRecord" ;
    schema1:maintainer [ a schema1:Person ;
            schema1:contactPoint [ a schema1:ContactPoint ;
                    schema1:email "metadata@azgs.az.gov" ] ;
            schema1:identifier "https://orcid.org/0000-0041-6041-6309" ;
            schema1:name "publications manager" ] ;
    schema1:sdDatePublished "2017-04-24" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
type: object
title: DDE Geoscience Discovery metadata schema
description: JSON schema for JSON-LD documents that describe geoscience datasets for
  the DDE Discovery profile. Composes CDIF mandatory and optional properties with
  DDE-specific required and optional extensions. DDE adds resource typing from the
  DDE ResourceTypeCode codelist, topic category and acquisition type keywords from
  DDE codelists, browse graphics, DDE profile conformance, alternate names, and measurement
  techniques. Conditional extensions for imagery (ddeImagery) and services (ddeServiceInfo)
  are NOT included in the base profile.
allOf:
- $ref: https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifMandatory/schema.yaml
- $ref: https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifOptional/schema.yaml
- $ref: https://usgin.github.io/ddeBuildingBlocks/build/annotated/bbr/metadata/DDEproperties/ddeRequired/schema.yaml
- $ref: https://usgin.github.io/ddeBuildingBlocks/build/annotated/bbr/metadata/DDEproperties/ddeOptional/schema.yaml
x-jsonld-prefixes:
  schema: http://schema.org/
  cdi: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/
  dcterms: http://purl.org/dc/terms/
  geosparql: http://www.opengis.net/ont/geosparql#
  spdx: http://spdx.org/rdf/terms#
  time: http://www.w3.org/2006/time#
  skos: http://www.w3.org/2004/02/skos/core#
  dde: https://www.ddeworld.org/resource/
  dcat: http://www.w3.org/ns/dcat#
  prov: http://www.w3.org/ns/prov#
  dqv: http://www.w3.org/ns/dqv#

```

Links to the schema:

* YAML version: [schema.yaml](https://usgin.github.io/ddeBuildingBlocks/build/annotated/bbr/metadata/profiles/DDEProfiles/DDEDiscovery/schema.json)
* JSON version: [schema.json](https://usgin.github.io/ddeBuildingBlocks/build/annotated/bbr/metadata/profiles/DDEProfiles/DDEDiscovery/schema.yaml)


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
[context.jsonld](https://usgin.github.io/ddeBuildingBlocks/build/annotated/bbr/metadata/profiles/DDEProfiles/DDEDiscovery/context.jsonld)

## Sources

* [DDE Metadata Standard](https://www.ddeworld.org)
* [CDIF book](https://cross-domain-interoperability-framework.github.io/cdifbook/metadata/schemaorgimplementation.html#schema-org-implementation-of-cdif-metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/ddeBuildingBlocks](https://github.com/usgin/ddeBuildingBlocks)
* Path: `_sources/profiles/DDEProfiles/DDEDiscovery`

