---
id: 25547e34-dd8f-4cbc-a8a1-4d156c682785
name: SVG-Onload-Alert-XSS-Payload
type: code
language: HTML
verified: true
created_at: '2023-04-06T03:56:43.345357+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Web
tags:
  - xss
  - payload
  - cloudflare-bypass
  - svg
validated: true
---

# SVG-Onload-Alert-XSS-Payload

## Code

```html
<svg/onload=%26nbsp;alert`bohdan`+
```

## Description

This HTML snippet is an XSS payload using an SVG element's onload attribute to execute JavaScript. The %26nbsp; encoding (for &nbsp;) helps bypass Cloudflare WAF filters that block direct <svg onload=alert()> patterns. When injected into a reflected context and rendered by the browser, it triggers an alert with the message 'bohdan'. This can be adapted for more malicious actions like data exfiltration.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| `bohdan` | The string displayed in the alert; replace with JS code like document.cookie for theft | `test` or `document.domain` |

## Usage

Inject this payload into vulnerable parameters (e.g., search fields) on Cloudflare-protected sites with reflected XSS. URL-encode if necessary (e.g., via --data-urlencode in curl). Test in a browser to confirm execution. Used in procedures like [[procedures/Cloudflare-XSS-Bypass-via-SVG-Onload-Alert]] for WAF evasion during client-side attacks.

## Detection

- WAF logs showing SVG tags or onload attributes in requests.
- Browser CSP violations or script execution logs.
- Client-side monitoring for unexpected alerts or network requests from onload events.
- Static analysis of reflected inputs for encoded entities like %26nbsp;.

## Related

- [[procedures/Cloudflare-XSS-Bypass-via-SVG-Onload-Alert]]
- [[tools/Burp-Suite]]
