---
data: exiftool -all image.jpg
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
updated_at: '2025-12-14T17:25:34.389Z'
id: a169c901-8538-43fd-96a6-45f730ecd8bb
verified: false
validated: true
submitted: true
---
# exiftool-extract

## Command

```bash
exiftool -all image.jpg
```

## Description

This command dumps all EXIF metadata from an image file, useful for extracting sensitive data like GPS coordinates after accessing via IDOR.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-all` | Extracts every available tag | Yes |
| `image.jpg` | Path to the image file | Yes |

## Examples

### Basic Usage

```bash
exiftool -all accessed_image.jpg
```

### Advanced Usage

```bash
exiftool -all -G image.jpg | grep GPS
```

## Expected Output

File Name : accessed_image.jpg
GPS Latitude : 37.7749 N
GPS Longitude : 122.4194 W
... (full tag list)

## Related

- [[Related Procedure: Extract-EXIF-Metadata-from-Image]]
