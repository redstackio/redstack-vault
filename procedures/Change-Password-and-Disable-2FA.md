---
tags:
  - password-change
  - 2fa-disable
  - account-settings
type: procedure
tools: []
tactics:
  - '[[Persistence]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Reversible Encryption]]'
updated_at: '2025-12-14T17:24:47.646Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 5cb702d5-68fe-42ce-94d8-672070c4cbc6
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Reversible Encryption]]'
---
# Change-Password-and-Disable-2FA

## Summary

This procedure updates the account password and disables two-step verification in Moneybird, which should normally invalidate all sessions but fails due to the vulnerability.

## Description

Targeting the account settings page, this step simulates or performs security hardening actions that expose the session persistence flaw. In an attack scenario, this could be triggered by the victim or an insider. The technical approach relies on the application's improper handling of pending sessions during config changes. Prerequisites: An active session to access settings. Expected outcomes: Settings updated, but pending logins unaffected.

## Requirements

1. Active login session to the Moneybird account
2. Access to the settings endpoint
3. Knowledge of current password for verification

## Defense

Defensive measures and detection strategies:

- Force logout of all sessions on password/MFA changes
- Log and alert on security setting modifications
- Implement session registry for immediate expiry

## Objectives

1. Alter password to a new secure value
2. Turn off MFA to remove verification barrier
3. Create conditions for session bypass validation

## Instructions

### Step 1: Access Account Settings

**Context**: Log in or use an existing session to reach configuration options.

Navigate to the account settings page, typically at https://my.moneybird.com/settings/account.

> Expected output: Settings dashboard with security options visible.

### Step 2: Update Password

**Context**: Change the password to invalidate associated sessions.

Enter the current password, then set a new one (e.g., generate a strong password) and confirm.

> Submit the form. Expected output: Success message confirming password update.

### Step 3: Disable Two-Step Verification

**Context**: Remove the MFA requirement, which should trigger session cleanups.

Locate the two-step verification toggle and disable it, following any confirmation prompts.

> Expected output: Confirmation that 2FA is now off, with no active MFA devices listed.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]] Persistence

### Techniques

- [[Reversible Encryption]] Multi-Factor Authentication Instrument

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[password-change]]
- [[2fa-disable]]
- [[account-settings]]
