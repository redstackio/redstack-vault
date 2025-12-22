---
id: proc-phabricator-session-rotate-001
name: Rotate-Phabricator-Session
tags:
  - csrf
  - session-management
  - phabricator
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:03.795Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Rotate-Phabricator-Session

## Summary

This procedure involves logging out and re-authenticating to Phabricator to rotate the session, demonstrating that the CSRF token remains valid due to its timer-based rotation mechanism.

## Description

Phabricator's CSRF tokens are not bound to sessions, allowing them to persist after logout. By logging out and back in, a new session is created, but the old token stays active until its timer expires. This procedure tests token persistence in a web environment, highlighting the vulnerability for subsequent replay attacks.

## Requirements

1. Extracted CSRF token from prior procedure
2. Valid Phabricator credentials
3. Web browser access to the instance

## Defense

Defensive measures and detection strategies:

- Bind tokens to session IDs and regenerate on login/logout
- Use one-time-use tokens for sensitive actions
- Log session changes and token usage anomalies

## Objectives

1. Invalidate the current session via logout
2. Establish a new session via re-authentication
3. Confirm old token is not invalidated

## Instructions

### Step 1: Perform Logout

**Context**: End the current session to simulate token detachment.

Navigate to the logout option in Phabricator (e.g., user menu) and click to log out. Wait 1-2 minutes to allow any timer checks.

> Expected output: User is redirected to login page; session cookies are cleared.

### Step 2: Re-Authenticate

**Context**: Create a new session to check token behavior.

Log back in using the same credentials. Inspect a new form to note if a new token is generated (it should be the same or similar due to timer).

> Expected output: New session active; compare new token to old—old remains usable as per vulnerability.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[phabricator]]
