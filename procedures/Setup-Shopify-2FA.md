---
id: proc-setup-shopify-2fa
name: Setup-Shopify-2FA
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:48.081Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Valid Accounts]]'
sub_techniques: []
tags:
  - 2fa-setup
  - shopify
commands: []
platforms:
  - Web
tools: []
skill_level: beginner
impact_level: low
detection_risk: low
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---

# Setup-Shopify-2FA

## Summary

This procedure configures Two Factor Authentication (2FA) on a Shopify admin account using Google Authenticator, establishing a baseline security layer that can later be bypassed via misconfiguration.

## Description

In the context of testing Shopify's authentication, this step enables local 2FA via an authenticator app on the admin panel. It targets the account settings endpoint and requires admin privileges. The outcome is a protected login flow that prompts for a time-based one-time password (TOTP) after email/password entry. Prerequisites include a valid Shopify store admin account with email/password login already set up.

## Requirements

1. Valid Shopify admin credentials (email and password).
2. Access to a TOTP app like Google Authenticator installed on a mobile device.
3. Web browser with JavaScript enabled for admin panel navigation.

## Defense

Defensive measures and detection strategies:

- Monitor account settings changes via Shopify audit logs for 2FA enablement.
- Enforce mandatory 2FA via store policies to prevent baseline weaknesses.

## Objectives

1. Enable 2FA to secure the account against password-only attacks.
2. Verify 2FA functionality through a test login.
3. Prepare the account for testing authentication method interactions.

## Instructions

### Step 1: Access Account Settings

**Context**: Navigate to the Shopify admin settings to locate the 2FA configuration.

No command required; use browser to visit `https://[store-name].myshopify.com/admin/settings/account` and log in if needed.

> Expected: Account settings page loads with security options visible.

### Step 2: Configure 2FA

**Context**: Set up TOTP-based 2FA using the provided QR code.

No command; in the "Two-step authentication" section, click "Set up two-step authentication", scan QR with Google Authenticator, and enter the generated code.

> Expected: Confirmation message; 2FA enabled, and future logins require code.

### Step 3: Verify 2FA

**Context**: Test the new 2FA prompt to ensure activation.

Log out and attempt login at `https://[store-name].myshopify.com/admin/auth/login`; enter credentials and confirm 2FA code is requested.

> Expected: Successful login only after valid 2FA input.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[2fa-setup]]
- [[shopify]]
