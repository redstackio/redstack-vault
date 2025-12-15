---
id: 123e4567-e89b-12d3-a456-426614174001
name: HackerOne-Enable-2FA-and-Deactivate-Account
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:42.828Z'
tactics:
  - '[[Credential Access]]'
techniques:
  - '[[Account Manipulation]]'
sub_techniques: []
tags:
  - 2fa-setup
  - account-deactivation
  - hackerone
commands: []
platforms:
  - Web
tools: []
skill_level: intermediate
impact_level: medium
detection_risk: low
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Account Manipulation]]'
---

# HackerOne-Enable-2FA-and-Deactivate-Account

## Summary

This procedure outlines enabling two-factor authentication on a HackerOne account and then deactivating it, which is a prerequisite for exploiting the 2FA bypass vulnerability during subsequent password reset.

## Description

In the context of the 2FA bypass attack on HackerOne, this step ensures the account is configured with 2FA but deactivated, creating a state where password reset does not enforce OTP verification. The target environment is the HackerOne web platform. Expected outcomes include account deactivation confirmation, setting up the bypass without alerting the user immediately.

## Requirements

1. Valid HackerOne account credentials
2. Access to an authenticator app (e.g., Google Authenticator) for 2FA setup
3. Web browser with internet access

## Defense

Defensive measures and detection strategies:

- Monitor account activity logs for unexpected deactivations
- Implement email notifications for all account status changes
- Use advanced 2FA methods like hardware keys that persist across resets

## Objectives

1. Configure 2FA to establish the vulnerable state
2. Deactivate the account to disable 2FA enforcement on reset
3. Prepare for email-based takeover without OTP

## Instructions

### Step 1: Enable 2FA

**Context**: Log into the account and set up two-factor authentication to ensure it's active before deactivation.

Navigate to the HackerOne settings page at https://hackerone.com/settings/security, select 'Two-Factor Authentication', scan the QR code with your authenticator app, and enter the generated OTP to confirm.

> Upon success, a confirmation message appears, and 2FA is enabled for future logins.

### Step 2: Deactivate Account

**Context**: With 2FA enabled, deactivate the account to trigger the bypass condition.

Go to account settings at https://hackerone.com/settings/account, select 'Deactivate Account', confirm the action (may require current password or OTP), and complete deactivation.

> Expected output: Account is marked as deactivated, and a confirmation email is sent.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]] Credential Access

### Techniques

- [[Account Manipulation]] Account Manipulation

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[2fa-setup]]
- [[account-deactivation]]
- [[hackerone]]
