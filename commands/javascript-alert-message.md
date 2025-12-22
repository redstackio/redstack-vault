---
id: a88b794b-c395-407e-8046-b27f1de61b8f
name: javascript-alert-message
type: command
executor: javascript
data: alert('XSS Test')
output: null
created_at: '2023-04-06T03:56:41.759214+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Web
tags:
  - xss
  - testing
verified: true
validated: true
---

# javascript-alert-message

## Command

```javascript
alert('XSS Test')
```

## Description

This JavaScript command displays a popup alert box with a message, used to test for XSS execution in the browser context without requiring additional parameters.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Message String | The text to display in the alert (e.g., 'XSS Test') | Yes |

## Examples

### Basic Usage

```javascript
alert('XSS Test')
```

### Advanced Usage

```javascript
alert(document.cookie)
```

## Expected Output

A browser popup alert box appears with the specified message, confirming JavaScript execution. For example: Alert box showing 'XSS Test'.

## Related

- [[procedures/Identify-and-Exploit-XSS-Vulnerabilities]]
