---
id: p-launch-shopify-background
tags:
  - setup
  - android
  - session
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
updated_at: '2025-12-14T17:28:36.400Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Launch-Shopify-App-in-Background

## Summary

This procedure launches the Shopify Android app and keeps it running in the background to maintain an active session, enabling subsequent intent-based bypass without triggering full authentication.

## Description

For the biometrics bypass attack, the app must be in a state where it's authenticated but not foregrounded. This allows DeepLinkActivity to process intents without re-prompting for biometrics. Tested on devices with ADB, but manual launch suffices.

## Requirements

1. Shopify app installed and logged in
2. Android device unlocked
3. No screen lock active during test

## Defense

Defensive measures and detection strategies:

- Implement session timeouts for background apps
- Require re-auth on intent receipt
- Log background activity transitions

## Objectives

1. Establish active session
2. Position app for intent exploitation
3. Avoid full closure to preserve state

## Instructions

### Step 1: Manual Launch

**Context**: Start the app to authenticate if needed, then background it.

No command; manual:

1. Tap the Shopify app icon to launch.
2. Authenticate with biometrics if prompted.
3. Navigate to home screen or press home button to background.
4. Verify in recent apps list.

> Expected: App runs without closing, session persists.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- setup
- session
