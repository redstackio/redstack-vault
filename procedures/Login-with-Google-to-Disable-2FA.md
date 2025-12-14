---
id: proc-google-login-disable-2fa
name: Login-with-Google-to-Disable-2FA
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:48.066Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Modify Authentication Process]]'
sub_techniques: []
tags:
  - 2fa-disable
  - google-login
  - shopify
commands: []
platforms:
  - Web
tools: []
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Modify Authentication Process]]'
---

# Login-with-Google-to-Disable-2FA

## Summary

This procedure authenticates via Google Apps on Shopify, triggering a silent disablement of local 2FA without user notification or option to revert.

## Description

By using the Google-specific login endpoint after enabling the service, Shopify's system deactivates the TOTP-based 2FA. This affects the `/admin/auth/login` flow and removes the 2FA settings tab. The attack scenario assumes an attacker with password knowledge but no 2FA access; the impact is full admin compromise. Prerequisites: Google Apps enabled and linked account.

## Requirements

1. Enabled Google Apps in Shopify settings.
2. Valid Google credentials for the linked account.
3. Prior 2FA setup to observe disablement.

## Defense

Defensive measures and detection strategies:

- Log authentication method switches and alert on 2FA disablements.
- Prevent silent changes to auth configs via UI locks.

## Objectives

1. Authenticate to trigger 2FA disable.
2. Confirm removal of 2FA from settings.
3. Enable subsequent password-only access.

## Instructions

### Step 1: Access Google Login Endpoint

**Context**: Direct to the Google Apps login variant.

Navigate to `https://[store-name].myshopify.com/admin/auth/login?google_apps=1`.

> Expected: Google sign-in button prominent.

### Step 2: Authenticate with Google

**Context**: Complete SSO to invoke the disable logic.

Click "Sign in with Google" and enter Google credentials; approve any prompts.

> Expected: Redirect to Shopify admin dashboard.

### Step 3: Verify 2FA Disablement

**Context**: Check settings for changes.

Go to `https://[store-name].myshopify.com/admin/settings/account`; confirm 2FA tab is gone.

> Expected: No 2FA options visible.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Modify Authentication Process]] Modify Authentication Process

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[2fa-disable]]
- [[google-login]]
- [[shopify]]
