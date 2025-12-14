---
tags:
  - bitwarden
  - android
  - app-kill
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
updated_at: '2025-12-14T17:31:42.449Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: ac93f00b-79f3-4bf1-a33e-48616b58dbeb
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Force-Kill-Bitwarden-App

## Summary

This procedure force-closes the Bitwarden app to lock its state, ensuring no active session interferes with biometric integrity invalidation.

## Description

Part of the Bitwarden biometric bypass attack, this step uses Android's task management to terminate the app process. It simulates a lock and prepares for biometric changes that trigger the vulnerability. Expected outcome: App fully locked, requiring re-authentication on reopen.

## Requirements

1. Physical access to Android device
2. Bitwarden app running
3. Knowledge of device task manager

## Defense

Defensive measures and detection strategies:

- Use app pinning or kiosk mode to prevent force-closing
- Log app terminations via device analytics
- Patch app to enforce session persistence checks

## Objectives

1. Lock the app session
2. Reset state for biometric change
3. Verify lock on reopen

## Instructions

### Step 1: Access Task Manager

**Context**: Identify and terminate the app process.

Swipe up from the bottom of the screen to open recent apps, or go to Settings > Apps. Locate Bitwarden and select 'Force Stop' or swipe it away.

> App process ends; no background activity remains.

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
