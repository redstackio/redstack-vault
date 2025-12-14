---
id: c4g5h6i7-j8k9-0124-fg02-345678901234
data: '-rotate 90'
tags:
  - testing
  - graphicsmagick
type: command
output: Image rotated by 90 degrees
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:24:14.472Z'
verified: false
validated: true
submitted: true
---
# -rotate 90

## Command

```bash
gm convert input.jpg -rotate 90 output.jpg
```
(Injected as argument: y=0 -rotate 90)

## Description

Appends a rotation flag to confirm GraphicsMagick usage during vulnerability reconnaissance, rotating the image 90 degrees if processed.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -rotate | Rotation option | Yes |
| 90 | Degrees to rotate (clockwise) | Yes |

## Examples

### Basic Usage

```bash
y=0 -rotate 90
```
(As injected parameter)

### Advanced Usage

```bash
y=0 -rotate 180 -resize 50%
```

## Expected Output

Processed image shows 90-degree rotation, confirming tool and injection point.

## Related

- [[commands/ps-aux]]
