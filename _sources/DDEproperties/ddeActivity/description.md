# DDE acquisition activity

Narrows [cdifProvActivity](../../../cdifDataType/cdifProvActivity) for DDE
acquisition. It adds two things and inherits everything else.

## What it requires

**At least one instrument typed with a DDE acquisition category.** The four
categories are:

| category | DDE element |
|---|---|
| `dde:sensorType` | `sensor` |
| `dde:platform` | `platform` |
| `dde:equipment` | `equipment` |
| `dde:signalGenerator` | `signalGenerator` |

`cdifProvActivity` already requires an instrument described in place to carry the
Wikidata measuring-instrument term, so a DDE instrument's `schema:additionalType`
carries both:

```json
"schema:additionalType": [
  { "@id": "dde:sensorType" },
  { "@id": "https://www.wikidata.org/entity/Q3099911" }
]
```

The constraint uses `contains`, not `items`: an acquisition may list instruments
that are not DDE-categorised beside the ones that are, and `items` would reject
them. The four categories are separate `anyOf` branches rather than one `enum`, so
each can be extended independently and a failure names which was expected.

## What it does not require

**A data collector.** The DDE XSD has no collector element — `MD_Imagery` is
`sensor` [0..*], `platform`, `equipment`, `signalGenerator`, `wavelength` and
`processingLevel`, every one `minOccurs="0"` — so a `DataCollector` participant is
a convention rather than an obligation. `DataCollectorRole` in `$defs` records the
shape DDE imagery conventionally uses, a `schema:Role` with `roleName`
`DataCollector` wrapping a Person or an Organization, without imposing it.
Participants of any other shape `cdifProvActivity` permits remain valid.

## What it inherits

`schema:startTime`, `schema:endTime`, `schema:agent`, `schema:object`,
`schema:result`, `schema:location`, `schema:actionProcess`,
`schema:additionalProperty` and the rest come from `cdifProvActivity` unchanged,
including its requirement that an activity carry at least one of
`schema:instrument`, `schema:object` or `schema:actionProcess`.
