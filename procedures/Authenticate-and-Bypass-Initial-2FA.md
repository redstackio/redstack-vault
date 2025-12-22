---
tags:
  - authentication-bypass
  - 2fa-bypass
  - md5-manipulation
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:33:06.055Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 67788b43-7d56-49c7-83c2-7f2fae2b0a03
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Authenticate and Bypass Initial 2FA

## Summary

This procedure uses extracted credentials to authenticate to the application and bypass two-factor authentication by exploiting a client-side MD5 hash check without server-side verification.

## Description

The login endpoint accepts the leaked username 'brian.oliver' and password 'V7h0inzX'. During 2FA, the challenge parameter is set to the MD5 hash of an arbitrary answer like 'test' (098f6bcd4621d373cade4e832627b4f6), and challenge_answer='test', tricking the client-side validation to issue a session cookie.

## Requirements

1. Valid credentials from log extraction
2. Intercepting proxy like Burp Suite for request manipulation
3. Knowledge of the 2FA flow from source code

## Defense

Defensive measures and detection strategies:

- Implement server-side generation and verification of 2FA challenges
- Use secure hashing like Argon2 instead of MD5 for any client checks
- Log and monitor failed 2FA attempts with anomaly detection

## Objectives

1. Gain authenticated session as the target user
2. Bypass 2FA to access account features
3. Obtain session cookie for further exploitation

## Instructions

### Step 1: Submit Login Credentials

**Context**: POST credentials to the root endpoint.

Intercept the login form submission in Burp and modify to include username and password.

> Expected output: Redirect to 2FA challenge page.

### Step 2: Manipulate 2FA Challenge

**Context**: Alter the POST parameters for 2FA bypass.

Set challenge_answer='test' and challenge='098f6bcd4621d373cade4e832627b4f6' (MD5 of 'test') in the POST to /.

> Expected output: Valid session cookie issued, access to account dashboard.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques

- None

## Commands Used

None

## Tools Used

Burp Suite for interception.

## Tags

- authentication-bypass
- 2fa-bypass
- md5-manipulation
