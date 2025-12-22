---
id: 60a609e2-461f-4bf5-bc3f-02120553d951
name: javascript-alert-window-origin
type: command
executor: javascript
data: alert(window.origin)
output: null
created_at: '2023-04-06T03:56:41.758818+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Web
tags:
  - xss
  - context-verification
verified: true
validated: true
---

# javascript-alert-window-origin

## Command

```javascript
alert(window.origin)
```

## Description

This command alerts the origin of the current window (protocol + host + port), helping verify the execution context in XSS testing to ensure it's running in the target's domain.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| window.origin | Built-in property accessing the origin | No (built-in) |

## Examples

### Basic Usage

```javascript
alert(window.origin)
```

### Advanced Usage

```javascript
alert('Origin: ' + window.origin)
```

## Expected Output

Alert box displaying the origin, e.g., 'https://example.com:443', confirming the script's access level.

## Related

- [[procedures/Identify-and-Exploit-XSS-Vulnerabilities]]
