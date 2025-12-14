---
id: curl-login-001
data: >-
  curl -X POST 'https://merchant.rbmonkey.com/api/auth/login' -H 'Content-Type:
  application/json' -d '{"username": "testuser", "password": "testpass"}'
tags:
  - authentication
  - web
  - api
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:29.060Z'
verified: false
validated: true
submitted: true
---
# curl-login-merchant

## Command

```bash
curl -X POST 'https://merchant.rbmonkey.com/api/auth/login' \
  -H 'Content-Type: application/json' \
  -d '{"username": "testuser", "password": "testpass"}'
```

## Description

This command authenticates to the RBKmoney merchant portal API by sending a POST request with username and password credentials, retrieving an authorization token for subsequent API calls.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method | Yes |
| `https://merchant.rbmonkey.com/api/auth/login` | Login endpoint URL | Yes |
| `-H 'Content-Type: application/json'` | Sets JSON content type header | Yes |
| `-d '{"username": "...", "password": "..."}'` | JSON payload with credentials | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://merchant.rbmonkey.com/api/auth/login' -H 'Content-Type: application/json' -d '{"username": "testuser", "password": "testpass"}'
```

### Advanced Usage

```bash
curl -X POST 'https://merchant.rbmonkey.com/api/auth/login' -H 'Content-Type: application/json' -d '{"username": "testuser", "password": "testpass"}' -v
```

## Expected Output

JSON response with token: {"token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...", "user_id": 123}

## Related

- [[commands/curl-verify-auth]]
- [[procedures/Authenticate-to-Merchant-Portal]]
