---
id: proc-gitlab-submit-modified
tags:
  - otp-submission
  - bypass
  - 2fa
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:31:30.870Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
---
# Submit Modified Request with Target OTP

## Summary

This procedure replaces the OTP value in the modified request with the target's valid code and forwards it to the server, triggering authentication as the target due to the injected login parameter.

## Description

With user[login] set to target, changing user[otp_attempt] to the target's 6-digit code causes the server to verify against the target's account. The SessionsController selects the user via params[:login], bypassing the session ID. Success grants target session without password.

## Requirements

1. Modified request with target login
2. Valid target OTP code
3. Burp Suite for forwarding

## Defense

Defensive measures and detection strategies:

- Bind OTP verification strictly to session user
- Implement OTP one-time use per session
- Detect and block requests with mismatched user params

## Objectives

1. Update OTP to target's code
2. Forward request to /users/sign_in
3. Achieve successful auth response

## Instructions

### Step 1: Replace OTP Value

**Context**: Edit the otp_attempt field to use target's code.

In Burp, change value of user[otp_attempt] from attacker's (e.g., 212421) to target's (e.g., 123456).

> Maintains multipart format.

### Step 2: Forward Request

**Context**: Send the altered request to the server.

Click Forward in Burp Proxy or send via Repeater.

> Expected: 302 redirect or success page as target user.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[otp-submission]]
- [[bypass]]
- [[2fa]]
