---
id: cmd-834366-session-check
name: hackerone-session-check
type: command
executor: http
data: |-
  GET /current_user.json HTTP/1.1
  Cookie: session=:session;
  ...
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:57.545Z'
platforms:
  - Web
tags:
  - session
  - verification
verified: false
validated: true
submitted: true
---

# hackerone-session-check

## Command

```http
GET /current_user.json HTTP/1.1
Host: hackerone.com
Cookie: session=extracted_session_value;
```

## Description

Verifies if a session from a login attempt (e.g., with invalid token) is authenticated.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Cookie: session | Session ID from login response | Yes |

## Examples

### Basic Usage

```bash
curl -H 'Cookie: session=abc123' https://hackerone.com/current_user.json
```

## Expected Output

HTTP 200 OK: {"csrf_token":":token","signed_in?":false,"is_member_of_teams":false}

## Related

- [[procedures/Bypass-HackerOne-Login-CSRF-Token]]
