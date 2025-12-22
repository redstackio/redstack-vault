---
type: code
language: javascript
verified: true
created_at: '2023-04-06T03:56:42Z'
updated_at: '2023-04-10T20:21:41Z'
platforms:
  - Web
tags:
  - xss
  - obfuscation
  - bracket-notation
validated: true
---

# JavaScript-Alert-Document-Domain-Bracket-Notation

## Code

```javascript
<script>window['alert'](document['domain'])</script>
```

## Description

This JavaScript snippet uses bracket notation to access window.alert and document.domain, bypassing filters that scan for dotted property access like .alert or .domain. When injected via XSS, it triggers an alert displaying the current webpage's domain, confirming code execution.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| (None) | Hardcoded payload; customize by replacing 'domain' with other properties if needed | N/A |

## Usage

Inject into vulnerable inputs like URL parameters (?q=<payload>) or form fields in reflected/stored XSS scenarios. Test in browser console first. Ideal for initial XSS confirmation in filtered environments.

## Detection

- WAF rules matching bracket notation patterns (e.g., ['alert'], ['domain']).\n- Browser dev tools showing unexpected alerts or console errors from malformed <script> tags.\n- CSP violations if script execution is restricted.\n
## Related

- [[procedures/XSS-Dot-Filter-Bypass-Using-Exotic-Payloads]]
