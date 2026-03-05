## DDE Image Profile

DDE profile for image resources. Extends DDEDiscovery with a resource type constraint and the ddeImagery building block for imagery-specific properties.

### Resource type codes
image, photograph, explanatoryFigure, map

### Composed building blocks

1. **DDEDiscovery** — Base DDE discovery profile
2. **ddeImagery** — Optional imagery properties: sensor type, platform, equipment, collector, startTime, endTime, signalGenerator, wavelength, processedLevel
3. **Resource type constraint** — `schema:termCode` must be one of the image group codes
