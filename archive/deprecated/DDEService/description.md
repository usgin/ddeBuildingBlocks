## DDE Service Profile

DDE profile for service resources. Extends DDEDiscovery with a resource type constraint and the ddeServiceInfo building block for service-specific properties.

### Resource type codes
repository, service, webAPI

### Composed building blocks

1. **DDEDiscovery** — Base DDE discovery profile
2. **ddeServiceInfo** — Service properties: serviceType (mandatory), containsOperations, accessProperties, operatedDataset, endpointDescription
3. **Resource type constraint** — `schema:termCode` must be one of the service group codes
