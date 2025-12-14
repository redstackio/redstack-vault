---
data: base64 malicious.svg > encoded.txt
tags:
  - encoding
  - payload
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:20.324Z'
id: 98a255b5-7223-49b7-bef7-f975de97c496
verified: false
validated: true
submitted: true
---
# generate-base64-svg

## Command

```bash
base64 malicious.svg > encoded.txt
```

## Description

This command encodes an SVG file to base64 format, useful for embedding malicious content in JSON payloads for file upload exploits.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `malicious.svg` | Input SVG file path | Yes |
| `> encoded.txt` | Output redirection to file | Yes |

## Examples

### Basic Usage

```bash
base64 malicious.svg > encoded.txt
```

### Advanced Usage

```bash
base64 -w 0 malicious.svg  # No line wraps, direct to stdout
```

## Expected Output

Base64-encoded string written to encoded.txt, e.g., PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIG9ubG9hZD0iYWxlcnQoZG9jdW1lbnQuZG9tYWluKSI+PC9zdmc+

## Related

- [[commands/curl-upload-signature]]
