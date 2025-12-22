---
tags:
  - logout
  - session-invalidation
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
impact_level: medium
detection_risk: low
sub_techniques: []
id: 319cad8d-7892-4970-8e38-de4dc450f576
created_at: '2025-12-14T17:31:19.566Z'
updated_at: '2025-12-14T17:31:19.566Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Logout-from-OWOX-Portal-and-Gmail

## Summary

This procedure performs a logout from both the OWOX portal and the associated Gmail session to trigger invalidation, which fails due to the broken session management.

## Description

Logging out from the portal should clear local sessions, and Gmail logout revokes OAuth tokens. However, the vulnerability leaves residual data (e.g., cookies or cached tokens) that allows bypassing re-auth. This step is crucial to expose the flaw by simulating a complete termination.

## Requirements

1. Active OWOX and Gmail sessions
2. Web browser
3. Access to account settings

## Defense

Defensive measures and detection strategies:

- Fully invalidate all session tokens and cookies on logout
- Coordinate OAuth revocation with identity provider
- Audit logout events for incomplete terminations

## Objectives

1. Attempt complete session termination
2. Expose invalidation failure
3. Set up for bypass testing

## Instructions

### Step 1: Logout from OWOX

**Context**: End the portal session.

Locate the Logout button in the portal (e.g., user menu) and click it.

> Redirect to login page with confirmation.

### Step 2: Logout from Gmail

**Context**: Revoke OAuth access separately.

Visit https://accounts.google.com/, go to Security > Third-party apps, or simply sign out from Gmail.

> Gmail shows signed-out state; revoke OWOX if listed.

### Step 3: Verify Logout

**Context**: Confirm both are terminated.

Attempt to access a portal page; it should prompt login. Check Gmail login status.

> Both show unauthenticated states.

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
