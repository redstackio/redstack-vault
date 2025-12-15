---
tags:
  - brute-force
  - otp
  - rate-limit-bypass
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/submit-otp-for-auth]]'
verified: false
platforms:
  - Mobile
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Brute Force]]'
updated_at: '2025-12-14T17:30:47.321Z'
sub_techniques:
  - '[[Password Guessing]]'
id: 0910125d-158a-4aa8-aa6f-d0da7868da02
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Brute Force]]'
---
# Brute-Force-OTP-Using-Token-Endpoint

## Summary

This procedure exploits the absence of rate limiting on the OTP submission endpoint to brute-force the 4-digit code using automated tools like Burp Intruder, achieving authentication without limits.

## Description

Using the token from the login initiation, POST requests to the token-specific endpoint (/api/v3/login/phone/{token}) with varying 4-digit 'response' values allow guessing the OTP. Success is detected by 200 status and specific response length/content. The API's openresty backend lacks protections, enabling ~10,000 attempts quickly. Prerequisites: Valid token and Burp Suite. Outcome: Authenticated status with user_id.

## Requirements

1. Burp Suite for request capture and Intruder automation
2. Valid login token from prior step
3. Target endpoint accessible

## Defense

Defensive measures and detection strategies:

- Rate limit OTP attempts (e.g., 3-5 per token)
- Expire tokens after short period or failed attempts
- Log and alert on repeated failures from same IP/token
- Use CAPTCHA or multi-factor beyond OTP

## Objectives

1. Guess the 4-digit OTP via brute-force
2. Bypass authentication mechanism
3. Gain initial access to user session

## Instructions

### Step 1: Capture and Configure Brute-Force

**Context**: Intercept a sample OTP request in Burp, send to Intruder, and set payload for 0000-9999.

**Command** ([[commands/submit-otp-for-auth]]):
```bash
curl -X POST https://hackerone.affirm-odin.com/api/v3/login/phone/SOMETOKEN \
  -H "Content-Type: application/json; charset=UTF-8" \
  -H "Affirm-User-Agent: Affirm-Android" \
  -H "Affirm-App-Version: 3.62.3" \
  -H "Affirm-App-Version-Code: 312" \
  -H "Affirm-OS-Version: 22" \
  -d '{"response":"0000"}'
```

> Vary the 'response' value in Intruder. Expected output on success: HTTP 200, response length ~109 with 'status': 'authenticated' and user_id. Filter results by status and length.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Brute Force]] Brute Force

### Sub-Techniques

- [[Password Guessing]] Password Guessing

## Commands Used

- [[commands/submit-otp-for-auth]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- brute-force
- otp
