---
id: proc-002
tags:
  - membership-removal
  - session-testing
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
updated_at: '2025-12-14T17:28:52.145Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Simulate-Crew-Kickout

## Summary

This procedure simulates the removal of a member from a crew to test whether the session is invalidated, highlighting potential authorization issues.

## Description

Crew administrators can remove members via the platform's admin interface. This step assumes coordination with an admin or self-administration if possible. The key is to observe that session tokens persist without re-verification of membership status, allowing continued access. This is performed in a web browser to maintain the exact session context.

## Requirements

1. Access to a crew administrator account
2. Active membership in the target crew
3. Same browser session as initial join

## Defense

Defensive measures and detection strategies:

- Invalidate sessions immediately upon membership changes
- Add server-side checks for current status on every action
- Alert admins on unauthorized post-removal actions

## Objectives

1. Remove account from crew membership
2. Preserve the existing session for testing
3. Confirm non-member status via profile or UI

## Instructions

### Step 1: Access Admin Panel

**Context**: Log in as crew admin to initiate removal.

Navigate to the crew management section and select the member for removal.

> Expected: Admin interface loads with member list.

### Step 2: Execute Kickout

**Context**: Perform the removal action.

Click the remove/kick button for the target member and confirm.

> Expected: Confirmation of removal and updated member list.

### Step 3: Verify Removal Status

**Context**: Check that membership is revoked without session logout.

As the removed user, refresh the crew page or check profile.

> Expected: Status shows as non-member, but session remains logged in.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[membership-removal]]
- [[session-testing]]
