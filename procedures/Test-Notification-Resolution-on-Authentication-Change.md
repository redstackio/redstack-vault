---
id: d4e5f6g7-h8i9-0123-defg-456789012345
tags:
  - information-disclosure
  - authentication-testing
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:29:09.357Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Account Discovery]]'
---
# Test Notification Resolution on Authentication Change

## Summary

This procedure interacts with unauthorized notifications and tests resolution by logging out and back in, confirming the issue ties to session cache.

## Description

Clicking unauthorized notifications reveals access limits (e.g., 404 errors), while logout/login forces cache refresh, resolving the leak. This demonstrates the flaw's session-specific nature and aids in scoping impact. Web-focused; outcomes validate temporary privacy exposure.

## Requirements

1. Observed persistent unauthorized notifications
2. Ability to log out/in to HackerOne
3. Browser session management

## Defense

Defensive measures and detection strategies:

- Tie cache keys strictly to session IDs
- Audit authentication flows for cache bypasses
- Alert on mismatched user-notification accesses

## Objectives

1. Assess interaction limits on leaked data
2. Verify resolution via auth cycle
3. Confirm non-persistent nature post-fix

## Instructions

### Step 1: Interact with Notifications

**Context**: Click unauthorized entries to test access depth.

Select and click a foreign notification in the feed.

> Expect 'page not found' error, indicating partial leak (metadata only).

### Step 2: Log Out and Log In

**Context**: Break session to invalidate cache.

Navigate to logout, then re-authenticate with credentials.

> Feed should normalize, removing unauthorized items.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Account Discovery]] Account Discovery

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[information-disclosure]]
- [[authentication-testing]]
- [[privacy-leak]]
