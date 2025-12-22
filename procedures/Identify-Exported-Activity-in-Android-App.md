---
tags:
  - android
  - recon
  - exported-activity
type: procedure
tools:
  - '[[tools/Android-Debug-Bridge-ADB]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/adb-pull-manifest]]'
verified: false
platforms:
  - Android
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[T1422]]'
updated_at: '2025-12-14T17:24:42.069Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 8aec16c9-e19a-499b-acff-4a656b6985b3
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[T1422]]'
---
# Identify Exported Activity in Android App

## Summary

This procedure involves analyzing an Android app's manifest to identify exported activities that may be vulnerable to intent-based attacks, such as in the LINE Lite app where SelectShareActivity lacks URI validation.

## Description

In Android apps, exported activities can receive intents from other apps. By examining the AndroidManifest.xml, attackers can discover components like com.linecorp.linelite.ui.android.share.SelectShareActivity that handle share intents without proper checks, enabling file access exploits. This is performed on a rooted device, emulator, or via ADB with debugging enabled. Prerequisites include ADB setup and the target app installed.

## Requirements

1. Android device or emulator with USB debugging enabled
2. ADB installed on host machine
3. Target app (LINE Lite < 2.17.0) installed
4. Basic knowledge of Android app structure

## Defense

Defensive measures and detection strategies:

- Use tools like MobSF for static analysis to flag exported components
- Implement intent filters with permission checks in app development
- Monitor for anomalous app interactions via device logs

## Objectives

1. Locate exported activities in the app manifest
2. Assess for validation weaknesses
3. Prepare for intent crafting

## Instructions

### Step 1: Pull AndroidManifest.xml Using ADB

**Context**: Retrieve the app's manifest file to inspect exported components.

**Command** ([[commands/adb-pull-manifest]]):
```bash
adb shell pm path com.linecorp.linelite | xargs adb pull
unzip base.apk AndroidManifest.xml
aapt dump xmltree AndroidManifest.xml AndroidManifest.xml > manifest.txt
grep -i exported manifest.txt
```

> This command locates the APK path, pulls it, extracts the manifest, decodes it with aapt (included in Android SDK), and searches for exported activities. Expected output includes lines like <activity android:name="com.linecorp.linelite.ui.android.share.SelectShareActivity" android:exported="true"> confirming the vulnerability.

### Step 2: Analyze for Vulnerabilities

**Context**: Review the activity's intent filters and code for URI handling flaws.

**Instructions**: Use decompilers like JADX to inspect the activity's source, looking for unvalidated getIntent().getData() calls.

**Expected Output**: Identification of SelectShareActivity as handling share intents without URI verification.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[T1422]] System Network Configuration Discovery (adapted for app component discovery)

### Sub-Techniques


## Commands Used

- [[commands/adb-pull-manifest]]

## Tools Used

- [[tools/Android-Debug-Bridge-ADB]]

## Tags

- [[android]]
- [[recon]]
- [[exported-activity]]
