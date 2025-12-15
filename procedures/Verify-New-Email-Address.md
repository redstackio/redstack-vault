---
id: d4e5f6g7-h8i9-0123-defg-456789012345
tags:
  - email-verification
  - account-persistence
type: procedure
tools: []
tactics:
  - '[[Persistence]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Manipulation]]'
updated_at: '2025-12-14T17:33:12.027Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Account Manipulation]]'
---
# Verify-New-Email-Address

## Summary

This procedure completes the email verification sent exclusively to the new address after an unverified change, solidifying the redirection of account controls without alerting the victim.

## Description

Upon submitting a new email on Coursera.org, a verification email is dispatched only to that address, not the original. The attacker, controlling the new email, can confirm the change, updating the account's primary contact. This step is crucial for intercepting future password resets and ensures the old email receives no notifications.

## Requirements

1. Access to the attacker-controlled email inbox
2. Pending verification from Coursera
3. Open session on coursera.org

## Defense

Defensive measures and detection strategies:

- Dual verification: Send codes to both old and new emails
- Rate-limit email changes per account
- Audit logs for verification events

## Objectives

1. Activate the new email as the account's primary
2. Prevent victim awareness of the change
3. Enable subsequent recovery actions

## Instructions

### Step 1: Check Attacker Email

**Context**: Retrieve the verification message.

Open the email client for the new address and locate the Coursera verification email containing a link or code.

### Step 2: Complete Verification

**Context**: Confirm the change on the platform.

Return to coursera.org, click the verification link from the email, or enter the code in the prompted field.

**Expected Output**: Confirmation page stating the email has been successfully updated.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]]

### Techniques

- [[Account Manipulation]]

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[email-verification]]
- [[account-persistence]]
