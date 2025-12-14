---
tags:
  - cookie-theft
  - session-hijacking
type: procedure
tools:
  - '[[tools/EditThisCookie]]'
tactics:
  - '[[Credential Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Steal Web Session Cookie]]'
updated_at: '2025-12-14T17:24:47.877Z'
sub_techniques: []
id: 203af611-596a-4848-af18-be444a98a251
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Steal Web Session Cookie]]'
---
# Steal Victim's Session Cookies

## Summary

This procedure outlines methods to extract active session cookies from a victim's browser during an authenticated session on the HackerOne platform, enabling subsequent session hijacking.

## Description

In the context of the HackerOne vulnerability, session cookies are critical for maintaining authenticated access. Attackers can steal these via techniques like XSS injection, man-in-the-middle attacks, malware, or physical access to the victim's device. The stolen cookies allow impersonation without needing credentials or 2FA. This targets the web session on https://hackerone.com/, where cookies like _h1_session persist server-side.

## Requirements

1. Access to victim's browser or network traffic (e.g., via phishing or compromised endpoint)
2. Tools for cookie extraction (browser dev tools or extensions)
3. Knowledge of the target domain (hackerone.com)

## Defense

Defensive measures and detection strategies:

- Implement HttpOnly and Secure flags on cookies to prevent client-side access
- Use short session timeouts and invalidate on new logins
- Monitor for anomalous logins from new IPs or user agents

## Objectives

1. Extract valid session cookies from victim's browser
2. Prepare cookies for import into attacker's environment
3. Enable persistent access bypassing re-authentication

## Instructions

### Step 1: Access Victim's Browser Session

**Context**: Gain temporary access to the victim's device or intercept traffic while they are logged into https://hackerone.com/.

No specific command; use browser developer tools (F12 > Application > Cookies) to view and copy session cookies like _h1_session.

> Expected output: List of cookies with names, values, and domains. Copy the session-related ones.

### Step 2: Export Cookies

**Context**: Save the cookies in a format suitable for import, such as JSON or plain text.

Use manual copy or a script to export. For example, in Chrome DevTools, right-click and export.

> Expected output: Cookie data file or clipboard content ready for transfer to attacker's browser.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]] Credential Access

### Techniques

- [[Steal Web Session Cookie]] Steal Web Session Cookie

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/EditThisCookie]]

## Tags

- [[cookie-theft]]
- [[session-hijacking]]
