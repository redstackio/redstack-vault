---
tags:
  - android
  - source-code-review
  - broadcast
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Android
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[System Information Discovery]]'
updated_at: '2025-12-14T17:24:42.255Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 3160c7ba-fcef-447a-b754-5ed9602049ec
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[System Information Discovery]]'
---
# Review-Nextcloud-Android-Source-Code-for-Insecure-Broadcasts

## Summary

This procedure involves statically analyzing the Nextcloud Android app's source code to identify uses of unprotected sticky broadcasts that expose sensitive file upload and sync information, enabling potential interception by malicious apps.

## Description

The Nextcloud Android app uses Context.sendStickyBroadcast to notify about file operations, which are globally accessible without package restrictions. By reviewing the GitHub source, attackers can pinpoint exact locations where intents carry account details, file paths, and status updates. This is a reconnaissance step for mobile app security assessments, targeting Java-based Android apps with insecure inter-component communication (ICC).

## Requirements

1. Access to GitHub repository (public for Nextcloud)
2. Basic Java and Android development knowledge
3. Text editor or IDE like Android Studio for code navigation

## Defense

Defensive measures and detection strategies:

- Use LocalBroadcastManager for internal app communications
- Apply permission checks or package targeting to broadcasts
- Static analysis tools like MobSF to detect exported receivers/broadcasts

## Objectives

1. Locate vulnerable broadcast sends in source code
2. Document exposed data types (e.g., account, files)
3. Assess feasibility of interception attacks

## Instructions

### Step 1: Access Repository

**Context**: Clone or browse the Nextcloud Android source to begin analysis.

Navigate to https://github.com/nextcloud/android and search for files like FileUploader.java and SyncFolderHandler.java.

### Step 2: Examine Broadcast Calls

**Context**: Identify sendStickyBroadcast usages and inspect intent payloads.

Review FileUploader.java:

- Line 1116: Context.sendStickyBroadcast for UPLOAD_FINISH
- Line 1136: Context.sendStickyBroadcast for UPLOADS_ADDED
- Line 1170: Context.sendStickyBroadcast for UPLOAD_START

Check SyncFolderHandler.java:

- Line 186 and 201: Similar broadcasts for sync events

Extract intent extras like account name, file URI, and status.

### Step 3: Validate Exposure

**Context**: Confirm broadcasts are not restricted to the app's package.

Note absence of LocalBroadcastManager; broadcasts use global Context, making them interceptable by any exported receiver.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[System Information Discovery]] System Information Discovery

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[android]]
- [[source-review]]
- [[icc-exploitation]]
