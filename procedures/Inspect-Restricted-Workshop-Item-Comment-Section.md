---
id: proc-steam-inspect-restricted
tags:
  - idor
  - steam
  - workshop
  - recon
type: procedure
tools:
  - '[[tools/Firefox-Quantum]]'
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:29.177Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Inspect-Restricted-Workshop-Item-Comment-Section

## Summary

This procedure involves navigating to a Steam Workshop item tied to a game not owned by the user, confirming the comment posting restriction to validate the target for IDOR exploitation.

## Description

By selecting a specific workshop item (e.g., ID 1404861377) without owning the associated game, the UI disables comment posting, highlighting the access control. This reconnaissance step identifies the vulnerability scope without any server-side interaction beyond page load.

## Requirements

1. Access to Steam Workshop from previous login
2. Knowledge of a target item ID for a non-owned game
3. Browser with developer tools optional for UI inspection

## Defense

Defensive measures and detection strategies:

- Enforce client-side checks with server validation
- Log access to restricted item pages

## Objectives

1. Confirm ownership-based restriction
2. Note existing comment count for later use
3. Identify target IDs

## Instructions

### Step 1: Select Target Item

**Context**: Choose and load a restricted workshop item.

In the browser, navigate to https://steamcommunity.com/sharedfiles/filedetails/?id=1404861377.

> Page loads with item details.

### Step 2: Examine Comment Section

**Context**: Verify the disabled posting functionality.

Scroll to the comments area; observe that viewing is allowed but the input box is grayed out with an ownership message.

> Restriction confirmed visually.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Firefox-Quantum]]

## Tags

- idor
- recon
- restricted
