---
data: 'curl -I http://gameday.websummit.net.s3-website-eu-west-1.amazonaws.com'
tags:
  - aws
  - http
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 64a39d66-04b3-4b9a-a9c4-a7fb72b35c62
created_at: '2025-12-14T05:32:24.278Z'
updated_at: '2025-12-14T05:32:24.278Z'
verified: false
validated: true
submitted: true
---
# curl-access-s3-endpoint

## Command

```bash
curl -I http://gameday.websummit.net.s3-website-eu-west-1.amazonaws.com
```

## Description

Sends a HEAD request to an S3 website endpoint to check for existence without downloading content, revealing errors for non-existent buckets.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-I` | Performs a HEAD request only | Yes |
| `http://...` | The S3 website URL | Yes |

## Examples

### Basic Usage

```bash
curl -I http://gameday.websummit.net.s3-website-eu-west-1.amazonaws.com
```

### Advanced Usage

```bash
curl http://gameday.websummit.net.s3-website-eu-west-1.amazonaws.com
```

## Expected Output

HTTP 404 or XML error body indicating NoSuchBucket.

## Related

- [[Related Procedure]]
