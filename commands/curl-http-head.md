---
id: 123e4567-e89b-12d3-a456-426614174005
name: curl-http-head
type: command
executor: bash
data: 'curl -I http://users.tweetdeck.com'
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T05:32:23.514Z'
platforms:
  - Linux
  - macOS
tags:
  - http
  - recon
verified: false
validated: true
submitted: true
---

# curl-http-head

## Command

```bash
curl -I http://users.tweetdeck.com
```

## Description

Sends a HEAD request to check for AWS S3 error pages indicating missing buckets.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-I` | HEAD request only (headers) | Yes |
| `http://users.tweetdeck.com` | Target URL | Yes |

## Examples

### Basic Usage

```bash
curl -I http://users.tweetdeck.com
```

### Advanced Usage

```bash
curl -I -v http://users.tweetdeck.com
```

## Expected Output

HTTP headers with 403/404 and AWS XML error body.

## Related

- [[Related Procedure]]
