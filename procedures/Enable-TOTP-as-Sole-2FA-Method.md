---
id: proc-001
tags:
  - 2fa
  - totp
  - setup
  - authentication
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:24:47.486Z'
skill_level: beginner
impact_level: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Enable-TOTP-as-Sole-2FA-Method

## Summary

This procedure configures a test account to use Time-based One-Time Password (TOTP) as the exclusive 2FA method, isolating it from other options like U2F to test for implementation gaps during a security assessment of authentication flows.

## Description

In the context of evaluating 2FA robustness in web applications like Legal Robot, this step simulates a user opting for software-based 2FA without hardware backups. It involves accessing the authentication settings during a feature rollout and enabling TOTP via QR code scanning. The goal is to establish a baseline for subsequent checks on recovery mechanisms, highlighting potential lockout risks if authenticator access is lost. Prerequisites include a valid test account and browser access to the settings UI.

## Requirements

1. Active test account with login credentials
2. Authenticator app (e.g., Google Authenticator) installed on a mobile device
3. Web browser with access to the application's 2FA settings page

## Defense

Defensive measures and detection strategies:

- Ensure all 2FA methods provide uniform recovery options in UI design reviews
- Monitor for unusual 2FA configuration changes via audit logs
- Implement automated tests for 2FA completeness during feature rollouts

## Objectives

1. Isolate TOTP as the only active 2FA method
2. Verify successful TOTP integration for logins
3. Prepare account state for recovery feature testing

## Instructions

### Step 1: Access 2FA Settings

**Context**: Log in to the test account and navigate to the authentication or security settings to begin 2FA configuration.

No specific command; use the web interface to select 'Enable 2FA' or similar option.

> Expected: QR code and setup instructions appear for TOTP.

### Step 2: Enable TOTP Exclusively

**Context**: Scan the QR code with your authenticator app and enter a generated code to confirm, ensuring U2F or other methods are disabled.

No command; complete the form submission in the browser.

> Expected: Confirmation message that TOTP is now required for logins, with no other 2FA active.

### Step 3: Validate TOTP Functionality

**Context**: Log out and log back in using a TOTP code to ensure the setup is enforced without fallbacks.

No command; perform manual login test.

> Expected: Successful authentication via TOTP code only.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[2fa]]
- [[totp]]
- [[authentication]]
