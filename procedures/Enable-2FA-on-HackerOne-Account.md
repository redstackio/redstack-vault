---
tags:
  - 2fa-setup
  - prerequisite
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
updated_at: '2025-12-14T17:33:12.292Z'
skill_level: low
impact_level: low
detection_risk: low
sub_techniques: []
id: b29c2c7a-c87f-4fb0-84a8-710eb01aaf20
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Enable-2FA-on-HackerOne-Account

## Summary

This procedure sets up two-factor authentication on a HackerOne account using the known email and password, preparing the target for the 2FA reset bypass exploit.

## Description

In the context of exploiting the HackerOne 2FA reset vulnerability, enabling 2FA is a prerequisite step to ensure the account has active two-factor protection that can later be targeted. This involves logging into the account settings via the web interface and configuring TOTP-based 2FA. The procedure assumes the attacker already possesses the victim's credentials and is performed to simulate or confirm the vulnerable state. Expected outcome is an account with 2FA enabled, allowing subsequent login attempts to trigger the reset flow.

## Requirements

1. Valid email and password for the target HackerOne account
2. Web browser with internet access to https://hackerone.com
3. TOTP app (e.g., Google Authenticator) for setup

## Defense

Defensive measures and detection strategies:

- Monitor account settings changes for unauthorized 2FA enablement
- Enable login alerts to notify users of any access attempts
- Use IP-based anomaly detection to flag logins from unfamiliar locations

## Objectives

1. Activate 2FA on the target account to enable reset exploitation
2. Verify 2FA functionality before proceeding to bypass
3. Sign out cleanly to reset the login state

## Instructions

### Step 1: Log In to Account

**Context**: Access the HackerOne dashboard using provided credentials to reach settings.

Navigate to https://hackerone.com/login and enter the email and password.

> Successful login redirects to the account dashboard.

### Step 2: Configure 2FA

**Context**: Enable TOTP-based two-factor authentication in account preferences.

Go to account settings (typically under profile icon > Settings > Security), select 'Enable Two-Factor Authentication', scan the QR code with a TOTP app, and enter the generated code to confirm.

> 2FA is now active; a backup code may be provided for recovery.

### Step 3: Sign Out

**Context**: Log out to prepare for the exploit login attempt.

Click the profile icon and select 'Sign Out'.

> Account session ends, ready for next login.

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
- [[prerequisite]]
