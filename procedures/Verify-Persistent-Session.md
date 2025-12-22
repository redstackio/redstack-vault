---
tags:
  - session-persistence
  - validation
type: procedure
tools:
  - '[[tools/Mozilla-Firefox]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Local Accounts]]'
updated_at: '2025-12-14T17:31:11.341Z'
sub_techniques: []
id: 6b8aea64-570f-47ca-8b17-b9de23e756a8
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Local Accounts]]'
---
# Verify-Persistent-Session

## Summary

This procedure tests whether an active session remains valid after a password change on another browser, confirming the broken session management vulnerability that enables unauthorized access.

## Description

Post-password change, the application fails to invalidate sessions across browsers, rooted in the disabled session revocation feature in the PHP backend (Airship CMS). This allows attackers to exploit unattended sessions on shared devices, accessing sensitive account data without credentials.

## Requirements

1. Pre-existing session on a separate browser
2. Password already changed on another session
3. Ability to interact with the application interface

## Defense

Defensive measures and detection strategies:

- Centralize session management with database-backed tokens that can be bulk-revoked
- Use heartbeat checks to detect and terminate stale sessions
- Audit logs for session activity post-password changes

## Objectives

1. Confirm no automatic logout after password update
2. Demonstrate continued access to protected resources
3. Validate the vulnerability for reporting or exploitation

## Instructions

### Step 1: Switch to Primary Browser

**Context**: Return to the unaffected browser to check session status.

Activate the first browser (e.g., Firefox) and observe if any logout occurred.

> Expected: No change; user remains logged in.

### Step 2: Refresh Protected Page

**Context**: Force a server interaction to test session validity.

Navigate to `https://bridge.cspr.ng/` or refresh the current page.

> Page loads with user data; session cookie persists in dev tools.

### Step 3: Perform Account Action

**Context**: Execute a privileged operation to ensure full access.

View account details or perform a non-sensitive action.

> Success: Action completes without authentication prompt, confirming persistence.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Local Accounts]] Local Accounts

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Mozilla-Firefox]]

## Tags

- session-persistence
- validation
