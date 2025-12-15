---
id: proc-email-change-impersonate
tags:
  - email-change
  - impersonation
  - session-persistence
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:24:48.486Z'
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
# Change-Email-to-Victim-for-Impersonation

## Summary

This procedure exploits the lack of session invalidation during email changes on Drugs.com to switch the account email to a victim's address, allowing immediate impersonation via the trusted session without 2FA.

## Description

Targeting the account details page, the attacker updates the email field to the victim's address. Due to the root cause—sessions not being terminated post-change and device trust persisting—the new email inherits the authenticated session. No ownership verification is required, enabling unauthorized access. This occurs in a web environment and leads to full platform interaction on the victim's behalf.

## Requirements

1. Existing trusted session from attacker account
2. Knowledge of victim's email address
3. Access to https://www.drugs.com/account/details/

## Defense

Defensive measures and detection strategies:

- Invalidate all sessions on email modification
- Send notifications to both old and new emails for changes
- Log and alert on email updates without 2FA re-challenge

## Objectives

1. Associate trusted session with victim's identity
2. Gain unauthorized access to victim's account actions
3. Test persistence by logging out and back in

## Instructions

### Step 1: Access Account Details

**Context**: Navigate to the email update interface.

Log in to the trusted account and go to https://www.drugs.com/account/details/.

### Step 2: Update Email Address

**Context**: Perform the change without triggering verification.

Locate the email field, enter the victim's email, and submit the update form.

### Step 3: Verify Session Persistence

**Context**: Confirm the bypass by testing login.

Log out of the account, then log back in using the victim's email and the original password (if known, or rely on session). No OTP should be prompted.

**Expected Output**: Successful login to dashboard as the victim.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[email-change]]
- [[impersonation]]
- [[session-persistence]]
