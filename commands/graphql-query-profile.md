---
id: cmd-graphql-query-profile-001
data: >-
  curl -X POST https://entry.line.me/graphql -H "Content-Type: application/json"
  -H "Authorization: Bearer YOUR_TOKEN" -d '{"query": "query { user(id:
  \"TARGET_USER_ID\") { profileImage { id } } }"}'
tags:
  - graphql
  - verification
type: command
output: JSON user profile details
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:53.097Z'
verified: false
validated: true
submitted: true
---
# graphql-query-profile

## Command

```bash
curl -X POST https://entry.line.me/graphql \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -d '{"query": "query { user(id: \"TARGET_USER_ID\") { profileImage { id } } }"}'
```

## Description

This command queries a user's profile via GraphQL to verify image details, useful for post-exploitation validation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | HTTP POST | Yes |
| `-H "Content-Type: application/json"` | JSON type | Yes |
| `-H "Authorization: Bearer YOUR_TOKEN"` | Auth token | Yes |
| `-d '{...}'` | Query payload with user ID | Yes |
| `user(id)` | Target user identifier | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://entry.line.me/graphql -H "Content-Type: application/json" -H "Authorization: Bearer YOUR_TOKEN" -d '{"query": "query { user(id: \"user_789\") { profileImage { id } } }"}'
```

### Advanced Usage

Query multiple fields:

```bash
curl -X POST https://entry.line.me/graphql -H "Content-Type: application/json" -H "Authorization: Bearer YOUR_TOKEN" -d '{"query": "query { user(id: \"TARGET_ID\") { id name profileImage { id url } } }"}'
```

## Expected Output

JSON like {"data": {"user": {"profileImage": null } } } if deleted, or with image details if present.

## Related

- [[commands/graphql-delete-image]]
- [[procedures/Exploit-IDOR-to-Delete-Profile-Image]]
