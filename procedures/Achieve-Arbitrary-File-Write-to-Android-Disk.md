---
tags:
  - file-write
  - persistence
  - android-storage
type: procedure
tools: []
tactics:
  - '[[Persistence]]'
commands: []
verified: false
platforms:
  - Android
  - Mobile
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Remote File Copy]]'
updated_at: '2025-12-14T17:24:44.899Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: e3d8fc12-11c8-4d78-9a3e-8a7016d36acd
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Remote File Copy]]'
---
# Achieve-Arbitrary-File-Write-to-Android-Disk

## Summary

This procedure completes the exploit by automatically saving the downloaded file to the Android device's disk, exploiting the app's storage permissions for silent persistence.

## Description

The MetaMask in-app browser's download handling writes files to accessible storage (e.g., Downloads folder) without notification, due to absent prompts in deeplink flows. This allows arbitrary content placement, potentially for malware or data exfil. UGWST analysis showed files persist post-download. Targets: Android with MetaMask. Outcomes: Compromised device storage enabling further attacks.

## Requirements

1. Ongoing download from prior browser step
2. Device storage permissions granted to MetaMask (default)
3. Access to verify file placement (e.g., via file explorer or ADB)

## Defense

Defensive measures and detection strategies:

- Restrict app storage writes to sandboxed areas with audits
- Enable notifications for all file operations in mobile OS
- Use antivirus scanning for newly written files in app directories

## Objectives

1. Persist malicious file on device disk
2. Evade user detection until after write
3. Enable secondary exploits like execution or exfiltration

## Instructions

### Step 1: Configure Download Path

**Context**: Ensure the download targets writable storage.

The WebView defaults to external storage; no config needed. If customizing, use JS to specify filename in download attribute.

### Step 2: Complete Silent Write

**Context**: Allow the download to finish and write the file.

The process auto-saves to `/storage/emulated/0/Download/malicious.apk` or app cache. No intervention required; deeplink bypass ensures no alerts.

### Step 3: Validate File Placement

**Context**: Confirm the arbitrary write succeeded.

Pull the file with `adb pull /storage/emulated/0/Download/malicious.apk .` or check via device file manager. Verify contents match attacker file.

> Expected: File exists and is intact, indicating successful persistence.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]]

### Techniques

- [[Remote File Copy]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- file-write
- persistence
- android-storage
