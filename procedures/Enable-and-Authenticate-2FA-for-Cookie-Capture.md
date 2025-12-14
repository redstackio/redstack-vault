---
tags:
  - 2fa-setup
  - authentication
type: procedure
tools:
  - '[[tools/Browser-Cookie-Editor]]'
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
updated_at: '2025-12-14T17:24:47.953Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: f4289f56-ded5-4e5f-a861-4029fb04c424
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Enable-and-Authenticate-2FA-for-Cookie-Capture

## Summary

This procedure sets up and completes two-factor authentication on the HackerOne platform to generate valid session cookies that can later be stolen and reused for bypassing 2FA in subsequent sessions.

## Description

In the context of exploiting session cookie vulnerabilities, this procedure involves enabling 2FA in account settings, logging in with credentials, and entering the 2FA code to establish an authenticated session. The target environment is the HackerOne web platform, where session cookies are issued post-2FA without device-binding or re-verification checks. Prerequisites include valid account credentials and access to an authenticator app. Expected outcomes include a fully authenticated session with exportable cookies, enabling downstream bypass attacks.

## Requirements

1. Valid HackerOne username and password
2. Authenticator app (e.g., Google Authenticator) installed on a device
3. Browser with developer tools or cookie editor extension
4. Direct access to the target account (e.g., via phishing or prior compromise)

## Defense

Defensive measures and detection strategies:

- Implement device fingerprinting and IP binding for session cookies to prevent reuse across browsers
- Monitor for anomalous login patterns, such as logins from new devices without 2FA prompts
- Use short-lived session tokens and require re-authentication for sensitive actions

## Objectives

1. Activate 2FA to simulate legitimate user behavior and capture post-auth cookies
2. Complete full authentication to validate session establishment
3. Prepare cookies for export in the attack chain

## Instructions

### Step 1: Enable 2FA in Account Settings

**Context**: Navigate to the settings to activate secondary authentication, which is necessary to test the bypass.

No specific command; use the web interface:

- Log in to HackerOne.
- Go to Settings > Security > Two-Factor Authentication.
- Scan the QR code with an authenticator app and save the backup codes.

> This enables TOTP-based 2FA, confirming setup via email or on-screen message.

### Step 2: Log Out and Initiate Re-Login

**Context**: Force a fresh session to trigger 2FA.

- Click logout in the user menu.
- Enter username and password on the login page.

> Prompts the 2FA code entry field upon credential validation.

### Step 3: Enter 2FA Code and Complete Authentication

**Context**: Verify the second factor to issue session cookies.

- Open the authenticator app and enter the current TOTP code.
- Submit to finalize login.

> Successful login redirects to the dashboard, with session cookies set (inspect via browser dev tools: Application > Cookies > hackerone.com).

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Browser-Cookie-Editor]]

## Tags

- 2fa-setup
- authentication
