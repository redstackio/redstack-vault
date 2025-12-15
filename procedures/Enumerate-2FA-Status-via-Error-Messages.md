---
id: proc-gitlab-2fa-enumerate
tags:
  - information-disclosure
  - enumeration
  - 2fa
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Discovery]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Identity Information]]'
updated_at: '2025-12-14T17:31:30.860Z'
skill_level: intermediate
impact_level: low
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Gather Victim Identity Information]]'
---
# Enumerate 2FA Status via Error Messages

## Summary

This procedure exploits differing error messages on the GitLab sign-in endpoint to determine if a user has 2FA enabled, aiding target selection for bypass attacks.

## Description

Submitting invalid credentials yields 'Invalid username/password' for non-2FA users but 'Invalid two-factor code' for 2FA-enabled ones, leaking status. Target /users/sign_in with various usernames and observe responses.

## Requirements

1. List of usernames to test
2. Access to login endpoint
3. Proxy for request analysis

## Defense

Defensive measures and detection strategies:

- Standardize error messages to generic 'Invalid credentials'
- Rate limit login attempts per IP
- Log enumeration attempts

## Objectives

1. Identify 2FA-enabled users
2. Gather intel for bypass
3. Avoid detection

## Instructions

### Step 1: Submit Invalid Login

**Context**: Test a username with invalid password/OTP.

Use Burp Intruder or manual POST: user[login]=testuser&user[password]=wrong&user[otp_attempt]=000000

> Observe response body for error type.

### Step 2: Analyze Response

**Context**: Differentiate based on message.

'Invalid two-factor code' indicates 2FA; otherwise, not.

> Repeat for multiple users to build list.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Gather Victim Identity Information]] Gather Victim Identity Information

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[information-disclosure]]
- [[enumeration]]
- [[2fa]]
