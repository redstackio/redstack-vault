---
id: 6b8ab04f-a594-42b0-83af-d0ee5fb5bfea
name: imagemagick-convert-jpg-to-mvg
type: command
executor: bash
data: convert $_INPUT_IMAGE.jpg $_OUTPUT_MVG.mvg
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - imagemagick
  - conversion
verified: true
validated: true
---

# imagemagick-convert-jpg-to-mvg

## Command

```bash
convert $_INPUT_IMAGE.jpg $_OUTPUT_MVG.mvg
```

## Description

This ImageMagick command converts a JPG image to MVG format, which can trigger embedded payloads in vulnerable versions during processing. Used in exploits to simulate server-side handling of malicious uploads.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_INPUT_IMAGE | Path to input JPG file | Yes |
| $_OUTPUT_MVG | Path for output MVG file | Yes |

## Examples

### Basic Usage

```bash
convert image.jpg exploit.mvg
```

### Advanced Usage

```bash
convert -verbose image.jpg exploit.mvg
```

## Expected Output

Image conversion complete, with verbose mode showing processing details like "convert: MVG `exploit.mvg' @ warning/delegates.mvg.c/MvgDelegate/305" if payload triggers.

## Related

- [[procedures/ImageMagick-RCE-via-Malicious-MVG-Upload]]
- [[commands/imagemagick-identify-verbose]]
