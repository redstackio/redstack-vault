---
type: code
language: html
verified: true
created_at: '2023-04-06T03:56:43.367790+00:00'
updated_at: '2023-04-10T20:21:30.901305+00:00'
platforms:
  - Web
tags:
  - xss
  - payload
  - waf-bypass
  - cloudflare
validated: true
---

# xss-bypass-payload-img-onerror

## Code

```html
1'"><img/src/onerror=.1|alert``>
```

## Description

This HTML snippet is an obfuscated XSS payload designed to bypass common WAF filters, including Cloudflare's, by using a malformed img tag with an onerror event handler that executes JavaScript via alert(). The pipe (|) and backticks (``) help evade signature-based detection. It injects into reflected inputs to trigger execution when the page loads in a victim's browser.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | This is a static payload; customize the alert() content for specific actions like cookie exfiltration (e.g., replace alert`` with alert(document.cookie)) | N/A |

## Usage

Inject this payload into vulnerable input fields (e.g., search parameters, forms) on Cloudflare-protected sites. Use tools like curl or Burp Suite to submit it via POST/GET requests. Once reflected and rendered, it executes in the browser context, ideal for reflected XSS. For stored XSS, submit to persistent fields like comments.

## Detection

- WAF logs showing blocked or allowed suspicious strings like 'onerror' or 'alert'.
- Browser console errors from failed img src loads triggering onerror.
- Client-side CSP violations if policy blocks inline events.
- Network monitoring for unexpected JavaScript execution or beacons to external domains.

## Related

- [[procedures/Cloudflare-XSS-Bypass-via-Common-WAF-and-HTML-Injection]]
