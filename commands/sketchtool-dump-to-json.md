---
id: 4c18a485-4469-4a39-be49-35f7e867af96
name: sketchtool-dump-to-json
type: command
executor: bash
data: sketchtool dump $_SKETCH_FILE_PATH
output: null
created_at: '2023-04-06T03:55:52.632344+00:00'
updated_at: '2023-04-06T03:55:52.646937+00:00'
platforms:
  - macOS
tags:
  - design
  - extraction
  - file-analysis
verified: true
validated: true
---

# sketchtool-dump-to-json

## Command

```bash
sketchtool dump $_SKETCH_FILE_PATH
```

## Description

This command uses the Sketch CLI tool to dump the contents of a .sketch file into JSON format, exposing internal elements like text layers, metadata, and embedded strings where API tokens might be hidden during prototyping.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_SKETCH_FILE_PATH | Path to the .sketch file | Yes |

## Examples

### Basic Usage

```bash
sketchtool dump /path/to/design.sketch > design.json
```

### Advanced Usage

Dump and pipe to grep for token patterns: `sketchtool dump file.sketch | grep 'pk\.'`.

## Expected Output

JSON structure representing the document:

```json
{
  "document": {
    "pages": [
      {
        "name": "Page 1",
        "layers": [
          {
            "name": "Text Layer",
            "attributedString": {
              "string": "Mapbox token: pk.eyJ..."
            }
          }
        ]
      }
    ]
  }
}
```

## Related

- [[procedures/Mapbox-API-Token-Leakage]]
- [[commands/sketchtool-export-artboards-png]]
