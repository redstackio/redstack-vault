---
id: 39fd3f3d-e405-472d-8383-e151f0618342
name: Check-LAPS-Installation-and-Retrieve-Password
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:04.498776+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
techniques:
  - '[[techniques/Credential Dumping|T1003 - Credential Dumping]]'
sub_techniques: []
tags:
  - '[[tags/Active Directory Attacks]]'
  - '[[tags/LAPS]]'
  - '[[tags/Determine if LAPS is installed]]'
  - '[[tags/Reading LAPS Password]]'
commands:
  - '[[commands/powershell-get-childitem-laps-admpwd-dll]]'
  - '[[commands/powershell-get-filehash-laps-admpwd-dll]]'
  - '[[commands/powershell-get-authenticodesignature-laps-admpwd-dll]]'
  - '[[commands/powershell-get-adcomputer-laps-password]]'
platforms:
  - Windows
tools: []
validated: true
---

# Check-LAPS-Installation-and-Retrieve-Password

## Summary

This procedure determines if Microsoft's Local Administrator Password Solution (LAPS) is installed in an Active Directory environment by verifying the presence and integrity of the Admpwd.dll file, typically located on domain-joined machines with the Client Side Extension (CSE). If LAPS is confirmed, it retrieves the unique local administrator password for a target machine stored in Active Directory attributes. This allows attackers with domain read permissions to access local admin credentials for lateral movement or privilege escalation on workstations and servers.

## Description

LAPS automates the management of local administrator account passwords in domain environments, randomizing and storing them securely in AD as the ms-Mcs-AdmPwd attribute on computer objects. The Admpwd.dll is part of the LAPS CSE, which runs on client machines to update passwords periodically. Attackers can exploit this by first confirming LAPS deployment via file checks on a domain-joined system, then querying AD for the password using PowerShell cmdlets from the ActiveDirectory module. This technique is effective in environments where LAPS is partially implemented without strict permission controls on the ms-Mcs-AdmPwd attribute. Prerequisites include domain user credentials with read access to computer objects; execution typically occurs from a compromised workstation or via remote PowerShell.

## Requirements

1. Domain-joined Windows machine with PowerShell and ActiveDirectory module installed (for DLL checks and AD queries).
2. Valid domain credentials with read permissions on target computer objects in AD (e.g., member of Domain Users).
3. Network access to the target machine (for local DLL checks) and domain controllers (for AD queries).
4. PowerShell execution policy allowing script execution (bypass if needed).

## Defense

- Restrict read access to ms-Mcs-AdmPwd and related attributes using ACLs on computer objects, limiting to authorized admins only.
- Monitor AD for queries to LAPS attributes via auditing of directory service access events (Event ID 4662).
- Deploy LAPS with delegated permissions and regularly audit DLL integrity using file monitoring tools like Sysmon.
- Consider alternatives like Just-In-Time (JIT) administration or passwordless auth (e.g., Windows Hello) to mitigate static credential risks.

## Objectives

1. Confirm LAPS installation by verifying Admpwd.dll existence and integrity.
2. Retrieve the current local administrator password for a target machine from AD.
3. Enable lateral movement to the target machine using the obtained credentials.

## Instructions

### Step 1: Check for Admpwd.dll Presence

**Context**: Verify if the LAPS Client Side Extension is installed by checking for the Admpwd.dll file in the expected directory. This confirms LAPS deployment on the local or remote machine without relying on AD schema checks.

**Command** ([[commands/powershell-get-childitem-laps-admpwd-dll]]):
```powershell
Get-ChildItem 'C:\Program Files\LAPS\CSE\Admpwd.dll'
```

> This command lists file details like size and modification date. If the file does not exist, LAPS CSE is not installed locally, but AD-side components may still be present—proceed to AD query if domain access is available.

### Step 2: Verify Admpwd.dll Hash

**Context**: Compute the SHA256 hash of Admpwd.dll to ensure it matches Microsoft's official version and has not been tampered with, which could indicate a modified or fake LAPS implementation.

**Command** ([[commands/powershell-get-filehash-laps-admpwd-dll]]):
```powershell
Get-FileHash 'C:\Program Files\LAPS\CSE\Admpwd.dll'
```

> Expected hash for official Microsoft Admpwd.dll (version 6.2.x) is approximately 'A1B2C3D4E5F6...' (verify against known good values from Microsoft docs). A mismatch suggests potential compromise or custom build.

### Step 3: Verify Admpwd.dll Signature

**Context**: Check the digital signature of Admpwd.dll to confirm it is signed by Microsoft, providing assurance of authenticity before using any LAPS-related functionality.

**Command** ([[commands/powershell-get-authenticodesignature-laps-admpwd-dll]]):
```powershell
Get-AuthenticodeSignature 'C:\Program Files\LAPS\CSE\Admpwd.dll'
```

> Look for 'Valid' status and signer 'Microsoft Corporation'. Invalid signatures indicate tampering or unsigned modifications.

### Step 4: Retrieve LAPS Password from AD

**Context**: If LAPS is confirmed, query Active Directory for the ms-Mcs-AdmPwd attribute on the target computer object to obtain the current local admin password. This requires the ActiveDirectory module (import if needed: Import-Module ActiveDirectory).

**Command** ([[commands/powershell-get-adcomputer-laps-password]]):
```powershell
Get-ADComputer -Identity 'TARGET-COMPUTER-NAME' -Properties ms-Mcs-AdmPwd | Select-Object -ExpandProperty ms-Mcs-AdmPwd
```

> Replace 'TARGET-COMPUTER-NAME' with the actual computer name (e.g., WORKSTATION01). Success returns the plaintext password; if null or access denied, check permissions or LAPS config.
