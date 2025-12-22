---
id: 552c9bc6-debd-4436-aed7-489a2522a74b
name: Browse-SMB-Share-with-Credentials
type: procedure
verified: true
submitted: true
created_at: '2019-12-11T19:01:24.467538+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[Collection]]'
techniques:
  - '[[Data from Network Shared Drive]]'
sub_techniques: []
platforms:
  - Linux
  - Windows
tags:
  - network
  - service-attacks
commands:
  - '[[commands/smbclient-connect-authenticated]]'
tools:
  - '[[tools/Samba]]'
validated: true
---

# Browse-SMB-Share-with-Credentials

## Summary

This procedure authenticates to an SMB share using obtained credentials and browses contents interactively to collect data or identify further targets.

## Description

After credential acquisition, smbclient provides a shell-like interface to navigate shares (e.g., C$, ADMIN$). It's useful for exfiltrating files or mapping network structure. Supports NULL sessions if no creds, but here uses auth for deeper access. Targets Windows file sharing on port 445.

## Requirements

- Valid SMB credentials
- smbclient installed (Samba package)
- Target IP and share name (e.g., IPC$, C$)

## Defense

- Restrict share permissions (e.g., no guest access)
- Audit file access logs (Event ID 5145 for share access)
- Disable unnecessary shares via Group Policy
- Use EDR to monitor smbclient-like tools

## Objectives

- Authenticate to share
- List and navigate directories
- Download sensitive files if present

## Instructions

### Step 1: Connect to SMB Share

**Context**: Use credentials to mount the share interactively. Start with IPC$ for enumeration.

**Command** ([[commands/smbclient-connect-authenticated]]):
```bash
smbclient -U $_USERNAME%$_PASSWORD //$_TARGET_IP/$_SHARE_NAME
```

> % combines user:pass. Expected: smb: \> prompt. If fails, check creds/share. For NULL: omit -U.

### Step 2: Browse and Interact

**Context**: Once connected, use SMB commands to explore.

> ls (list), cd dir (change), get file (download), quit (exit). Why: Reveals configs, users. Decision: If no files, try other shares like SYSVOL.
