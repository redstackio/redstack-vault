---
id: 81533047-cdce-4113-abf3-1ca57817d302
name: List-Available-SMB-Shares
type: procedure
verified: true
submitted: true
created_at: '2019-12-04T17:49:54.294983+00:00'
updated_at: '2023-05-25T19:45:55.121753+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Network Share Discovery|T1135 - Network Share Discovery]]'
sub_techniques: []
platforms:
  - Linux
  - Windows
tags:
  - data-exposure
  - network
  - service-attacks
commands:
  - '[[commands/smbclient-list-smb-shares]]'
  - '[[commands/smbmap-list-smb-shares]]'
tools:
  - '[[tools/smbclient]]'
  - '[[tools/SMBMap]]'
validated: true
---

# List-Available-SMB-Shares

## Summary

This procedure queries a Windows target for available SMB shares using null sessions or authenticated access, revealing potential data repositories like SYSVOL.

## Description

SMB shares store files accessible over the network. Null sessions allow anonymous enumeration, while authentication provides permission details. This is key for discovering misconfigured shares containing sensitive info in AD environments.

## Requirements

- Target IP with SMB enabled (port 445)
- Optional: Low-privilege credentials
- smbclient or SMBMap installed

## Defense

- Disable null sessions via SMB policy
- Restrict share permissions to authenticated users only
- Monitor for enumeration attempts in Windows Event Logs (ID 5145)

## Objectives

1. List all accessible shares
2. Assess read/write permissions
3. Identify SYSVOL for GPP files

## Instructions

### Step 1: Attempt Null Session Enumeration with smbclient

**Context**: Try anonymous access first to avoid alerting defenses.

**Command** ([[commands/smbclient-list-smb-shares]]):
```bash
smbclient -U '' -N -L $_TARGET_IP
```

> Output shows shares like IPC$, SYSVOL; if failed, proceed to authenticated.

### Step 2: Authenticated Enumeration with SMBMap

**Context**: Use credentials for detailed permissions if null fails.

**Command** ([[commands/smbmap-list-smb-shares]]):
```bash
smbmap -u '$_USERNAME' -p '$_PASSWORD' -H $_TARGET_IP
```

> Provides permissions (e.g., READ ONLY); success if shares like SYSVOL listed.
