---
tags:
  - reverse-engineering
  - android
  - decompilation
type: procedure
tools:
  - '[[tools/APKTool]]'
  - '[[tools/JADX]]'
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Android
  - Mobile
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[T1422]]'
updated_at: '2025-12-14T17:25:52.843Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 42bc8ca9-fc52-445b-9da5-fe4d899a1f65
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[T1422]]'
---
---
id: 123e4567-e89b-12d3-a456-426614174001
name: Reverse-Engineer-Android-App
type: procedure
verified: false
submitted: false
created_at: 2023-10-01T00:00:00Z
updated_at: 2023-10-01T00:00:00Z
tactics: [[Discovery]]
techniques: [[T1422]]
sub_techniques: []
tags: reverse-engineering, android, decompilation
commands: []
platforms: Android, Mobile
tools: [[tools/APKTool]], [[tools/JADX]]
---

# Reverse-Engineer-Android-App

## Summary

This procedure involves decompiling an Android APK to analyze its source code, revealing internal logic such as API endpoints and validation mechanisms, primarily used in mobile app security assessments to identify vulnerabilities like IDOR.

## Description

In the context of the Bykea app attack, reverse engineering uncovers hardcoded legacy endpoints by reconstructing the app's Java code from the binary APK. This targets Android applications where source code is obfuscated but not fully protected. Prerequisites include a rooted device or emulator for APK extraction, and the process exposes network calls, authentication flows, and data handling without requiring server access. Expected outcomes include identification of unused code paths that remain executable.

## Requirements

1. Downloaded APK file of the target app (e.g., Bykea from device or store).
2. Java Development Kit (JDK) installed for decompilation tools.
3. Local machine with Linux/macOS/Windows for running decompilers.

## Defense

Defensive measures and detection strategies:

- Obfuscate app code using ProGuard or R8 to hinder reverse engineering.
- Implement runtime integrity checks (e.g., SafetyNet API) to detect tampering.
- Monitor for anomalous API calls from decompiled endpoints in server logs.

## Objectives

1. Extract and reconstruct app source code for analysis.
2. Identify hidden or legacy features in the codebase.
3. Enable further vulnerability discovery like insecure endpoints.

## Instructions

### Step 1: Extract and Decompile APK

**Context**: Obtain the APK and break it down into resources and Smali code using APKTool, which handles the binary structure.

No specific command; use APKTool GUI or CLI:

```bash
apktool d bykea.apk -o decompiled_app
```

> This outputs directories with manifest, assets, and Smali code. Inspect AndroidManifest.xml for permissions and components.

### Step 2: Reconstruct Java Source

**Context**: Convert Dalvik bytecode to readable Java using JADX for higher-level analysis of logic flows.

No specific command; run JADX:

```bash
jadx -d jadx_output bykea.apk
```

> Generates Java files; search for classes handling API requests, e.g., TripApiClient.java, to find endpoint constructions.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[T1422]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/APKTool]]
- [[tools/JADX]]

## Tags

- [[reverse-engineering]]
- [[android]]
