---
tags:
  - android
  - launch
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Android
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[T1416]]'
updated_at: '2025-12-14T03:46:31.944Z'
sub_techniques: []
id: 3d9b76b4-bd3b-4498-b207-24abe60897fa
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[T1416]]'
---
# Launch-Malicious-Attacker-App

## Summary

This procedure starts the malicious app to trigger the automated sequence of intents that exploit the vulnerability.

## Description

Launching the app initiates Handler postDelayed runnables for 8-second and 20-second delays, ensuring the Exness app is foregrounded and user session active before payload injection.

## Requirements

1. Malicious app installed
2. Device unlocked for app launch
3. Exness app already installed

## Defense

Defensive measures and detection strategies:

- Log intent launches from third-party apps
- Use app sandboxing to restrict cross-app activity starts
- Alert on unusual delayed executions

## Objectives

1. Begin the exploit timer
2. Ensure seamless transition to target app
3. Minimize user suspicion

## Instructions

### Step 1: Open Attacker App

**Context**: Manually or automatically start the app to run the exploit code.

Tap the app icon or use ADB: adb shell am start -n com.attacker/.MainActivity

> Expected output: App launches, potentially in background with timers active.

### Step 2: Monitor for Triggers

**Context**: Verify the app doesn't crash and delays are respected.

Observe logs via ADB logcat for intent starts.

> Expected output: No errors, sequence proceeds.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[T1416]] Cross-site Scripting (XSS)

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- android
- launch
