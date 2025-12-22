---
id: proc-brave-launch-001
tags:
  - brave-browser
  - mobile
type: procedure
tools:
  - '[[tools/Brave-Browser]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Android
  - iOS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:24:34.870Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Launch-Brave-Browser-on-Mobile-Device

## Summary

This procedure describes launching the Brave Browser app on Android or iOS devices to set up the environment for exploiting its QR code scanner vulnerability.

## Description

Brave Browser, built on Chromium, includes a QR code scanner that automatically opens decoded URLs. Launching the app prepares the device for scanning. Tested on Android 11 with Brave 1.50.114 (Chromium 112.0.5615.49). No commands are involved; it's app-based. Outcomes include readiness for subsequent scanning steps, with risks amplified by the lack of URL validation.

## Requirements

1. Mobile device with Android 11+ or iOS
2. Brave Browser installed (version 1.50.114 or vulnerable equivalent)
3. Device permissions for camera access

## Defense

Defensive measures and detection strategies:

- Update Brave to patched versions that add QR scan confirmations
- Use alternative browsers like Chrome that preview QR URLs
- Monitor app launch patterns for anomaly detection in mobile forensics

## Objectives

1. Initialize the vulnerable browser environment
2. Ensure compatibility for QR scanning exploit
3. Position for seamless transition to scanner access

## Instructions

### Step 1: Install Brave if Needed

**Context**: Ensure the vulnerable version is available.

Download from official sources or app stores; verify version in settings.

> No command; manual app installation.

### Step 2: Launch the App

**Context**: Open Brave to the main interface.

Tap the Brave icon on the home screen or app drawer.

> Expected: New tab page loads.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Brave-Browser]]

## Tags

- brave-browser
- mobile
