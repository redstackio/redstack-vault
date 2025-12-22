---
id: proc-examine-androidmanifest-deeplinks
tags:
  - recon
  - android
  - manifest
  - deeplink
type: procedure
tools: []
tactics:
  - '[[Impact]]'
commands: []
verified: false
platforms:
  - Android
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T17:24:39.769Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Examine-AndroidManifest-for-Registered-Deeplinks

## Summary

This procedure involves reviewing the AndroidManifest.xml file of the Nextcloud Android client to identify registered deeplinks, enabling targeted analysis of potential vulnerabilities in intent handling.

## Description

In Android apps, deeplinks are defined in the manifest to handle custom URI schemes. For the Nextcloud client, the `nc://login` scheme is registered to the `ModifiedAuthenticatorActivity`. This step is crucial for reconnaissance in mobile app security testing, as it reveals entry points for intent-based attacks like DoS via malformed inputs. Prerequisites include obtaining the APK (e.g., via download or extraction) and using tools like APKTool for decompilation.

## Requirements

1. Access to the Nextcloud Android APK file
2. Decompilation tool like APKTool or Jadx installed
3. Basic knowledge of Android app structure

## Defense

Defensive measures and detection strategies:

- Use app signing and integrity checks to prevent tampering with APKs
- Monitor for anomalous deeplink registrations in app updates
- Employ static analysis tools in CI/CD to validate manifest entries

## Objectives

1. Locate custom URI schemes and their handling activities
2. Identify potential vectors for intent exploitation
3. Gather details for subsequent code analysis

## Instructions

### Step 1: Decompile the APK

**Context**: Extract the manifest from the app package to inspect intent filters.

No specific command; use APKTool:

```bash
apktool d nextcloud.apk -o output_dir
```

> This decodes the APK into readable files, including AndroidManifest.xml. Review the file for `<intent-filter>` elements with `<data android:scheme="nc" android:host="login" />`.

### Step 2: Identify Target Activity

**Context**: Pinpoint the activity handling the deeplink.

Inspect the manifest for the activity name associated with the filter, such as `com.owncloud.android.authentication.ModifiedAuthenticatorActivity`.

**Expected Output**: Full path to the handler: `com.nextcloud.client/com.owncloud.android.authentication.ModifiedAuthenticatorActivity`.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Gather Victim Host Information]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- recon
- android
- manifest
