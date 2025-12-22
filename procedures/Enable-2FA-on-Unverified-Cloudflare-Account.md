---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
tags:
  - cloudflare
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
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Account Manipulation]]'
updated_at: '2025-12-14T17:24:48.115Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Account Manipulation]]'
---
# Enable-2FA-on-Unverified-Cloudflare-Account

## Summary

This procedure enables Two-Factor Authentication (2FA) on a newly created unverified Cloudflare account, locking it to the attacker's control and preventing the legitimate owner from accessing it without the 2FA secret.

## Description

Cloudflare's 2FA configuration lacks checks for account verification status, allowing unverified accounts to enable 2FA immediately after creation. The attacker accesses the settings page, generates a QR code or setup key, and configures an authenticator app. This manipulates the account security, leading to denial of access for the email owner during login or password resets. Prerequisites include having just created the unverified account.

## Requirements

1. Access to the unverified Cloudflare account dashboard
2. An authenticator app (e.g., Google Authenticator, Authy)
3. Web browser session

## Defense

Defensive measures and detection strategies:

- Require email verification before allowing 2FA enablement
- Audit logs for 2FA activations on unverified accounts and alert administrators
- Implement multi-step verification flows for security changes

## Objectives

1. Secure the unverified account with attacker-controlled 2FA
2. Block legitimate recovery paths
3. Enable potential full account takeover

## Instructions

### Step 1: Access Account Settings

**Context**: Log into the unverified account and navigate to security settings.

Log in using the temporary credentials from signup and go to My Profile > Authentication in the dashboard.

> This opens the 2FA setup interface without additional barriers.

### Step 2: Configure 2FA

**Context**: Generate and scan the 2FA secret to enable protection.

Click 'Enable 2FA', scan the displayed QR code with an authenticator app, or manually enter the setup key. Enter the generated code to confirm activation.

> Successful enablement updates the account to require 2FA for all future logins, controlled solely by the attacker.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]]

### Techniques

- [[Account Manipulation]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[cloudflare]]
- [[2fa]]
- [[account-manipulation]]
