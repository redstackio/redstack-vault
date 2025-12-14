---
id: cmd-message-listener-900619
data: >-
  window.addEventListener("message",(msg)=>{ console.log("got message", msg);
  alert(msg.data); });
tags:
  - event-listener
  - postmessage-receive
type: command
output: Console log and alert of received message data
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:55:20.991Z'
verified: false
validated: true
submitted: true
---
# setup-message-event-listener

## Command

```javascript
window.addEventListener("message",(msg)=>{ console.log("got message", msg); alert(msg.data); });
```

## Description

Sets up an event listener on the window for 'message' events from postMessage, logging and alerting the received data for exfiltrated token capture.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| event | "message" for postMessage events | Yes |
| handler | Callback to log/alert data | Yes |

## Examples

### Basic Usage

```javascript
window.addEventListener("message",(msg)=> console.log(msg.data));
```

### Advanced Usage

Include alert for immediate visibility as shown.

## Expected Output

Triggers on incoming messages, showing data in console/alert.

## Related

- [[Related Procedure]]
