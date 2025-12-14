---
tags:
  - 2fa-bypass
  - auth-bypass
  - nextcloud
  - web
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:45.433Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 2b98687c-a229-41dc-91a5-1567507e905f
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Nextcloud-2FA-Bypass-via-Setup-Challenge

## Summary

This procedure exploits a vulnerability in Nextcloud 17's login flow, where a missing check allows users to bypass an enforced 2FA provider by navigating to the `/login/setupchallenge` endpoint during the 2FA prompt and setting up an alternative provider, resulting in successful authentication without completing the original challenge.

## Description

In Nextcloud 17, after enforcing 2FA and configuring a provider, attempting login with just a password triggers the 2FA prompt. However, the application fails to validate that an existing 2FA is already configured, allowing direct access to the setup challenge page. This logic flaw enables attackers with valid credentials to circumvent second-factor protection, potentially leading to unauthorized access in environments relying on 2FA for security. The target environment is a web-based Nextcloud instance version 17, requiring admin setup for 2FA enforcement and user-level access for exploitation.

## Requirements

1. Access to Nextcloud 17 admin panel to enforce 2FA
2. Valid user account with an initial 2FA provider configured
3. Web browser for navigation and interaction
4. Direct network access to the Nextcloud login endpoint

## Defense

Defensive measures and detection strategies:

- Upgrade to Nextcloud versions beyond 17 where this issue is patched (e.g., 18+ with improved login checks)
- Implement web application firewall (WAF) rules to block unauthorized navigation to `/login/setupchallenge` during active sessions
- Monitor login logs for patterns of setup challenge access without prior 2FA completion
- Enforce strict session validation and require 2FA re-verification on endpoint changes

## Objectives

1. Bypass the configured 2FA challenge using only the password
2. Gain full authenticated access to the Nextcloud account
3. Demonstrate the impact of missing authentication flow validations

## Instructions

### Step 1: Enforce 2FA and Configure Initial Provider

**Context**: Prepare the environment by requiring 2FA and setting up the first provider to establish the vulnerable state.

As admin, enable 2FA in settings > Security > Two-factor authentication, setting it to required for all users. Then, as the user, go to personal settings > Security, enable a provider like TOTP, scan the QR code with an authenticator app, and verify with a code.

### Step 2: Initiate Logout and Password-Only Login

**Context**: Reset the session and start the login to reach the 2FA prompt.

Log out via the user menu. On the login page, enter username and password to submit, which should show the 2FA prompt for the initial provider.

### Step 3: Navigate to Setup Challenge and Configure Alternative

**Context**: Exploit the missing check by accessing the setup endpoint to add a new provider, bypassing the prompt.

With the 2FA prompt visible, manually enter `/login/setupchallenge` in the browser URL bar. Select a different 2FA provider (e.g., another app), complete its setup by scanning QR and verifying the code. The login should then complete automatically.

### Step 4: Verify Successful Access

**Context**: Confirm the bypass by checking account access without original 2FA completion.

Observe the redirect to the Nextcloud dashboard, indicating full authentication. Test by accessing protected features.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[2fa-bypass]]
- [[auth-bypass]]
- [[nextcloud]]
- [[web]]
