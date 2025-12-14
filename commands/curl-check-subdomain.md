---
id: cmd-uuid-7890
data: 'curl -v http://s3.websummit.net/'
tags:
  - recon
  - http-probe
type: command
output: >-
  HTTP/1.1 404 Not Found

  <xml version="1.0" encoding="UTF-8"?>

  <Error><Code>NoSuchBucket</Code><Message>The specified bucket does not
  exist</Message><BucketName>s3.websummit.net</BucketName>...</Error>
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T05:32:23.666Z'
verified: false
validated: true
submitted: true
---
# curl-check-subdomain

## Command

```bash
curl -v http://s3.websummit.net/
```

## Description

This command performs a verbose HTTP HEAD or GET request to a target subdomain to detect AWS S3 errors indicating a dangling bucket, useful for subdomain takeover reconnaissance.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-v` | Verbose output showing headers and response | Yes |
| `http://subdomain` | Target URL to probe | Yes |

## Examples

### Basic Usage

```bash
curl -v http://s3.example.com/
```

### Advanced Usage

```bash
curl -v -H "Host: s3.websummit.net" http://dws-content.s3-website-eu-west-1.amazonaws.com/
```

## Expected Output

Verbose logs with 404 status, followed by XML error: <Code>NoSuchBucket</Code>, confirming the bucket is available for takeover.

## Related

- [[Related Procedure: Detect-Dangling-S3-Bucket-Via-DNS]]
