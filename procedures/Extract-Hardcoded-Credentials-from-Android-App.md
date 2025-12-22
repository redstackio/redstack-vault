---
tags:
  - android
  - decompile
  - credential-access
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Android
techniques:
  - '[[File and Directory Discovery]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: fb3eb6e0-f217-4fd0-adfa-f7af1d8d4b6b
created_at: '2025-12-14T17:32:48.328Z'
updated_at: '2025-12-14T17:32:48.328Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Extract-Hardcoded-Credentials-from-Android-App

## Summary

This procedure involves decompiling an Android APK to inspect and extract hardcoded API credentials, such as those for Cloudinary, embedded in the app's source code. It targets client-side code where secrets are improperly stored, enabling credential theft without runtime execution.

## Description

In scenarios like the Reverb.com Android app, developers may hardcode sensitive configuration strings in Java files, violating best practices for cloud services. By decompiling the APK using tools like Jadx or APKTool, attackers can locate these strings in classes like CloudinaryFacade.java. The extracted credentials (cloud_name, api_key, api_secret) allow subsequent API authentication. Prerequisites include obtaining the APK from sources like the Google Play Store or direct download. Expected outcomes include full credential disclosure, leading to potential account compromise.

## Requirements

1. Android APK file for the target app (e.g., Reverb.com)
2. Decompilation tool installed (e.g., Jadx GUI or APKTool)
3. Basic knowledge of Java and Android app structure

## Defense

Defensive measures and detection strategies:

- Use environment variables or secure vaults (e.g., AWS Secrets Manager) for API credentials instead of hardcoding.
- Obfuscate app code with ProGuard or R8 to hinder decompilation.
- Implement runtime credential fetching from secure backends and monitor for anomalous API access patterns.

## Objectives

1. Locate hardcoded configuration strings in decompiled source.
2. Extract usable API credentials for cloud services.
3. Enable follow-on authentication and access.

## Instructions

### Step 1: Obtain and Decompile the APK

**Context**: Download the target APK and decompile it to access the source code.

Use a decompiler like Jadx:

```bash
jadx -d output_dir reverb.apk
```

> This command extracts the Java source code to the output directory. Navigate to com/reverb/app/CloudinaryFacade.java.

### Step 2: Search for Credentials

**Context**: Inspect the decompiled files for hardcoded strings containing API details.

Manually search in CloudinaryFacade.java for the configuration URL format.

**Expected Output**: String like 'cloudinary://434762629765715:█████@reverb', parsing to cloud_name='reverb', api_key='434762629765715', api_secret='█████'.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[File and Directory Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[android]]
- [[decompile]]
- [[credential-access]]
