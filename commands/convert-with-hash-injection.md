---
data: >-
  convert ORIGINAL_IMAGE -auto-orient -write /tmp/file2.erb
  /tmp/image_processing20210328-23426-63rmm2.png
tags:
  - injection
  - imagemagick
type: command
executor: bash
platforms:
  - Linux
id: 61aaf4c2-3df5-407d-9bb1-4cde0521e9ea
created_at: '2025-12-14T17:28:28.321Z'
updated_at: '2025-12-14T17:28:28.321Z'
verified: false
validated: true
submitted: true
---
# convert-with-hash-injection

## Command

```bash
convert ORIGINAL_IMAGE -auto-orient -write /tmp/file2.erb /tmp/image_processing20210328-23426-63rmm2.png
```

## Description

ImageMagick convert command injected via hash parameters, redirecting output to an arbitrary file path for exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| ORIGINAL_IMAGE | Input image | Yes |
| -auto-orient | Auto-orient image | No |
| -write /tmp/file2.erb | Write to arbitrary path | Yes |
| /tmp/image_processing... | Final output | Yes |

## Examples

### Basic Usage

```bash
convert input.jpg -auto-orient -write /tmp/out.erb output.png
```

### Advanced Usage

```bash
convert input.jpg -auto-orient -write /tmp/file2.erb /tmp/final.png
```

## Expected Output

Writes the processed image directly to /tmp/file2.erb as an intermediate step.

## Related

- [[Related Procedure]]
