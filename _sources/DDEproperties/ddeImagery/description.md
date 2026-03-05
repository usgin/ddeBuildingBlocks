## DDE Imagery Properties

Conditional extension for imagery resources. Maps DDE imagery acquisition metadata into the CDIF provenance pattern (cdifProv). This building block is composed into the DDEImage profile when describing remote sensing or other imagery datasets.

All properties are optional.

### Imagery acquisition via `prov:wasGeneratedBy`

Each imagery acquisition event is represented as a provenance activity following the cdifProv pattern. The activity captures:

- **Instruments** (`prov:used` with `schema:instrument`): Each instrument is typed via `schema:additionalType` with a DDE category:
  - `dde:sensorType` — Type of sensor (e.g., "Multispectral", "SAR", "LiDAR")
  - `dde:platform` — Platform carrying the sensor (e.g., "Landsat-8", "Sentinel-2A")
  - `dde:equipment` — Equipment used for acquisition (e.g., "Operational Land Imager")
  - `dde:signalGenerator` — Type of signal used (e.g., "Passive solar", "Active radar")
- **Participants** (`schema:participant`): The data collector as an agentInRole with `schema:roleName: "DataCollector"`
- **Temporal bounds**: `schema:startTime` and `schema:endTime` on the activity (ISO 8601)

### Dataset-level properties via `schema:additionalProperty`

Properties that describe the image product itself (not the acquisition activity):

- **`dde:wavelength`** — Wavelength range (e.g., "0.43-2.29 micrometers"). Value: string.
- **`dde:processedLevel`** — Processing level. Value from `ProcessingLevelCode` enum: Level0, Level1, Level2, Level3, Level4.
