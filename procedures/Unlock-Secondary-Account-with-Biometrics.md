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
updated_at: '2025-12-14T17:31:31.190Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 5f05b514-c8ad-4b5c-8ec6-35f0c48322fe
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Unlock-Secondary-Account-with-Biometrics

## Summary

This procedure unlocks the secondary account using valid biometrics, establishing an authenticated app session.

## Description

After restart, selecting and unlocking the secondary bypasses its own integrity (unaffected), providing a foothold. Expected outcome: App session active via secondary.

## Requirements

1. App locked
2. Secondary biometrics valid
3. Device fingerprint access

## Defense

Defensive measures and detection strategies:

- Isolate account sessions
- Flag cross-account unlocks
- Require global master password

## Objectives

1. Select secondary vault
2. Authenticate with biometrics
3. Gain app access

## Instructions

### Step 1: Reopen and Select

**Context**: Unlock secondary post-kill.

Launch app, choose secondary vault, scan fingerprint to unlock.

> Secondary vault opens.

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
