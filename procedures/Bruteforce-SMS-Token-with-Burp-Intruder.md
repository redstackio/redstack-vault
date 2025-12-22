---
tags:
  - bruteforce
  - token
  - rate-limiting-bypass
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/get-post-verify-token]]'
platforms:
  - Web
techniques:
  - '[[Brute Force]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques:
  - '[[Password Guessing]]'
id: 9dc65e4b-9465-4653-83da-aa3458e9861e
created_at: '2025-12-14T17:33:12.397Z'
updated_at: '2025-12-14T17:33:12.397Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Brute Force]]'
---
# Bruteforce-SMS-Token-with-Burp-Intruder

## Summary

This procedure uses Burp Suite Intruder to bruteforce the 6-digit SMS token on the verification endpoint, exploiting the absence of rate limiting to try all 1,000,000 combinations quickly.

## Description

After initiating the reset, the API endpoint /api/system/verification-codes/{token} allows unchecked queries. Using multithreading in Burp, an attacker can identify the valid token before the victim cancels. This works during off-hours to avoid interference. ReCAPTCHA is provided but not enforced.

## Requirements

1. Valid reset flow initiated (SMS sent)
2. Burp Suite configured as proxy
3. Target endpoint accessible

## Defense

Defensive measures and detection strategies:

- Add rate limiting (e.g., 10 attempts per minute per IP)
- Short token expiration (e.g., 5 minutes)
- Monitor for high-volume token checks

## Objectives

1. Identify the correct 6-digit token
2. Obtain security code for password reset
3. Enable account takeover

## Instructions

### Step 1: Capture and Configure Intruder

**Context**: Intercept a sample token check request in Burp and set up Intruder for payload positions on the 6 digits.

**Command** ([[commands/get-post-verify-token]]):
```bash
# Base for automation: GET example
curl -X GET https://helpdesk.bistudio.com/api/system/verification-codes/§000000§§§§§§ -v
# Or POST if endpoint requires: curl -X POST https://helpdesk.bistudio.com/api/system/verification-codes/§000000§§§§§§ -H "Content-Type: application/json" -d '{}'
```

> In Burp Intruder, use numbers payload (0-9) for each § position, multithreaded. Valid response shows success (e.g., 200 OK).

### Step 2: Launch Bruteforce

**Context**: Run the attack to find the matching token.

> Configure speed to ~1000 req/sec; monitor for valid responses. Expected: Token found in under 60 minutes worst-case.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Brute Force]] Brute Force

### Sub-Techniques

- [[Password Guessing]] Password Guessing

## Commands Used

- [[commands/get-post-verify-token]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[bruteforce]]
- [[token]]
- [[rate-limiting-bypass]]
