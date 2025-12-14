---
tags:
  - logout
  - cookie-clearing
  - session-invalidation
type: procedure
tools:
  - '[[tools/Cookies-Manager-Plus]]'
tactics:
  - '[[Defense Evasion]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Steal Web Session Cookie]]'
updated_at: '2025-12-14T17:33:12.457Z'
sub_techniques: []
id: 23056f5b-bbde-4fdb-8fe8-76914dd144ee
validated: true
mitre_tactics:
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Steal Web Session Cookie]]'
---
# Logout-and-Clear-Local-Cookies

## Summary

This procedure logs out from the target site and clears local browser cookies to end the legitimate session, highlighting the vulnerability where server-side cookies are not invalidated.

## Description

On https://micropurchase.18f.gov/, logout only removes client-side session traces but fails to expire server cookies tied to GitHub OAuth. Using a cookie manager, all domain-specific cookies are deleted, simulating a clean post-logout state. This step is crucial to demonstrate that reinjected cookies can revive the session, leading to takeover.

## Requirements

1. Active session from prior steps
2. Browser extension for cookie management
3. Access to the site's logout functionality

## Defense

Defensive measures and detection strategies:

- Ensure logout triggers immediate server-side token revocation and cookie invalidation
- Use one-time-use tokens or short-lived JWTs for sessions
- Detect rapid login/logout cycles or cookie manipulations

## Objectives

1. Terminate the local session without server invalidation
2. Clear browser state to test cookie persistence
3. Prepare environment for hijacking verification

## Instructions

### Step 1: Perform Logout

**Context**: Initiate site logout to remove session.

Click the logout button on https://micropurchase.18f.gov/.

> Expected: Redirect to login page; no account access.

### Step 2: Clear Site Cookies

**Context**: Manually delete all remaining cookies for the domain.

Use [[tools/Cookies-Manager-Plus]] to select and delete cookies for micropurchase.18f.gov.

> Expected: Empty cookie list for the domain in browser tools.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion]] Defense Evasion

### Techniques

- [[Steal Web Session Cookie]] Steal Web Session Cookie

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Cookies-Manager-Plus]]

## Tags

- [[logout]]
- [[cookie-clearing]]
- [[session-invalidation]]
