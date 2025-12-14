---
id: proc-bypass-2fa-password
name: Bypass-2FA-with-Password-Login
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:48.053Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Valid Accounts]]'
sub_techniques: []
tags:
  - auth-bypass
  - password-login
  - shopify
commands: []
platforms:
  - Web
tools: []
skill_level: intermediate
impact_level: high
detection_risk: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---

# Bypass-2FA-with-Password-Login

## Summary

This procedure exploits the disabled 2FA state to access the Shopify admin panel using only email and password, bypassing the previously enforced second factor.

## Description

Post-Google login, the standard auth endpoint allows credential-only access. This targets `/admin/auth/login` and assumes knowledge of the victim's password. The vulnerability stems from the lack of 2FA re-enforcement or notification. Outcome: Full admin access without additional verification, enabling data manipulation or further attacks.

## Requirements

1. Knowledge of target email/password.
2. Prior execution of Google login to disable 2FA.
3. No Google account access needed for this step.

## Defense

Defensive measures and detection strategies:

- Detect login anomalies like sudden 2FA absence via behavioral analytics.
- Mandate 2FA re-verification on auth method changes.

## Objectives

1. Gain admin access without 2FA.
2. Validate bypass success.
3. Demonstrate impact of misconfiguration.

## Instructions

### Step 1: Access Standard Login

**Context**: Use the traditional login page.

Go to `https://[store-name].myshopify.com/admin/auth/login`.

> Expected: Email/password fields only, no 2FA prompt.

### Step 2: Submit Credentials

**Context**: Attempt login without second factor.

Enter email and password; submit form.

> Expected: Direct admin panel access.

### Step 3: Confirm Access

**Context**: Verify full privileges.

Navigate sensitive areas like order management; ensure no restrictions.

> Expected: Unhindered admin functionality.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[auth-bypass]]
- [[password-login]]
- [[shopify]]
