---
tags:
  - android
  - intent-crafting
  - file-targeting
type: procedure
tools:
  - '[[tools/Android-Debug-Bridge-ADB]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Android
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:42.054Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: f015900a-6e9d-4cac-8582-2edf97986d8c
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Craft Malicious Intent for Private File Targeting

## Summary

This procedure crafts an Android Intent targeting a private file URI in the LINE Lite app's storage, exploiting the lack of validation in SelectShareActivity to set up file theft.

## Description

Android Intents allow inter-app communication. Here, a malicious app or ADB command constructs an intent with action VIEW or SEND, using a content URI like content://com.linecorp.linelite.file_provider/internal/path/to/private/file. This requires user interaction (e.g., button press) to send. The target is LINE Lite's internal storage files, such as /data/data/com.linecorp.linelite/files/private.db.

## Requirements

1. Knowledge of target app's file provider authority (com.linecorp.linelite.file_provider)
2. ADB access or ability to build a simple malicious APK
3. Installed target app with private files present

## Defense

Defensive measures and detection strategies:

- Validate all incoming intent URIs against whitelists in app code
- Use signature-based intent permissions
- Log and monitor intent receptions for anomalies

## Objectives

1. Create intent with malicious URI
2. Ensure it targets private storage
3. Prepare for transmission

## Instructions

### Step 1: Determine Private File Path

**Context**: Identify a target private file path within LINE Lite's data directory.

**Instructions**: Use ADB to list app files: adb shell run-as com.linecorp.linelite ls /data/data/com.linecorp.linelite/files/ to find paths like chat_history.db.

**Expected Output**: List of private files.

### Step 2: Construct Intent URI

**Context**: Build the content URI for the intent.

**Instructions**: Form URI as content://com.linecorp.linelite.file_provider/files/private_file.db. In a malicious app, use Intent intent = new Intent().setAction(Intent.ACTION_SEND).setDataAndType(Uri.parse("content://..."), "*/*");

**Expected Output**: Valid intent object ready to target the activity.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Android-Debug-Bridge-ADB]]

## Tags

- [[android]]
- [[intent-crafting]]
- [[file-targeting]]
