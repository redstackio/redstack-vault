---
id: 1370c7d9-fb99-4eac-a380-737c91ba8690
name: Enumerate-Domain-Group-ACLs-for-Abuse
type: procedure
verified: true
submitted: false
created_at: '2023-01-12T07:34:24.330891+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
  - '[[Discovery]]'
techniques:
  - '[[Domain Groups]]'
sub_techniques: []
tags:
  - active-directory
  - acl
  - powerview
  - discovery
  - privilege-escalation
commands:
  - '[[commands/find-interesting-domain-acls-powerview]]'
  - '[[commands/get-domain-object-acl-powerview]]'
platforms:
  - Windows
tools:
  - '[[tools/PowerView]]'
skill_level: intermediate
impact_level: medium
detection_risk: high
validated: true
---

# Enumerate-Domain-Group-ACLs-for-Abuse

## Summary

This procedure identifies potentially abusable Access Control Lists (ACLs) on Active Directory domain groups using PowerView, a PowerShell module for AD reconnaissance. It helps discover misconfigurations that could allow unauthorized group modifications, such as adding users to privileged groups, facilitating privilege escalation in a domain environment.

## Description

In Active Directory environments, ACLs define permissions on objects like groups. Abusable ACLs might grant low-privileged users rights to modify group memberships, potentially leading to lateral movement or escalation. This procedure uses PowerView's functions to enumerate interesting ACLs on specified groups and then inspects specific Access Control Entries (ACEs) for further details. It is typically used during internal reconnaissance after initial domain access, targeting groups like Domain Admins or other high-privilege ones. Success reveals entries where non-privileged identities have excessive rights, such as GenericAll or WriteDacl.

## Requirements

1. Domain-joined Windows host with PowerShell execution policy allowing scripts (e.g., Bypass).
2. Active Directory module access or PowerView loaded in the current session.
3. Valid domain credentials with read access to AD objects (low-privilege user sufficient for enumeration).
4. Network connectivity to a Domain Controller.

## Defense

Defensive measures and detection strategies:

- Monitor PowerShell execution logs for PowerView module imports and function calls like Find-InterestingDomainAcl.
- Implement least-privilege principles for AD delegations; regularly audit ACLs using tools like BloodHound or native ADUC.
- Enable Advanced Audit Policy for Directory Service Access to log permission changes.
- Use Endpoint Detection and Response (EDR) tools to alert on anomalous AD queries from non-admin accounts.

## Objectives

1. Identify groups with ACLs that grant excessive permissions to low-privileged users or groups.
2. Detail specific ACEs that could be leveraged for group membership manipulation.
3. Uncover paths for privilege escalation through AD misconfigurations.

## Instructions

### Step 1: Enumerate Interesting ACLs on Target Group

**Context**: This step scans for ACLs on the specified domain group that match known interesting patterns, such as permissions allowing membership changes. It filters results to focus on the target group, helping identify potential abuse vectors early.

**Command** ([[commands/find-interesting-domain-acls-powerview]]):
```powershell
Find-InterestingDomainAcl -ResolveGUIDs | ?{$_.IdentityReferenceName -match $GROUP_NAME}
```

> This command invokes PowerView's Find-InterestingDomainAcl function to query AD for ACLs with predefined 'interesting' permissions (e.g., ForceChangePassword, GenericAll). The -ResolveGUIDs flag translates GUIDs to readable names. The Where-Object filter (?{}) narrows results to the target group specified in $GROUP_NAME (e.g., 'Domain Admins'). Expected output includes details like IdentityReferenceName, ActiveDirectoryRights, and AccessControlType. If results show abusable rights (e.g., WriteOwner or DeleteChild), proceed to deeper analysis; otherwise, try another group.

### Step 2: Inspect Specific ACEs on the Group

**Context**: If the first step reveals potential issues, this step retrieves and filters the full ACL for the target group, resolving SIDs to names and checking for specific identities (e.g., a low-priv group) that have leveraged permissions. This provides granular insight into who can modify what.

**Command** ([[commands/get-domain-object-acl-powerview]]):
```powershell
Get-DomainObjectAcl -Identity $GROUP_NAME2 -ResolveGUIDs | ForEach-Object {$_ | Add-Member NoteProperty 'IdentityName' $(Convert-SidToName $_.SecurityIdentifier); $_} | ?{$_.IdentityName -match $GROUP_NAME1}
```

> This command uses Get-DomainObjectAcl to fetch all ACEs for the group in $GROUP_NAME2 (e.g., the privileged group). It resolves GUIDs/SIDs with -ResolveGUIDs and Convert-SidToName, adding an IdentityName property via ForEach-Object. The final filter matches against $GROUP_NAME1 (e.g., the suspicious principal). Expected output lists ACEs with details like SecurityIdentifier, ActiveDirectoryRights (e.g., 'GenericAll'), and IdentityName. Look for entries where a non-admin group/user has rights like AddMembers or WriteDacl, indicating an escalation path. Verify by cross-referencing with AD tools.
