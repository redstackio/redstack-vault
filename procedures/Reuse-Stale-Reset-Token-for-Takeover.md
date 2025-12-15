---
id: proc-003
tags:
  - account-takeover
  - token-reuse
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
  - '[[Use Alternate Authentication Material]]'
updated_at: '2025-12-14T17:31:52.080Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Use Alternate Authentication Material]]'
---
---

# Reuse-Stale-Reset-Token-for-Takeover

## Summary

This procedure uses a previously obtained password reset token—after a normal password change—to reset the password again, achieving account takeover on the Courier platform.

## Description

Exploiting the vulnerability at https://www.trycourier.app, this step reuses the stale reset code from email to perform an unauthorized password change. This occurs post-legitimate password update, proving tokens are not invalidated. In a real attack, an adversary with email access (e.g., shared cybercafe device) can takeover the account if the victim forgets to log out. Prerequisites: Unused reset token and email access. Outcome: Attacker sets new password, gaining full control.

## Requirements

1. The stale reset code from the initial request
2. Access to the email inbox
3. Target URL: https://www.trycourier.app

## Defense

Defensive measures and detection strategies:

- Bind reset tokens to single-use and invalidate on password changes
- Rate-limit reset attempts and alert on token reuse
- Use time-bound, cryptographically secure tokens with short expiry

## Objectives

1. Validate the old token's continued acceptance
2. Override the existing password with attacker-controlled one
3. Confirm account takeover capability

## Instructions

### Step 1: Retrieve Stale Token

**Context**: Access the original reset email.

Open the email inbox and locate the password reset message from step 1 of the chain.

### Step 2: Initiate Reset with Old Token

**Context**: Attempt to use the token despite the recent password change.

Navigate to the password reset page on https://www.trycourier.app. Enter the stale code and proceed to set a new password.

### Step 3: Complete and Verify Takeover

**Context**: Finalize the reset and test control.

Submit a new password using the token. Log in with the new credentials to confirm.

**Expected Output**: Reset succeeds; login with new password works, demonstrating takeover.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts
- [[Use Alternate Authentication Material]] Use Alternate Authentication Material

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[account-takeover]]
- [[token-reuse]]

---
