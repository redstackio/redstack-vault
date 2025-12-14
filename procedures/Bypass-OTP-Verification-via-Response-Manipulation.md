---
id: proc-otp-bypass
tags:
  - otp-bypass
  - response-manipulation
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
  - '[[tools/Caido]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:33:24.557Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Valid Accounts]]'
---
# Bypass-OTP-Verification-via-Response-Manipulation

## Summary

This procedure intercepts the OTP verification request on shop.mtn.ng using a proxy tool and modifies the server response to fake a successful verification, allowing linkage of an uncontrolled MSISDN without valid OTP.

## Description

The OTP endpoint (/mtn_otp/index/verification/) returns a JSON error for invalid OTPs, but lacks server-side revalidation. By altering the response in transit (e.g., status 400 to 200, success:false to true), the client accepts the verification. This exploits client-side trust in server responses, leading directly to ATO.

## Requirements

1. Proxy tool like Burp Suite or Caido configured for the browser
2. Valid session from account addition step
3. Knowledge of HTTP/JSON manipulation

## Defense

Defensive measures and detection strategies:

- Enforce server-side OTP revalidation on all actions post-verification
- Use signed responses or CSRF tokens to prevent tampering
- Monitor for anomalous proxy traffic or response mismatches

## Objectives

1. Simulate successful OTP without actual code
2. Link MSISDN to attacker account
3. Enable subsequent ATO

## Instructions

### Step 1: Trigger OTP Request

**Context**: Enter invalid OTP to generate the verification request.

After adding MSISDN, input bogus OTP (e.g., 123456) and submit.

> Expected: POST request to /mtn_otp/index/verification/ with params ajax=1&action=verifyotp&msisdn=[redacted]&otp=123456.

### Step 2: Intercept Request

**Context**: Capture using proxy.

Configure [[tools/Burp-Suite]] or [[tools/Caido]] to intercept; forward request unchanged.

> Expected: Response: HTTP/2 200 OK, JSON {"status":400,"message":"Invalid OTP","msisdn":"[redacted]","success":false}.

### Step 3: Modify and Forward Response

**Context**: Alter JSON to success.

Edit to {"status":200,"msisdn":"[redacted]","success":true}; remove error message; forward.

> Expected: Client processes as verified; MSISDN linked.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]
- [[tools/Caido]]

## Tags

- otp-bypass
- response-manipulation
