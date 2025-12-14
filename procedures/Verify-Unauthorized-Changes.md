---
id: proc-verify-changes-001
tags:
  - verification
  - impact-assessment
  - idor
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
updated_at: '2025-12-14T17:25:23.709Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Verify-Unauthorized-Changes

## Summary

This procedure logs into the victim store to confirm that the attacker's settings modifications have been applied without authorization.

## Description

Post-exploit, accessing the victim's low stock variants page reveals altered column visibility (e.g., hidden Title column), proving the IDOR allowed cross-user tampering. This validates the vulnerability's impact on UI presentation of inventory data.

## Requirements

1. Victim store credentials
2. Knowledge of applied changes (e.g., show_title=0)

## Defense

Defensive measures and detection strategies:

- Alert on settings changes from unexpected sources
- User notifications for configuration alterations

## Objectives

1. Access victim's settings
2. Observe modifications
3. Document impact

## Instructions

### Step 1: Log In as Victim

**Context**: Switch to User B's session.

Log in to test1.myshopify.com, access Stocky dashboard.

> Expected output: Dashboard loads.

### Step 2: Check Low Stock Columns

**Context**: Inspect for unauthorized changes.

Navigate to Low Stock Variants > Columns.

> Expected output: Columns match attacker's modifications (e.g., Title hidden).

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[verification]]
