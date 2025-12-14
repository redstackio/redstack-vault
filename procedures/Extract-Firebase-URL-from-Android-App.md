---
id: proc-uuid-1
tags:
  - android
  - reverse-engineering
  - credential-exposure
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Android
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unsecured Credentials]]'
updated_at: '2025-12-14T17:24:45.034Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Unsecured Credentials]]'
---
# Extract-Firebase-URL-from-Android-App

## Summary

This procedure involves inspecting the Zego Sense Android app's resources to extract the hardcoded Firebase Realtime Database URL, which is exposed in the strings.xml file, allowing attackers to identify and target the database endpoint.

## Description

In the attack scenario, the Android app contains sensitive configuration details like the Firebase URL in plain text within res/values/strings.xml. By decompiling the APK using tools like APKTool or Jadx, attackers can reveal this URL (https://api-project-615509201590.firebaseio.com), bypassing any obfuscation and enabling direct access to the cloud database. This is a common misconfiguration in mobile apps integrating third-party services. Prerequisites include obtaining the APK file, which can be downloaded from app stores or extracted from devices. Expected outcomes include full URL exposure, setting the stage for unauthenticated database interactions.

## Requirements

1. Android APK file for Zego Sense app
2. Decompilation tool like APKTool or Android Studio
3. Basic knowledge of Android resource files

## Defense

Defensive measures and detection strategies:

- Obfuscate sensitive URLs and use environment variables or secure vaults for configuration
- Implement app integrity checks to detect tampering or decompilation attempts
- Monitor for anomalous access patterns to Firebase endpoints from non-app sources

## Objectives

1. Reveal hardcoded Firebase database URL
2. Identify target endpoint for exploitation
3. Enable subsequent read/write operations

## Instructions

### Step 1: Obtain and Decompile the APK

**Context**: Acquire the app APK and decompile it to access internal resources.

Download the Zego Sense APK from a trusted source or extract from a device. Use APKTool to decompile:

```bash
apktool d zego-sense.apk
```

> This extracts the app structure, including res/values/strings.xml. Expected output: Decompiled directory with XML files.

### Step 2: Inspect strings.xml

**Context**: Locate the Firebase URL in the app's string resources.

Open res/values/strings.xml and search for "firebase_database_url".

**Command** (manual inspection, no CLI):

Examine the file contents:

```xml
<string name="firebase_database_url">https://api-project-615509201590.firebaseio.com/</string>
```

> This reveals the exact URL. Expected output: Hardcoded endpoint string.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Unsecured Credentials]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- android
- reverse-engineering
- credential-exposure
