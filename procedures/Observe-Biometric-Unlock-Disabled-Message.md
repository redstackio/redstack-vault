---
tags:
  - bitwarden
  - android
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
updated_at: '2025-12-14T17:31:31.200Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: adab3976-ef50-466e-b791-5d43f1d11448
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Observe-Biometric-Unlock-Disabled-Message

## Summary

This procedure verifies the biometric integrity invalidation by checking for the disable message in the Bitwarden app.

## Description

Following fingerprint enrollment, reopening the app displays the pending verification message due to the false flag (GH-1026). This confirms the vulnerability trigger without further action. Expected outcome: Biometric unlock blocked for primary account.

## Requirements

1. Bitwarden app installed
2. New fingerprint enrolled
3. Device access

## Defense

Defensive measures and detection strategies:

- User education on biometric change prompts
- App logging for integrity flag changes
- Immediate patching of affected versions

## Objectives

1. Reopen app to check state
2. Confirm disable message
3. Validate flag invalidation

## Instructions

### Step 1: Reopen App

**Context**: Launch the app to observe the effect.

Tap the Bitwarden app icon. The screen should show 'Biometric unlock disabled pending verification of master password'.

> Message indicates successful invalidation; biometrics unavailable.

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
- [[android]]
