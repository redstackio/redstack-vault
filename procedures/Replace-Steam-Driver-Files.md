---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567893
tags:
  - driver-replacement
  - file-modification
type: procedure
tools:
  - '[[tools/Steam]]'
tactics:
  - '[[Privilege Escalation]]'
commands: []
verified: false
platforms:
  - Windows
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T17:29:36.126Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
---
# Replace-Steam-Driver-Files

## Summary

This procedure replaces legitimate Steam Remote Play driver files with malicious versions in the writable directory, exploiting the lack of runtime integrity checks to enable kernel driver installation.

## Description

After Steam startup, the driver directory remains writable by normal users. Replacing `SteamStreamingMicrophone.sys` and `SteamStreamingSpeakers.sys` with tampered files (e.g., from fake_driver.zip) allows SteamServices to install them without verification during the first Remote Play session, leading to privilege escalation.

## Requirements

1. Steam running on Windows 10 x64
2. Malicious driver files prepared (e.g., sized 40KB and 8KB)
3. Standard user access (directory is writable)

## Defense

Defensive measures and detection strategies:

- Implement file integrity monitoring (e.g., Windows Defender ATP) on Steam directories
- Set driver directories to read-only for non-admin users
- Scan for anomalous file sizes or signatures in driver folders

## Objectives

1. Modify driver files post-Steam startup
2. Avoid triggering auto-replacement
3. Position for malicious installation

## Instructions

### Step 1: Locate Driver Directory

**Context**: Navigate to the vulnerable writable path where drivers reside.

Open File Explorer and go to `C:\Program Files (x86)\Steam\drivers\Windows10\x64`.

> Expected output: Directory accessible with original sys files present.

### Step 2: Backup Original Files

**Context**: Optionally preserve originals, though not required for attack.

Copy `SteamStreamingMicrophone.sys` and `SteamStreamingSpeakers.sys` to a safe location.

> Expected output: Backups created.

### Step 3: Replace with Malicious Files

**Context**: Overwrite with tampered drivers while Steam runs to bypass checks.

Extract files from `fake_driver.zip` and replace the originals. Verify sizes: Microphone ~40KB, Speakers ~8KB.

> Expected output: Modified files in place, no Steam restart.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Steam]]

## Tags

- [[driver-replacement]]
- [[file-modification]]
