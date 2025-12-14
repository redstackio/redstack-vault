---
data: >-
  curl -X GET -H "X-Auth-Token: ADMIN_AUTH_TOKEN" -H "X-User-Id: ADMIN_USER_ID"
  https://rocket-chat.example.com/api/v1/channels.messages?roomId=TARGET_ROOM_ID&count=50
tags:
  - api
  - rocket.chat
  - verification
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:47.377Z'
id: 6725deb0-c46b-40ec-973d-b4f21a8fb56f
verified: false
validated: true
submitted: true
---
# curl-getmessages-rocket-chat

## Command

```bash
curl -X GET -H "X-Auth-Token: ADMIN_AUTH_TOKEN" -H "X-User-Id: ADMIN_USER_ID" https://rocket-chat.example.com/api/v1/channels.messages?roomId=TARGET_ROOM_ID&count=50
```

## Description

Retrieves recent messages from a Rocket.Chat channel for verification purposes.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `roomId` | Target room ID | Yes |
| `count` | Number of messages | No (default 20) |

## Examples

### Basic Usage

```bash
curl -X GET -H "X-Auth-Token: abc" ... https://chat.example.com/api/v1/channels.messages?roomId=room789&count=50
```

## Expected Output

JSON array of messages; check for absence of target ID.

## Related

- [[procedures/Verify-Message-Deletion-in-Rocket.Chat]]
