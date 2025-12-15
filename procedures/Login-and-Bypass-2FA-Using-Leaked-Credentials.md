---
tags:
  - 2fa-bypass
  - auth-bypass
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
  - '[[tools/MD5-Hash-Generator]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/md5-hash-compute]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Domain Accounts]]'
updated_at: '2025-12-14T17:32:57.998Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 47d8acc0-d849-4995-b1e6-d5b2ab481a69
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Domain Accounts]]'
---
# Login and Bypass 2FA Using Leaked Credentials

## Summary

Use leaked username/password and compute MD5 of prior challenge_answer to bypass 2FA on customer portal.

## Description

Weak 2FA reuses MD5 of previous answer without validation. Login at app.bountypay.h1ctf.com, intercept 2FA request, submit MD5('bD83Jk27dQ') as challenge.

## Requirements

1. Leaked credentials
2. Burp Repeater for interception
3. MD5 computation tool

## Defense

Defensive measures: Implement time-based OTP, rate limit auth attempts; Detection: Monitor for repeated MD5 patterns in logs.

## Objectives

1. Authenticate with creds
2. Bypass 2FA
3. Expected outcome: Session cookie

## Instructions

### Step 1: Perform Login

**Context**: Submit initial credentials.

Enter username brian.oliver, password V7h0inzX at login form.

> Expected output: 2FA prompt.

### Step 2: Intercept and Modify 2FA

**Context**: Compute and submit bypass.

**Command** ([[commands/md5-hash-compute]]):
```bash
echo -n 'bD83Jk27dQ' | openssl md5
```

> Use result in Burp Repeater for challenge field. Expected output: Valid session.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Domain Accounts]] Domain Accounts

### Sub-Techniques

- None

## Commands Used

- [[commands/md5-hash-compute]]

## Tools Used

- [[tools/Burp-Suite]]
- [[tools/MD5-Hash-Generator]]

## Tags

- 2fa-bypass
- auth-bypass
