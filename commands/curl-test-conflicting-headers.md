---
data: >-
  curl -v -X POST -H "Transfer-Encoding: chunked" -H "Content-Length: 100" -d
  "0\r\n\r\nSMUGGLED_PAYLOAD" http://example.com/test
tags:
  - http-smuggling
type: command
executor: bash
platforms:
  - Linux
  - Windows
id: 8ddaae37-da3a-43be-9395-82978a7849cc
created_at: '2025-12-13T09:01:21.759Z'
updated_at: '2025-12-13T09:01:21.759Z'
verified: false
validated: true
submitted: true
---
# curl-test-conflicting-headers

## Command

```bash
curl -v -X POST -H "Transfer-Encoding: chunked" -H "Content-Length: 100" -d "0\r\n\r\nSMUGGLED_PAYLOAD" http://example.com/test
```

## Description

Sends a POST request with conflicting headers to test if cURL allows both, including a smuggled payload.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-v` | Verbose output | Yes |
| `-X POST` | Specify POST method | Yes |
| `-H "Transfer-Encoding: chunked"` | Set Transfer-Encoding header | Yes |
| `-H "Content-Length: 100"` | Set Content-Length header | Yes |
| `-d "0\r\n\r\nSMUGGLED_PAYLOAD"` | Data payload with chunked ending and smuggled content | Yes |

## Examples

### Basic Usage

```bash
curl -v -X POST -H "Transfer-Encoding: chunked" -H "Content-Length: 100" -d "0\r\n\r\nSMUGGLED_PAYLOAD" http://example.com/test
```

## Expected Output

HTTP request sent with both headers, verbose output showing headers and response.

## Related

- [[procedures/Create-Test-Request-with-Conflicting-Headers]]
- [[procedures/Observe-cURL-Header-Behavior]]
