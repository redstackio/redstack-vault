---
tags:
  - 2fa
  - account-manipulation
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
updated_at: '2025-12-14T17:31:30.616Z'
sub_techniques: []
id: 97ad5090-f205-491d-8bb1-27cd11ad9d72
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Account Manipulation]]'
---
# Disable-2FA-in-Account

## Summary

This procedure disables two-factor authentication in the victim's Basecamp account after response capture, allowing the victim to change their password without 2FA barriers while preserving the captured response's utility.

## Description

Logged in via the captured session or fresh login, the attacker accesses settings to turn off 2FA. This step ensures the password change step can proceed smoothly for the victim. Target is Basecamp's web settings; prerequisites include active session. Outcome: 2FA removed, account in password-only mode.

## Requirements

1. Active authenticated session
2. Access to security settings
3. No additional tools needed

## Defense

Defensive measures and detection strategies:

- Require re-authentication (e.g., current password) for disabling 2FA
- Log and alert on 2FA disable events
- Enforce cooldown periods after security changes

## Objectives

1. Deactivate 2FA to simplify victim password change
2. Maintain account access post-disable
3. Avoid triggering additional security prompts

## Instructions

### Step 1: Access Settings

**Context**: Re-enter account configuration.

**Instructions**: From dashboard, go to profile/account settings and select 2FA section.

> Expected output: 2FA status shown as enabled.

### Step 2: Disable 2FA

**Context**: Turn off the feature.

**Instructions**: Click disable option, confirm if prompted (may require backup code or password).

> Expected output: Confirmation; 2FA status updated to off.

### Step 3: Logout

**Context**: Secure the session.

**Instructions**: Log out to wait for victim action.

> Expected output: Sign-in page.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]] Persistence

### Techniques

- [[Account Manipulation]] Account Manipulation

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[2fa]]
- [[account-manipulation]]
