---
tags:
  - 2fa-enable
  - security-settings
  - mfa-setup
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
updated_at: '2025-12-14T17:24:47.455Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: fb2f6001-043f-4289-a9e6-a2dc3de72239
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Enable-2FA-on-CS-Money-Security-Page

## Summary

This procedure activates two-factor authentication (2FA) on a CS Money account via the web interface, which is essential for testing the platform's session invalidation logic during security enhancements.

## Description

The CS Money security page at https://cs.money/security/ provides an interface for enabling MFA using an authenticator app. This step involves navigating to the settings, scanning a QR code, and verifying with a time-based one-time password (TOTP). In an attack scenario, this simulates a user enabling 2FA after an attacker has gained initial access, highlighting flaws if existing sessions persist. Prerequisites include an active session on the device. Expected outcomes: 2FA enabled account-wide, but potentially without session termination on other devices.

## Requirements

1. Active login session on the device performing the enablement
2. Authenticator app installed (e.g., Google Authenticator, Authy)
3. Camera access for QR code scanning (if using mobile app)

## Defense

Defensive measures and detection strategies:

- Automatically log out all sessions upon 2FA enablement
- Require re-authentication across all active sessions post-MFA setup
- Log and alert on 2FA activations for account owners

## Objectives

1. Successfully enable 2FA for the account
2. Trigger any backend session management changes
3. Prepare for verification of session impacts

## Instructions

### Step 1: Navigate to Security Settings

**Context**: Access the 2FA configuration area.

From the logged-in dashboard on Device A, go to https://cs.money/security/ and locate the 2FA or MFA enablement section.

> The page should display options for setting up two-factor authentication.

### Step 2: Complete 2FA Setup

**Context**: Follow the activation prompts to bind an authenticator.

Scan the provided QR code with your authenticator app, enter the generated 6-digit code, and submit to enable 2FA.

> A success message confirms activation; the account now requires 2FA for future logins.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[2fa-enable]]
- [[security-settings]]
- [[mfa-setup]]
