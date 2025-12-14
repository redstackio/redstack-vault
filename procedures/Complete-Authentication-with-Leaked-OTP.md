---
id: proc-uuid-3
tags:
  - auth-bypass
  - account-takeover
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-complete-auth]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:32:48.483Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
---
# Complete-Authentication-with-Leaked-OTP

## Summary

This procedure uses the extracted OTP from the leaked API response to verify and authenticate, bypassing SMS delivery and achieving account takeover or unauthorized sign-up.

## Description

With the OTP in hand, submit it alongside the phone number to the verification endpoint. This exploits the trust in the OTP mechanism, allowing attackers to impersonate users or create accounts with fake numbers. Applicable to web APIs with OTP flows, it leads to full access, including junk account creation. Prerequisites include the leaked OTP and endpoint knowledge.

## Requirements

1. Leaked OTP code from previous inspection
2. Phone number used in the request
3. Access to the verification API endpoint (e.g., /api/auth/verify)

## Defense

Defensive measures and detection strategies:

- Enforce short OTP expiration (e.g., 60 seconds) and one-time use
- Add device fingerprinting or additional factors to verification
- Monitor for rapid OTP requests and verifications from the same IP

## Objectives

1. Successfully authenticate without SMS
2. Gain access to target account or create new one
3. Demonstrate full impact of the vulnerability

## Instructions

### Step 1: Submit Verification Request

**Context**: Send the phone and OTP to the verification endpoint to complete the auth flow.

**Command** ([[commands/curl-complete-auth]]):
```bash
curl -X POST https://target.com/api/auth/verify -H "Content-Type: application/json" -d '{"phone": "+1234567890", "otp": "123456"}'
```

> Replace "123456" with the actual OTP. This returns a session token or user ID on success (e.g., {"token": "abc123"}). Failure indicates invalid OTP or rate limits.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-complete-auth]]

## Tools Used


## Tags

- auth-bypass
- account-takeover
