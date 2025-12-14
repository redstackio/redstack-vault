---
tags:
  - account-takeover
  - otp-verification
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Persistence]]'
commands:
  - '[[commands/curl-verify-otp-claim]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Modify Authentication Process]]'
updated_at: '2025-12-14T17:28:44.225Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 0efb75e3-9b77-41df-9b0c-d068af77c7a0
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Modify Authentication Process]]'
---
---

# Verify-OTP-to-Claim-Restaurant-Ownership

## Summary

This procedure uses the intercepted OTP to verify and claim ownership of the target unclaimed restaurant, mapping the attacker's email as owner/manager via the Zomato API.

## Description

The /restaurant-onboard-diy/v2/verify-auto-claim-otp endpoint accepts the OTP, requestId, and resId without checking if the OTP was sent to a phone linked to the resId. Submitting the attacker's received OTP associates their pre-mapped email (from an existing restaurant) to the target, achieving takeover. This exploits improper authorization, allowing control over the restaurant listing for edits, deletions, or further abuse.

## Requirements

1. Valid OTP from previous SMS receipt
2. requestId from OTP initiation response
3. Target resId
4. Attacker's Zomato account with at least one existing mapped restaurant
5. HTTP client like curl

## Defense

Defensive measures and detection strategies:

- Validate OTP sender phone against resId ownership records during verification
- Require multi-factor auth or email confirmation post-OTP
- Audit ownership changes and flag rapid or anomalous claims
- Restrict claiming to verified business owners via additional docs

## Objectives

1. Submit manipulated OTP for verification
2. Map attacker's details to target restaurant
3. Gain persistent control over the listing

## Instructions

### Step 1: Submit Verification Request

**Context**: POST the OTP and requestId to the verification endpoint with the target resId to complete the ownership claim.

**Command** ([[commands/curl-verify-otp-claim]]):
```bash
curl -X POST https://www.zomato.com/restaurant-onboard-diy/v2/verify-auto-claim-otp \
  -H "Content-Type: application/json" \
  -d '{"verificationCode": "OTP_FROM_SMS", "requestId": "REQUEST_ID_FROM_STEP1", "resId": "VICTIM_RESID"}'
```

> Replace OTP_FROM_SMS with the 6-digit code (e.g., "123456"), REQUEST_ID_FROM_STEP1 with the ID (e.g., "abc123"), and VICTIM_RESID accordingly. Expected output: {"status":"success","message":"Restaurant claimed successfully"}. Verify in Zomato dashboard that the restaurant is now under attacker's email.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]] Persistence

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Modify Authentication Process]] Modify Authentication Process

### Sub-Techniques


## Commands Used

- [[commands/curl-verify-otp-claim]]

## Tools Used

- [[tools/curl]]

## Tags

- account-takeover
- authorization-bypass
- api-exploit

---
