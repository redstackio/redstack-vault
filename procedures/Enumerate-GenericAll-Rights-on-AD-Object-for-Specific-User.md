---
id: 1124ef37-ed21-4189-8afe-ed30e1fbaf86
name: Enumerate-GenericAll-Rights-on-AD-Object-for-Specific-User
type: procedure
verified: true
submitted: false
created_at: '2023-01-12T18:36:32.706786+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - >-
    [[techniques/Permission Groups Discovery|T1069 - Permission Groups
    Discovery]]
sub_techniques: []
tags:
  - '[[tags/Enumeration]]'
  - active-directory
commands:
  - '[[commands/Get-ObjectAcl-Enumerate-GenericAll-Rights]]'
platforms:
  - Windows
tools:
  - '[[tools/PowerView]]'
validated: true
---

# Enumerate-GenericAll-Rights-on-AD-Object-for-Specific-User

## Summary

This procedure uses PowerShell to enumerate Active Directory objects where a specific user has GenericAll rights, which grant full control over the object, such as the ability to add the user to groups or reset passwords. It is useful in post-exploitation scenarios to identify privilege escalation paths via excessive permissions.

## Description

GenericAll is an Active Directory access control entry (ACE) that provides full rights to an object, equivalent to ownership for most operations. By querying the ACLs of AD objects for a target user (often the attacker's compromised account), this procedure identifies objects where the user has this permission. This discovery aids in mapping attack paths, such as adding the user to privileged groups or modifying sensitive objects. The technique relies on domain credentials and requires access to a domain-joined Windows system with PowerView loaded. It targets Windows Active Directory environments and helps uncover misconfigurations in permission delegation.

## Requirements

1. Domain user credentials with read access to AD objects (e.g., compromised low-privilege account).
2. PowerShell execution policy allowing scripts (bypass if needed).
3. PowerView module loaded (via [[tools/PowerView]]).
4. Network access to a Domain Controller or LDAP server.
5. Target username ($USERNAME variable set to the specific user to check).

## Defense

- Monitor for unusual LDAP queries or PowerShell invocations accessing ACLs (e.g., via Event ID 4662 for object access).
- Implement least privilege: Regularly audit and remove unnecessary GenericAll permissions using tools like BloodHound.
- Enable Advanced Audit Policy for Directory Service Access to log permission enumerations.
- Use Microsoft Defender for Identity to detect anomalous permission discovery activities.

## Objectives

1. Identify AD objects (users, groups, computers) where the specified user has GenericAll rights.
2. Highlight potential privilege escalation vectors, such as modifiable group memberships.
3. Verify success by checking for ActiveDirectoryRights: GenericAll in the output.

## Instructions

### Step 1: Load PowerView Module

**Context**: Ensure the PowerView module is imported to access AD enumeration functions like Get-ObjectAcl. This step is prerequisite for querying ACLs.

Download and import PowerView if not already loaded:

```powershell
import-module PowerView.ps1
```

> This command loads the necessary cmdlets. Expected output: No errors, module functions available via Get-Command.

### Step 2: Set Target Username and Enumerate GenericAll Rights

**Context**: Specify the username to check and run the ACL enumeration filtered for GenericAll rights. This reveals objects the user can fully control.

**Command** ([[commands/Get-ObjectAcl-Enumerate-GenericAll-Rights]]):
```powershell
Get-ObjectAcl -SamAccountName $USERNAME -ResolveGUIDs | ? {$_.ActiveDirectoryRights -eq "GenericAll"}
```

> Replace $USERNAME with the target user (e.g., 'attackeruser'). The -ResolveGUIDs flag translates GUIDs to readable names. The Where-Object (?) filters for GenericAll. Expected output: List of ACEs showing IdentityReference and ActiveDirectoryRights if permissions exist; empty if none found.

### Step 3: Analyze Output for Escalation Paths

**Context**: Review the results to identify exploitable objects, such as groups where membership can be modified.

Manually inspect the output for object types (e.g., groups) and plan next actions like adding the user via Set-DomainObject.

> Success criteria: Presence of entries like 'ActiveDirectoryRights: GenericAll' indicates exploitable permissions. If no output, the user lacks such rights.
