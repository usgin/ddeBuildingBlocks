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
