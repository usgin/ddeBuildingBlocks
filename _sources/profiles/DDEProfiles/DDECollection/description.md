## DDE Collection Profile

DDE profile for collection resources. Extends DDEDiscovery with a resource type constraint and requires `schema:hasPart` to describe collection members.

### Resource type codes
aggregate, collection, series, learningResource, guide

### Composed building blocks

1. **DDEDiscovery** — Base DDE discovery profile
2. **Resource type constraint** — `schema:termCode` must be one of the collection group codes
3. **`schema:hasPart`** (required) — Array of collection members, each with at least `schema:name`

### Collection member structure
Each member in `schema:hasPart` must have:
- `schema:name` (required) — Name of the collection member
- `schema:description` (optional) — Description of the member
- `schema:url` (optional) — URL to the member resource
