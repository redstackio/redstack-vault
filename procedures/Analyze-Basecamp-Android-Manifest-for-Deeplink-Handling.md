---
tags:
  - android
  - manifest-analysis
  - deeplink
type: procedure
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Android
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:26:27.196Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 83c73050-acb3-4a77-8a0a-7955abb75457
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Analyze Basecamp Android Manifest for Deeplink Handling

## Summary

This procedure involves inspecting the AndroidManifest.xml of the Basecamp app to identify deeplink intent filters and vulnerable parameters like 'filename' used for local file operations, enabling discovery of path traversal opportunities.

## Description

In the context of mobile app security testing, analyzing the manifest reveals how the app handles external URLs, particularly deeplinks that trigger file saves. For Basecamp, the manifest declares handling of https://3.basecamp.com/* with a 'filename' query parameter, which lacks sanitization, allowing subsequent exploitation. This step is crucial for reconnaissance in app vulnerability assessments and requires access to the APK file.

## Requirements

1. Basecamp APK file (download from official sources or extract from device)
2. Android development tools (e.g., Android Studio, APKTool, or aapt for manifest extraction)
3. Basic knowledge of Android intent filters and URI schemes

## Defense

Defensive measures and detection strategies:

- Implement app manifest obfuscation or runtime deeplink validation
- Monitor for anomalous APK analyses in security logs
- Use mobile security frameworks like Mobile Security Framework (MobSF) for automated manifest scanning

## Objectives

1. Identify deeplink schemes and associated activities
2. Locate query parameters involved in file handling
3. Confirm lack of input validation for traversal payloads

## Instructions

### Step 1: Extract and Parse Manifest

**Context**: Obtain and decode the APK to access the AndroidManifest.xml file.

Use APKTool or aapt to decompile:

Decompile the APK to view intent filters for deeplinks.

> Expected: Manifest shows <intent-filter> with data scheme "https://3.basecamp.com/*" and extras for 'filename'.

### Step 2: Review Intent Filters

**Context**: Examine filters for file save intents triggered by deeplinks.

Search for actions like VIEW or SEND that process query parameters.

> Expected: Confirmation of 'filename' parameter passed unsanitized to file write operations.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[File and Directory Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[android]]
- [[manifest-analysis]]
- [[deeplink]]
