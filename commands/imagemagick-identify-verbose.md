---
id: f52327eb-78de-45a4-b261-4feba38ad59e
name: imagemagick-identify-verbose
type: command
executor: bash
data: identify -verbose $_INPUT_FILE
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - imagemagick
  - identification
verified: true
validated: true
---

# imagemagick-identify-verbose

## Command

```bash
identify -verbose $_INPUT_FILE
```

## Description

This ImageMagick command identifies and describes an image file in verbose detail, parsing formats like MVG and potentially executing embedded commands in vulnerable setups. Key for triggering RCE in malicious file processing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_INPUT_FILE | Path to the image or MVG file to analyze | Yes |
| -verbose | Outputs detailed metadata and processing info | Built-in |

## Examples

### Basic Usage

```bash
identify -verbose exploit.mvg
```

### Advanced Usage

```bash
identify -verbose -format "%m\n" exploit.mvg
```

## Expected Output

Detailed image info like:

Image: exploit.mvg
Format: MVG (Magick Vector Graphics)
Geometry: 640x480+0+0
...

In exploits, may show errors or warnings if payload executes.

## Related

- [[procedures/ImageMagick-RCE-via-Malicious-MVG-Upload]]
- [[commands/imagemagick-convert-jpg-to-mvg]]
