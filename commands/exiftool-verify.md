---
data: exiftool -GPS* image.jpg
tags:
  - exif
  - metadata
type: command
output: null
executor: bash
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:34.393Z'
id: 446f7f0f-3e9c-426f-81e4-050ba2d70f60
verified: false
validated: true
submitted: true
---
# exiftool-verify

## Command

```bash
exiftool -GPS* image.jpg
```

## Description

This command uses exiftool to display only GPS-related EXIF tags from a JPEG image, verifying the presence of geolocation metadata before upload testing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-GPS*` | Filters output to GPS tags only | Yes |
| `image.jpg` | Path to the target image file | Yes |

## Examples

### Basic Usage

```bash
exiftool -GPS* gps_sample.jpg
```

### Advanced Usage

```bash
exiftool -GPS:all -csv gps_sample.jpg > gps_data.csv
```

## Expected Output

GPS Latitude : 37 deg 46' 29.64" N
GPS Longitude: 122 deg 25' 9.98" W
GPS Altitude : 10.5 m

## Related

- [[Related Procedure: Prepare-Images-with-EXIF-Data]]
