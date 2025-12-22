---
id: cmd-uuid-2
data: >-
  curl -X POST https://hackerone.com/graphql -H "Content-Type: application/json"
  -d '{"query":"{ user(username: \"jobert\") {
  soft_launch_invitations(first:100, state:open) { total_count } } }"}'
tags:
  - graphql
  - api
  - verification
type: command
output: '{"data": {"user": {"soft_launch_invitations": {"total_count": 0}}}}'
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:35.093Z'
verified: false
validated: true
submitted: true
---
# graphql-verify-fix-invitations

## Command

```bash
curl -X POST https://hackerone.com/graphql -H "Content-Type: application/json" -d '{"query":"{ user(username: \"jobert\") { soft_launch_invitations(first:100, state:open) { total_count } } }"}'
```

## Description

This command sends a simplified GraphQL query to verify that authorization fixes have been applied, checking the total_count of open soft_launch_invitations for a target user, which should now return 0 for unauthorized access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies HTTP POST method | Yes |
| `-H "Content-Type: application/json"` | Sets JSON content type header | Yes |
| `-d '{...}'` | JSON payload with simplified query | Yes |
| `username` | Target username (e.g., "jobert") | Yes |
| `first` | Pagination limit (e.g., 100) | Yes |
| `state` | Invitation state filter (e.g., "open") | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://hackerone.com/graphql -H "Content-Type: application/json" -d '{...}'
```

### Advanced Usage

Change the state parameter to other values like "accepted" to test different filters post-fix.

## Expected Output

JSON response showing total_count: 0, e.g., {"data":{"user":{"soft_launch_invitations":{"total_count":0}}}}, confirming the vulnerability is resolved.

## Related

- [[procedures/Query-User-Private-Invitations-via-GraphQL]]
