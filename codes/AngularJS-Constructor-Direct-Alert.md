---
type: code
language: JavaScript
verified: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
tags:
  - xss
  - angularjs
  - payload
platforms:
  - Web
validated: true
---

# AngularJS-Constructor-Direct-Alert

## Code

```javascript
{{constructor.constructor('alert(1)')()}}
```

## Description

This payload exploits client-side template injection in AngularJS by directly accessing the global constructor function to create and execute a new function that triggers an alert(1). It is effective against basic unsandboxed expressions in early AngularJS versions.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | The payload is self-contained; replace 'alert(1)' with custom JavaScript for advanced exploitation. | N/A |

## Usage

Inject into vulnerable AngularJS template fields (e.g., {{input}}) via form submission or URL parameters for reflected XSS. For stored XSS, submit to persistent inputs like comments. Use browser dev tools to test in isolated environments.

## Detection

- Monitor for inline JavaScript execution in CSP logs.
- Browser console errors or network requests to external scripts post-injection.
- WAF rules matching constructor or alert patterns in inputs.

## Related

- [[procedures/Angular-AngularJS-Stored-Reflected-XSS-Simple-Alert]]
