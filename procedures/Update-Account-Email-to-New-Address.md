---
tags:
  - email-update
  - twitter
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Valid Accounts]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 9d189e3f-cfdc-48f9-bab4-ddff42721f35
created_at: '2025-12-14T17:33:06.122Z'
updated_at: '2025-12-14T17:33:06.122Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Update-Account-Email-to-New-Address

## Summary

This procedure changes the email associated with a Twitter account to a new address and verifies it, simulating a legitimate user update while preserving the old reset link's validity.

## Description

Accessing account settings, this step updates the email from abcd@x.com to efgh@x.com and completes verification. The vulnerability lies in the reset token not being invalidated, allowing later exploitation. This requires login credentials and access to the new email.

## Requirements

1. Logged-in Twitter account
2. Access to new email efgh@x.com
3. Existing password

## Defense

Defensive measures and detection strategies:

- Invalidate all pending reset tokens on email change
- Require re-authentication for sensitive updates

## Objectives

1. Shift email association to new address
2. Verify the update process
3. Expose reset token persistence flaw

## Instructions

### Step 1: Access Settings

**Context**: Log in and navigate to email settings.

Log in with existing credentials, go to Settings > Your account > Email, and enter new email efgh@x.com.

> Twitter prompts for verification.

### Step 2: Verify New Email

**Context**: Confirm the change via new email.

Check efgh@x.com for the verification link and click it to finalize the update.

> Account now uses efgh@x.com as primary email.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[email-update]]
- [[twitter]]
