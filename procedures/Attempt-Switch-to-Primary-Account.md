---
tags:
  - bitwarden
  - android
  - vault-switch
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
updated_at: '2025-12-14T17:31:31.195Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 4f480352-d763-42f1-8bfd-da8c1eb3dcdc
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Attempt-Switch-to-Primary-Account

## Summary

This procedure tests switching to the primary account to confirm biometric unlock is still blocked.

## Description

From the secondary account, attempting to switch verifies the integrity check holds initially. This step highlights the vulnerability's conditional bypass. Expected outcome: Switch blocked, requiring master password.

## Requirements

1. Secondary account unlocked
2. Primary account pending
3. App access

## Defense

Defensive measures and detection strategies:

- Consistent integrity checks across accounts
- Log failed vault switches
- Require master password for all multi-account ops

## Objectives

1. Select primary vault
2. Confirm block
3. Validate vulnerability setup

## Instructions

### Step 1: Use Vault Switcher

**Context**: Attempt access to primary.

Tap the profile or sidebar to open vault switcher, select primary account, and try biometric unlock.

> Unlock fails; prompts for master password.

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
- [[vault-switch]]
