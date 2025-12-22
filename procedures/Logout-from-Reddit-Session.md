---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567892
tags:
  - logout
  - session
  - web
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:33:24.119Z'
skill_level: low
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
---

# Logout-from-Reddit-Session

## Summary

This procedure terminates the active Reddit session after initial account creation, clearing any session-based state to enable re-authentication via OAuth.

## Description

Following account creation, logging out ensures that the next login attempt treats the OAuth flow as a fresh authentication, exploiting the lack of email ownership verification in Reddit's system. This is a standard web action via the user interface.

## Requirements

1. Active logged-in session on Reddit
2. Web browser access

## Defense

Defensive measures and detection strategies:

- Log session terminations and correlate with subsequent logins from same IP
- Implement session binding to OAuth tokens for continuity checks

## Objectives

1. End current session without deleting account linkage
2. Prepare for OAuth re-login
3. Avoid session hijacking interference

## Instructions

### Step 1: Access User Menu

**Context**: Locate and use the logout functionality.

Click on the user avatar or username in the top-right corner of Reddit to open the menu.

> Select "Log Out" from the dropdown.

### Step 2: Confirm Session End

**Context**: Verify logout success.

You should be redirected to the homepage or login page, with no access to account features.

> Check by attempting to access /u/username – it should prompt login.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- logout
- session
- web

---
