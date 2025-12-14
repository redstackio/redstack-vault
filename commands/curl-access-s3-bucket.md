---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
name: curl-access-s3-bucket
type: command
executor: bash
data: 'curl -I http://suspected-bucket-name.s3.amazonaws.com/'
output: HTTP/1.1 200 OK\n...
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:24:45.364Z'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - recon
  - cloud
  - http
verified: false
validated: true
submitted: true
---

# curl-access-s3-bucket

## Command

```bash
curl -I http://suspected-bucket-name.s3.amazonaws.com/
```

## Description

This command uses curl to perform a HEAD request on an AWS S3 bucket URL to test for public read access, revealing if sensitive objects like source code can be accessed without authentication. Use it during reconnaissance to identify misconfigured cloud storage.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-I` | Fetch headers only (HEAD request) | Yes |
| `http://suspected-bucket-name.s3.amazonaws.com/` | S3 bucket endpoint URL | Yes |

## Examples

### Basic Usage

```bash
curl -I http://example-bucket.s3.amazonaws.com/
```

### Advanced Usage

```bash
curl http://example-bucket.s3.amazonaws.com/ -o listing.xml
```

## Expected Output

Description of what output to expect when the command runs successfully.

HTTP/1.1 200 OK headers if public; includes Content-Type: application/xml for bucket listings. For full GET, XML with <ListBucketResult> containing object keys.

## Related

- [[Related Procedure|procedures/Access-Public-AWS-S3-Bucket]]
