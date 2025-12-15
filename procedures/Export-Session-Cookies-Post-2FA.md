---
tags:
  - cookie-export
  - session-theft
type: procedure
tools:
  - '[[tools/Browser-Cookie-Editor]]'
tactics:
  - '[[Credential Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Adversary-in-the-Middle]]'
updated_at: '2025-12-14T17:24:47.940Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: f6e82c1a-09d0-4d13-af9b-a4ef5ebe68cf
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Adversary-in-the-Middle]]'
---
# Export-Session-Cookies-Post-2FA

## Summary

This procedure extracts session cookies from a browser after successful 2FA authentication on HackerOne, enabling their reuse to bypass 2FA in other sessions.

## Description

Following 2FA completion, session cookies (e.g., _hackerone_session) are stored in the browser without additional binding. This procedure uses a cookie editor to export these for transfer. The attack scenario involves an attacker with initial access capturing cookies via MitM or direct export. Target is the HackerOne web app; outcomes include portable authentication data for impersonation.

## Requirements

1. Active 2FA-authenticated session in browser
2. Browser extension for cookie management (e.g., EditThisCookie for Chrome)
3. Knowledge of domain-specific cookies (hackerone.com)

## Defense

Defensive measures and detection strategies:

- Enforce HttpOnly and Secure flags on cookies to limit client-side access
- Implement cookie encryption or signing to detect tampering
- Log cookie access attempts and monitor for export patterns in browser extensions

## Objectives

1. Capture all relevant session cookies post-2FA
2. Export in a transferable format (JSON/text)
3. Enable reuse without re-authentication

## Instructions

### Step 1: Inspect Session Cookies

**Context**: Identify authentication-related cookies in the active session.

- Open browser developer tools (F12).
- Navigate to Application/Storage > Cookies > https://hackerone.com.
- Note keys like _session_id or auth tokens.

> Lists all cookies with values; focus on those set during login.

### Step 2: Export Cookies Using Editor Tool

**Context**: Use extension to copy cookies for external use.

- Install and activate [[tools/Browser-Cookie-Editor]].
- Click the extension icon on the HackerOne page.
- Select all cookies and export as JSON or clipboard copy.

> Generates a file or text with name=value pairs, e.g., {"_hackerone_session": "value"}.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]] Credential Access

### Techniques

- [[Adversary-in-the-Middle]] Adversary-in-the-Middle

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Browser-Cookie-Editor]]

## Tags

- cookie-export
- session-theft
