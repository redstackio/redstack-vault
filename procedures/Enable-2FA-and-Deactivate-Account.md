---
id: proc-uuid-1
tags:
  - 2fa-setup
  - account-deactivation
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
  - '[[Account Manipulation]]'
updated_at: '2025-12-14T17:31:30.820Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Account Manipulation]]'
---
# Enable-2FA-and-Deactivate-Account

## Summary

This procedure enables two-factor authentication on a HackerOne account and then deactivates it, creating the precondition for bypassing 2FA during recovery. It exploits the platform's failure to enforce 2FA on deactivated accounts.

## Description

In the context of the HackerOne vulnerability, an attacker first gains temporary access to the account (or simulates as the user) to enable 2FA via the settings page. Then, the account is deactivated, which should logically require reactivation with 2FA but does not. This step is crucial as it sets up the bypass by placing the account in a deactivated state where recovery skips security checks. Prerequisites include valid login credentials; expected outcome is a deactivated account with 2FA configured but unenforced.

## Requirements

1. Valid HackerOne account credentials (username/email and password)
2. Access to a web browser for navigation
3. Email access for any confirmation notifications

## Defense

Defensive measures and detection strategies:

- Monitor account settings changes, such as 2FA enablement or deactivation, via audit logs
- Implement email alerts for deactivation attempts and require 2FA for all recovery actions
- Use anomaly detection to flag rapid sequences of 2FA setup followed by deactivation

## Objectives

1. Establish 2FA as the active security layer to demonstrate bypass effectiveness
2. Deactivate the account to trigger the logical flaw in recovery processes
3. Prepare for password reset without reactivation enforcement

## Instructions

### Step 1: Log In and Enable 2FA

**Context**: Access the account settings to configure two-factor authentication, ensuring the bypass targets an protected account.

Navigate to the HackerOne login page, enter credentials, and after login, go to Account Settings > Security. Select "Enable Two-Factor Authentication," scan the QR code with an authenticator app (e.g., Google Authenticator), and enter the generated code to confirm. Save backup codes for recovery.

> Successful enablement redirects to settings with 2FA status shown as active.

### Step 2: Deactivate the Account

**Context**: Immediately after 2FA setup, deactivate the account to enter the vulnerable state.

From the same settings page, scroll to the account management section and click "Deactivate Account." Confirm the action via the prompted dialog. Check the associated email for a deactivation confirmation.

> Expected output: Account access is revoked, and a confirmation email is received stating the account is deactivated.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Account Manipulation]] Account Manipulation

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[2fa-setup]]
- [[account-deactivation]]
- [[auth-bypass]]
