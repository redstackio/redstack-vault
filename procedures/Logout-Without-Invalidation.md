---
tags:
  - logout
  - session
type: procedure
tools: []
tactics:
  - '[[Defense Evasion]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:31:42.643Z'
sub_techniques: []
id: df8e52f8-6fca-4ab8-9daa-60f8ad8d4afc
validated: true
mitre_tactics:
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Logout-Without-Invalidation

## Summary

This procedure performs a user logout in the HackerOne application, which fails to invalidate server-side session tokens, leaving cookies reusable for hijacking.

## Description

In vulnerable session management, logout only clears client-side state but does not expire or revoke cookies server-side. This targets OWASP A2 Broken Authentication flaws. Prerequisites: Active session. Outcome: Apparent logout with persistent cookies.

## Requirements

1. Active authenticated session
2. Access to logout functionality in the app

## Defense

Defensive measures and detection strategies:

- Server-side session destruction on logout (e.g., delete token from store)
- Immediate cookie expiration or invalidation headers on logout response
- Audit logs for logout events followed by unauthorized re-access

## Objectives

1. Simulate victim logout
2. Preserve cookies for reuse test
3. Expose persistence flaw

## Instructions

### Step 1: Initiate Logout

**Context**: Trigger the logout action to end the session.

No command; app action:

1. Navigate to user profile or settings in HackerOne
2. Click 'Logout' button

> Redirects to login page; session appears terminated.

### Step 2: Confirm Logout State

**Context**: Verify no access to protected areas.

Attempt to access dashboard.

> Expected: Prompted for login; cookies still in browser but session invalid (in secure impl.).

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion]] Defense Evasion

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[logout]]
- [[session]]
