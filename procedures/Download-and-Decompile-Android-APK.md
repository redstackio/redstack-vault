---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567891
name: Download-and-Decompile-Android-APK
tags:
  - android
  - decompile
  - reverse-engineering
type: procedure
tools:
  - '[[tools/apktool]]'
  - '[[tools/jadx]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/apk-download]]'
  - '[[commands/apktool-decompile]]'
verified: false
platforms:
  - Android
  - Mobile
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:24:42.524Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Download-and-Decompile-Android-APK

## Summary

This procedure involves downloading the target Android APK file and decompiling it to access the application's code and resources, enabling further analysis for vulnerabilities like hardcoded credentials.

## Description

In the context of mobile app security testing, decompiling an APK is a foundational step for reverse engineering. For the 8x8 app, this reveals embedded URLs and configurations pointing to third-party services. Prerequisites include a Linux or Windows environment with Java installed. Expected outcomes include access to smali code, manifests, and assets, which can be searched for sensitive data.

## Requirements

1. Internet access to download the APK from sources like APKMirror or Google Play (via extraction tools)
2. Java Development Kit (JDK) version 8 or higher
3. Installed tools like apktool and jadx

## Defense

Defensive measures and detection strategies:

- Obfuscate app code using ProGuard or R8 to hinder decompilation
- Implement app integrity checks with SafetyNet or certificate pinning
- Monitor for unusual APK downloads or decompilation attempts in app distribution logs

## Objectives

1. Acquire the intact APK file for analysis
2. Decompile to extract readable code and resources
3. Prepare for credential hunting in the app's internals

## Instructions

### Step 1: Download the APK

**Context**: Obtain the 8x8 Android app APK for local analysis.

**Command** ([[commands/apk-download]]):
```bash
evap -a com.8x8.vvc -o 8x8.apk
```

> This command uses a tool like Evap to extract the APK from a connected device or emulator. Expected output is the 8x8.apk file saved locally.

### Step 2: Decompile with Apktool

**Context**: Break down the APK into smali code and resources for inspection.

**Command** ([[commands/apktool-decompile]]):
```bash
apktool d 8x8.apk -o decompiled_app
```

> Decompiles the APK, outputting directories like smali/, res/, and AndroidManifest.xml. Verify by checking for no errors in the console.

### Step 3: Analyze Bytecode with Jadx

**Context**: Convert Dalvik bytecode to readable Java for easier credential spotting.

**Command** ([[commands/jadx-decompile]]):
```bash
jadx -d jadx_output 8x8.apk
```

> Generates Java source files in jadx_output/. Open in an IDE to browse for strings.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques


## Commands Used

- [[commands/apk-download]]
- [[commands/apktool-decompile]]
- [[commands/jadx-decompile]]

## Tools Used

- [[tools/apktool]]
- [[tools/jadx]]

## Tags

- android
- decompile
- apk
