---
id: cmd-uuid-2
data: alert('Shell')
tags:
  - javascript
  - test
type: command
output: null
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:52:43.719Z'
verified: false
validated: true
submitted: true
---
# javascript-alert-shell-test

## Command

```javascript
alert('Shell')
```

## Description

A simple JavaScript alert sent via the XSS shell to test and demonstrate arbitrary code execution in the victim's browser.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `alert` | JS function to show message box | Yes |
| `'Shell'` | Message displayed | Yes |

## Examples

### Basic Usage

```javascript
alert('Shell')
```

### Advanced Usage

```javascript
alert(document.cookie)
```

## Expected Output

A popup alert box in the victim's browser saying 'Shell'.

## Related

- [[Related Procedure: Establish-and-Interact-with-XSS-Shell]]
