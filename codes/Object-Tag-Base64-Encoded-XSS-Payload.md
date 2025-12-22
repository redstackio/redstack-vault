---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
name: Object-Tag-Base64-Encoded-XSS-Payload
type: code
language: html
verified: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
tags:
  - xss
  - waf-bypass
  - payload
platforms:
  - Web
validated: true
---

# Object-Tag-Base64-Encoded-XSS-Payload

## Code

```html
<object data='data:text/html;;;;;base64,PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg=='></object>
```

## Description

This HTML code snippet uses an 'object' tag to embed a Base64-encoded data URI containing malicious HTML/script. When injected into a vulnerable web application, it bypasses WAFs that do not decode Base64, allowing the browser to render and execute the XSS payload (here, alert(1)). The multiple semicolons in the data URI enhance evasion against strict parsers.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| Base64 Payload | The Base64-encoded HTML/script to execute (replace the fixed string) | PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg== (encodes to <script>alert(1)</script>) |

## Usage

Embed this snippet directly into user-controlled inputs like search queries, form fields, or URL parameters in applications vulnerable to reflected/stored XSS. For testing, append to a URL (e.g., ?input=<object...>) and load in a browser. Customize the Base64 for advanced payloads, such as document.cookie exfiltration to an attacker server. Used in red team engagements to test WAF efficacy against encoding evasions.

## Detection

- WAF logs showing unblocked 'object' tags with data URIs.
- Browser CSP violations or console errors from unauthorized script execution.
- Network monitoring for anomalous data URI requests or Base64 patterns in payloads.
- Client-side scanning for decoded content revealing <script> tags.

## Related

- [[procedures/Base64-Encoded-HTML-Data-URI-WAF-Bypass-for-XSS]]
