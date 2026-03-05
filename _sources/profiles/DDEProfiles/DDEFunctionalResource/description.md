## DDE Functional Resource Profile

DDE profile for functional resources. Extends DDEDiscovery with a resource type constraint and requires a `schema:relatedLink` with `schema:linkRelationship` of `implementationSoftware`.

### Resource type codes
application, webApplication, model

### Composed building blocks

1. **DDEDiscovery** — Base DDE discovery profile
2. **Resource type constraint** — `schema:termCode` must be one of the functional resource group codes
3. **`schema:relatedLink`** — Must contain at least one link with `schema:linkRelationship: "implementationSoftware"` pointing to the software that implements the functional resource
