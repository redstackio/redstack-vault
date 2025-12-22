---
id: d62a8867-d4ed-47c3-8e6d-a48cb41bf64d
type: code
language: JavaScript
verified: true
created_at: '2023-04-06T03:56:42.768240+00:00'
updated_at: '2023-04-10T20:21:46.075934+00:00'
tags:
  - xss
  - obfuscation
  - global-scope
platforms:
  - Web
  - Browser
validated: true
---

# Find-Alert-Function-Index-in-Global-Scope

## Code

```javascript
c=0; for(i in self) { if(i == "alert") { console.log(c); } c++; }
// 5
```

## Description

This snippet iterates over the global scope (self) to count properties and log the index of the 'alert' function, enabling index-based access for obfuscation in XSS payloads.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| N/A | No variables; outputs index to console | N/A |

## Usage

Run in browser console to determine the alert index (often 5), then use in subsequent obfuscated calls to avoid naming 'alert' directly.

## Detection

- Console logging of numeric indices during enumeration.
- Behavioral analysis for loops over global objects in scripts.

## Related

- [[procedures/Bypass-XSS-Alert-Filter-Using-Alternate-Functions]]
