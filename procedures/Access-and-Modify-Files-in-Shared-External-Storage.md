---
tags:
  - android
  - shared-storage
  - modification
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Android
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[T1533]]'
updated_at: '2025-12-14T17:24:39.410Z'
sub_techniques: []
id: 6425e268-0202-4390-81d5-7c2b24d42c2a
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[T1533]]'
---
# Access and Modify Files in Shared External Storage

## Summary

This procedure demonstrates how a third-party Android app can access, read, modify, or delete media files stored by the Nextcloud app in shared external storage, exploiting the lack of access controls.

## Description

Android's shared external storage (/sdcard/) allows apps with basic permissions to interact with files in /sdcard/Android/media/com.nextcloud.client/nextcloud/ACCOUNT/. Even with Nextcloud's app lock enabled, local files remain unprotected. An attacker can use any app (malicious or benign) to perform operations like overwriting files with empty content or deleting them, leading to potential data loss or corruption upon sync.

## Requirements

1. Android device with downloaded Nextcloud media files in shared storage.
2. Third-party app installed with READ_EXTERNAL_STORAGE and WRITE_EXTERNAL_STORAGE permissions.
3. File explorer or custom app capable of navigating /sdcard/.

## Defense

Defensive measures and detection strategies:

- Migrate to Android versions with scoped storage (API 29+), which limits shared access.
- Configure Nextcloud app to use internal storage only (if available in updates).
- Regularly audit installed apps' permissions and scan for unauthorized file access via device logs.
- Use endpoint detection tools to monitor storage modifications.

## Objectives

1. Retrieve sensitive file contents for confidentiality breach.
2. Alter or delete files to compromise integrity.
3. Operate without user detection or app lock interference.

## Instructions

### Step 1: Access Shared Folder

**Context**: Use a third-party app to locate and interact with the exposed files.

No specific command; perform via app UI or ADB if rooted:

- Open a file manager app (e.g., built-in Files app).
- Navigate to /sdcard/Android/media/com.nextcloud.client/nextcloud/ACCOUNT/.
- List files and read contents (e.g., open image to view).

### Step 2: Perform Modifications

**Context**: Alter files to demonstrate integrity violation.

- Select a file (e.g., image.jpg).
- Overwrite with empty file: Copy an empty file to replace it, or delete directly.

> Changes are immediate and undetectable until sync; verify by checking file size or existence.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[T1533]] Data from Local System

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[android]]
- [[shared-storage]]
- [[modification]]
