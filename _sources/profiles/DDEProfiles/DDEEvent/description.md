## DDE Event Profile

DDE profile for event resources. Extends DDEDiscovery with a resource type constraint and requires `schema:temporalCoverage` (mandatory temporal extent for events).

### Resource type codes
initiative, fieldSession

### Composed building blocks

1. **DDEDiscovery** — Base DDE discovery profile
2. **Resource type constraint** — `schema:termCode` must be one of the event group codes
3. **`schema:temporalCoverage`** (required) — Temporal extent of the event
