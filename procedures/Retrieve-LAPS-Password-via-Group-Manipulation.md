---
type: procedure
description: >-
  This procedure outlines how to manipulate LAPS group memberships to gain read
  access to local administrator passwords stored in Active Directory for
  domain-joined computers.
verified: true
submitted: false
created_at: '2023-04-06T03:56:04.530170+00:00'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[tactics/Persistence|TA0003 - Persistence]]'
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
techniques:
  - '[[techniques/Account Manipulation|T1098 - Account Manipulation]]'
  - '[[techniques/OS Credential Dumping|T1003 - OS Credential Dumping]]'
sub_techniques: []
tags:
  - active-directory-attacks
  - laps
  - credential-access
  - group-manipulation
commands:
  - '[[commands/Add-DomainGroupMember-to-LAPS-ADM-Group]]'
  - '[[commands/Add-DomainGroupMember-to-LAPS-READ-Group]]'
  - '[[commands/Get-ADComputer-for-LAPS-Password]]'
platforms:
  - Windows
  - Active Directory
tools:
  - '[[tools/PowerView]]'
validated: true
---

# Retrieve-LAPS-Password-via-Group-Manipulation

## Summary

This procedure enables an attacker with domain access to add their controlled user account to the LAPS READ group, granting permission to retrieve the randomized local administrator password for a target domain-joined computer from Active Directory attributes. LAPS (Local Administrator Password Solution) automatically manages and rotates these passwords, storing them securely in AD, but improper group access controls can allow unauthorized retrieval for lateral movement or privilege escalation.

## Description

LAPS is a Microsoft solution that randomizes and manages local administrator passwords on domain-joined Windows computers, storing the current password in the ms-Mcs-AdmPwd attribute of the computer's AD object. Access to this attribute is controlled via ACLs and groups like 'LAPS READ' (for viewing passwords) and 'LAPS ADM' (for resetting). This procedure assumes the attacker has compromised domain credentials sufficient to modify group memberships (e.g., via Domain Admin or delegated rights). By adding a controlled user to these groups, the attacker can then query AD for the password using standard PowerShell cmdlets. This technique is realistic in environments with weak delegation or auditing, allowing escalation from initial foothold to local admin on multiple machines. Success provides plaintext credentials for RDP, WMI, or other remote access, facilitating further network compromise.

## Requirements

1. Domain-joined Windows machine with PowerShell access and compromised credentials (e.g., Domain Admin or rights to modify group membership).
2. PowerView module loaded for group manipulation (requires .NET and PowerShell v2+).
3. ActiveDirectory PowerShell module installed (via RSAT or Import-Module ActiveDirectory) for password retrieval.
4. Target computer name or DN in AD.
5. Network access to a Domain Controller for AD queries.

## Defense

- Restrict LAPS group memberships to only authorized service accounts via protected groups or fine-grained ACLs on the ms-Mcs-AdmPwd attribute.
- Enable auditing for group membership changes and AD attribute reads using Advanced Audit Policy (e.g., DS Access events in Event ID 4662).
- Implement least privilege: Delegate LAPS access minimally and use Just-In-Time (JIT) administration tools like PIM.
- Monitor PowerShell execution logs (Module Logging, Script Block Logging) for suspicious cmdlets like Add-DomainGroupMember or Get-ADComputer.
- Rotate LAPS passwords more frequently and enforce strong ACLs to prevent unauthorized reads.

## Objectives

1. Add attacker-controlled user to LAPS ADM and READ groups to gain management and read permissions.
2. Query Active Directory for the ms-Mcs-AdmPwd attribute of the target computer.
3. Obtain the plaintext local administrator password for use in lateral movement or privilege escalation.

## Instructions

### Step 1: Add User to LAPS ADM Group

**Context**: The LAPS ADM group grants permissions to reset LAPS passwords. Adding the controlled user here provides optional management capabilities, but is often unnecessary for just reading; include it for full control. This step uses PowerView to avoid direct AD modifications that might trigger alerts.

**Command** ([[commands/Add-DomainGroupMember-to-LAPS-ADM-Group]]):
```powershell
Add-DomainGroupMember -Identity 'LAPS ADM' -Members 'user1' -Credential $cred -Domain "domain.local"
```

> This command adds the specified user to the LAPS ADM group. Replace 'user1' with the attacker-controlled username, $cred with a PSCredential object (e.g., Get-Credential), and "domain.local" with the target domain. Expected output is a success confirmation or the group object if verbose; errors indicate insufficient privileges or non-existent group.

### Step 2: Add User to LAPS READ Group

**Context**: The LAPS READ group is required to access the ms-Mcs-AdmPwd attribute. This step grants read permissions, enabling password retrieval without full admin rights on the computer itself. Perform this after Step 1 to ensure layered access.

**Command** ([[commands/Add-DomainGroupMember-to-LAPS-READ-Group]]):
```powershell
Add-DomainGroupMember -Identity 'LAPS READ' -Members 'user1' -Credential $cred -Domain "domain.local"
```

> Similar to Step 1, this targets the READ group. Upon success, the user can now query LAPS attributes. Verify by checking group membership with Get-DomainGroupMember if needed. If the group doesn't exist, the environment may not have LAPS fully deployed.

### Step 3: Retrieve LAPS Password from Active Directory

**Context**: With read permissions granted, query the target computer's AD object for the stored password. This retrieves the current randomized local admin password, valid until the next rotation (default 30 days). Use the ActiveDirectory module for native querying.

**Command** ([[commands/Get-ADComputer-for-LAPS-Password]]):
```powershell
Import-Module ActiveDirectory
Get-ADComputer -Identity "$_TARGET_COMPUTER" -Properties ms-Mcs-AdmPwd | Select-Object -ExpandProperty ms-Mcs-AdmPwd
```

> Replace $_TARGET_COMPUTER with the computer's name (e.g., WORKSTATION01). The Import-Module ensures the cmdlet is available. Expected output is the plaintext password string; if blank or error, check permissions, LAPS deployment, or attribute existence. Use this password for tools like psexec or RDP to access the target.
