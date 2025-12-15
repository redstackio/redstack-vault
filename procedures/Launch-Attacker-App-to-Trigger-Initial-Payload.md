---
id: proc-uuid-003
tags:
  - android
  - intent-launch
  - xss
type: procedure
tools:
  - '[[tools/Custom-Attacker-App]]'
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Android
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:33:06.354Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Launch-Attacker-App-to-Trigger-Initial-Payload

## Summary

This procedure starts the custom attacker app, which automatically launches the Exness app and prepares for payload injection via intents.

## Description

The attacker app uses PackageManager.getLaunchIntentForPackage to target com.exness.investments and startActivity to open it. This creates the context for subsequent intent injections targeting SMFeedbackActivity, exploiting the improper export in AndroidManifest.xml.

## Requirements

1. Both apps installed on the same device
2. No special permissions beyond standard app launch
3. Device not in restricted mode

## Defense

Defensive measures and detection strategies:

- Set exported='false' for sensitive activities in manifest
- Implement intent validation in onCreate/onNewIntent
- Monitor for cross-app launches in app analytics

## Objectives

1. Initiate the exploit sequence
2. Ensure target app is foregrounded
3. Set up for delayed payload delivery

## Instructions

### Step 1: Open Attacker App

**Context**: Start the malicious app to trigger automation.

Tap the attacker app icon on the home screen.

**Expected Output**: App launches; logs show intent preparation.

### Step 2: Monitor Auto-Launch

**Context**: Verify target app activation.

Observe as the app uses startActivity after internal delays.

**Expected Output**: Exness app opens automatically.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript (prepares for JS payload)

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Custom-Attacker-App]]

## Tags

- android
- intent-launch
- xss
