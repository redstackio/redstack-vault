---
data: >-
  curl -X POST -H "X-Auth-Token: YOUR_AUTH_TOKEN" -H "X-User-Id: YOUR_USER_ID"
  -H "Content-Type: application/json"
  https://rocket-chat.example.com/api/v1/method.call -d
  '{"msg":"method","method":"sendMessage","params":[{"rid":"TARGET_ROOM_ID","msg":"Test
  message for ID capture"}],"id":"unique_id_1"}'
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
updated_at: '2025-12-14T17:25:47.390Z'
id: 08902d85-bf87-4278-b0ba-27d47778a49b
verified: false
validated: true
submitted: true
---
# curl-sendmessage-rocket-chat

## Command

```bash
curl -X POST -H "X-Auth-Token: YOUR_AUTH_TOKEN" -H "X-User-Id: YOUR_USER_ID" -H "Content-Type: application/json" https://rocket-chat.example.com/api/v1/method.call -d '{"msg":"method","method":"sendMessage","params":[{"rid":"TARGET_ROOM_ID","msg":"Test message for ID capture"}],"id":"unique_id_1"}'
```

## Description

Sends a message to a Rocket.Chat channel via the API and returns the message ID in the response. Used for capturing object references in IDOR attacks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | HTTP method | Yes |
| `-H "X-Auth-Token: ..."` | Authentication token | Yes |
| `-H "X-User-Id: ..."` | User ID | Yes |
| `-d '...'` | JSON payload with method and params | Yes |
| `rid` in params | Target room ID | Yes |
| `msg` in params | Message text | Yes |

## Examples

### Basic Usage

```bash
curl -X POST -H "X-Auth-Token: abc123" -H "X-User-Id: user456" -H "Content-Type: application/json" https://chat.example.com/api/v1/method.call -d '{"msg":"method","method":"sendMessage","params":[{"rid":"room789","msg":"Hello"}],"id":"id1"}'
```

### Advanced Usage

Add more params like attachments if needed.

## Expected Output

JSON: {"msg": "result", "result": {"_id": "CZZqd6rMsiqbsqa9h", ...}}

## Related

- [[commands/curl-deletemessage-rocket-chat]]
- [[procedures/Capture-Message-ID-via-SendMessage-API-in-Rocket.Chat]]
