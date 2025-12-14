---
id: proc-uuid-002
tags:
  - smb
  - access-control
  - initial-access
type: procedure
tools:
  - '[[tools/smbclient]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/smbclient-connect-anon]]'
verified: false
platforms:
  - SMB
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[External Remote Services]]'
updated_at: '2025-12-14T17:31:52.665Z'
skill_level: beginner
impact_level: high
detection_risk: medium
sub_techniques:
  - '[[T1133.001]]'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[External Remote Services]]'
---
# Access-SMB-Shares-Without-Authentication

## Summary

This procedure demonstrates connecting to and extracting data from SMB shares that lack proper authentication, as seen in the exposure of Starbucks CCTV footage in Thailand.

## Description

Exploiting improper access controls, attackers connect anonymously to SMB shares hosting sensitive files. The target environment includes SMB servers in regions like Thailand, with shares for CCTV backups. Expected outcomes include downloading videos and images, leading to privacy violations.

## Requirements

1. Identified SMB host and share from prior reconnaissance
2. smbclient tool for anonymous connections
3. Local storage for downloaded files

## Defense

Defensive measures and detection strategies:

- Enforce authentication on all SMB shares using Active Directory or local accounts
- Disable null sessions and guest access in SMB configuration
- Log and alert on anonymous SMB connections via Windows Event Logs or Sysmon

## Objectives

1. Establish anonymous connection to exposed share
2. Retrieve sensitive files like CCTV footage
3. Exfiltrate data without detection

## Instructions

### Step 1: Connect to SMB Share Anonymously

**Context**: Initiate a null session to the exposed share.

**Command** ([[commands/smbclient-connect-anon]]):
```bash
smbclient //target-ip/CCTV-Backup -N
```

> This connects without a password. Expected output: 'smb: \> ' prompt indicating successful anonymous login.

### Step 2: Download Files

**Context**: Navigate and transfer files from the share.

**Command** (inside smbclient):
```bash
ls
get footage.mp4
exit
```

> 'ls' lists files, 'get' downloads them. Expected output: Files saved locally, confirming access to sensitive content.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[External Remote Services]] External Remote Services

### Sub-Techniques

- [[T1133.001]] SMB/Windows Admin Shares

## Commands Used

- [[commands/smbclient-connect-anon]]

## Tools Used

- [[tools/smbclient]]

## Tags

- [[smb]]
- [[initial-access]]
