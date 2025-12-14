---
id: cmd-uuid-004
name: curl-fetch-file
type: command
executor: bash
data: 'curl -I https://target.com/files/xss.zip'
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:47:12.810Z'
platforms:
  - Linux
tags:
  - fetch
  - headers
verified: false
validated: true
submitted: true
---

# curl-fetch-file

## Command

```bash
curl -I https://target.com/files/xss.zip
```

## Description

Fetches HTTP headers for a remote file to check MIME types and security headers.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -I | HEAD request only | Yes |
| URL | File URL | Yes |

## Examples

### Basic Usage

```bash
curl -I https://example.com/file
```

### Advanced Usage

Verbose: ```bash
curl -v -I https://target.com/files/xss.zip
```

## Expected Output

HTTP/1.1 200 OK
Content-Type: application/zip
(No nosniff header).

## Related

- [[commands/curl-upload-file]]
