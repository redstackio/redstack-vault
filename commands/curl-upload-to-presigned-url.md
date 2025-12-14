---
id: cmd-uuid-2
data: >-
  curl -X PUT -T largefile.txt
  "https://bucket.s3.amazonaws.com/key?X-Amz-Algorithm=AWS4-HMAC-SHA256&..." -H
  "Content-Type: text/plain" -H "Content-MD5: ACTUAL_LARGE_MD5_BASE64"
tags:
  - http
  - put
  - s3
type: command
output: HTTP/1.1 200 OK
executor: bash
platforms:
  - Cloud (AWS)
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T05:32:10.032Z'
verified: false
validated: true
submitted: true
---
# curl-upload-to-presigned-url

## Command

```bash
curl -X PUT -T largefile.txt "https://bucket.s3.amazonaws.com/key?X-Amz-Algorithm=AWS4-HMAC-SHA256&..." -H "Content-Type: text/plain" -H "Content-MD5: ACTUAL_LARGE_MD5_BASE64"
```

## Description

Uploads a file to an S3 presigned URL via PUT, bypassing size limits due to unsigned content-length.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X PUT` | HTTP method for upload | Yes |
| `-T largefile.txt` | Local file to upload | Yes |
| URL | Presigned S3 URL | Yes |
| `-H "Content-Type: ..."` | MIME type | Yes |
| `-H "Content-MD5: ..."` | Base64 MD5 of file | Yes |

## Examples

### Basic Usage

```bash
curl -X PUT -T file.txt "https://s3..." -H "Content-Type: text/plain"
```

### Advanced Usage

```bash
curl -X PUT -T largefile.bin "https://bucket.s3.amazonaws.com/key?presigned" -H "Content-Type: application/octet-stream" -H "Content-MD5: MD5_BASE64"
```

## Expected Output

S3 response: <ETag>"md5-hash"</ETag> or HTTP 200.

## Related

- [[Related Procedure]]
