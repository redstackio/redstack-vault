---
data: >-
  curl -X POST -H "X-Auth-Token: YOUR_AUTH_TOKEN" -H "X-User-Id: YOUR_USER_ID"
  -H "Content-Type: application/json"
  https://rocket-chat.example.com/api/v1/method.call -d
  '{"msg":"method","method":"leaveRoom","params":[{"rid":"TARGET_ROOM_ID"}],"id":"unique_id_2"}'
tags:
  - api
  - rocket.chat
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:47.387Z'
id: 64369c1f-5aea-496b-b8ad-1f28d37b45fe
verified: false
validated: true
submitted: true
---
# curl-leavechannel-rocket-chat

## Command

```bash
curl -X POST -H "X-Auth-Token: YOUR_AUTH_TOKEN" -H "X-User-Id: YOUR_USER_ID" -H "Content-Type: application/json" https://rocket-chat.example.com/api/v1/method.call -d '{"msg":"method","method":"leaveRoom","params":[{"rid":"TARGET_ROOM_ID"}],"id":"unique_id_2"}'
```

## Description

Leaves a Rocket.Chat channel using the leaveRoom method, removing user membership.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-d '...'` | JSON with leaveRoom params | Yes |
| `rid` | Room ID to leave | Yes |

## Examples

### Basic Usage

```bash
curl -X POST -H "X-Auth-Token: abc123" ... -d '{"msg":"method","method":"leaveRoom","params":[{"rid":"room789"}],"id":"id2"}'
```

## Expected Output

{"success": true}

## Related

- [[procedures/Leave-Rocket.Chat-Channel]]
