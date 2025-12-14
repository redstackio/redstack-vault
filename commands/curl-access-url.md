---
data: 'curl -L http://blog.gnipcentral.com/'
tags:
  - web
  - verification
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 45cc9e73-eb4f-450e-b566-14b8ca33220f
created_at: '2025-12-14T04:51:26.387Z'
updated_at: '2025-12-14T04:51:26.387Z'
verified: false
validated: true
submitted: true
---
# curl-access-url

## Command

```bash
curl -L http://blog.gnipcentral.com/
```

## Description

Fetches the content from a URL, following redirects to verify subdomain takeover.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-L` | Follow redirects | Yes |
| `http://blog.gnipcentral.com/` | Target URL | Yes |

## Examples

### Basic Usage

```bash
curl -L http://blog.gnipcentral.com/
```

### Advanced Usage

```bash
curl -L -v http://blog.gnipcentral.com/
```

## Expected Output

HTML content from the S3 bucket, e.g., <h1>POC Takeover</h1>, after redirect.

## Related

- [[Related Procedure: Verify-Subdomain-Takeover-with-POC]]
