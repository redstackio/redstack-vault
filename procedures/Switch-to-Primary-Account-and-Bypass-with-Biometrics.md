---
tags:
  - bitwarden
  - android
  - bypass
  - biometric
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
updated_at: '2025-12-14T17:31:31.187Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 202355a8-0c56-414a-bd7f-30f868b344f2
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Switch-to-Primary-Account-and-Bypass-with-Biometrics

## Summary

This procedure exploits the core vulnerability by switching to the primary account from secondary and unlocking biometrically, bypassing the integrity check.

## Description

From the secondary session, switching allows biometrics to succeed due to flawed enforcement on vault changes post-restart (GH-1093). This grants unauthorized primary access. Expected outcome: Primary vault open without master password; attacker can view/delete items and enable device sync.

## Requirements

1. Secondary account unlocked
2. Primary pending but switchable
3. Biometrics available

## Defense

Defensive measures and detection strategies:

- Enforce integrity per vault independently
- Log biometric unlocks across accounts
- Patch to require master on changes (see HackerOne #1929915)

## Objectives

1. Switch to primary vault
2. Unlock with biometrics
3. Access sensitive data

## Instructions

### Step 1: Perform Vault Switch

**Context**: Exploit the switch context.

In the app, use vault switcher to select primary, then scan fingerprint.

> Biometrics succeed; primary vault unlocks, bypassing re-auth.

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
- [[bypass]]
