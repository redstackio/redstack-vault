---
id: 9fae5c16-d3e0-457d-9aca-9a9342ee0d81
name: Install-PoC-Android-App-for-Interception
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:21.765Z'
tactics:
  - '[[Execution]]'
techniques:
  - '[[T1409]]'
tags:
  - android
  - poc-app
  - installation
platforms:
  - Android
tools:
  - '[[tools/PoC-Android-Application]]'
skill_level: low
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[T1409]]'
---

# Install-PoC-Android-App-for-Interception

## Summary

This procedure installs a custom PoC Android application on the target device to intercept and modify ZIP files synced to the LINE Keep service.

## Description

The PoC app is pre-built to monitor LINE's file syncs and replace legitimate ZIPs with malicious ones. It requires physical or remote access to the Android device for installation and prompts for STORAGE permission to access files. In the attack, this enables seamless replacement during sync, targeting the path traversal vulnerability in ZIP extraction. Prerequisites include sideloading capabilities or user consent for installation.

## Requirements

1. Android device with developer options enabled for sideloading
2. APK file for the PoC app
3. User interaction to grant STORAGE permission

## Defense

Defensive measures and detection strategies:

- Enforce app installation from trusted sources only
- Monitor for unknown apps requesting storage access
- Use mobile device management (MDM) to restrict sideloading

## Objectives

1. Deploy interception capability on the device
2. Secure necessary permissions for file manipulation
3. Enable automatic ZIP replacement during LINE sync

## Instructions

### Step 1: Download and Install APK

**Context**: Sideload the PoC app onto the device.

No command; transfer the APK via USB or download, then install via Android settings.

> Enable 'Unknown Sources' if needed.

### Step 2: Grant Permissions

**Context**: Allow the app to access storage for interception.

No command; when prompted on first launch, grant STORAGE permission.

> Confirm permission in app settings post-install.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[T1409]] Installed Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/PoC-Android-Application]]

## Tags

- [[android]]
- [[poc-app]]
- [[installation]]
