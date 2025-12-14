---
tags:
  - session-persistence
  - 2fa-bypass
  - verification
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
updated_at: '2025-12-14T17:24:47.434Z'
skill_level: beginner
impact_level: high
detection_risk: medium
sub_techniques: []
id: b94143a6-2404-4b20-a43b-a19a2fb92227
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Verify-Persistent-Session-on-Second-Device

## Summary

This procedure tests whether an existing session on a secondary device remains valid after 2FA activation on the primary device, exposing the session management vulnerability in CS Money.

## Description

By reloading pages on Device B without re-authentication, this step demonstrates the core flaw: lack of session invalidation upon MFA enablement. In an attack narrative, an intruder with prior session access can continue operations undetected. The environment is the CS Money web platform; prerequisites include pre-existing login on Device B and recent 2FA activation. Expected outcome: Unauthorized access persists, bypassing 2FA.

## Requirements

1. Pre-established session on Device B before 2FA enablement
2. 2FA confirmed active on the account
3. No manual logout on Device B

## Defense

Defensive measures and detection strategies:

- Implement server-side session termination on security events like 2FA enable
- Use short session timeouts and force re-auth for sensitive actions
- Monitor for session anomalies across devices post-MFA changes

## Objectives

1. Confirm session activity without 2FA intervention
2. Highlight the bypass potential for existing access
3. Validate the vulnerability's impact on account security

## Instructions

### Step 1: Return to Secondary Device

**Context**: Resume interaction on the untouched session.

Switch to Device B and ensure the browser is still on https://cs.money/ with the prior login state.

> The session cookies or tokens should remain intact.

### Step 2: Reload and Access Content

**Context**: Trigger any potential session checks via page refresh.

Reload the dashboard or any account page (e.g., press F5 or Ctrl+R). Attempt basic actions like viewing balance.

> If the page loads and actions succeed without 2FA, the bypass is confirmed, indicating the flaw.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[session-persistence]]
- [[2fa-bypass]]
- [[verification]]
