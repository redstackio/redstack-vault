---
tags:
  - auth-bypass
  - account-takeover
type: procedure
tools:
  - '[[tools/Google-Authenticator]]'
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
updated_at: '2025-12-14T17:25:18.047Z'
skill_level: intermediate
impact_level: critical
detection_risk: medium
sub_techniques: []
id: 22608648-87b2-46b4-bd77-50caa0aaa5b2
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Generate-and-Use-TOTP-Codes-for-Bypass

## Summary

This procedure uses the TOTP app to generate and submit valid 2FA codes during critical account actions, bypassing protections and enabling full compromise such as email changes or deletion.

## Description

With the secret imported, the attacker triggers 2FA-protected endpoints (e.g., email update or account deletion) and supplies fresh TOTP codes from the app. The server validates them as legitimate due to the secret match, allowing unauthorized actions. Prerequisites: Active session and functional TOTP generator. Outcomes: Successful high-privilege operations, resulting in account takeover.

## Requirements

1. Active Algolia session from prior steps
2. Google Authenticator with imported secret generating codes
3. Access to protected endpoints (e.g., /account/email, /account/delete)

## Defense

Defensive measures and detection strategies:

- Implement server-side checks for TOTP drift and rate-limit code submissions
- Log and alert on sensitive actions like email changes or deletions, correlating with session origins
- Enforce multi-factor beyond TOTP, such as biometrics or recovery questions

## Objectives

1. Generate timely TOTP codes for submission
2. Bypass 2FA on critical endpoints
3. Complete account compromise actions

## Instructions

### Step 1: Navigate to Protected Action

**Context**: Select a high-impact endpoint requiring 2FA.

No specific command; From the account dashboard, go to settings for email update, recovery codes, or deletion.

> Page loads with 2FA prompt after initiating the action.

### Step 2: Generate and Submit Code

**Context**: Use the app to provide a valid code.

No specific command; Open Google Authenticator, note the current 6-digit code, and enter it into the 2FA field on the web page. Submit.

> Server accepts if code is within time window; action proceeds.

### Step 3: Confirm Compromise

**Context**: Verify the action's success.

No specific command; Check for confirmation messages, e.g., 'Email updated successfully' or account deletion notice.

> Full control achieved; repeat for multiple actions if needed.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Google-Authenticator]]

## Tags

- auth-bypass
- account-takeover
