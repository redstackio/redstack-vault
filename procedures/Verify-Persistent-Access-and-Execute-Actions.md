---
tags:
  - unauthorized-access
  - profile-edit
  - exploitation
type: procedure
tools: []
tactics:
  - '[[Persistence]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:31:42.807Z'
sub_techniques: []
id: ea1716dc-a499-4f42-a671-413078329c19
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Verify Persistent Access and Execute Actions

## Summary

This procedure tests and exploits persistent sessions by performing authenticated actions in an unaffected browser after invalidation attempts elsewhere.

## Description

With a session flaw confirmed, this exploits the persistence to conduct unauthorized operations, such as account modifications. It highlights the impact on web apps where server-side session handling fails to sync across instances, allowing continued access despite security actions.

## Requirements

1. Confirmed active secondary session post-refresh
2. Knowledge of sensitive features (e.g., profile edit)
3. No interference from the primary session

## Defense

Defensive measures and detection strategies:

- Use centralized session stores with global invalidation (e.g., Redis with pub/sub)
- Alert on concurrent actions from multiple sessions post-auth change

## Objectives

1. Validate ongoing access without re-auth
2. Demonstrate impact through account actions
3. Quantify risk of unauthorized persistence

## Instructions

### Step 1: Attempt Sensitive Operations

**Context**: Perform actions requiring valid authentication to test bounds.

In the secondary browser, navigate to editable areas like the account profile. Attempt changes, such as updating email or name fields, and submit. Alternatively, access any restricted view-only data.

**Expected Output**: Changes save successfully or data displays without auth prompts.

### Step 2: Confirm No Invalidation

**Context**: Re-verify session state after actions.

Refresh the page again or navigate to another authenticated endpoint to ensure persistence holds.

**Expected Output**: Continued access without logout.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- unauthorized-access
- exploitation
