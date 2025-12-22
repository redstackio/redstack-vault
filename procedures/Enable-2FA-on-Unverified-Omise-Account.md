---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
name: Enable-2FA-on-Unverified-Omise-Account
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:48.091Z'
tactics:
  - '[[Impact]]'
techniques:
  - '[[Endpoint Denial of Service]]'
sub_techniques: []
tags:
  - 2fa-bypass
  - account-takeover
  - dos
commands: []
platforms:
  - Web
tools: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---

# Enable-2FA-on-Unverified-Omise-Account

## Summary

This procedure allows an attacker to activate two-factor authentication on a newly created, unverified account on the Omise dashboard, locking out the legitimate email owner by controlling the 2FA secrets without any additional verification.

## Description

Following unverified account creation on https://dashboard.omise.co/, the security settings permit immediate 2FA enablement. Attackers can scan the QR code or note the secret key using their own authenticator app, ensuring only they can authenticate. This results in a denial of service for the victim, who cannot log in, register a new account with their email, or complete password resets without the attacker's 2FA code. The procedure targets web applications lacking verification gates for sensitive actions and requires login to the fraudulent account.

## Requirements

1. Successful completion of unverified account creation
2. Access to an authenticator app (e.g., Google Authenticator)
3. Logged-in session on the fraudulent account

## Defense

Defensive measures and detection strategies:

- Enforce email or identity verification before enabling 2FA
- Rate-limit or audit 2FA activations on new accounts
- Provide admin overrides or support escalation for lockout disputes
- Log and alert on rapid account creation followed by 2FA setup

## Objectives

1. Secure persistent control over the hijacked account
2. Prevent victim recovery through standard mechanisms
3. Achieve high-impact denial of service on the targeted email

## Instructions

### Step 1: Access Security Settings

**Context**: Log into the fraudulent account and navigate to the 2FA configuration area.

After signup, log in using the created credentials. Go to the account settings menu and select the "Two Factor Authentication" or security section.

### Step 2: Activate 2FA

**Context**: Enable 2FA without verification to claim control of the account.

Click to enable 2FA. A QR code or secret key will be displayed. Scan it with your authenticator app and enter the generated code to confirm. The feature activates immediately.

> No command is executed; this is a manual UI interaction. Expected output: Confirmation message stating 2FA is enabled, with logout requiring the new code.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Endpoint Denial of Service]] Endpoint Denial of Service

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[2fa-bypass]]
- [[account-takeover]]
- [[dos]]
