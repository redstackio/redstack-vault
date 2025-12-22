---
id: proc-uuid-2
tags:
  - session-revocation
  - logout
  - web-settings
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:25:53.656Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Revoke-HackerOne-Session

## Summary

This procedure revokes the current user session on HackerOne via the settings page, simulating session expiration and confirming invalidation for standard HTTP requests while highlighting the GraphQL-specific flaw.

## Description

Targeted at HackerOne's session management, this procedure accesses the sessions page to revoke the active session, leading to logout. It demonstrates that while standard sessions are invalidated, GraphQL authorizations persist. The environment is the web platform at https://hackerone.com. Prerequisites are an active authenticated session. Outcomes include confirmed logout, setting up for replay validation.

## Requirements

1. Active authenticated session on HackerOne
2. Direct access to https://hackerone.com/settings/sessions
3. No additional tools required

## Defense

Defensive measures and detection strategies:

- Ensure session revocation invalidates all token types, including GraphQL-specific ones
- Log and alert on session revocation events for anomaly detection
- Implement token blacklisting or short-lived JWTs for API sessions

## Objectives

1. Invalidate the current session via UI
2. Verify logout for standard requests
3. Prepare for testing GraphQL persistence

## Instructions

### Step 1: Access Sessions Management Page

**Context**: Navigate to the session settings to view active sessions.

In the browser, go to https://hackerone.com/settings/sessions.

> Expected output: List of active sessions displayed, including the current one.

### Step 2: Revoke Current Session

**Context**: Select and destroy the active session.

Click on the current session and select 'Revoke' or 'Destroy' option.

> Expected output: Confirmation message; session token invalidated for UI.

### Step 3: Observe Logout

**Context**: Confirm session expiration by checking access.

Attempt to navigate to a protected page; expect redirection.

> Expected output: Redirected to https://hackerone.com/login, confirming revocation.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- session-revocation
- logout
- hackerone-settings
