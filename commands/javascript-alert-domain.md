---
data: alert(document.domain)
tags:
  - xss
  - proof-of-concept
type: command
executor: javascript
platforms:
  - Web
id: d11abf26-1568-4694-9a61-00ce96117f54
created_at: '2025-12-11T03:47:50.246Z'
updated_at: '2025-12-11T03:47:50.246Z'
verified: false
validated: true
submitted: true
---
# javascript-alert-domain

## Command

```javascript
alert(document.domain)
```

## Description

Displays an alert with the current domain to prove XSS execution on the target site.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `document.domain` | Gets the domain of the page | Yes |

## Examples

### Basic Usage

```javascript
alert(document.domain)
```

## Expected Output

Popup alert showing 'gitlab.com'.

## Related

- [[procedures/Host-Malicious-Script-on-Attacker-Domain]]
- [[procedures/Trigger-and-Verify-XSS-Execution]]
