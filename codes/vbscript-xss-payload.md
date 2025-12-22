---
type: code
language: javascript
verified: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Web
  - Browser
tags:
  - xss
  - vbscript
  - injection
validated: true
---

# vbscript-xss-payload

## Code

```javascript
vbscript:msgbox("XSS")
```

## Description

This payload uses the vbscript: protocol to execute a message box in Internet Explorer, simulating XSS execution. It leverages IE's support for VBScript handlers, which may not be filtered like javascript:.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| N/A | No variables; replace msgbox content for custom actions (e.g., steal cookies via VBScript) | msgbox(document.cookie) |

## Usage

Inject into href or event handlers in IE-targeted tests. Use Burp Suite to place in links; a msgbox confirms execution. Targeted at legacy environments for compatibility testing.

## Detection

- IE-specific logs for VBScript execution.
- Filters blocking vbscript: protocols.
- Absence in modern browsers (Chrome/Firefox) limits scope.

## Related

- [[procedures/xss-injection-via-javascript-data-uri-vbscript]]
