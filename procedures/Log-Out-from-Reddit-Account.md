---
tags:
  - logout
  - session-management
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:32:58.379Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 83f455e3-11d4-4d97-bbda-54cd876edbb2
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Log Out from Reddit Account

## Summary

This procedure ends the active session on a Reddit account created or accessed via Google OAuth, preparing for the next phase of testing duplicate email registration without session interference.

## Description

After logging in via OAuth, this step performs a standard logout from the Reddit interface. The backend email association persists, but the session is cleared, allowing fresh registration attempts. This highlights the lack of session-based email locking in the system. Performed manually in a web browser.

## Requirements

1. Active Reddit session from prior OAuth login
2. Web browser
3. No additional credentials needed

## Defense

Defensive measures and detection strategies:

- Log session terminations and correlate with subsequent registrations
- Implement session tokens that enforce email uniqueness during active periods
- Audit logout events for patterns indicating vulnerability probing

## Objectives

1. Clear the current session
2. Maintain email association for duplicate testing
3. Enable registration without authentication conflicts

## Instructions

### Step 1: Access Account Menu

**Context**: Locate the logout option in the user interface.

From the Reddit dashboard, click on the user avatar or profile menu in the top-right corner.

> This opens the account options dropdown.

### Step 2: Initiate Logout

**Context**: Execute the logout action to end the session.

Select "Log Out" from the menu.

> Expected output: Immediate redirect to the login page with no active session.

### Step 3: Verify Logout

**Context**: Confirm the session has ended.

Attempt to access a protected page; you should be redirected to login.

> Expected output: Prompt to log in again, confirming successful logout.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- logout
- session-termination
