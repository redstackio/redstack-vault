---
tags:
  - logout
  - persistence
  - uber
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
updated_at: '2025-12-14T17:31:10.975Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: fdbd7ee7-1da0-4da8-9eb5-39e471eaead3
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Verify-Access-After-Logout

## Summary

This procedure confirms the URL token's non-expiration by accessing settings after logging out, proving persistent unauthorized access.

## Description

Logging out terminates the session, but the URL token remains valid, allowing continued modifications. This targets Uber's auth misconfiguration; requires the copied URL. Outcome: Demonstration of indefinite access risk.

## Requirements

1. Copied URL from settings
2. Original session active for logout
3. Ability to change password (optional)

## Defense

Defensive measures and detection strategies:

- Invalidate tokens on logout
- Tie tokens to sessions
- Alert on post-logout accesses

## Objectives

1. Terminate session
2. Retest URL access
3. Confirm token persistence

## Instructions

### Step 1: Log Out Original Session

**Context**: End authentication to simulate real-world separation.

From the dashboard, click the profile icon and select "Log out."

> Confirm logout by attempting to access a protected page, which should redirect to login.

### Step 2: Reload URL Post-Logout

**Context**: Validate token independence.

In the new browser, paste and load the URL again. Change a notification setting and save.

> Changes apply without re-auth; optionally change password in another session and retest.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[logout]]
- [[Persistence]]
- [[uber]]
