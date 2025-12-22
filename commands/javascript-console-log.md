---
id: 3f61100d-f8d2-4709-b1f2-89d5731407f0
name: javascript-console-log
type: command
executor: javascript
data: console.log('XSS Test Successful')
output: null
created_at: '2023-04-06T03:56:41.759303+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Web
tags:
  - xss
  - stealth-testing
verified: true
validated: true
---

# javascript-console-log

## Command

```javascript
console.log('XSS Test Successful')
```

## Description

This command logs a message to the browser's developer console, ideal for stealthy XSS verification without visible popups, useful in stored XSS scenarios.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Message String | The data to log (e.g., 'XSS Test Successful') | Yes |

## Examples

### Basic Usage

```javascript
console.log('XSS Test Successful')
```

### Advanced Usage

```javascript
console.log(document.domain + ' - ' + window.origin)
```

## Expected Output

Message appears in the browser console (F12 > Console tab), e.g., 'XSS Test Successful', without user notification.

## Related

- [[procedures/Identify-and-Exploit-XSS-Vulnerabilities]]
