---
tags:
  - android
  - configuration
  - drozer
type: procedure
tools:
  - '[[tools/Drozer]]'
  - '[[tools/Drozer-Agent]]'
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
updated_at: '2025-12-14T17:24:39.879Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 9040687c-5f87-444d-ad0b-439573885e8f
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Configure-Passcode-and-Install-Drozer

## Summary

This procedure enables passcode protection in the Nextcloud app to enforce authentication and installs the Drozer framework along with its agent on the target device, setting the stage for intent-based exploitation.

## Description

To demonstrate the bypass, the app's built-in passcode must be activated, simulating a locked state. Drozer, an Android security assessment tool, is then installed on the host and agent on the device. The embedded server is started to allow remote console interactions, enabling attackers to probe and invoke app components like exported activities without standard authentication flows.

## Requirements

1. Running Android emulator with Nextcloud installed and logged in
2. Host with Python and Drozer framework
3. ADB access to the device

## Defense

Defensive measures and detection strategies:

- Disable or restrict sideloading of assessment APKs like Drozer Agent
- Monitor for unusual APK installations via mobile device management (MDM)
- Audit app permissions and exported components during development

## Objectives

1. Activate passcode to secure the app interface
2. Deploy Drozer for component analysis and exploitation
3. Start embedded server for console connectivity

## Instructions

### Step 1: Enable Passcode in Nextcloud

**Context**: Configure app-level protection to trigger the bypass target.

**Instructions**: Open Nextcloud settings, navigate to Security, and set a passcode. Close and reopen the app to verify the lock screen appears.

> Expected output: Passcode prompt blocks access to UI upon reopen.

### Step 2: Install Drozer Framework and Agent

**Context**: Prepare the assessment tools on host and device.

**Instructions**: On host, install Drozer via pip: `pip install drozer`. Download and install Drozer Agent APK on device via ADB: `adb install drozer-agent.apk`. Start the embedded server in the agent app.

> Expected output: Agent installed, server running and listening on device port.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Drozer]]
- [[tools/Drozer-Agent]]

## Tags

- android
- configuration
- drozer
