---
id: '[UUID]'
tags:
  - authentication-bypass
  - pin-bypass
  - time-manipulation
  - rocket-chat
  - mobile-security
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Mobile
  - iOS
  - Android
submitted: true
created_at: '[TIMESTAMP]'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:31:11.285Z'
skill_level: low
impact_level: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Verify-PIN-Lock-Activation

## Summary

This procedure tests the Rocket.Chat app's lock state by attempting to reopen it, confirming the PIN prompt appears due to the inactivity timeout based on system time.

## Description

After the timeout has passed, relaunching the app should display the PIN screen, verifying the lock's engagement. This step ensures the vulnerability condition is met before proceeding to time manipulation. Physical access is required; success indicates the app's time-based auth is active and bypassable.

## Requirements

1. Inactivity timeout elapsed from prior step
2. Physical access to relaunch the app
3. No PIN entry during verification

## Defense

Defensive measures and detection strategies:

- Audit app logs for repeated lock activations without unlocks
- Enforce stronger auth like biometrics that can't be timed out easily
- Detect patterns of app open/close cycles indicative of testing

## Objectives

1. Confirm PIN prompt blocks access to app features
2. Validate lock ties to system time for exploitation
3. Prepare for clock rollback without alerting the app

## Instructions

### Step 1: Reopen the App

**Context**: Check if the lock has engaged.

Launch the Rocket.Chat app from the device home screen or recent apps.

### Step 2: Observe and Close

**Context**: Note the prompt without authenticating.

Verify the PIN entry screen appears, then close the app without inputting the code.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[authentication-bypass]]
- [[pin-bypass]]
- [[time-manipulation]]
- [[rocket-chat]]
- [[mobile-security]]
