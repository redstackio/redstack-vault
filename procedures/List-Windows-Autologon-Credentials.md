---
id: 27bc330c-ee4c-4fe5-b1d4-1b3ce0c5fcd8
name: List-Windows-Autologon-Credentials
type: procedure
verified: true
submitted: true
created_at: '2020-03-17T23:49:26.728082+00:00'
updated_at: '2023-05-25T19:47:55.607962+00:00'
tactics:
  - '[[Credential Access]]'
techniques:
  - '[[Security Account Manager]]'
sub_techniques: []
tags:
  - credential-access
  - enumeration
  - registry
commands:
  - '[[commands/reg-query-autologon-creds]]'
platforms:
  - Windows
tools: []
validated: true
---

# List-Windows-Autologon-Credentials

## Summary

Query the Windows registry on a compromised host to extract plaintext credentials stored for automatic logon, often used in legacy or kiosk setups.

## Description

The Winlogon registry key stores DefaultUserName, DefaultPassword, and DefaultDomainName in cleartext if auto-logon is enabled. Accessible by any local user, this provides easy creds for lateral movement.

## Requirements

- Local access to target (e.g., via WinRM shell)
- Registry read permissions (standard user)
- No additional tools needed

## Defense

- Disable auto-logon feature (Set AutoAdminLogon to 0)
- Encrypt or avoid storing passwords in registry
- Monitor registry access (Event ID 4657 for Winlogon key)

## Objectives

1. Check for auto-logon configuration
2. Extract stored credentials
3. Use for pivoting

## Instructions

### Step 1: Query Winlogon Registry Key

**Context**: Dump the key containing auto-logon settings.

**Command** ([[commands/reg-query-autologon-creds]]):
```cmd
reg query "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon"
```

> Run from cmd or PS. Look for AutoAdminLogon=1, then Default* values.

**Expected Output**: DefaultPassword REG_SZ Password123; DefaultUserName REG_SZ user.

### Step 2: Parse and Validate Creds

**Context**: Identify if creds are present and test them.

If AutoAdminLogon=1 and passwords shown, note domain/local. Test with `runas /user:cred cmd`.

If no password, check for cached logons or other keys.

### Step 3: Securely Store for Use

**Context**: Avoid logging; use in next steps like WinRM.
