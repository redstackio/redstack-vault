---
data: 'curl -vv http://podcasts.slack-core.com'
tags:
  - http
  - verification
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T04:51:10.697Z'
id: ea9b7532-3038-4a74-ba78-5f3604ed791e
verified: false
validated: true
submitted: true
---
# curl-verbose-http-request

## Command

```bash
curl -vv http://podcasts.slack-core.com
```

## Description

Sends a verbose HTTP GET request to the subdomain to fetch the root page and inspect headers/response, verifying custom redirects post-takeover.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -vv | Verbose output showing connection details | Yes |
| http://podcasts.slack-core.com | Target URL for GET request | Yes |

## Examples

### Basic Usage

```bash
curl -vv http://podcasts.slack-core.com
```

### Advanced Usage

```bash
curl -vv -L http://podcasts.slack-core.com
```

## Expected Output

HTTP/1.1 301 Moved Permanently with Location: https://hackerone.com, served by nginx on IP 5.135.16.40.

## Related

- [[Related Procedure: Verify-Subdomain-Takeover-Control]]
