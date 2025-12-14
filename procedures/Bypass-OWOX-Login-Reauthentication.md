---
tags:
  - bypass
  - authentication-bypass
  - web
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Valid Accounts]]'
skill_level: low
impact_level: high
detection_risk: high
sub_techniques: []
id: 21d1c7ba-d310-4d3e-b758-427ab8be4a18
created_at: '2025-12-14T17:31:19.563Z'
updated_at: '2025-12-14T17:31:19.563Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Bypass-OWOX-Login-Reauthentication

## Summary

This procedure exploits the session management flaw to access the OWOX portal without re-entering credentials after logout, achieving full authentication bypass.

## Description

Due to incomplete session invalidation, clicking Sign In post-logout uses residual data (e.g., browser cache or unexpired cookies) to replay the session, granting unauthorized access. This leads to account takeover risks, allowing data exfiltration or malicious actions.

## Requirements

1. Prior logout with persistent artifacts
2. Same browser session
3. No credential clearing (e.g., no incognito)

## Defense

Defensive measures and detection strategies:

- Clear all client-side session data on logout
- Implement server-side session blacklisting
- Detect and alert on session reuse post-logout

## Objectives

1. Gain unauthorized access
2. Demonstrate account takeover potential
3. Validate vulnerability impact

## Instructions

### Step 1: Return to Portal

**Context**: Re-initiate the sign-in process.

Navigate back to https://support.owox.com/hc/ after logout.

> Login page loads.

### Step 2: Click Sign In

**Context**: Trigger the flawed re-auth flow.

Click the Sign In button without selecting or entering any credentials.

> System fails to prompt for Gmail OAuth.

### Step 3: Access Dashboard

**Context**: Confirm bypass success.

Observe automatic redirect to authenticated areas.

> Full account access without credentials.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[bypass]]
