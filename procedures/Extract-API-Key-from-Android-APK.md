---
id: proc-uuid-1
tags:
  - android
  - apk
  - credential-access
  - reverse-engineering
type: procedure
tools:
  - '[[tools/apktool]]'
tactics:
  - '[[Credential Access]]'
commands:
  - '[[commands/apktool-decompile]]'
  - '[[commands/grep-search-strings]]'
verified: false
platforms:
  - Android
  - Mobile
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Steal Application Access Token]]'
updated_at: '2025-12-14T17:32:38.680Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques:
  - '[[T1528.001]]'
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Steal Application Access Token]]'
---
# Extract-API-Key-from-Android-APK

## Summary

This procedure demonstrates how to decompile an Android APK file to extract a plaintext-stored Google Maps API key, exploiting insecure storage practices in mobile apps like Zenly.

## Description

Android APKs are ZIP archives containing app resources and code. Sensitive data like API keys stored in plaintext (e.g., in strings.xml or manifest) can be easily extracted via decompilation. This targets apps without obfuscation or secure storage, allowing attackers to obtain keys for further abuse. Prerequisites include the APK file and a local environment with decompilation tools. Expected outcome: Retrieval of the API key string.

## Requirements

1. Target APK file (e.g., Zenly.apk downloaded from app store or device)
2. Java Runtime Environment (for apktool)
3. Local machine with bash or equivalent shell

## Defense

Defensive measures and detection strategies:

- Obfuscate or encrypt API keys in app code and use server-side validation
- Implement API restrictions like IP allowlisting, referer checks, and per-key quotas in Google Cloud Console
- Monitor app decompilation attempts via integrity checks (e.g., SafetyNet API)

## Objectives

1. Decompile the APK to access internal files
2. Search for and extract the API key
3. Validate the key for use in subsequent abuse

## Instructions

### Step 1: Decompile the APK

**Context**: Use apktool to unpack the APK into readable resources and smali code, exposing plaintext strings.

**Command** ([[commands/apktool-decompile]]):
```bash
apktool d target.apk -o decompiled_dir
```

> This command decodes the APK resources. Expected output: A 'decompiled_dir' folder with assets, res, and smali directories. No errors indicate success.

### Step 2: Search for the API Key

**Context**: Grep through decompiled files for common API key patterns (Google keys often start with 'AIza').

**Command** ([[commands/grep-search-strings]]):
```bash
grep -r "AIza" decompiled_dir/
```

> This recursively searches for the key. Expected output: Lines showing the full key, e.g., in res/values/strings.xml.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]] Credential Access

### Techniques

- [[Steal Application Access Token]] Steal Application Access Token

### Sub-Techniques

- [[T1528.001]] Steal Application Access Token: Application Access Token (adapted for mobile API keys)

## Commands Used

- [[commands/apktool-decompile]]
- [[commands/grep-search-strings]]

## Tools Used

- [[tools/apktool]]

## Tags

- android
- apk
- reverse-engineering
