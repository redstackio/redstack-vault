---
tags:
  - phabricator
  - account-takeover
  - password-reset
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
updated_at: '2025-12-14T17:31:30.984Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 90c9b5e2-3841-4a6a-b355-340ef82602b7
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Use-Old-Reset-Link-for-Account-Takeover

## Summary

This procedure exploits the non-expiring reset token by using an old link post-email change to reset the password and takeover the account.

## Description

The scenario assumes access to a compromised old email (a@x.com) containing the reset link. Despite the email change to b@x.com, the token remains valid, allowing password reset. Target: Phabricator reset endpoint; outcome: Unauthorized access. Prerequisites: Old reset link and no consumption of it.

## Requirements

1. Access to old email with reset link
2. The link must be unused
3. Web browser for link interaction

## Defense

Defensive measures and detection strategies:

- Invalidate reset tokens on email or any profile changes
- Bind tokens to current email and validate on use
- Monitor for reset usage from unexpected IPs or after changes

## Objectives

1. Reset password with old token
2. Gain account control
3. Demonstrate vulnerability impact

## Instructions

### Step 1: Access Old Link

**Context**: Retrieve and open the previously saved reset URL.

Open the email from a@x.com and click the reset link.

> Expected: Redirect to password reset form.

### Step 2: Set New Password

**Context**: Complete the takeover.

Enter a new password and submit the form.

> Expected: Password updated successfully.

### Step 3: Verify Access

**Context**: Confirm control.

Log out and log in with the new password.

> Expected: Full account access achieved.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[phabricator]]
- [[account-takeover]]
- [[password-reset]]
