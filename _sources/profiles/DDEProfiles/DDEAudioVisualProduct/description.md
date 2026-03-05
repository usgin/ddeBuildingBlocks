## DDE AudioVisual Product Profile

DDE profile for audiovisual resources. Extends DDEDiscovery with a resource type constraint and adds `schema:duration`.

### Resource type codes
movie, sound

### Composed building blocks

1. **DDEDiscovery** — Base DDE discovery profile
2. **Resource type constraint** — `schema:termCode` must be one of the audiovisual group codes
3. **`schema:duration`** (optional) — Duration in ISO 8601 format (e.g., PT1H30M, PT45S)
