---
id: proc-uuid-3
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
techniques: []
updated_at: '2025-12-14T17:27:42.621Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
---
# Sign-Out-to-Prepare-for-CSRF

## Summary

This procedure logs out the current session to reset the state for testing the login CSRF vulnerability.

## Description

After injecting the XSS payload, signing out ensures the login form is accessible in an unauthenticated state, allowing interception and PoC generation for CSRF exploitation.

## Requirements

1. Active authenticated session
2. Access to logout functionality

## Defense

Defensive measures and detection strategies:

- Secure logout by invalidating session tokens server-side
- Rate-limit login attempts post-logout

## Objectives

1. Terminate current session
2. Return to login state
3. Prepare for CSRF testing

## Instructions

### Step 1: Initiate Logout

**Context**: End the session after payload injection.

Click the 'Sign out' or 'Logout' button in the application.

> Expected: Redirect to login page, session cleared.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques


### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[logout]]
- [[web]]
