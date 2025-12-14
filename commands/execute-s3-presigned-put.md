---
id: cmd-uuid-2
data: >-
  curl -X PUT
  "https://haystack-production-storage-us-east-1.s3.amazonaws.com/<key>?x-amz-storage-class=<>&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=<>&X-Amz-Date=<>&X-Amz-Expires=300&X-Amz-SignedHeaders=content-length%3Bcontent-md5%3Bcontent-type%3Bhost&X-Amz-Signature=<>
  " -H "Content-Type: <content_type>" -H "Content-MD5: <checksum>" --data-binary
  @<file>
tags:
  - aws
  - s3
  - upload
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T05:32:13.695Z'
verified: false
validated: true
submitted: true
---
# execute-s3-presigned-put

## Command

```bash
curl -X PUT "https://haystack-production-storage-us-east-1.s3.amazonaws.com/<key>?x-amz-storage-class=<>&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=<>&X-Amz-Date=<>&X-Amz-Expires=300&X-Amz-SignedHeaders=content-length%3Bcontent-md5%3Bcontent-type%3Bhost&X-Amz-Signature=<> " \
  -H "Content-Type: <content_type>" \
  -H "Content-MD5: <checksum>" \
  --data-binary @<file>
```

## Description

Executes a presigned PUT to upload file content directly to an AWS S3 bucket, bypassing app authentication using generated signatures.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| <key> | S3 object key from upload initiation | Yes |
| X-Amz-Credential | Temporary AWS creds | Yes |
| X-Amz-Signature | HMAC signature | Yes |
| X-Amz-Date | Timestamp | Yes |
| Content-Type | File MIME type | Yes |
| Content-MD5 | Base64 MD5 of body | Yes |
| <file> | Path to arbitrary file | Yes |

## Examples

### Basic Usage

```bash
curl -X PUT "https://haystack-production-storage-us-east-1.s3.amazonaws.com/abc/key?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA...&X-Amz-Date=20231001T...&X-Amz-Expires=300&X-Amz-SignedHeaders=...&X-Amz-Signature=xyz..." \
  -H "Content-Type: image/svg+xml" \
  -H "Content-MD5: O7o+..." \
  --data-binary @test.svg
```

### Advanced Usage

Upload larger binary with storage class:

```bash
curl -X PUT "https://haystack-production-storage-us-east-1.s3.amazonaws.com/abc/key?x-amz-storage-class=INTELLIGENT_TIERING&..." \
  -H "Content-Type: application/octet-stream" \
  -H "Content-MD5: ..." \
  --data-binary @malicious.bin
```

## Expected Output

HTTP/1.1 200 OK

## Related

- [[commands/initiate-active-storage-upload]]
- [[procedures/Update-and-Execute-S3-PUT-Upload]]
