---
id: p5e6f7g8-h9i0-1234-efgh-5678901234
tags:
  - session-refresh
  - authentication
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
updated_at: '2025-12-14T17:28:28.746Z'
skill_level: basic
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Refresh-Session-via-Logout-Login

## Summary

This procedure logs out and back into Tumblr to refresh the session, ensuring the injected cookies persist and the DoS effect is confirmed across sessions.

## Description

Session refresh tests cookie persistence post-injection. Targets the login/logout endpoints. Prerequisites: Injected cookies. Expected: Re-login with cookies intact, blocking future auth.

## Requirements

1. Current active session.
2. Valid credentials.
3. Injected malicious cookies.

## Defense

Defensive measures and detection strategies:

- Clear sensitive cookies on logout.
- Detect session anomalies post-login.

## Objectives

1. Terminate current session.
2. Re-establish session to test persistence.
3. Verify cookies survive refresh.

## Instructions

### Step 1: Log Out

**Context**: End the current session.

Click logout from account menu or visit logout endpoint.

> Redirect to login page.

### Step 2: Log Back In

**Context**: Re-authenticate.

Enter credentials at https://www.tumblr.com/.

> Dashboard loads; check dev tools for persistent cookies.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- session-refresh
- authentication
- web

