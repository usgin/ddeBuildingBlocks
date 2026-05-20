# DDE Building Blocks repository

Building blocks for Deep-time Digital Earth (DDE) metadata profiles,
using the OGC Building Blocks pattern.


Modular schema components for DDE resource type metadata. Imports shared
schema.org and CDIF property building blocks from the CDIF Building Blocks repository.


## Building Blocks

### `dde.bbr.metadata.DDEproperties.ddeResourceType` — DDE Resource Type

**Type:** schema

Constrains schema:additionalType to require at least one DefinedTerm from the DDE ResourceTypeCode codelist. The DDE resource type vocabulary includes 32 resource types from the DDE spec Table 18. Defines properties: schema:additionalType. Uses building blocks: definedTerm (schemaorgProperties).

### `dde.bbr.metadata.DDEproperties.ddeGeographicDataset` — DDE Geographic Dataset Properties

**Type:** schema

Conditional extension for geographic dataset resources. Implements MD_SpatialRepresentation (DDE spec Table 5): mandatory spatialCoverage, plus spatialRepresentationType, spatialResolution, referenceSystemType, and referenceSystemIdentifier. Defines properties: schema:spatialCoverage, schema:additionalProperty. Uses building blocks: spatialExtent (schemaorgProperties), additionalProperty (schemaorgProperties), identifier (schemaorgProperties).

### `dde.bbr.metadata.DDEproperties.ddeCatalogRecord` — DDE Catalog Record

**Type:** schema

Extends cdifCatalogRecord to require DDE conformance declaration. Adds dcterms:conformsTo constraint for ddeCore BB URI.

### `dde.bbr.metadata.DDEproperties.ddeCore` — DDE Core metadata properties

**Type:** schema

DDE core extensions beyond CDIF discovery: DDE resource type (from ResourceTypeCode), topic category keywords (from TopicCategoryCode), acquisition type keywords (from AcquisitionTypeCode), browse graphic images, and DDE profile conformance declaration. Defines properties: schema:subjectOf, schema:additionalType, schema:keywords, schema:image. Uses building blocks: cdifCore (cdifProperties), definedTerm (schemaorgProperties), ddeCatalogRecord (DDEproperties), ddeResourceType (DDEproperties).

### `dde.bbr.metadata.DDEproperties.ddeImagery` — DDE Imagery Properties

**Type:** schema

Conditional extension for imagery resources using the CDIF provenance pattern (cdifProv). Maps DDE imagery acquisition metadata into prov:wasGeneratedBy activities: sensor, platform, equipment, and signalGenerator become typed instruments; collector becomes a participant with DataCollector role; startTime and endTime are activity temporal bounds. Wavelength and processedLevel remain as dataset-level schema:additionalProperty values. Defines properties: prov:wasGeneratedBy, schema:additionalProperty. Uses building blocks: instrument, agentInRole, person, organization, additionalProperty (schemaorgProperties).

### `dde.bbr.metadata.profiles.DDEProfiles.DDEAudioVisualProduct` — DDE AudioVisual Product profile

**Type:** schema

DDE profile for audiovisual resources (movie, sound). Extends DDEDiscovery with resource type constraint and schema:duration.

### `dde.bbr.metadata.profiles.DDEProfiles.DDECollection` — DDE Collection profile

**Type:** schema

DDE profile for collection resources (aggregate, collection, series, learningResource, guide). Extends DDEDiscovery with resource type constraint and requires schema:hasPart for collection members.

### `dde.bbr.metadata.profiles.DDEProfiles.DDEDataset` — DDE Dataset profile

**Type:** schema

DDE profile for dataset resources (dataset, dataCatalog, geographicDataset, nonGeographicDataset). Extends DDEDiscovery with resource type constraint. For geographicDataset, compose additionally with ddeGeographicDataset.

### `dde.bbr.metadata.profiles.DDEProfiles.DDEDiscovery` — DDE Geoscience Discovery metadata

**Type:** schema

Gather building blocks to generate a DDE Geoscience Discovery record. Composes CDIF mandatory and optional properties with DDE required and optional extensions for geoscience metadata.

### `dde.bbr.metadata.profiles.DDEProfiles.DDEDocument` — DDE Document profile

**Type:** schema

DDE profile for document resources (document, article, thesis, book, poster, webPage). Extends DDEDiscovery with resource type constraint.

### `dde.bbr.metadata.profiles.DDEProfiles.DDEEvent` — DDE Event profile

**Type:** schema

DDE profile for event resources (initiative, fieldSession). Extends DDEDiscovery with resource type constraint and requires schema:temporalCoverage.

### `dde.bbr.metadata.profiles.DDEProfiles.DDEFunctionalResource` — DDE Functional Resource profile

**Type:** schema

DDE profile for functional resources (application, webApplication, model). Extends DDEDiscovery with resource type constraint and requires a relatedLink with implementationSoftware linkRelationship.

### `dde.bbr.metadata.profiles.DDEProfiles.DDESemanticResource` — DDE Semantic Resource profile

**Type:** schema

DDE profile for semantic resources (semanticResource, definedTermSet). Extends DDEDiscovery with resource type constraint.

### `dde.bbr.metadata.profiles.DDEProfiles.DDESoftware` — DDE Software profile

**Type:** schema

DDE profile for software resources. Extends DDEDiscovery with resource type constraint.

### `dde.bbr.metadata.profiles.DDEProfiles.DDEWebAPI` — DDE WebAPI profile

**Type:** schema

DDE profile for resources that are web services. Composes ddeCore, ddeOptional, and the CDIF webAPI building block. Narrows serviceType to the DDE ServiceTypeCode codelist. Includes dataset references for operated datasets.

### `dde.bbr.metadata.profiles.DDEProfiles.DDEImage` — DDE Image profile

**Type:** schema

DDE profile for image resources (image, photograph, explanatoryFigure, map). Extends DDEDiscovery with resource type constraint and ddeImagery conditional properties (sensor, platform, equipment, etc.).

