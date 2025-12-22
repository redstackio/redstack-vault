---
tags:
  - logout-flaw
  - session-management
type: procedure
tools: []
tactics:
  - '[[Credential Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Steal Web Session Cookie]]'
updated_at: '2025-12-14T17:31:19.371Z'
sub_techniques: []
id: d987e5c3-616d-45b3-b27e-8c14007a206a
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Steal Web Session Cookie]]'
---
# Logout-Without-Invalidating-Session-Cookies

## Summary

This procedure performs a logout action in Coursera, highlighting the failure to invalidate session cookies, which remain usable for unauthorized access.

## Description

Execute the logout function via the web interface, which updates the UI to reflect a logged-out state but does not destroy server-side session data or expire cookies immediately. This leads to a delay in invalidation (up to hours), allowing cookie reuse. Target environment is the authenticated Coursera session. Outcomes include persistent cookies exploitable for session hijacking.

## Requirements

1. Active authenticated session from prior login.
2. Access to logout endpoint or UI button.
3. Browser with cookie inspection capabilities.

## Defense

Defensive measures and detection strategies:

- Enforce immediate cookie expiration and server-side session deletion on logout.
- Use token blacklisting for active sessions.
- Log and alert on post-logout access attempts using the same cookies.

## Objectives

1. Trigger logout without full session termination.
2. Verify cookie persistence post-logout.
3. Expose the vulnerability for exploitation.

## Instructions

### Step 1: Initiate Logout

**Context**: Use the application's logout feature to end the session.

No command; click the logout button or navigate to the logout endpoint (e.g., /logout).

> UI shows logged-out state, but inspect cookies to confirm they remain unchanged.

### Step 2: Validate Persistence

**Context**: Check if cookies are still present and potentially valid.

Use browser developer tools to view cookies for coursera.org.

> Cookies like session tokens are intact, indicating improper invalidation.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]] Credential Access

### Techniques

- [[Steal Web Session Cookie]] Steal Web Session Cookie

### Sub-Techniques


## Commands Used


## Tools Used

