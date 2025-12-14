---
id: c4g5h6i7-j8k9-0124-fghi-890123456789
data: >-
  curl -X POST https://target/api/v1/resetPassword -H "Content-Type:
  application/json" -d '{"token": "$RESET_HASH", "newPassword": "$NEW_PASS"}'
tags:
  - api
  - takeover
type: command
output: Password reset success.
executor: bash
platforms:
  - Web
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:33:24.535Z'
verified: false
validated: true
submitted: true
---
# curl-reset-password

## Command

```bash
curl -X POST https://target/api/v1/resetPassword -H "Content-Type: application/json" -d '{"token": "$RESET_HASH", "newPassword": "$NEW_PASS"}'
```

## Description

Completes password reset using the hash token in Rocket.Chat.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `{"token": "$RESET_HASH"}` | Reset hash | Yes |
| `{"newPassword": "$NEW_PASS"}` | New password | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://target/api/v1/resetPassword -H "Content-Type: application/json" -d '{"token": "abcDEF123", "newPassword": "NewPass123"}'
```

## Expected Output

JSON: {"success": true}

## Related

- [[commands/curl-forgot-password]]
