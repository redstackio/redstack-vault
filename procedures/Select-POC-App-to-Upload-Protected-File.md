---
id: uuid-proc-5
tags:
  - exploitation
  - path-traversal
  - leak
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/Insufficient-Path-Check]]'
verified: false
platforms:
  - Android
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[File and Directory Discovery]]'
  - '[[Unsecured Credentials]]'
updated_at: '2025-12-14T17:24:41.940Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
  - '[[Unsecured Credentials]]'
---
# Select POC App to Upload Protected File

## Summary

This procedure selects the POC app in the file picker, causing it to provide a private file URI that bypasses validation and uploads sensitive data to the shareable folder.

## Description

The bypass exploits the incomplete check in FileUploader.java, which only blocks '/data/data/' but not '/data/user/0/', allowing access to user-private storage.

## Requirements

1. Upload intent active
2. POC app ready
3. Vulnerable Nextcloud version

## Defense

Defensive measures and detection strategies:

- Update path check to block '/data/user/' variants
- Audit uploaded files for private path origins
- Implement URI scheme validation

## Objectives

1. Trigger POC to return private URI
2. Bypass validation and upload file
3. Achieve data leakage via public share

## Instructions

### Step 1: Choose POC App

**Context**: Resolve intent to malicious provider.

In chooser, select "poc" app.

**Expected Output**: Activity launches briefly and returns URI.

### Step 2: Confirm Upload

**Context**: App processes URI, hits vulnerable check.

The upload proceeds as the path check [[commands/Insufficient-Path-Check]] fails to block:

```java
if (file.getStoragePath().startsWith("/data/data/")) { Log_OC.d(TAG, "Upload from sensitive path is not allowed"); return; }
```

> Logs only for exact match; '/data/user/0/' passes. Expected output: File uploads to folder.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[File and Directory Discovery]] File and Directory Discovery
- [[Unsecured Credentials]] Unsecured Credentials

### Sub-Techniques


## Commands Used

- [[commands/Insufficient-Path-Check]]

## Tools Used


## Tags

- [[bypass]]
- [[upload-exploitation]]
