---
id: uuid-for-attack-chain
tags:
  - android
  - credential-leak
  - reverse-engineering
  - api-keys
type: attack_chain
tools:
  - '[[tools/keyhacks]]'
tactics:
  - '[[Credential Access]]'
verified: false
platforms:
  - Android
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Decompile-Android-APK-to-Access-Resources]]'
  - '[[procedures/Search-for-Hardcoded-API-Keys-in-Decompiled-Files]]'
step_count: 2
techniques:
  - '[[Unsecured Credentials]]'
  - '[[Credentials In Files]]'
updated_at: '2025-12-14T17:32:39.140Z'
description: >-
  Attack chain demonstrating the extraction of sensitive API keys hardcoded in
  an Android app's strings.xml file through APK decompilation and inspection,
  leading to potential impersonation and malicious API usage.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Unsecured Credentials]]'
  - '[[Credentials In Files]]'
---
# Extracting Hardcoded API Keys from Android App via Decompilation

Multi-stage attack chain demonstrating a complete workflow for discovering and extracting insecurely stored API keys in an Android application, enabling attackers to impersonate the app and perform unauthorized API requests.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Decompile APK] --> B[Extract and Validate Keys]
    B --> C[Impersonate App for Malicious Requests]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/apktool]] (for decompilation, inferred standard tool)
- [[tools/keyhacks]]
- Java Development Kit (JDK) for running decompilers

### Target Environment

- Android APK file (obtainable from app stores or direct download)
- Local machine with Linux/macOS/Windows for reverse engineering tools
- No network access required for extraction, but internet needed to validate keys

### Initial Access Requirements

- Possession of the target APK file
- No credentials or prior access needed; the vulnerability is client-side

## Detailed Attack Procedures

### Step 1: Decompile the Android APK
procedure: [[procedures/Decompile-Android-APK-to-Access-Resources]]

**Objective**: Reverse engineer the APK to access internal resources like strings.xml containing hardcoded sensitive data.

**Instructions**: Obtain the APK (e.g., via sideloading or download). Use a decompiler like apktool to unpack the APK:

```bash
apktool d target.apk -o decompiled_output
```

Navigate to the decompiled_output/res/values/ directory to inspect strings.xml.

**Expected Output**: Unpacked APK resources, including XML files with string definitions.

**Success Indicators**:
- APK successfully decompiled without errors
- strings.xml file accessible and readable

### Step 2: Search for Sensitive Information
procedure: [[procedures/Search-for-Hardcoded-API-Keys-in-Decompiled-Files]]

**Objective**: Identify and extract API keys/tokens from decompiled files, then validate their activity and permissiveness.

**Instructions**: Manually inspect strings.xml for patterns like 'AIza' (Google API keys) or MapBox tokens. Use grep for automation:

```bash
grep -r "AIza" decompiled_output/res/values/strings.xml
```

Validate extracted keys using [[tools/keyhacks]] to check if they are active:

```bash
python keyhacks.py --google-maps <extracted_key>
```

**Expected Output**: List of potential keys with validation results indicating if they are live and permissive.

**Success Indicators**:
- Sensitive strings (e.g., API keys) found in strings.xml
- Keys confirmed active via validation tool

## Attack Chain Summary

### Key Achievements

1. Successful decompilation of the APK to reveal internal resources
2. Extraction of multiple hardcoded API keys for Google Maps and MapBox
3. Validation confirming keys allow impersonation for malicious requests, potentially leading to data pollution

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Unsecured Credentials]] Unsecured Credentials
- [[Credentials In Files]] Credentials In Files

### MITRE ATT&CK Tactics

- [[Credential Access]] Credential Access

---
*Last updated: 2023-10-01T00:00:00Z*
