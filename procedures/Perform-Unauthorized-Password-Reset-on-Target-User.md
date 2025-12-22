---
tags:
  - account-takeover
  - password-reset
  - authorization-bypass
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Account Manipulation]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 336b9a67-33e8-4e09-ba88-a3d421a4c516
created_at: '2025-12-14T17:33:06.688Z'
updated_at: '2025-12-14T17:33:06.688Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Account Manipulation]]'
---
# Perform-Unauthorized-Password-Reset-on-Target-User

## Summary

This procedure exploits the authorization flaw to reset a target user's password in the Lemlist tenant, enabling the attacker to set a known password for subsequent takeover attempts.

## Description

Once the vulnerability is confirmed, the attacker uses the tenant admin interface to target a specific user's account—requiring prior invitation acceptance—and performs a password reset without legitimate permissions. This bypasses standard auth checks in the user management features, directly modifying the victim's credentials. The action is executed via the web UI, with potential API interception for verification.

## Requirements

1. Confirmed access to target user's profile as tenant admin
2. Target user must have accepted the tenant invitation
3. Knowledge of a new password to set for the attacker

## Defense

Defensive measures and detection strategies:

- Add explicit permission checks before allowing password resets
- Require secondary verification (e.g., email confirmation) for resets
- Monitor for anomalous admin actions on user accounts

## Objectives

1. Successfully alter the target user's password
2. Confirm the change propagates to the authentication system
3. Prepare for immediate account access attempt

## Instructions

### Step 1: Select Target Account

**Context**: Identify and isolate the vulnerable user account.

In the user management dashboard, search for and select the target user who has accepted the invitation.

> Expected: User profile opens without access denial.

### Step 2: Initiate Password Reset

**Context**: Trigger the reset action to modify credentials.

Locate the password reset or edit credential option in the profile. Enter a new password controlled by the attacker and submit the change.

> Expected: Success message or updated profile status.

### Step 3: Verify Reset

**Context**: Ensure the reset is effective by checking application state.

Refresh the user list or inspect API responses in developer tools to confirm the password update.

> Expected: No errors; credentials reflect the change.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Account Manipulation]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[account-takeover]]
- [[password-reset]]
- [[authorization-bypass]]
