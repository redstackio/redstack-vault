---
tags:
  - android
  - setup
  - emulation
type: procedure
tools:
  - '[[tools/Android-Studio-AVD]]'
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
updated_at: '2025-12-14T17:24:39.883Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: b05ccc0d-995e-492f-a054-6a26fff614b0
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Set-Up-Android-Emulation-and-Install-Nextcloud

## Summary

This procedure sets up a non-rooted Android 9 emulated environment using Android Studio AVD and installs the Nextcloud Client app with user authentication, preparing the target for passcode configuration and exploitation testing.

## Description

In an attack scenario targeting mobile apps, emulating the target device allows safe reproduction of vulnerabilities without risking physical hardware. Here, Android Studio's AVD creates a non-rooted Android 9 instance to mimic a standard user device. The Nextcloud app is then installed from official sources and authenticated with real credentials to ensure the app state includes synced files and settings, enabling accurate testing of passcode bypass.

## Requirements

1. Host machine with Android Studio installed
2. Access to Nextcloud account credentials
3. Internet connection for APK download

## Defense

Defensive measures and detection strategies:

- Use rooted devices or emulators only in isolated lab environments
- Monitor for unauthorized emulator instances via endpoint detection tools
- Enforce app installation from trusted sources only

## Objectives

1. Establish a reproducible Android 9 non-rooted environment
2. Install and authenticate Nextcloud app to simulate user state
3. Prepare for subsequent passcode and tool setup

## Instructions

### Step 1: Launch Android Studio AVD

**Context**: Create and boot an emulated non-rooted Android 9 device to serve as the test target.

**Instructions**: Open Android Studio, navigate to AVD Manager, create a new virtual device with Android 9 (API level 28) image, ensuring no root is enabled. Start the emulator.

> Expected output: Emulator boots to Android home screen, confirming non-rooted status via adb shell checks.

### Step 2: Install Nextcloud Client

**Context**: Download and deploy the Nextcloud Android app to the emulator.

**Instructions**: Download the latest Nextcloud APK from the official site or Play Store mirror, then use ADB to install: `adb install nextcloud.apk`. Open the app and log in with valid credentials.

> Expected output: App launches, account syncs files, confirming authentication success.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Android-Studio-AVD]]

## Tags

- android
- setup
- emulation
