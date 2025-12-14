---
id: proc-decompile-apk-001
tags:
  - decompilation
  - credential-extraction
  - information-disclosure
  - android
type: procedure
tools:
  - '[[tools/apktool]]'
  - '[[tools/jadx]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/apktool-decompile]]'
  - '[[commands/grep-search-strings]]'
verified: false
platforms:
  - Linux
  - Mobile (Android)
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Credentials In Files]]'
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:24:44.531Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Credentials In Files]]'
  - '[[File and Directory Discovery]]'
---
# Decompile APK and Extract Leaked Tokens

## Summary

This procedure decompiles an Android APK file to reveal embedded sensitive information, such as internal tokens or credentials, which may have been hardcoded during development.

## Description

Android APKs can be reverse-engineered using tools like apktool to unpack resources, manifest, and smali code. In the Uber case, development builds on devbuilds.uber.com contained leaked tokens, discoverable by searching decompiled assets and code. This targets misconfigurations where secrets bypass security scans. Prerequisites include a downloaded APK; outcomes are extracted credentials usable for unauthorized access, emphasizing mobile app security hygiene.

## Requirements

1. Downloaded APK file (e.g., uber-dev.apk).
2. apktool or jadx installed (Java runtime required for jadx).
3. Basic command-line skills for searching files.
4. Optional: Text editor or IDE for manual inspection.

## Defense

Defensive measures and detection strategies:

- Implement secret scanning in build pipelines (e.g., using Trivy or GitGuardian).
- Obfuscate code and use secure storage for tokens (e.g., Android Keystore).
- Regularly audit public-facing build artifacts for exposures.

## Objectives

1. Unpack and decompile the APK structure.
2. Identify and extract hardcoded tokens or credentials.
3. Validate tokens for potential exploitation.

## Instructions

### Step 1: Decompile the APK

**Context**: Use apktool to disassemble the APK into readable smali code and resources for analysis.

**Command** ([[commands/apktool-decompile]]):
```bash
apktool d uber-dev.apk -o decompiled-output
```

> Decompiles the APK to a directory named decompiled-output. Expected output: Progress messages ending with "I: Copying raw classes..." and a success note. The directory will contain AndroidManifest.xml, res/, and smali/ folders.

### Step 2: Search for Leaked Tokens

**Context**: Scan decompiled files for sensitive strings like API keys or auth tokens commonly hardcoded in dev builds.

**Command** ([[commands/grep-search-strings]]):
```bash
grep -r -i "token\|api_key\|credential\|uber_internal" decompiled-output/
```

> Recursively searches for keywords. Expected output: File paths and lines containing matches, e.g., "decompiled-output/assets/config.json: "auth_token": "uber-secret-12345"." Manually inspect and copy potential tokens.

### Step 3: Inspect with GUI Tool (Optional)

**Context**: For easier navigation, load the APK into jadx GUI to view decompiled Java/Kotlin source.

**Command** (jadx-gui):
```bash
jadx-gui uber-dev.apk
```

> Launches the GUI; browse classes and search for strings. Expected: Viewable source code revealing hardcoded values.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Credentials In Files]]
- [[File and Directory Discovery]]

### Sub-Techniques


## Commands Used

- [[commands/apktool-decompile]]
- [[commands/grep-search-strings]]

## Tools Used

- [[tools/apktool]]
- [[tools/jadx]]

## Tags

- [[decompilation]]
- [[credential-extraction]]
- [[information-disclosure]]
- [[android]]
