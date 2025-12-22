---
tags:
  - password-change
  - account-takeover
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
updated_at: '2025-12-14T17:31:19.238Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: d7d8bccf-9528-4dcc-8fb6-1242a2a8394d
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Complete-Password-Change

## Summary

This final procedure sets a new password using the reused token, resulting in full account compromise.

## Description

At the reset form accessed via the old token, entering and confirming a new password updates the account credentials without needing the new email. This completes the takeover, allowing exclusive control if the attacker has old email access but not the original password.

## Requirements

1. Access to the reset form via old token
2. Desired new password
3. No active session

## Defense

Defensive measures and detection strategies:

- Require secondary verification for resets
- Log and alert on password changes post-email update
- Implement token single-use enforcement

## Objectives

1. Update password unauthorized
2. Gain persistent account access
3. Achieve takeover

## Instructions

### Step 1: Enter New Password

**Context**: Fill the form to apply changes.

**Instructions**: In the reset form, input a strong new password in both fields and submit.

> System processes and confirms the change.

### Step 2: Verify Access

**Context**: Test the takeover.

**Instructions**: Log in using the new password to access the dashboard.

> Successful login indicates compromise.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[password-change]]
- [[account-takeover]]
