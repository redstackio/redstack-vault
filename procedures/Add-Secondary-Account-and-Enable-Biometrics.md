---
tags:
  - bitwarden
  - android
  - secondary-account
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Android
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:31:31.197Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 92a8e359-2e2b-4878-97c0-abbbf7cc2af9
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Add-Secondary-Account-and-Enable-Biometrics

## Summary

This procedure adds a secondary Bitwarden account and enables biometrics for it, creating a valid authentication path for the bypass.

## Description

While the primary account is pending, this step introduces a secondary account unaffected by the integrity flag. It uses normal signup flow and enables biometrics. Expected outcome: Secondary account ready with working biometrics.

## Requirements

1. Bitwarden app open (primary pending)
2. Secondary account credentials
3. Device biometrics available

## Defense

Defensive measures and detection strategies:

- Limit multi-account support or require separate auth
- Audit account additions in app logs
- Enforce master password for all switches

## Objectives

1. Add secondary account
2. Enable its biometrics
3. Maintain valid auth context

## Instructions

### Step 1: Add Account

**Context**: Introduce the secondary account.

In Settings > Accounts, tap 'Add Account'. Enter secondary email and master password, then log in.

> Secondary vault added.

### Step 2: Enable Biometrics for Secondary

**Context**: Activate unlock for secondary.

In secondary settings > Security > Unlock with Biometrics, toggle on.

> Biometrics enabled for secondary.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[bitwarden]]
- [[secondary-account]]
