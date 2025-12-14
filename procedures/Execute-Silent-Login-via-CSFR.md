---
id: proc-execute-silent-login
tags:
  - silent-login
  - session-hijack
  - csrf-execution
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
  - '[[Drive-by Compromise]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:15.326Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
  - '[[Exploit Public-Facing Application]]'
---
# Execute-Silent-Login-via-CSFR

## Summary

This procedure executes the CSRF PoC to silently authenticate the victim's browser session to the attacker's Infogram account, exploiting the absence of CSRF tokens and session prompts for undetected takeover.

## Description

With the victim logged into their own account, loading the PoC triggers a cross-site POST to the login endpoint using attacker credentials. Due to no token validation, the server processes it in the victim's session context, overwriting authentication without UI changes or warnings. The session persists until manual logout or expiry, allowing further exploitation. This targets web platforms vulnerable to login CSRF, leading to account confusion and unauthorized actions.

## Requirements

1. Victim's browser with active Infogram session
2. Deployed CSRF PoC accessible to victim
3. Same browser instance for session sharing

## Defense

Defensive measures and detection strategies:

- Enforce CSRF tokens on login forms
- Add confirmation prompts for logins from unusual contexts
- Log and alert on session changes without explicit user action

## Objectives

1. Force victim session into attacker's account
2. Maintain stealth without visual indicators
3. Enable subsequent session-based attacks

## Instructions

### Step 1: Prepare Victim Session

**Context**: Ensure the victim is authenticated in their account to provide the session for hijacking.

Have the victim log into Infogram normally and keep the tab/session open.

**Expected Output**: Active victim session cookies present.

### Step 2: Trigger PoC Interaction

**Context**: Lure the victim to load and submit the PoC in the same browser.

Send the PoC link disguised as Infogram content. Upon load, the hidden form auto-submits the forged login.

**Expected Output**: POST request sent; no error in console.

### Step 3: Verify Silent Switch

**Context**: Confirm the session has switched without alerting the victim.

In dev tools, inspect cookies or attempt a low-impact action (e.g., view profile) – it should reflect attacker's data. Avoid refresh to keep stealth.

**Expected Output**: Session now tied to attacker account.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[silent-login]]
- [[session-hijack]]
- [[csrf-execution]]
