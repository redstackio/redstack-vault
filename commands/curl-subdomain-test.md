---
id: h8i9j0k1-l2m3-4567-hijk-890123456789
data: 'curl -I https://$1'
tags:
  - http
  - validation
type: command
output: HTTP/1.1 200 OK
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T04:51:10.860Z'
verified: false
validated: true
submitted: true
---
# curl-subdomain-test

## Command

```bash
curl -I https://musical.ly.example.com
```

## Description

Fetches HTTP headers from a subdomain to validate if it's serving content from the hijacked S3 bucket.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-I` | Fetch headers only | Yes |
| `https://domain` | The URL to test | Yes |

## Examples

### Basic Usage

```bash
curl -I https://musical.ly.example.com
```

### Advanced Usage

```bash
curl -s -I https://musical.ly.example.com | grep -i x-amz
```

## Expected Output

Headers including 'HTTP/1.1 200 OK' and S3-specific like 'x-amz-request-id'.

## Related

- [[Related Procedure: Validate-Subdomain-Hijacking]]
