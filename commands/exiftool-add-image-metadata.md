---
id: aaf675d8-ff9c-459e-9577-fbb2f922568e
name: exiftool-add-image-metadata
type: command
executor: bash
data: >-
  exiftool -Copyright="PayloadsAllTheThings" -Artist="Pentest"
  -ImageUniqueID="Example" payload.jpg
output: null
created_at: '2023-04-06T03:56:41.078561+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - metadata
  - exif
verified: true
validated: true
---

# exiftool-add-image-metadata

## Command

```bash
exiftool -Copyright="PayloadsAllTheThings" -Artist="Pentest" -ImageUniqueID="Example" payload.jpg
```

## Description

This command adds benign EXIF metadata tags to an image file using ExifTool, useful for disguising payloads in file upload attacks by simulating legitimate tagging.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -Copyright="PayloadsAllTheThings" | Sets the copyright notice | Yes |
| -Artist="Pentest" | Sets the artist/author field | Yes |
| -ImageUniqueID="Example" | Sets a unique identifier for the image | Yes |
| payload.jpg | Target image file to modify | Yes |

## Examples

### Basic Usage

```bash
exiftool -Copyright="Test" image.jpg
```

### Advanced Usage

```bash
exiftool -Artist="Author" -Description="Test Image" -GPSLatitude=40.7128 image.jpg
```

## Expected Output

Terminal output: "1 image files updated" followed by a summary of written tags. The image file is backed up as payload.jpg_original if not overwritten.

## Related

- [[Related Procedure|procedures/Inject-PHP-Code-into-Image-Metadata-for-RCE]]
- [[Related Tool|tools/ExifTool]]
