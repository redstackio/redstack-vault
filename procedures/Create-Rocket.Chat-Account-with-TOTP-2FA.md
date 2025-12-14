---
tags:
  - setup
  - 2fa
  - rocket-chat
type: procedure
tools:
  - '[[tools/Web-Inspector]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:31:11.190Z'
sub_techniques: []
id: 0a2b7553-9f3d-4f58-9018-77b3e134a5bc
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create Rocket.Chat Account with TOTP 2FA

## Summary

This procedure sets up a test user account in Rocket.Chat with TOTP two-factor authentication enabled, providing a controlled environment to demonstrate the 2FA bypass vulnerability.

## Description

In the context of testing the Rocket.Chat TOTP bypass, this initial setup involves registering a new account and configuring 2FA via TOTP. The target is a web-based Rocket.Chat instance running on JavaScript/Meteor/Node.js. Prerequisites include network access to the instance's registration endpoint. Successful completion results in an account that requires both password and TOTP for login, simulating a protected user.

## Requirements

1. Network access to the Rocket.Chat web interface.
2. No existing account or session on the target instance.
3. Authenticator app (e.g., Google Authenticator) for TOTP setup.

## Defense

Defensive measures and detection strategies:

- Enforce strong account creation policies, such as CAPTCHA on registration.
- Monitor for unusual account creation patterns from the same IP.

## Objectives

1. Establish a 2FA-enabled account for vulnerability testing.
2. Verify TOTP functionality before attempting bypass.
3. Prepare for subsequent login and exploitation steps.

## Instructions

### Step 1: Register New Account

**Context**: Access the registration form to create a basic user account.

Navigate to the Rocket.Chat homepage and click 'Register' or the equivalent link. Fill in username, email, and password fields, then submit.

> Expected output: Confirmation message and redirect to setup or dashboard.

### Step 2: Enable TOTP 2FA

**Context**: Configure two-factor authentication during or after account creation.

In the user settings or setup wizard, select 'Enable Two-Factor Authentication'. Scan the QR code with your authenticator app and enter the generated TOTP code to verify.

> Expected output: Success message confirming 2FA activation; future logins require TOTP code.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Web-Inspector]]

## Tags

- [[setup]]
- [[2fa]]
- [[rocket-chat]]
