---
id: a6afbe1c-85db-4edf-92fa-089cf9aec604
name: Observe-App-Crash-and-File-Overwrite
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:21.737Z'
tactics:
  - '[[Collection]]'
techniques:
  - '[[Data from Local System]]'
tags:
  - crash
  - overwrite
  - verification
platforms:
  - Android
tools: []
skill_level: low
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Data from Local System]]'
---

# Observe-App-Crash-and-File-Overwrite

## Summary

This procedure verifies the exploit success by monitoring the app crash and confirming overwrites in private storage directories.

## Description

Post-extraction, the LINE app throws a SecurityException due to access violations, but the traversal has already overwritten files in /data/data/jp.naver.line.android/files/. Use ADB or file explorer to inspect changes. A related pre-fixed insecure storage issue in external storage is noted but not exploited here. This confirms compromise of sensitive app data.

## Requirements

1. Rooted device or ADB access for file inspection
2. Crash logs accessible via logcat
3. Knowledge of target file paths

## Defense

Defensive measures and detection strategies:

- Enable detailed crash logging and anomaly detection
- Audit file changes in private directories
- Implement file integrity checks post-extraction

## Objectives

1. Capture the SecurityException crash
2. Verify overwrites in private app folders
3. Assess impact on app functionality and data

## Instructions

### Step 1: Monitor During Extraction

**Context**: Watch for immediate crash.

Use ADB logcat to observe:

```bash
adb logcat | grep SecurityException
```

> Expect crash log with extraction error.

### Step 2: Inspect Files

**Context**: Check for overwrites.

Use ADB shell to examine directories:

```bash
adb shell ls /data/data/jp.naver.line.android/files/
```

> Look for modified or new files from malicious ZIP.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Data from Local System]] Data from Local System

### Sub-Techniques


## Commands Used

- [[commands/adb-logcat-security]]
- [[commands/adb-shell-ls-files]]

## Tools Used


## Tags

- [[crash]]
- [[overwrite]]
- [[verification]]
