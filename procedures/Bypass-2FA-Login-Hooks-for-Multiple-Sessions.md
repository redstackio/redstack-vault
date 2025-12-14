---
tags:
  - 2fa
  - authentication-bypass
  - session-management
  - persistence
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Persistence]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
techniques:
  - '[[Valid Accounts]]'
skill_level: low
impact_level: medium
detection_risk: low
sub_techniques: []
id: 2e7f7909-ebf8-4920-85be-273f2be2b441
created_at: '2025-12-14T17:24:45.540Z'
updated_at: '2025-12-14T17:24:45.540Z'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Persistence]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Bypass-2FA-Login-Hooks-for-Multiple-Sessions

## Summary

This procedure exploits a vulnerability in the 2FA login flow where standard logon hooks, including session logout mechanisms, are skipped. It allows users to maintain multiple active sessions simultaneously, which can be used for persistent access or to evade single-session policies in web applications like Legal Robot.

## Description

In the target web application, the 2FA authentication process was implemented without integrating the regular logon hooks that handle session management, such as logging out other existing sessions upon new login. This flaw was identified during the addition of new 2FA options. An attacker with valid credentials can leverage this to create and sustain multiple sessions, potentially aiding in session hijacking or maintaining unauthorized access across devices without triggering logout events. The procedure involves manual login steps using a web browser to demonstrate the bypass, confirming no session conflicts occur.

## Requirements

1. Valid user account with 2FA enabled on the target web application
2. Access to the 2FA method (e.g., authenticator app for TOTP codes)
3. Multiple web browsers or incognito modes for testing concurrent sessions
4. Network connectivity to the application's login endpoint (typically HTTPS)

## Defense

Defensive measures and detection strategies:

- Ensure 2FA login flows execute all standard logon hooks, including session invalidation for prior sessions
- Implement session limits and monitoring for concurrent logins from the same account
- Use logging to track login events and session creations, alerting on multiple active sessions
- Enforce single-session policies with automatic logout on new authentications

## Objectives

1. Bypass session logout during 2FA authentication to enable multiple concurrent sessions
2. Verify persistence of existing sessions post-2FA login
3. Demonstrate potential for unauthorized persistent access using valid credentials

## Instructions

### Step 1: Establish Baseline Active Session

**Context**: Create an initial authenticated session to test against the bypass.

Log in to the target application using standard credentials (non-2FA if available, or complete a prior login). Navigate to the protected dashboard and confirm access.

> Verify in browser developer tools (F12 > Application > Cookies) that a session cookie is set and valid.

### Step 2: Execute 2FA Login in New Session

**Context**: Perform the 2FA login to trigger the hook bypass.

Open a new browser window or incognito mode. Enter the same credentials and proceed to 2FA verification (e.g., input TOTP code from authenticator app). Complete the login and access the dashboard.

> No command required; monitor for any logout prompts or redirects, which should not occur due to the bypass.

### Step 3: Validate Multiple Sessions

**Context**: Confirm both sessions remain active, proving the vulnerability.

Switch back to the initial browser session, refresh the page, and perform an action (e.g., view account settings). Repeat in the 2FA session. Both should remain authenticated without interference.

> Check developer tools in both browsers for persistent session tokens. If both succeed, the bypass is confirmed.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Persistence]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[2fa]]
- [[authentication-bypass]]
- [[session-management]]
- [[Persistence]]
