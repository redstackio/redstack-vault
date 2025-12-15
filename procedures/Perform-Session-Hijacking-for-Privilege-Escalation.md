---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567893
name: Perform-Session-Hijacking-for-Privilege-Escalation
tags:
  - session-hijacking
  - privilege-escalation
  - web-session
type: procedure
tools: []
tactics:
  - '[[Credential Access]]'
  - '[[Privilege Escalation]]'
commands: []
verified: false
platforms:
  - Linux
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Steal Web Session Cookie]]'
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T17:28:52.039Z'
sub_techniques:
  - '[[T1539.001]]'
validated: true
mitre_tactics:
  - '[[Credential Access]]'
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Steal Web Session Cookie]]'
  - '[[Exploitation for Privilege Escalation]]'
---
# Perform-Session-Hijacking-for-Privilege-Escalation

## Summary

This procedure hijacks an admin session in Ubiquiti EdgeOS using stolen session data from file-system exposure, escalating privileges from operator to root access and enabling full system compromise.

## Description

Session management in EdgeOS lacks adequate protections, allowing hijacked cookies or tokens from read-only sessions to impersonate admin users. This leads to root-level control over the router, including configuration changes and potential network pivoting. Prerequisites include extracted session data from the file-system exploit.

## Requirements

1. Extracted admin session cookie or token from prior procedure
2. Active browser session on the target interface
3. Understanding of cookie manipulation via dev tools

## Defense

Defensive measures and detection strategies:

- Use secure, HTTP-only, and SameSite cookies for sessions
- Implement session IP binding and timeout enforcement
- Monitor for session anomalies like sudden privilege changes in access logs

## Objectives

1. Inject hijacked session data into the current browser
2. Escalate to admin/root privileges
3. Validate full system access

## Instructions

### Step 1: Inspect Current Session

**Context**: Examine the operator session to identify cookie fields for replacement.

Open browser dev tools (F12), go to Application/Storage > Cookies, and note the session cookie name (e.g., EDGEOS_SESSION).

> Expected output: List of current cookies, including the operator session ID.

### Step 2: Replace with Hijacked Data

**Context**: Substitute the admin session token to assume elevated identity.

Edit the session cookie value with the extracted admin token. Set domain and path to match the EdgeOS interface.

> Expected output: Cookie updated without errors; session persists.

### Step 3: Refresh and Escalate

**Context**: Reload the interface to apply the hijacked session and gain root access.

Refresh the dashboard page and attempt admin-only actions, such as editing configurations or accessing shell.

> Expected output: Full admin dashboard with editable options and root command execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]] Credential Access
- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Steal Web Session Cookie]] Steal Web Session Cookie
- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation

### Sub-Techniques

- [[T1539.001]] Steal Web Session Cookie: Cookie Theft

## Commands Used


## Tools Used


## Tags

- [[session-hijacking]]
- [[privilege-escalation]]
- [[web-session]]
