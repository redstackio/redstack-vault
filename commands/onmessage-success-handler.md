---
id: 123e4567-e89b-12d3-a456-426614174007
name: onmessage-success-handler
type: command
executor: javascript
data: >-
  window.onmessage=(e)=>{ e.data==="success"&&( console.log('attack success'),
  window.onmessage=null, clearInterval(interval) ); };
output: Console log 'attack success' and cleanup on receiving 'success'.
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:55:06.689Z'
platforms:
  - Web
tags:
  - xss
  - handler
verified: false
validated: true
submitted: true
---

# onmessage-success-handler

## Command

```javascript
window.onmessage=(e)=>{ e.data==="success"&&( console.log('attack success'), window.onmessage=null, clearInterval(interval) ); };
```

## Description

Attaches an event listener to the window for incoming messages, checking for 'success' to log confirmation, remove the listener, and stop the interval in the XSS exploit flow.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| e.data | Checks for 'success' string in message data | Yes |

## Examples

### Basic Usage

```javascript
window.onmessage = (e) => { if (e.data === 'success') console.log('done'); };
```

### Advanced Usage

```javascript
window.onmessage = (e) => { if (e.data === 'success') { console.log('attack success'); clearInterval(interval); } };
```

## Expected Output

Console: 'attack success'; interval cleared; listener removed.

## Related

- [[Related Procedure|procedures/Trigger-XSS-by-Visiting-and-Clicking-Link]]
