---
id: proc-coinbase-delete-001
tags:
  - deletion
  - coinbase
type: procedure
tools: []
tactics:
  - '[[Defense Evasion]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:31:31.046Z'
skill_level: basic
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Delete-Coinbase-Recurring-Payment

## Summary

This procedure details deleting a confirmed recurring payment on Coinbase beta to test restoration safeguards, revealing gaps in re-verification requirements.

## Description

After confirming a payment, use the UI to delete it, which updates the payment state to inactive. Normally, restoration or recreation demands fresh 2FA, but this step sets up the vulnerability by removing the active schedule without built-in undo. Target environment is the web interface; outcomes include a deleted state, emphasizing the need for state-aware endpoints.

## Requirements

1. Active confirmed recurring payment
2. Authenticated session on beta.coinbase.com
3. UI access to payment management

## Defense

Defensive measures and detection strategies:

- Require confirmation dialogs for deletions with audit logs
- Implement soft deletes with recovery windows requiring re-auth
- Monitor deletion patterns for unusual activity

## Objectives

1. Transition payment to deleted state
2. Verify no native restoration path exists
3. Prepare for testing unauthorized recovery

## Instructions

### Step 1: Access Payment Management

**Context**: Navigate to the list of recurring payments in the dashboard.

No command; use web UI to locate the payment by ID.

> Select the payment and choose delete option.

### Step 2: Confirm Deletion

**Context**: Submit the deletion, observing the state change.

Confirm via UI prompt; no API call captured here.

> Payment should show as deleted, with no active schedule.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion]] Defense Evasion

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- deletion
- coinbase
