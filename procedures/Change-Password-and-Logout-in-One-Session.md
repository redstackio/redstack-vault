---
tags:
  - password-change
  - logout
  - session-invalidation
type: procedure
tools: []
tactics:
  - '[[Persistence]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:31:42.812Z'
sub_techniques: []
id: 9f8ee36e-4454-4fc9-b940-e24188ee250b
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Change Password and Logout in One Session

## Summary

This procedure alters account credentials and terminates a session to trigger expected invalidation of all associated sessions in a web application.

## Description

Password changes and logouts should propagate server-side session destruction to prevent unauthorized persistence. This step targets the primary session in a multi-session setup, using the app's built-in forms. If flawed, other sessions remain active, exposing the vulnerability. Applies to any web app with account management features.

## Requirements

1. Active authenticated session in the target browser
2. Knowledge of current password for change verification
3. Access to account settings page

## Defense

Defensive measures and detection strategies:

- Enforce server-side session destruction on password changes and logouts
- Log all auth events for anomaly detection, e.g., failed logins post-change

## Objectives

1. Update account password to simulate security action
2. Explicitly end the current session
3. Test for global session invalidation

## Instructions

### Step 1: Initiate Password Change

**Context**: Access and modify the account password.

In the primary browser session, navigate to the account settings or security section. Locate the password change form, enter the current password, provide a new strong password, and confirm it. Submit the form to apply the change.

**Expected Output**: Success message confirming password update, possibly with a prompt to log in again.

### Step 2: Perform Logout

**Context**: Terminate the session post-change to reinforce invalidation.

After password confirmation, select the logout button or menu option. This should clear local session data and notify the server.

**Expected Output**: Redirection to the login page, with session ended.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- password-change
- logout
