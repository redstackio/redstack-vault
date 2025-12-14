---
data: 'window.addEventListener("message",this.handleMessage)'
tags:
  - xss
  - postmessage
  - event-listener
type: command
executor: javascript
platforms:
  - Web
id: 1af81b71-837f-415e-a559-80ce7a88b52d
created_at: '2025-12-14T03:16:02.497Z'
updated_at: '2025-12-14T03:16:02.497Z'
verified: false
validated: true
submitted: true
---
# add-message-event-listener

## Command

```javascript
window.addEventListener("message",this.handleMessage)
```

## Description

This JavaScript command adds an event listener for 'message' events to the window object, typically used in React components like the Polaris demo's Demo component to receive postMessages and update state via handleMessage. In the vulnerability context, it lacks origin validation, allowing malicious payloads from any source.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| "message" | The event type to listen for (postMessage events) | Yes |
| this.handleMessage | The callback function to process the event data | Yes |

## Examples

### Basic Usage

```javascript
window.addEventListener("message", function(e) { console.log(e.data); });
```

### Advanced Usage

```javascript
window.addEventListener("message", this.handleMessage, false);
```

## Expected Output

Listens silently for postMessage events; no visible output unless the handler logs or alerts. In the demo, it processes {ast: {code: ...}} and sets React state, potentially rendering injected content.

## Related

- [[Related Procedure]]
