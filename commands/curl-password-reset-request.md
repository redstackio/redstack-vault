---
id: cmd-curl-forgot-password
data: >-
  curl -X POST 'http://target:3000/api/v1/users.forgotPassword' -H
  'Content-Type: application/json' -d '{"user":{"email":"target@example.com"}}'
tags:
  - api
  - reset
type: command
output: '{"success": true}'
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:19.889Z'
verified: false
validated: true
submitted: true
---
# curl-password-reset-request

## Command

```bash
curl -X POST 'http://target:3000/api/v1/users.forgotPassword' -H 'Content-Type: application/json' -d '{"user":{"email":"target@example.com"}}'
```

## Description

Sends a manual password reset request using curl to generate the token.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -X POST | HTTP method | Yes |
| URL | Endpoint | Yes |
| -d | JSON payload with email | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'http://target:3000/api/v1/users.forgotPassword' -H 'Content-Type: application/json' -d '{"user":{"email":"target@example.com"}}'
```

## Expected Output

{"success": true, "message": "Email sent"}

## Related

- [[commands/curl-password-reset-submit]]
