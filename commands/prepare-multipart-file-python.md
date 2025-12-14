---
data: >-
  m = MultipartEncoder(fields={'file': ('xss_poc.png', open('Dust/xss.html',
  'rb'), 'text/html')})
tags:
  - multipart
  - file
type: command
output: null
executor: python
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:55:38.396Z'
id: 36bbe77c-2c48-4631-a3e2-950fb89b745f
verified: false
validated: true
submitted: true
---
# prepare-multipart-file-python

## Command

```python
m = MultipartEncoder(fields={'file': ('xss_poc.png', open('Dust/xss.html', 'rb'), 'text/html')})
```

## Description

Creates a MultipartEncoder object for the malicious HTML file, specifying filename, file content, and content-type.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| fields | Dict with 'file' key and tuple (name, file, mime) | Yes |

## Examples

### Basic Usage

```python
m = MultipartEncoder(fields={'file': ('xss_poc.png', open('Dust/xss.html', 'rb'), 'text/html')})
```

## Expected Output

Encoder object ready for POST data.

## Related

- [[commands/post-file-upload-python]]
