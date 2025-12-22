---
id: 55027df5-3342-4e23-9124-d3aa3f73a355
name: Enumerate-User-Group-Membership-in-Active-Directory
type: procedure
verified: true
submitted: false
created_at: '2023-01-12T07:19:09.943097+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
  - '[[Discovery]]'
techniques:
  - '[[Domain Groups]]'
sub_techniques: []
tags:
  - Active Directory
  - Enumeration
  - Discovery
commands:
  - '[[commands/get-adprincipalgroupmembership-user]]'
  - '[[commands/get-netgroup-username-powerview]]'
  - '[[commands/get-netgroupmember-groupname-powerview]]'
platforms:
  - Windows
tools: []
validated: true
---

# Enumerate-User-Group-Membership-in-Active-Directory

## Summary

This procedure enumerates the group memberships of a specified user in an Active Directory environment to identify potential privileged access. It uses native PowerShell Active Directory module commands or PowerView functions to query group associations, helping attackers discover if a user has elevated permissions such as Domain Admin rights.

## Description

In Active Directory domains, users are often members of multiple groups that grant varying levels of access. Enumerating group membership reveals if a compromised user account belongs to privileged groups like Domain Admins, Enterprise Admins, or other security-sensitive groups. This technique is commonly used during reconnaissance to assess the scope of compromise and plan privilege escalation. The procedure supports both the built-in Active Directory PowerShell module (requiring RSAT tools) and the PowerView toolkit for stealthier enumeration in restricted environments. It targets Windows domain-joined systems with domain authentication.

## Requirements

1. Domain-joined Windows system with PowerShell execution policy allowing scripts.
2. Active Directory module installed (via RSAT) for native commands, or PowerView script loaded for alternative queries.
3. Valid domain credentials with read access to AD objects (low-privilege user sufficient).
4. Network connectivity to a Domain Controller.

## Defense

- Enable PowerShell logging (Module, Script Block, and Transcription) to monitor AD queries.
- Implement Least Privilege: Restrict AD read access and monitor anomalous enumeration from user accounts.
- Use tools like Microsoft ATA or Azure AD Identity Protection to detect unusual group membership queries.
- Block unsigned script execution and monitor for PowerView imports via Sysmon or EDR.

## Objectives

1. Identify all groups a target user belongs to, focusing on privileged ones.
2. Assess the user's effective permissions for further exploitation.
3. Validate membership in high-value groups like Domain Admins.

## Instructions

### Step 1: Enumerate Groups Using PowerView

**Context**: Use the PowerView toolkit to query group membership for a specific username. This method is useful in environments where the AD module is unavailable or monitored, as PowerView performs LDAP queries directly.

**Command** ([[commands/get-netgroup-username-powerview]]):
```powershell
Get-NetGroup -UserName $USER
```

> Replace `$USER` with the target username (e.g., `john.doe`). This command retrieves all groups containing the specified user. Expected output includes group names, descriptions, and member counts. Look for privileged groups like `Domain Admins` to confirm elevated access.

### Step 2: Enumerate Groups Using Native AD Module

**Context**: If the Active Directory module is available, use the built-in cmdlet for a straightforward query. This is faster but may generate more detectable logs on domain controllers.

**Command** ([[commands/get-adprincipalgroupmembership-user]]):
```powershell
Get-ADPrincipalGroupMembership -Identity $USER | Select Name
```

> Replace `$USER` with the target username. The `Select Name` filters output to group names only for clarity. Expected output is a list of group names the user belongs to. Verify for sensitive groups and note any nested memberships.

### Step 3: Enumerate Members of a Specific Group

**Context**: To reverse the query and check members of a known privileged group (e.g., Domain Admins), use this step to confirm if the target user or related accounts are included. This helps in broader discovery.

**Command** ([[commands/get-netgroupmember-groupname-powerview]]):
```powershell
Get-NetGroupMember -GroupName "Domain Admins"
```

> Replace `"Domain Admins"` with the target group name. Expected output lists all members, including users and nested groups. Success is indicated by the presence of the target user in the member list, confirming privileged access.
