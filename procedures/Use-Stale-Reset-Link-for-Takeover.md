---
id: proc-use-stale-token-takeover
tags:
  - account-takeover
  - stale-token
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:31:11.149Z'
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
# Use-Stale-Reset-Link-for-Takeover

## Summary

This procedure exploits the persistent password reset token in Concrete CMS to perform an unauthorized password change, resulting in account takeover.

## Description

After multiple password changes have invalidated sessions, the original reset token remains valid due to improper invalidation logic. Activating this stale token allows setting a new password, bypassing normal authentication and granting full account control to the attacker.

## Requirements

1. Stored reset link from earlier step
2. Web browser to access the link
3. Knowledge of current password (for verification post-takeover)

## Defense

Defensive measures and detection strategies:

- Strictly invalidate reset tokens on any password change or login
- Use one-time-use tokens with database flagging
- Monitor for token usage after session invalidation events

## Objectives

1. Reset password using expired token
2. Achieve unauthorized account access
3. Confirm vulnerability exploitation

## Instructions

### Step 1: Activate Stale Link

**Context**: Use the preserved reset URL to access the change form.

**Instructions**: Paste the original reset link into your browser and load it. The form should appear despite prior changes.

> If the link is still valid, proceed to password input.

### Step 2: Set New Password and Verify

**Context**: Complete the reset and test control.

**Instructions**: Enter a new password in the form, confirm it, and submit. Then, log in using the new password.

> Successful login with the attacker-controlled password indicates takeover.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[account-takeover]]
- [[stale-token]]
- [[auth-bypass]]
