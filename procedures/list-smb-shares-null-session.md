---
id: 81533047-cdce-4113-abf3-1ca57817d302
name: list-smb-shares-null-session
type: procedure
verified: true
submitted: true
created_at: '2019-12-04T17:49:54.294983+00:00'
updated_at: '2023-05-25T19:45:55.121753+00:00'
tactics:
  - '[[Discovery]]'
techniques:
  - '[[Network Share Discovery]]'
sub_techniques: []
tags:
  - data-exposure
  - network
  - service-attacks
  - smb
commands:
  - '[[commands/smbclient-list-smb-shares]]'
  - '[[commands/smbmap-list-smb-shares]]'
platforms:
  - Linux
  - Windows
tools:
  - '[[tools/smbclient]]'
  - '[[tools/SMBMap]]'
validated: true
---

# List SMB Shares Null Session

## Summary

This procedure queries a Windows SMB server to list available shares using a null session (anonymous access), helping identify exposed resources like SYSVOL without credentials. It's useful in initial reconnaissance to map network shares in an AD environment.

## Description

SMB shares on Windows systems can often be enumerated anonymously if not properly restricted, revealing administrative shares (ADMIN$, C$), IPC$, and domain-specific ones like SYSVOL. This technique leverages tools like smbclient and smbmap to perform the enumeration, providing details on share names, types, and permissions. In attack scenarios, this leads to discovering misconfigured shares containing sensitive data, such as GPP files with encrypted passwords.

## Requirements

1. Network connectivity to target on port 445 (SMB)
2. Kali Linux or similar with smbclient and smbmap installed
3. No credentials needed for null session
4. Target: Windows host or domain member

## Defense

- Restrict null sessions via SMB signing and registry keys (e.g., RestrictAnonymous=2)
- Monitor SMB traffic for enumeration attempts using tools like Zeek or Windows Event Logs (ID 4625 for anon logons)
- Use firewalls to limit SMB access to trusted networks

## Objectives

1. Identify accessible SMB shares anonymously
2. Determine share permissions (READ, WRITE, NO ACCESS)
3. Spot sensitive shares like SYSVOL for further exploitation

## Instructions

### Step 1: List Shares with smbclient

**Context**: smbclient provides a basic listing of shares using null authentication, ideal for quick checks.

**Command** ([[commands/smbclient-list-smb-shares]]):
```bash
smbclient -U '' -N -L $_TARGET_IP
```

> This attempts anonymous connection and lists shares. Expected: Table of sharename, type, comment (e.g., SYSVOL Disk).

### Step 2: Enumerate with smbmap for Permissions

**Context**: smbmap extends enumeration by showing read/write permissions, helping prioritize accessible shares.

**Command** ([[commands/smbmap-list-smb-shares]]):
```bash
smbmap -u '' -p '' -H $_TARGET_IP
```

> Outputs IP, share disks, and permissions (e.g., SYSVOL READ ONLY). If authenticated, provide creds for deeper access.

### Step 3: Verify and Document

**Context**: Cross-reference outputs to confirm shares like SYSVOL are accessible, preparing for browsing.

No command; manually note accessible shares for next steps.
