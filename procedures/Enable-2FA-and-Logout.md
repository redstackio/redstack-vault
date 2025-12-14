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
updated_at: '2025-12-14T17:31:30.623Z'
sub_techniques: []
id: 4712912f-ddd2-4884-9b79-2371412b2cfd
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Account Manipulation]]'
---
# Enable-2FA-and-Logout

## Summary

This procedure enables two-factor authentication (2FA) in the victim's Basecamp account to facilitate response capture in a replay attack, followed by logout to reset the session state.

## Description

After initial login, the attacker navigates to account settings to activate 2FA, generates backup codes, and logs out. This step is crucial for the vulnerability exploitation as it allows capturing a 2FA-authenticated response later. The target environment is Basecamp's web interface, and prerequisites include an active session. Outcomes include 2FA enabled and a clean logout.

## Requirements

1. Active session from initial login
2. Access to account settings page
3. Ability to generate and store backup codes securely

## Defense

Defensive measures and detection strategies:

- Alert on 2FA enable/disable events tied to unusual IPs
- Require email confirmation for security setting changes
- Monitor for rapid 2FA toggling as a sign of compromise

## Objectives

1. Activate 2FA to enable backup code usage
2. Obtain backup codes for subsequent login
3. Log out to prepare for fresh authentication capture

## Instructions

### Step 1: Access Account Settings

**Context**: Locate and enter the security settings to enable 2FA.

**Instructions**: From the dashboard, click on profile or account menu and select 'Two-Factor Authentication' or similar.

> Expected output: 2FA setup page loads with QR code or setup options.

### Step 2: Enable 2FA and Generate Backup Codes

**Context**: Complete the 2FA setup process.

**Instructions**: Scan QR code with an authenticator app or follow prompts, then generate and save backup codes.

> Expected output: Confirmation message; backup codes listed (store one for later use).

### Step 3: Logout

**Context**: End the current session.

**Instructions**: Click logout button in the user menu.

> Expected output: Redirect to sign-in page; no active session.

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
