---
id: cmd-curl-authenticate-enjin
data: >-
  curl -X POST 'https://platform.enjin.io/api/login' -H 'Content-Type:
  application/json' -d '{"email":"your@email.com","password":"yourpass"}'
tags:
  - auth
  - web
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:22.479Z'
verified: false
validated: true
submitted: true
---
# curl-authenticate-enjin

## Command

```bash
curl -X POST 'https://platform.enjin.io/api/login' -H 'Content-Type: application/json' -d '{"email":"your@email.com","password":"yourpass"}'
```

## Description

Authenticates to the Enjin platform API to obtain a bearer token for subsequent authenticated requests, such as invitations.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| your@email.com | User email | Yes |
| yourpass | User password | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://platform.enjin.io/api/login' -H 'Content-Type: application/json' -d '{"email":"user@example.com","password":"pass123"}'
```

### Advanced Usage

```bash
curl -X POST 'https://platform.enjin.io/api/login' -H 'Content-Type: application/json' -d '{"email":"user@example.com","password":"pass123"}' -c cookies.txt
```

## Expected Output

JSON response: {"token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...", "user_id": 123}.

## Related

- [[Related Procedure|procedures/Exploit-Enjin-Invitation-Race-Condition]]
