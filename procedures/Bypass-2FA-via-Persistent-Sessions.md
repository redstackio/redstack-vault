---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
tags:
  - 2fa-bypass
  - session-management
  - authentication-bypass
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-04T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:24:48.372Z'
skill_level: low
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Bypass 2FA via Persistent Sessions

## Summary

This procedure exploits improper session management in web applications like SideFX, where enabling two-factor authentication (2FA) does not invalidate or require re-authentication for existing sessions. An attacker with prior access to a session cookie can use it to perform high-impact actions, such as changing the account password, effectively bypassing the newly enabled 2FA protection.

## Description

The vulnerability stems from a failure in the authentication system to terminate active sessions upon 2FA activation. In the SideFX platform, users can log in from multiple browsers or devices, and enabling 2FA via the profile page only affects future logins. Existing sessions persist, allowing unauthorized access to sensitive features. This is particularly dangerous if the session cookie was compromised earlier (e.g., via XSS, malware, or shared device). The attack requires initial credential access but demonstrates how 2FA alone is insufficient without robust session handling. Expected outcomes include successful execution of privileged actions without 2FA, leading to account compromise.

## Requirements

1. Valid username and password for the target SideFX account.
2. Two separate web browsers (e.g., Chrome incognito and Firefox) to simulate distinct sessions.
3. Direct network access to https://sidefx.com over HTTPS.
4. Basic knowledge of web navigation; no advanced tools needed.

## Defense

Defensive measures and detection strategies:

- Enforce session invalidation: Upon 2FA enablement, log out all other active sessions and require re-login with 2FA.
- Implement session binding: Tie sessions to specific devices or IP addresses and monitor for anomalies.
- Require 2FA for all sensitive actions: Even in existing sessions, prompt for 2FA on password changes or profile updates.
- Log and alert on multi-session activity: Detect simultaneous logins from different locations and notify users.
- Use secure cookie flags: Set HttpOnly, Secure, and SameSite=Strict on session cookies to limit theft and misuse.

## Objectives

1. Exploit persistent sessions to access protected account functions post-2FA enablement.
2. Perform unauthorized modifications, such as password changes, to achieve account takeover.
3. Validate the vulnerability by confirming session activity without re-authentication.

## Instructions

### Step 1: Establish Multiple Active Sessions

**Context**: Simulate an attacker with access to an existing session by creating concurrent logins, representing a stolen cookie scenario.

Navigate to https://sidefx.com in two different browsers and log in using the target credentials.

> Manual browser action. Expected output: Both sessions grant access to the account dashboard.

### Step 2: Activate 2FA in the Primary Session

**Context**: Trigger the vulnerable state by enabling 2FA, which should ideally invalidate other sessions but does not.

In the first browser, access https://sidefx.com/profile, select the 2FA enable option, and complete the setup (e.g., enter authenticator app code or backup keys).

> Manual process. Expected output: Profile page shows '2FA activated' confirmation.

### Step 3: Confirm Persistence of Secondary Session

**Context**: Test if the second session is terminated or challenged, revealing the improper management.

In the second browser, refresh the current page or attempt to access a protected resource like the profile.

> Manual browser refresh. Expected output: Session remains fully functional with no 2FA prompt or logout.

### Step 4: Execute Bypass via Sensitive Action

**Context**: Leverage the active session to demonstrate impact by altering account details without 2FA.

In the second browser, return to https://sidefx.com/profile, initiate a password change, enter new credentials, and submit.

> Manual form submission. Expected output: Password updated successfully without any 2FA verification step.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- 2fa-bypass
- session-management
- authentication-bypass
