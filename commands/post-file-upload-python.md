---
data: >-
  response = requests.post(url=uploadUrl, headers=headers, cookies=cookies,
  data=m)
tags:
  - upload
  - post
type: command
output: JSON response with downloadUrl
executor: python
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:55:38.390Z'
id: 167a4313-4fa2-4cd9-9bfc-50bfa220be33
verified: false
validated: true
submitted: true
---
# post-file-upload-python

## Command

```python
response = requests.post(url=uploadUrl, headers=headers, cookies=cookies, data=m)
```

## Description

Uploads the malicious file using multipart data to the presigned URL.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| url | Presigned upload URL | Yes |
| headers | Browser-like headers | Yes |
| cookies | Auth cookies | Yes |
| data | Multipart encoder | Yes |

## Examples

### Basic Usage

```python
response = requests.post(url=uploadUrl, headers=headers, cookies=cookies, data=m)
```

## Expected Output

JSON with 'file' containing 'downloadUrl'.

## Related

- [[commands/print-shareable-url-python]]
