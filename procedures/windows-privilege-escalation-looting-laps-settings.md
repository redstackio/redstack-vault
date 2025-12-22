---
type: procedure
verified: true
submitted: false
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - '[[techniques/OS Credential Dumping|T1003 - OS Credential Dumping]]'
  - '[[techniques/Credentials in Registry|T1214 - Credentials in Registry]]'
tags:
  - '[[tags/EoP - Looting for passwords]]'
  - '[[tags/LAPS Settings]]'
  - '[[tags/Windows - Privilege Escalation]]'
commands:
  - '[[commands/reg-query-laps-policy]]'
  - '[[commands/powershell-get-laps-password]]'
platforms:
  - Windows
tools: []
validated: true
---

# Windows Privilege Escalation - Looting LAPS Settings

## Summary

This procedure outlines how to extract Local Administrator Password Solution (LAPS) configuration settings from the Windows registry and retrieve the actual LAPS-managed local administrator password from Active Directory. LAPS is a Microsoft feature that randomly generates and stores unique local admin passwords for domain-joined machines in AD, allowing authorized users to retrieve them for administrative tasks. Attackers can abuse this to obtain plaintext credentials for privilege escalation on target systems.

## Description

In a Windows domain environment, LAPS automates the management of local administrator accounts by setting a unique password for each machine, stored in the AD computer object's ms-Mcs-AdmPwd attribute. This procedure first verifies LAPS deployment via local registry policies (which control settings like password complexity and expiration), then queries AD to loot the password for a specific target computer. Success enables logging in as local admin (often with elevated privileges) for persistence, lateral movement, or data access. This technique assumes the attacker has initial foothold as a domain user with delegated read access to the ms-Mcs-AdmPwd attribute (common for helpdesk roles). If permissions are insufficient, escalation to a privileged account may be needed first. The approach leverages built-in Windows tools, avoiding external dependencies where possible.

## Requirements

1. Domain-joined Windows machine (Windows 10/Server 2016+ with LAPS deployed in the environment).
2. PowerShell with Active Directory module (install via RSAT: Add-WindowsCapability -Online -Name Rsat.ActiveDirectory.DS-LDS.Tools~~~~0.0.1.0).
3. Domain user credentials with read access to AD computer objects (specifically the ms-Mcs-AdmPwd attribute; default for Domain Users in some configs).
4. Target computer name or DN for the AD query.
5. Local administrative access if querying registry on a remote/target machine (use reg query remotely via psexec or similar if needed).

## Defense

- Restrict ms-Mcs-AdmPwd attribute permissions in AD to only authorized groups (e.g., via ACLs on the attribute, denying read to Domain Users).
- Enable AD auditing for attribute access and monitor LDAP queries for ms-Mcs-AdmPwd (use tools like Microsoft ATA or SIEM integration).
- Implement Privileged Access Workstations (PAW) for admin tasks and rotate LAPS passwords more frequently than default (30 days).
- Deploy LAPS with the AdmPwd.PSO module for PowerShell-only access, avoiding direct attribute reads.
- Monitor for anomalous local admin logons and use endpoint detection for PowerShell AD module usage.

## Objectives

1. Verify LAPS configuration to confirm password management is active.
2. Extract the plaintext LAPS password for a target machine from Active Directory.
3. Use the obtained credentials to escalate privileges on the target system.
4. Facilitate lateral movement to other domain-joined hosts using the local admin account.

## Instructions

### Step 1: Verify LAPS Policy Settings Locally

**Context**: Before attempting to loot passwords, confirm LAPS is enabled and review its policy settings (e.g., password length, expiration) in the local registry. This step helps assess the environment and ensures LAPS is deployed; the policy is typically pushed via Group Policy from AD.

**Command** ([[commands/reg-query-laps-policy]]):

```cmd
reg query "HKLM\Software\Policies\Microsoft Services\AdmPwd"
```

> This queries the registry hive where LAPS policies are stored. If the key exists, LAPS is likely configured. Review values like AdmPwdExpirationPeriod (password age in days) and PasswordSettings (complexity flags). If the key is absent, LAPS may not be enforced on this machine—pivot to AD query anyway, as passwords could still be set.

**Expected Output**: A list of registry values under the key, such as:

```
HKEY_LOCAL_MACHINE\Software\Policies\Microsoft Services\AdmPwd

    AdmPwdExpirationPeriod    REG_DWORD    0x1e
    PasswordSettings    REG_DWORD    0x1
```

**Success Indicators**:
- The AdmPwd key exists and contains policy values.
- No access denied errors (indicating sufficient local permissions).

### Step 2: Retrieve LAPS Password from Active Directory

**Context**: Query Active Directory for the ms-Mcs-AdmPwd attribute on the target computer object to obtain the current local administrator password. This attribute holds the plaintext password, updated periodically by the LAPS client on the target machine. Requires domain authentication and appropriate AD read permissions.

**Command** ([[commands/powershell-get-laps-password]]):

```powershell
Import-Module ActiveDirectory
Get-ADComputer -Identity $_COMPUTER_NAME -Properties ms-Mcs-AdmPwd | Select-Object -ExpandProperty ms-Mcs-AdmPwd
```

> Substitute $_COMPUTER_NAME with the target (e.g., WORKSTATION01). Run in an elevated PowerShell session on a domain-joined machine. If the AD module is unavailable, install RSAT or use ADSI LDAP queries as an alternative (see related procedures). The password is stored in cleartext, valid until the next rotation.

**Expected Output**: The plaintext password string, such as:

```
P@ssw0rd123!
```

**Success Indicators**:
- Password retrieved without permission errors.
- The ms-Mcs-AdmPwd property is populated (not null).
- Verify by testing login to the target machine with the credential (e.g., via RDP or PSEXEC).
