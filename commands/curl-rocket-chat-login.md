---
data: >-
  curl http://127.0.0.1:3000/api/v1/login -d
  "username=<USER_NAME>&password=<PASSWORD>"
tags:
  - authentication
  - api
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 0c4693c2-006d-4769-81dc-ee4c1d9fc860
created_at: '2025-12-13T23:55:06.261Z'
updated_at: '2025-12-13T23:55:06.261Z'
verified: false
validated: true
submitted: true
---
# curl-rocket-chat-login

## Command

```bash
curl http://127.0.0.1:3000/api/v1/login -d "username=<USER_NAME>&password=<PASSWORD>"
```

## Description

Authenticates to the Rocket.Chat REST API using provided credentials, returning an authToken and userId for subsequent requests.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-d` | POST data string with username and password | Yes |
| `username` | Attacker's username | Yes |
| `password` | Attacker's password | Yes |

## Examples

### Basic Usage

```bash
curl http://127.0.0.1:3000/api/v1/login -d "username=attacker&password=pass123"
```

### Advanced Usage

For remote server:

```bash
curl https://chat.example.com/api/v1/login -d "username=attacker&password=pass123" --insecure
```

## Expected Output

JSON: {"status": "success", "data": {"authToken": "abc123...", "userId": "user456..."}}

## Related

- [[commands/curl-rocket-chat-post-message-xss]]
- [[procedures/Authenticate-to-Rocket.Chat-API]]
