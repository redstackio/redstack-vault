---
data: 'curl -I https://assets.goubiquiti.com'
tags:
  - http
  - verification
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 0decc0d1-01b3-4035-a74b-72fdcf83abdf
created_at: '2025-12-14T04:51:10.526Z'
updated_at: '2025-12-14T04:51:10.526Z'
verified: false
validated: true
submitted: true
---
# curl-access-subdomain

## Command

```bash
curl -I https://assets.goubiquiti.com
```

## Description

This command sends a HEAD request to a subdomain to check HTTP status and headers, revealing S3 errors for unconfigured buckets.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-I` | HEAD request only (headers) | Yes |
| `URL` | Target subdomain URL | Yes |

## Examples

### Basic Usage

```bash
curl -I https://assets.goubiquiti.com
```

### Advanced Usage

```bash
curl -v https://assets.goubiquiti.com
```

## Expected Output

HTTP/1.1 404 Not Found
Content-Type: application/xml
<Error><Code>NoSuchBucket</Code>...

## Related

- [[Related Procedure: Verify S3 Bucket Absence]]
