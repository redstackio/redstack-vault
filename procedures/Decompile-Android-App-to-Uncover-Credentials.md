---
id: proc-uuid-001
tags:
  - android
  - decompilation
  - reverse-engineering
type: procedure
tools:
  - '[[tools/jadx]]'
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Android
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Hardware]]'
updated_at: '2025-12-14T17:24:44.665Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Hardware]]'
---
# Decompile-Android-App-to-Uncover-Credentials

## Summary

This procedure involves reverse engineering an Android APK file to inspect its source code and resources, often revealing embedded secrets like API endpoints or hardcoded credentials during routine analysis.

## Description

In the context of mobile app security testing, decompiling an Android app allows attackers to examine the app's logic, network communications, and configuration data. For the Zomato app, this uncovered development credentials while searching for new API endpoints. The process targets the APK binary, converting it to readable Java/Kotlin code and XML resources. Prerequisites include obtaining the APK and a decompilation tool; outcomes include potential exposure of sensitive strings if not obfuscated.

## Requirements

1. APK file of the target app (e.g., downloaded from Play Store)
2. Java runtime environment (JDK 8+)
3. Decompilation tool like jadx installed
4. Basic knowledge of Android app structure

## Defense

Defensive measures and detection strategies:

- Obfuscate code using ProGuard or R8 to hide strings and logic
- Avoid embedding production or dev credentials in app binaries; use secure storage like Android Keystore
- Monitor for anomalous APK downloads or decompilation attempts via app integrity checks (e.g., SafetyNet)

## Objectives

1. Extract and analyze app source code for vulnerabilities
2. Identify embedded secrets or endpoints
3. Enable further reconnaissance on discovered elements

## Instructions

### Step 1: Obtain and Prepare APK

**Context**: Acquire the target APK for decompilation.

Download the Zomato APK using a tool like apkpure or adb. Verify its integrity with SHA256 if needed.

### Step 2: Decompile Using Jadx

**Context**: Convert the APK to source code for inspection.

Execute jadx to decompile the APK into a directory of readable files. Use the GUI for browsing or CLI for scripting.

**Command** (jadx-decompile):
```bash
jadx -d output_dir zomato.apk
```

> This command generates a 'output_dir' with decompiled classes, resources, and manifests. Search for network classes like Retrofit or OkHttp configurations.

### Step 3: Search for Secrets

**Context**: Manually or programmatically scan for hardcoded data.

Use grep to find potential credentials in the decompiled files.

**Command** (grep-search):
```bash
grep -r -i "auth\|basic\|password" output_dir/
```

> Expected output includes lines with encoded or plaintext credentials. Review context to confirm relevance to the target domain.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Hardware]] Gather Victim Host Information: Domain

### Sub-Techniques

- None

## Commands Used

- None specific

## Tools Used

- [[tools/jadx]]

## Tags

- [[android]]
- [[decompilation]]
