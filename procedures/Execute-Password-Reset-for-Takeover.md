---
id: p3q4r5s6-t7u8-9012-defg-345678901234
name: Execute-Password-Reset-for-Takeover
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:58.280Z'
tactics:
  - '[[Credential Access]]'
techniques:
  - '[[Valid Accounts]]'
sub_techniques: []
tags:
  - password-reset
  - account-takeover
commands: []
platforms:
  - Web
tools: []
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---

# Execute-Password-Reset-for-Takeover

## Summary

This procedure leverages a CSRF-induced email change to hijack the password reset flow, allowing the attacker to gain full control of the compromised account.

## Description

In web applications like the vulnerable DoD portal, changing the email via CSRF positions the attacker to intercept password reset emails. By requesting a reset with the new email, the attacker receives the link, resets the password, and logs in, effectively taking over the account. This assumes the reset feature sends links to the registered email without additional verification. The process is manual and relies on timely execution to avoid victim detection.

## Requirements

1. Attacker control over the email set via CSRF
2. Access to the application's password reset endpoint
3. No secondary verification (e.g., SMS) on the account

## Defense

Defensive measures and detection strategies:

- Require multi-factor approval for email changes and resets
- Delay reset links or use time-bound tokens with notifications
- Audit reset requests for unusual patterns (e.g., immediate follows to email changes)

## Objectives

1. Initiate password reset using the hijacked email
2. Complete the reset process to set new credentials
3. Achieve persistent access to the account

## Instructions

### Step 1: Initiate Reset Request

**Context**: Trigger the password reset flow.

Navigate to the login page, click 'Forgot Password' or similar, and enter the modified email (attacker@evil.com). Submit the request.

**Expected Output**: Confirmation message; reset email sent.

### Step 2: Retrieve and Follow Reset Link

**Context**: Access the emailed instructions.

Check the attacker's email inbox for the reset link from the application. Click the link to access the password change form.

### Step 3: Set New Password and Verify Access

**Context**: Finalize the takeover.

Enter a new password in the form and submit. Log out and log back in with the new credentials to confirm control.

**Expected Output**: Successful login; full account access.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]] Credential Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[credential-access]]
- [[web-takeover]]
