---
id: p3c4d5e6-f7g8-9012-cdef-3456789012
tags:
  - brute-force
  - otp-bruteforce
  - intruder
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Brute Force]]'
updated_at: '2025-12-14T17:24:48.205Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques:
  - '[[Password Spraying]]'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Brute Force]]'
---
# Brute-Force mfaToken with Burp Intruder

## Summary

This procedure automates brute-forcing of the 6-digit mfaToken using Burp Intruder's payload capabilities, exploiting no rate limits when Intercept is active to test thousands of OTPs efficiently.

## Description

The SingleStore 2FA endpoint lacks enforcement against rapid submissions in intercepted scenarios. By marking mfaToken as a payload position and using a Numbers payload type (e.g., range 000000-999999), the attack identifies the correct OTP via response differences, applicable to both static and TOTP codes.

## Requirements

1. Intercepted 2FA request from previous step
2. Burp Suite Intruder configured
3. Knowledge of OTP format (6 digits)

## Defense

Defensive measures and detection strategies:

- Implement server-side rate limiting on mfaToken submissions
- Add CAPTCHA or progressive delays after failures
- Monitor for anomalous request volumes from single IPs

## Objectives

1. Test OTP range without session interruption
2. Exploit lack of WAF or limit enforcement
3. Narrow down to correct code quickly

## Instructions

### Step 1: Send to Intruder

**Context**: Transfer the held request for payload setup.

In Burp Proxy, right-click the request and select "Send to Intruder".

> Opens Intruder tab with the request loaded.

### Step 2: Configure Payload

**Context**: Mark and set up brute-force parameters.

Clear positions, highlight mfaToken value, click Add §. Set Attack type to Sniper, Payloads to Numbers, from 000000 to 999999 (or test range like 160000-170000), step 1. Ensure Intercept on in Proxy to hold responses.

> Start attack; processes requests sequentially without resets.

### Step 3: Launch Attack

**Context**: Execute the brute-force.

Click Start attack.

> Expected: Table of responses with lengths/status codes; incorrect: 200/303, correct: 302.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Brute Force]] Brute Force

### Sub-Techniques

- [[Password Spraying]] Password Spraying (adapted for OTP)

## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[brute-force]]
- [[otp-bruteforce]]
