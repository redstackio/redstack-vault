---
id: b6b99d32-66c0-44fa-95ca-628a6d58c29d
name: imagemagick-create-white-image
type: command
executor: bash
data: 'convert -size 110x110 xc:white payload.jpg'
output: null
created_at: '2023-04-06T03:56:41.078512+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - image-creation
  - payload
verified: true
validated: true
---

# imagemagick-create-white-image

## Command

```bash
convert -size 110x110 xc:white payload.jpg
```

## Description

This command uses ImageMagick's convert utility to generate a blank 110x110 pixel white JPEG image, serving as a base for embedding malicious metadata in payload creation workflows.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -size 110x110 | Specifies the image dimensions in pixels | Yes |
| xc:white | Creates a solid white canvas | Yes |
| payload.jpg | Output filename for the generated image | Yes |

## Examples

### Basic Usage

```bash
convert -size 110x110 xc:white payload.jpg
```

### Advanced Usage

```bash
convert -size 200x200 xc:black malicious.png
```

## Expected Output

No terminal output if successful; a new file payload.jpg is created (approximately 1-2 KB). Verify with ls -la payload.jpg or display the image to confirm it's a plain white square.

## Related

- [[Related Procedure|procedures/Inject-PHP-Code-into-Image-Metadata-for-RCE]]
- [[Related Tool|tools/ImageMagick]]
