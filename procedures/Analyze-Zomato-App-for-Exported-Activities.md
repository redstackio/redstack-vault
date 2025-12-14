---
tags:
  - android
  - static-analysis
  - exported-activity
type: procedure
tools:
  - '[[tools/Android-Debug-Bridge]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/adb-pull-apk]]'
  - '[[commands/aapt-dump-badging]]'
verified: false
platforms:
  - Android
submitted: true
techniques:
  - '[[Gather Victim Host Information]]'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: b3ee43c8-e9ff-4cd6-a1a3-615419d3d144
created_at: '2025-12-14T17:25:18.221Z'
updated_at: '2025-12-14T17:25:18.221Z'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Analyze-Zomato-App-for-Exported-Activities

## Summary

This procedure involves static analysis of the Zomato Order Android app to identify exported activities that can be invoked by external intents, focusing on components like DeepLinkRouter that lack proper restrictions.

## Description

In Android apps, exported activities declared in AndroidManifest.xml with exported=true can be started by any app or external trigger without authentication. This procedure pulls the app's APK and inspects the manifest to find such vulnerabilities, enabling further exploitation like intent redirection. It requires a device with the app installed and ADB access. Expected outcome: Confirmation of vulnerable exported components.

## Requirements

1. Android device/emulator with Zomato Order app installed and USB debugging enabled
2. ADB installed on the host machine
3. aapt tool from Android SDK

## Defense

Defensive measures and detection strategies:

- Set exported=false for sensitive activities unless necessary
- Use intent filters with specific schemes/hosts to restrict access
- Monitor app behavior for unexpected intent launches via logcat

## Objectives

1. Identify exported activities vulnerable to external invocation
2. Map potential entry points for intent-based attacks
3. Gather details for crafting malicious intents

## Instructions

### Step 1: Pull the App APK

**Context**: Retrieve the APK file from the device for offline analysis.

**Command** ([[commands/adb-pull-apk]]):
```bash
adb shell pm path com.application.zomato
adb pull /data/app/com.application.zomato-*/base.apk zomato.apk
```

> This command lists the APK path and pulls it to the host. Expected output: APK file saved locally.

### Step 2: Dump Manifest for Exported Activities

**Context**: Extract activity declarations to check for exported=true.

**Command** ([[commands/aapt-dump-badging]]):
```bash
aapt dump badging zomato.apk | grep -A 10 "activity"
```

> Filters output to show activities. Look for DeepLinkRouter with exported=true. Expected output: Manifest details confirming export status.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Gather Victim Host Information]]

### Sub-Techniques


## Commands Used

- [[commands/adb-pull-apk]]
- [[commands/aapt-dump-badging]]

## Tools Used

- [[tools/Android-Debug-Bridge]]

## Tags

- [[android]]
- [[static-analysis]]
