---
data: 'uploadUrl = response.json()[''file''][''uploadUrl'']'
tags:
  - parse
  - json
type: command
output: null
executor: python
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:55:38.398Z'
id: f58a55e1-b54e-4ca9-aa7f-78f669d15fab
verified: false
validated: true
submitted: true
---
# extract-upload-url-python

## Command

```python
uploadUrl = response.json()['file']['uploadUrl']
```

## Description

Parses the JSON response to extract the presigned upload URL for the file.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| response | Response object | Yes |

## Examples

### Basic Usage

```python
uploadUrl = response.json()['file']['uploadUrl']
```

## Expected Output

String URL for upload.

## Related

- [[commands/post-file-upload-python]]
