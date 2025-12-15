---
tags:
  - passcode
  - android
  - security-settings
type: procedure
tools: []
tactics: []
commands: []
verified: false
platforms:
  - Android
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques: []
updated_at: '2025-12-14T17:24:44.679Z'
sub_techniques: []
id: 84f4019a-df37-4540-aaea-57895ede06ab
validated: true
---
# Enable-Passcode-Protection-in-Talk-App

## Summary

This procedure activates passcode lock in the Nextcloud Talk Android app to simulate protected state that can be bypassed via notifications.

## Description

Enabling passcode protection adds a layer of local authentication to the app, requiring entry on launch. This is done via app settings and is crucial for demonstrating the bypass. The target is User B's device; outcome is a locked app ready for notification testing.

## Requirements

1. Logged-in Talk app on Android (User B)
2. Physical access to device
3. App version with passcode feature

## Defense

Defensive measures and detection strategies:

- Regularly update app to patch bypass issues
- Use device-level biometrics over app passcodes

## Objectives

1. Activate passcode feature
2. Lock the app
3. Confirm protection is active

## Instructions

### Step 1: Access Settings

**Context**: Navigate to security options.

Open Talk app, tap profile icon, go to Settings > Security.

### Step 2: Set Passcode

**Context**: Enable and configure lock.

Select "Passcode Lock", toggle on, enter and confirm a passcode (e.g., 1234). Exit app to lock it.

**Expected Output**: App closes; relaunch prompts for passcode.

## MITRE ATT&CK Mapping

### Tactics


### Techniques


### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[passcode-protection]]
- [[app-security]]
