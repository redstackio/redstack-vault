---
id: c5h6i7j8-k9l0-1235-ghij-901234567890
data: >-
  curl -X POST https://target/api/v1/login -d '{"user": "$USERNAME", "password":
  "$PASSWORD"}'
tags:
  - api
  - auth
type: command
output: Auth tokens and user ID.
executor: bash
platforms:
  - Web
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:33:24.533Z'
verified: false
validated: true
submitted: true
---
# rocket-chat-login

## Command

```bash
curl -X POST https://target/api/v1/login -d '{"user": "$USERNAME", "password": "$PASSWORD"}'
```

## Description

Authenticates to Rocket.Chat via LDAP or local creds, returning session tokens.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `{"user": "$USERNAME"}` | Username or email | Yes |
| `{"password": "$PASSWORD"}` | Password | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://target/api/v1/login -d '{"user": "attacker@ldap", "password": "pass123"}'
```

## Expected Output

JSON: {"data": {"authToken": "abc123", "userId": "user456"}}

## Related

- [[commands/curl-users-list]]
