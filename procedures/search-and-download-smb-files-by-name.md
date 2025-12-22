---
id: 4d1e4a4d-cd7e-4614-be4b-805795cce47a
name: search-and-download-smb-files-by-name
type: procedure
verified: true
submitted: true
created_at: '2019-12-04T18:19:37.061420+00:00'
updated_at: '2023-05-25T19:47:12.339932+00:00'
tactics:
  - '[[Collection]]'
techniques:
  - '[[Data from Network Shared Drive]]'
sub_techniques: []
tags:
  - data-exposure
  - network
  - service-attacks
  - smb
commands:
  - '[[commands/smbmap-search-smb-share-recursively]]'
platforms:
  - Linux
  - Windows
tools:
  - '[[tools/SMBMap]]'
validated: true
---

# Search and Download SMB Files by Name

## Summary

This procedure recursively searches SMB shares for files matching specific names or patterns (e.g., 'Groups.xml', 'password') and automatically downloads them. It's efficient for harvesting sensitive data from large shares like SYSVOL in AD environments.

## Description

SMB shares often hold configs, scripts, and policy files with embedded secrets. smbmap automates recursive traversal, pattern matching, and download, reducing manual effort. Useful post-enumeration to target known vulnerable files like GPP XMLs containing cPassword attributes.

## Requirements

1. Accessible share (null or auth)
2. smbmap installed (pip install smbmap)
3. Target IP and share name
4. Optional: Creds for auth shares

## Defense

- Implement file name obfuscation or remove sensitive files from shares
- Log file access events (Windows ID 4663) and alert on recursive patterns
- Use DLP tools to scan shares for PII/secrets

## Objectives

1. Recursively search share for target filenames
2. Download all matches automatically
3. Collect potential credential sources

## Instructions

### Step 1: Prepare Search Parameters

**Context**: Identify keywords from recon (e.g., 'Groups' for GPP files).

No command; define $_FILENAME as 'Groups.xml' or '*pass*'.

### Step 2: Execute Recursive Search and Download

**Context**: smbmap crawls the share, matches files, and saves locally.

**Command** ([[commands/smbmap-search-smb-share-recursively]]):
```bash
smbmap -u '$_USERNAME' -p '$_PASSWORD' -R $_SHARE_NAME -H $_TARGET_IP -A $_FILENAME -q
```

> For null: empty u/p. Expected: '[+] Match found! Downloading: path\file'.

### Step 3: Verify Downloads

**Context**: Check local files for content.

```bash
ls -la *.xml
cat Groups.xml | grep cPassword
```

> Confirms encrypted strings extracted.
