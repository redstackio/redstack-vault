---
id: cmd-837328-form-update-basic
data: >-
  ws.send(JSON.stringify({type: 'form-update', element: '#algo-id', value:
  'hello', clientId: 'x', roomId: '5ce6e50b298f7c6e0acb68c6'}));
tags:
  - websocket
  - testing
type: command
output: null
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:27.994Z'
verified: false
validated: true
submitted: true
---
# websocket-form-update-basic

## Command

```javascript
ws.send(JSON.stringify({
  type: 'form-update',
  element: '#algo-id',
  value: 'hello',
  clientId: 'x',
  roomId: '5ce6e50b298f7c6e0acb68c6'
}));
```

## Description

Sends a basic WebSocket payload to update the #algo-id element's value to 'hello' in a Quantopian collaboration room, demonstrating arbitrary DOM manipulation for fuzzing or testing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| type | Event type for form updates | Yes |
| element | CSS selector of target element | Yes |
| value | New value to set | Yes |
| clientId | Client identifier | Yes |
| roomId | Collaboration room ID | Yes |

## Examples

### Basic Usage

```javascript
ws.send(JSON.stringify({type: 'form-update', element: '#algo-id', value: 'hello', clientId: 'x', roomId: '5ce6e50b298f7c6e0acb68c6'}));
```

### Advanced Usage

Use in a full connection script:

```javascript
const ws = new WebSocket('wss://quantopian.com/ws/room/5ce6e50b298f7c6e0acb68c6');
ws.onopen = () => { /* send above */ };
```

## Expected Output

The #algo-id input field updates to 'hello' across all connected clients in the room; no console errors.

## Related

- [[commands/websocket-form-update-preferences]]
- [[procedures/Send-Malicious-WebSocket-Form-Update]]
