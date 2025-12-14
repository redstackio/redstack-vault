---
tags:
  - recon
  - android
  - deeplink
  - manifest
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Android
submitted: true
created_at: '2024-10-01'
techniques:
  - '[[Hardware]]'
updated_at: '2025-12-14T17:27:57.892Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 4c86aac6-99d2-4c32-a862-9ff925e2f03f
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Hardware]]'
---
# Analyze-Periscope-Android-Manifest-for-Deeplinks

## Summary

This procedure involves decompiling the Periscope Android APK to extract and analyze the AndroidManifest.xml file, identifying internal deeplink schemes that can be abused for CSRF attacks, such as the follow action path.

## Description

In the context of mobile app security testing, analyzing the app's manifest reveals intent filters and deeplink handlers. For Periscope, this exposes schemes like 'pscp://user/<user-id>/follow' without CSRF protections, allowing attackers to craft links that bypass confirmations present in the web interface. Prerequisites include obtaining the APK (e.g., from app stores or device extraction) and using a decompiler like APKTool. Expected outcome: Discovery of exploitable deeplinks leading to unauthorized actions.

## Requirements

1. Periscope Android APK file
2. APK decompiler tool (e.g., APKTool installed on a development machine)
3. Basic knowledge of Android XML structure

## Defense

Defensive measures and detection strategies:

- Implement app-level CSRF tokens or confirmation prompts for sensitive actions like following
- Restrict deeplink schemes to external-only or add validation in intent handlers
- Monitor for anomalous app launches via mobile security tools like Mobile Security Framework (MobSF)

## Objectives

1. Identify deeplink schemes and paths in the manifest
2. Confirm lack of confirmation for follow action in app vs. web
3. Gather technical details for crafting exploits

## Instructions

### Step 1: Decompile the APK

**Context**: Extract the AndroidManifest.xml from the Periscope APK to inspect intent filters.

Use an APK decompiler to unpack the app:

(Decompilation is typically done via GUI or command-line tool like `apktool d periscope.apk -o output_dir`)

> This outputs the manifest in output_dir/AndroidManifest.xml. Look for <intent-filter> with <data android:scheme="pscp" android:host="user" /> revealing paths like /follow.

### Step 2: Examine Data Tags

**Context**: Parse the XML for exploitable deeplinks.

Open AndroidManifest.xml and search for <data> tags:

(Grep or manually review for schemes 'pscp' and 'pscpd', hosts 'user', paths '/follow')

> Expected: Confirmation of pscp://user/<user-id>/follow as a direct action handler without prompts.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Hardware]]

### Sub-Techniques

-

## Commands Used

-

## Tools Used

-

## Tags

- recon
- android
- deeplink
- manifest
