---
tags:
  - android
  - adb
  - shell-access
type: procedure
tools:
  - '[[tools/Android-Debug-Bridge]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/list-adb-devices]]'
  - '[[commands/open-adb-shell]]'
verified: false
platforms:
  - Android
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[T1426]]'
updated_at: '2025-12-14T17:24:40.103Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 28cd1712-5aa1-40f7-a146-7155399e77c3
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[T1426]]'
---
# Establish-ADB-Connection-to-Device

## Summary

This procedure enables USB debugging and establishes an ADB shell connection to the Android device, providing command-line access for querying local Content Providers without root.

## Description

ADB (Android Debug Bridge) allows communication with the device over USB. With debugging enabled, attackers can access the shell to run 'content query' commands against exported providers. This simulates access by a connected computer or malicious app with similar privileges.

## Requirements

1. Android device with USB debugging enabled (Developer Options)
2. Computer with Android SDK platform-tools installed
3. USB cable for connection

## Defense

Defensive measures and detection strategies:

- Disable USB debugging in production
- Use device encryption and lock screens
- Monitor USB connections via logs

## Objectives

1. Verify device connectivity
2. Gain interactive shell for local queries
3. Enable exploitation of app components

## Instructions

### Step 1: Enable Debugging and Connect

**Context**: Prepare device for ADB interaction.

Enable Developer Options (tap Build Number 7x in Settings > About Phone), then toggle USB Debugging. Connect device to computer via USB.

### Step 2: List Devices

**Context**: Confirm connection before shell access.

**Command** ([[commands/list-adb-devices]]):
```bash
adb devices
```

> Lists attached devices; authorize on device if prompted. Expected output: Device serial followed by 'device' status.

### Step 3: Open Shell

**Context**: Enter device shell for subsequent commands.

**Command** ([[commands/open-adb-shell]]):
```bash
adb shell
```

> Drops into interactive shell. Expected output: Device prompt like '$ '.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[T1426]] System Information Discovery

### Sub-Techniques


## Commands Used

- [[commands/list-adb-devices]]
- [[commands/open-adb-shell]]

## Tools Used

- [[tools/Android-Debug-Bridge]]

## Tags

- [[android]]
- [[adb]]
