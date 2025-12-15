---
tags:
  - cookie-import
  - session-impersonation
type: procedure
tools:
  - '[[tools/EditThisCookie]]'
tactics:
  - '[[Defense Evasion]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Steal Web Session Cookie]]'
updated_at: '2025-12-14T17:24:47.875Z'
sub_techniques: []
id: c3f7d299-c28f-4aba-9ad4-e354c4f16f53
validated: true
mitre_tactics:
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Steal Web Session Cookie]]'
---
# Import Stolen Cookies into Browser

## Summary

This procedure details importing stolen session cookies into the attacker's browser using a cookie editing extension, allowing session impersonation on HackerOne even after the victim logs out locally and creates a new session.

## Description

After stealing cookies, the attacker uses a browser extension to inject them into their own session. This exploits HackerOne's failure to invalidate old sessions on new logins. The victim clearing history logs them out client-side, but server-side persistence allows the attacker to reuse the cookies. Target: https://hackerone.com/ cookies.

## Requirements

1. Stolen cookie data from victim
2. Browser extension like EditThisCookie installed
3. Attacker's browser pointed to the target domain

## Defense

Defensive measures and detection strategies:

- Enforce session invalidation on logout or new login
- Use device fingerprinting to detect session anomalies
- Log and alert on multiple concurrent sessions

## Objectives

1. Successfully load stolen cookies into attacker's browser
2. Maintain session validity despite victim actions
3. Prepare for unauthorized access

## Instructions

### Step 1: Install and Open Extension

**Context**: Prepare the browser environment for cookie manipulation.

Install [[tools/EditThisCookie]] from the browser store. Navigate to https://hackerone.com/ and open the extension.

> Expected output: Extension interface showing current cookies for the domain.

### Step 2: Import Cookies

**Context**: Add the stolen cookie values to override or add to the current session.

In the extension, click 'Import' and paste the stolen cookie data (e.g., name: _h1_session, value: abc123, domain: .hackerone.com). Save changes.

> Expected output: Confirmation that cookies are set; refresh the page to verify session activation.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion]] Defense Evasion

### Techniques

- [[Steal Web Session Cookie]] Steal Web Session Cookie

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/EditThisCookie]]

## Tags

- [[cookie-import]]
- [[session-impersonation]]
