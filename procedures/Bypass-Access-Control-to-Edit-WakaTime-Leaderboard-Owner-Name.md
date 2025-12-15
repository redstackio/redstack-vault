---
tags:
  - access-bypass
  - waktime
  - edit-owner
  - ui-bypass
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
updated_at: '2025-12-14T17:28:59.276Z'
skill_level: intermediate
impact_level: medium
detection_risk: high
sub_techniques: []
id: 100a20ab-1063-4243-a4c1-c65dd8cea75b
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Bypass-Access-Control-to-Edit-WakaTime-Leaderboard-Owner-Name

## Summary

This procedure exploits an access control flaw in WakaTime, allowing a member to modify the owner's name despite receiving a forbidden error, due to incomplete validation in the edit feature.

## Description

The vulnerability arises from inadequate role-based permission enforcement in the private leaderboard's members/settings page. After role transfer, a member can attempt to edit the owner's name, initially failing with an error, but a subsequent interaction reveals the change was applied, likely via a race condition or backend persistence issue. Targets WakaTime web app; requires prior role setup. Outcome: Unauthorized owner detail modification, risking confusion or escalation.

## Requirements

1. WakaTime account with member privileges in a private leaderboard
2. Owner account with editable name field
3. Web browser to interact with UI elements

## Defense

Defensive measures and detection strategies:

- Implement server-side validation for all edit operations
- Use consistent permission checks on frontend and backend
- Monitor for discrepancies between UI errors and data changes
- Log edit attempts with role context for review

## Objectives

1. Attempt unauthorized edit to trigger the bypass
2. Confirm persistence of change via re-interaction
3. Achieve modification of protected owner data

## Instructions

### Step 1: Attempt Name Edit

**Context**: From member account, try to edit owner's name to test controls.

Log in as member (account A), go to members section, click edit on owner (B)'s name, enter 'testing', submit.

> Expected output: Forbidden error message, no visible change.

### Step 2: Re-Attempt to Confirm Bypass

**Context**: Repeat the action to expose the applied change.

Click edit button again on owner's name.

> Expected output: Popup shows 'Enter new name for testing', confirming backend application.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[access-bypass]]
- [[waktime]]
- [[edit-owner]]
