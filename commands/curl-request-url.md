---
data: 'curl -v https://security.olx.com/*'
tags:
  - recon
  - http
  - s3
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 03f2ffb9-b5ee-49be-8868-ab0398149a84
created_at: '2025-12-14T17:26:11.919Z'
updated_at: '2025-12-14T17:26:11.919Z'
verified: false
validated: true
submitted: true
---
# curl-request-url

## Command

```bash
curl -v https://security.olx.com/*
```

## Description

This command uses curl to send a verbose HTTP GET request to a target URL with a wildcard path, designed to trigger and capture S3 'NoSuchKey' error responses for misconfiguration detection.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-v` | Enables verbose mode to show request/response headers and details | Yes |
| `https://security.olx.com/*` | The target URL with wildcard path to request non-existent S3 key | Yes |

## Examples

### Basic Usage

```bash
curl -v https://security.olx.com/*
```

### Advanced Usage

```bash
curl -v -H "User-Agent: Mozilla/5.0" https://security.olx.com/* | grep -i error
```

## Expected Output

A response including HTTP 404 status, XML-formatted error like:

```
<Error><Code>NoSuchKey</Code><Message>The specified key does not exist.</Message><RequestId>ABC123</RequestId><HostId>XYZ789</HostId></Error>
```
This discloses S3 backend usage and metadata IDs.

## Related

- [[Related Procedure: Detect-S3-Bucket-Misconfiguration-via-Wildcard-Key-Request]]
