---
id: 0a8996a8-4573-481d-a0bc-5543b5d55b39
name: sketchtool-export-artboards-png
type: command
executor: bash
data: >-
  sketchtool export artboards $_SKETCH_FILE_PATH --output=$_OUTPUT_DIR
  --formats=png
output: null
created_at: '2023-04-06T03:55:52.632405+00:00'
updated_at: '2023-04-06T03:55:52.647009+00:00'
platforms:
  - macOS
tags:
  - design
  - extraction
  - file-analysis
verified: true
validated: true
---

# sketchtool-export-artboards-png

## Command

```bash
sketchtool export artboards $_SKETCH_FILE_PATH --output=$_OUTPUT_DIR --formats=png
```

## Description

Exports all artboards from a Sketch file as PNG images, useful for visually inspecting or OCR-scanning design prototypes that may contain pasted API tokens or credentials in mockups.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_SKETCH_FILE_PATH | Path to the input .sketch file | Yes |
| $_OUTPUT_DIR | Directory to save PNG files | Yes |
| --formats=png | Output format (png, jpg, etc.) | No (default: pdf) |

## Examples

### Basic Usage

```bash
sketchtool export artboards mydesign.sketch --output=./exports --formats=png
```

### Advanced Usage

Export specific artboards: `sketchtool export artboards mydesign.sketch --items=Artboard1,Artboard2 --output=./exports --formats=png`.

## Expected Output

PNG files named after artboards in $_OUTPUT_DIR, e.g., Artboard1.png, containing visual elements for further analysis.

## Related

- [[procedures/Mapbox-API-Token-Leakage]]
- [[commands/sketchtool-dump-to-json]]
