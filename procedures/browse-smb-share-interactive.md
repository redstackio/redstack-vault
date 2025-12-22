---
id: 552c9bc6-debd-4436-aed7-489a2522a74b
name: browse-smb-share-interactive
type: procedure
verified: true
submitted: true
created_at: '2019-12-11T19:01:24.467538+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
  - '[[Collection]]'
techniques:
  - '[[Data from Network Shared Drive]]'
sub_techniques: []
tags:
  - network
  - service-attacks
  - smb
commands:
  - '[[commands/smbclient-connect-to-smb-share]]'
platforms:
  - Linux
  - Windows
tools:
  - '[[tools/smbclient]]'
validated: true
---

# Browse SMB Share Interactive

## Summary

This procedure uses smbclient to establish an interactive session with an SMB share, allowing directory listing, file navigation, and downloads. It's essential for exploring enumerated shares like SYSVOL to locate sensitive files without full file transfer tools.

## Description

Once shares are identified, an interactive SMB client enables shell-like navigation (ls, cd, get, put). Null sessions work if permitted, but authenticated access reveals more. In AD attacks, this targets SYSVOL for GPP files, exploiting legacy configs where admins store passwords.

## Requirements

1. Discovered share name (e.g., SYSVOL) from prior enumeration
2. smbclient installed (part of Samba)
3. Network access to port 445
4. Optional: Credentials for restricted shares

## Defense

- Enable SMB signing and require authentication for shares
- Audit share access in Windows Event Logs (ID 5145 for share access)
- Remove unnecessary shares and use ACLs to deny anon access

## Objectives

1. Navigate share directories interactively
2. List and identify sensitive files (e.g., Groups.xml)
3. Download files for offline analysis

## Instructions

### Step 1: Connect to Share

**Context**: Initiate null or authenticated connection to the target share.

**Command** ([[commands/smbclient-connect-to-smb-share]]):
```bash
smbclient -U '$_USERNAME%$_PASSWORD' //$_TARGET_IP/$_SHARE_NAME
```

> For null: omit -U or use empty creds. Expected: 'smb: \>' prompt.

### Step 2: List and Navigate Files

**Context**: Use shell commands to explore; 'ls' lists, 'cd' changes dirs.

At the smb prompt:
```bash
ls
cd Policies
ls
```

> Reveals files like Groups.xml in {GUID}/Machine/Preferences.

### Step 3: Download Files

**Context**: Transfer interesting files locally for further processing.

At the smb prompt:
```bash
get Groups.xml
exit
```

> Downloads file; verify locally with 'ls'.
