---
data: >-
  response = requests.post('https://dust.tt/api/w/<workspace_sid>/files',
  cookies=cookies, json=json_data)
tags:
  - api
  - post
type: command
output: JSON response with uploadUrl
executor: python
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:55:38.401Z'
id: deb84d5c-d76f-40db-a944-9b99efbec38d
verified: false
validated: true
submitted: true
---
# post-upload-metadata-python

## Command

```python
response = requests.post('https://dust.tt/api/w/<workspace_sid>/files', cookies=cookies, json=json_data)
```

## Description

Sends POST request to Dust API with file metadata to obtain presigned upload URL.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| url | API endpoint with workspace SID | Yes |
| cookies | Auth cookies | Yes |
| json | Metadata dict | Yes |

## Examples

### Basic Usage

```python
response = requests.post('https://dust.tt/api/w/<workspace_sid>/files', cookies=cookies, json=json_data)
```

## Expected Output

JSON object containing 'file' with 'uploadUrl'.

## Related

- [[commands/extract-upload-url-python]]
