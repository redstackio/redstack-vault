---
id: 4d1e4a4d-cd7e-4614-be4b-805795cce47a
name: Search-and-Download-Files-from-SMB-Share
type: procedure
verified: true
submitted: true
created_at: '2019-12-04T18:19:37.061420+00:00'
updated_at: '2023-05-25T19:47:12.339932+00:00'
tactics:
  - '[[tactics/Collection|TA0009 - Collection]]'
techniques:
  - >-
    [[techniques/Data from Network Shared Drive|T1039 - Data from Network Shared
    Drive]]
sub_techniques: []
platforms:
  - Linux
  - Windows
tags:
  - data-exposure
  - network
  - service-attacks
commands:
  - '[[commands/smbmap-search-smb-share-recursively]]'
tools:
  - '[[tools/SMBMap]]'
validated: true
---

# Search-and-Download-Files-from-SMB-Share

## Summary

This procedure recursively searches SMB shares for files matching patterns (e.g., passwords, XML) and automatically downloads them.

## Description

SMB shares often hold sensitive docs; SMBMap crawls directories, matching filenames and pulling files. Useful post-enumeration to target GPP files in SYSVOL without manual browsing.

## Requirements

- Accessible share (e.g., SYSVOL)
- Credentials for read access
- SMBMap installed

## Defense

- Remove unnecessary files from shares
- Implement file access auditing
- Use DLP tools to scan share contents

## Objectives

1. Search for specific filenames
2. Download matching files
3. Collect sensitive data

## Instructions

### Step 1: Recursive Search and Download

**Context**: Target SYSVOL for GPP files like Groups.xml.

**Command** ([[commands/smbmap-search-smb-share-recursively]]):
```bash
smbmap -u $_USERNAME -p $_PASSWORD -R $_SHARE_NAME -H $_TARGET_IP -A $_FILENAME -q
```

> Quiet mode (-q) suppresses output; files download to current dir.

### Step 2: Verify Downloads

**Context**: Check for downloaded files and inspect.

ls downloaded_files/; cat Groups.xml | grep cpassword.

> Success if target files present.
