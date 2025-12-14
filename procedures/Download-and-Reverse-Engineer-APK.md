---
tags:
  - apk-reverse
  - mobile-analysis
type: procedure
tools:
  - '[[tools/JADX]]'
  - '[[tools/ADB]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/jadx-gui-decompile]]'
  - '[[commands/adb-install-apk]]'
verified: false
platforms:
  - Android
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[T1407]]'
updated_at: '2025-12-14T17:32:57.981Z'
skill_level: advanced
impact_level: medium
detection_risk: low
sub_techniques: []
id: b8da8d55-a935-4893-a030-4abdf3db7bec
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[T1407]]'
---
# Download and Reverse Engineer APK

## Summary

Download and decompile an Android APK to uncover deep links and hardcoded secrets.

## Description

From internal server, download BountyPay.apk, use JADX to decompile, analyze AndroidManifest.xml for intents like one://part/?start=PartTwoActivity, install on device.

## Requirements

1. Access to APK URL
2. JADX tool installed
3. Android device/emulator

## Defense

Defensive measures: Obfuscate APK code, avoid hardcoding secrets; Detection: Monitor APK downloads from internal paths.

## Objectives

1. Decompile APK
2. Identify deep links
3. Expected outcome: Source code and manifests

## Instructions

### Step 1: Decompile APK

**Context**: Extract Java source.

**Command** ([[commands/jadx-gui-decompile]]):
```bash
jadx-gui BountyPay.apk
```

> Expected output: Decompiled classes and XML.

### Step 2: Install on Device

**Context**: Prepare for runtime analysis.

**Command** ([[commands/adb-install-apk]]):
```bash
adb install -r -t BountyPay.apk
```

> Expected output: Installation success.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[T1407]] Structure Consumption

### Sub-Techniques

- None

## Commands Used

- [[commands/jadx-gui-decompile]]
- [[commands/adb-install-apk]]

## Tools Used

- [[tools/JADX]]
- [[tools/ADB]]

## Tags

- apk-reverse
- mobile-analysis
