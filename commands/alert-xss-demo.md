---
id: cmd-alert-xss-demo-2024
data: alert('XSS by skavans at ' + document.domain)
tags:
  - xss
  - demo
  - alert
type: command
output: 'Alert box popup with ''XSS by skavans at [domain]'''
executor: javascript
platforms:
  - Web
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-13T23:55:06.470Z'
verified: false
validated: true
submitted: true
---
# alert-xss-demo

## Command

```javascript
alert('XSS by skavans at ' + document.domain)
```

## Description

JavaScript command to display an alert demonstrating XSS execution, including the current domain for proof-of-concept.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| document.domain | Current domain for context | No |

## Examples

### Basic Usage

```javascript
alert('XSS by skavans at ' + document.domain)
```

### Advanced Usage

```javascript
alert('XSS Successful on ' + document.domain + ' - Account Compromised')
```

## Expected Output

Browser alert dialog with message like 'XSS by skavans at chaturbate.com'.

## Related

- [[Related Procedure]]
