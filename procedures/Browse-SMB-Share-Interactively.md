---
id: 552c9bc6-debd-4436-aed7-489a2522a74b
name: Browse-SMB-Share-Interactively
type: procedure
verified: true
submitted: false
created_at: '2019-12-11T19:01:24.467538+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
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
  - network
  - service-attacks
commands:
  - '[[commands/smbclient-connect-to-smb-share]]'
tools:
  - '[[tools/smbclient]]'
validated: true
---

# Browse-SMB-Share-Interactively

## Summary

This procedure connects to an SMB share using smbclient to interactively browse and download files, useful for exploring SYSVOL contents.

## Description

Interactive browsing simulates a shell on the share, allowing ls, cd, get commands. Ideal for manual inspection of policy files in AD environments where automated tools might miss nested directories.

## Requirements

- Discovered share name (e.g., SYSVOL)
- Credentials if not null session
- smbclient installed

## Defense

- Audit share access in Event Logs (ID 5140)
- Use SMB signing to prevent tampering
- Limit share exposure to trusted networks

## Objectives

1. Connect to specific share
2. List and navigate directories
3. Download target files

## Instructions

### Step 1: Connect to the Share

**Context**: Establish session; omit credentials for null if possible.

**Command** ([[commands/smbclient-connect-to-smb-share]]):
```bash
smbclient -U $_USERNAME%$_PASSWORD //$_TARGET_IP/$_SHARE_NAME
```

> Prompts for interactive shell; use 'help' for commands.

### Step 2: Browse and Download

**Context**: Navigate to Policies folder and get Groups.xml.

In shell: ls, cd Policies, get Groups.xml.

> Exit with 'quit'; success if files listed/downloaded.
