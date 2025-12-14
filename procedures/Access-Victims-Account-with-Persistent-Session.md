---
tags:
  - account-takeover
  - 2fa-bypass
type: procedure
tools:
  - '[[tools/EditThisCookie]]'
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
updated_at: '2025-12-14T17:24:47.871Z'
sub_techniques: []
id: 7893dae4-e59f-4786-a2c6-addc10673c1b
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Access Victim's Account with Persistent Session

## Summary

This procedure demonstrates accessing a victim's HackerOne account using imported persistent session cookies, bypassing 2FA since the old session remains valid server-side after the victim's new login.

## Description

With cookies imported, the attacker navigates to the platform. HackerOne's session management flaw allows the old authenticated session to persist, granting full access without re-authentication. This leads to account takeover, including viewing reports and sensitive data on https://hackerone.com/.

## Requirements

1. Imported stolen cookies in attacker's browser
2. Victim has performed new login (to test persistence)
3. Direct access to https://hackerone.com/

## Defense

Defensive measures and detection strategies:

- Implement automatic session invalidation on new authentications
- Require 2FA for all session initiations, not just logins
- Use behavioral analytics to detect concurrent sessions

## Objectives

1. Gain unauthorized access to victim's account
2. Bypass 2FA via session reuse
3. Perform actions leading to data exfiltration or modification

## Instructions

### Step 1: Navigate to Target

**Context**: Test the persistent session by accessing the protected area.

Open https://hackerone.com/ in the browser with imported cookies. The session should authenticate automatically.

> Expected output: Redirect to dashboard without login prompt.

### Step 2: Verify Access and Perform Actions

**Context**: Confirm full control and execute takeover actions.

Browse to account sections like profile or reports. Change settings or download data to validate.

> Expected output: Successful interactions, e.g., viewing private hackerone reports.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/EditThisCookie]]

## Tags

- [[account-takeover]]
- [[2fa-bypass]]
