---
tags:
  - api-login
  - token-generation
  - mobile
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/initiate-sms-login-token]]'
verified: false
platforms:
  - Mobile
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:30:47.323Z'
sub_techniques: []
id: c54c048e-5150-4b9a-8317-86e98c90f7ec
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Generate-Login-Token-with-Phone-Number

## Summary

This procedure initiates the Affirm mobile login flow by submitting a phone number via SMS channel to generate a temporary, non-expiring login token, setting up for subsequent OTP brute-force.

## Description

In the Affirm API, the /api/v3/login/phone/ endpoint accepts a phone number and channel (SMS) to return a response_url containing a unique token. This token does not expire, allowing repeated use without limits. The attack targets this to enable brute-forcing the 4-digit OTP sent via SMS. Prerequisites include network access to the API and a target phone number. Expected outcome is a valid token for OTP submission.

## Requirements

1. Direct HTTP access to Affirm API (e.g., hackerone.affirm-odin.com)
2. Target phone number in E.164 format without +1 or dashes (e.g., 7022170000)
3. Tools like curl or Burp Suite for request interception

## Defense

Defensive measures and detection strategies:

- Implement token expiry (e.g., 5-10 minutes) on login tokens
- Enforce rate limiting on OTP attempts per token or IP (e.g., 5 attempts max)
- Monitor for high-volume requests to login endpoints
- Require device fingerprinting headers from the start

## Objectives

1. Obtain a non-expiring token for OTP brute-force
2. Prepare for unauthorized authentication
3. Enable account takeover via API access

## Instructions

### Step 1: Submit Phone Number for Token

**Context**: Send POST request to initiate SMS OTP and generate token.

**Command** ([[commands/initiate-sms-login-token]]):
```bash
curl -X POST https://hackerone.affirm-odin.com/api/v3/login/phone/ \
  -H "Content-Type: application/json; charset=UTF-8" \
  -H "User-Agent: okhttp/3.13.1" \
  -H "Affirm-User-Agent: Affirm-Android" \
  -d '{"channel":"sms","address":"7022170000"}'
```

> This command emulates an Android app request. Expected output: HTTP 200 with {"response_url": "/api/v3/login/phone/SOMETOKEN"}. Extract the token from response_url for next steps.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/initiate-sms-login-token]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- api-login
- token-generation
