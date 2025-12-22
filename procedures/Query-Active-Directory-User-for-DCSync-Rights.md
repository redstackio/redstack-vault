---
id: d0104fca-b063-47bf-844b-a4a64e3a3399
name: Query-Active-Directory-User-for-DCSync-Rights
type: procedure
verified: true
submitted: false
created_at: '2020-03-20T22:38:48.772506+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - >-
    [[techniques/Permission-Groups-Discovery|T1069 - Permission Groups
    Discovery]]
sub_techniques: []
platforms:
  - Windows
tags:
  - '[[tags/Active Directory]]'
  - '[[tags/Enumeration]]'
  - '[[tags/powershell]]'
commands:
  - '[[commands/get-aduser-list-users-with-sid]]'
  - '[[commands/get-objectacl-query-user-dcsync-rights]]'
tools:
  - '[[tools/PowerView]]'
validated: true
---

# Query-Active-Directory-User-for-DCSync-Rights

## Summary

This procedure enumerates Active Directory users and their Security Identifiers (SIDs) using the native PowerShell ActiveDirectory module, then leverages PowerView to query specific users for DCSync replication privileges. DCSync rights allow an attacker to replicate directory data, effectively extracting password hashes from the domain controller, enabling pass-the-hash or other credential-based attacks.

## Description

In an Active Directory environment, DCSync attacks exploit replication privileges to mimic domain controller behavior and pull sensitive data like NTLM hashes without direct DC access. This procedure first lists all AD users with their SIDs to identify potential targets, then checks ACLs on the domain's naming context for extended rights like DS-Replication-Get-Changes and DS-Replication-Get-Changes-All granted to user SIDs. It targets Windows domain environments where the attacker has domain-joined access with read permissions. Success reveals users (often service accounts or admins) that can perform DCSync, facilitating lateral movement or persistence.

## Requirements

1. Domain-joined Windows host with PowerShell ActiveDirectory module installed (part of RSAT tools).
2. PowerView script downloaded and imported into the PowerShell session.
3. Valid domain credentials with at least read access to AD objects.
4. Network connectivity to a domain controller for AD queries.

## Defense

- Enable advanced auditing for directory service access and object access on domain controllers.
- Monitor PowerShell execution logs for ActiveDirectory module usage and unusual queries (e.g., Get-ADUser, Get-ObjectAcl).
- Implement least privilege: Restrict replication rights to only necessary Domain Admins or service accounts.
- Use tools like Microsoft ATA or Azure AD Identity Protection to detect anomalous AD enumeration.

## Objectives

1. Enumerate all AD users and capture their SIDs for targeted querying.
2. Identify users with DCSync-capable privileges by inspecting ACLs for replication extended rights.
3. Validate potential for credential extraction attacks without alerting typical defenses.

## Instructions

### Step 1: Enumerate AD Users with SIDs

**Context**: Retrieve a list of all domain users and their SIDs to identify candidates for DCSync rights checking. This step uses the native ActiveDirectory module, which is commonly available on domain-joined systems.

**Command** ([[commands/get-aduser-list-users-with-sid]]):
```powershell
Get-ADUser -Filter * | Select-Object -Property name,sid
```

> This command queries the entire AD user base and outputs usernames alongside SIDs. Pipe the output to a file if needed for scripting further queries (e.g., | Export-Csv users.csv). Expected output includes a table of users like Administrator (S-1-5-21-...-500). If no users appear, verify module import with Import-Module ActiveDirectory.

### Step 2: Import PowerView for Advanced Querying

**Context**: PowerView provides enhanced AD enumeration capabilities beyond native modules, including ACL resolution for privilege detection. Download and import it to enable the Get-ObjectAcl function.

**Instructions**: Download the dev branch of PowerView from GitHub (https://github.com/PowerShellMafia/PowerSploit/blob/master/Recon/PowerView.ps1) and execute in PowerShell:
```powershell
. .\PowerView.ps1
```

> Confirm import by running Get-Command Get-ObjectAcl. This step requires internet access or pre-downloaded script; errors may occur if execution policy blocks it (bypass with Set-ExecutionPolicy Bypass).

### Step 3: Query User SID for DCSync Rights

**Context**: For each SID of interest (e.g., from Step 1), query the domain's ACLs to check for replication privileges. Focus on rights like DS-Replication-Get-Changes (for password changes) and DS-Replication-Get-Changes-All (full replication). This reveals if the user can perform DCSync via tools like Mimikatz.

**Command** ([[commands/get-objectacl-query-user-dcsync-rights]]):
```powershell
Get-ObjectAcl -Identity "dc=$_DC1,dc=$_DC2" -ResolveGUIDs | ? {$_.SecurityIdentifier -match "$_SID"}
```

> Replace $_DC1 and $_DC2 with domain components (e.g., megabank,local) and $_SID with the target SID. Run for high-privilege users first. Expected output shows ACE entries; look for ActiveDirectoryRights: ExtendedRight and ObjectAceType: DS-Replication-Get-Changes or DS-Replication-Get-Changes-All with AceQualifier: AccessAllowed. Errors like access denied are common but do not prevent results if rights exist. If no output, the user lacks DCSync privileges.
