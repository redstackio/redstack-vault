---
id: proc-uuid-2
tags:
  - password-reset
  - account-recovery
  - auth-bypass
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
updated_at: '2025-12-14T17:31:30.817Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Reset-Password-on-Deactivated-Account

## Summary

This procedure performs a password reset on a deactivated HackerOne account using email access, exploiting the lack of 2FA enforcement or reactivation during recovery.

## Description

With control over the victim's email, the attacker requests a password reset on the HackerOne platform. The system sends a reset link to the email, allowing a new password to be set without checking the account's deactivated status or requiring 2FA. This logical flaw enables the attacker to update credentials in a state where normal login protections are bypassed. Prerequisites include email access; expected outcome is a new password set on the deactivated account.

## Requirements

1. Access to the victim's email account associated with HackerOne
2. Web browser for the reset process
3. Knowledge of the target email address

## Defense

Defensive measures and detection strategies:

- Enforce account reactivation with 2FA before allowing password resets on deactivated accounts
- Log and alert on password reset attempts for deactivated accounts
- Require additional verification (e.g., security questions) for recovery on inactive accounts

## Objectives

1. Update account credentials without triggering 2FA or reactivation
2. Maintain the deactivated state to avoid security prompts
3. Position for direct login with new password

## Instructions

### Step 1: Initiate Password Reset

**Context**: Start the recovery flow from the login page to receive a reset link via email.

Go to the HackerOne login page, click "Forgot Password?", and enter the target email address. Submit the request to trigger the reset email.

> Expected output: An email arrives with a temporary reset link and expiration notice.

### Step 2: Set New Password

**Context**: Use the reset link to change the password without any additional checks.

Click the link in the email, enter a new strong password twice, and submit. The system updates the password without prompting for 2FA or account status verification.

> Successful completion shows a confirmation message, and the account remains deactivated but with updated credentials.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[password-reset]]
- [[account-recovery]]
- [[auth-bypass]]
