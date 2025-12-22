---
tags:
  - role-transfer
  - waktime
  - ownership
  - privilege-escalation
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:28:59.278Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 50db9f4d-0ffc-445b-b2a6-734fece27dc4
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Transfer-Ownership-in-WakaTime-Leaderboard

## Summary

This procedure demonstrates transferring ownership roles within a WakaTime private leaderboard, demoting the original owner to member and promoting another to owner, which sets the stage for access control testing.

## Description

Role management in WakaTime leaderboards allows owners to assign privileges, but this can be abused in vulnerability scenarios. The procedure targets the members/settings page, updating roles via the UI. Prerequisites include existing membership in a private leaderboard. The outcome is a role reversal, enabling tests for unauthorized actions by the demoted account.

## Requirements

1. Access to WakaTime private leaderboard as current owner
2. At least two member accounts in the leaderboard
3. Web browser session logged in as owner

## Defense

Defensive measures and detection strategies:

- Require confirmation for ownership transfers
- Audit logs for role changes with alerts on frequent modifications
- Enforce multi-factor approval for privilege escalations

## Objectives

1. Switch owner and member roles
2. Verify role enforcement in the application
3. Prepare for privilege bypass testing

## Instructions

### Step 1: Access Members Settings

**Context**: Navigate to the role management interface.

Log in as current owner (account A), go to 'test1' leaderboard, select members/settings tab.

> Expected output: List of members with current roles displayed.

### Step 2: Update Roles

**Context**: Assign new owner and demote original.

Edit account B to owner role, edit account A to member role, save changes.

> Expected output: Updated roles visible in the members list.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[role-transfer]]
- [[waktime]]
- [[ownership]]
