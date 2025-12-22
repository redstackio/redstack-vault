---
id: b6627471-cb7f-4971-b734-a65009c3a604
name: find-interesting-domain-acls-powerview
type: command
executor: powershell
data: >-
  Find-InterestingDomainAcl -ResolveGUIDs | ?{$_.IdentityReferenceName -match
  $GROUP_NAME}
output: null
created_at: '2023-01-12T07:34:23.268122+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Windows
tags:
  - active-directory
  - acl
  - discovery
verified: true
validated: true
---

# find-interesting-domain-acls-powerview

## Command

```powershell
Find-InterestingDomainAcl -ResolveGUIDs | ?{$_.IdentityReferenceName -match $GROUP_NAME}
```

## Description

This PowerShell command uses the PowerView module to enumerate Active Directory ACLs that match predefined 'interesting' patterns indicative of potential abuse, such as permissions allowing group modifications. It filters results for a specific group name stored in the $GROUP_NAME variable. Use this during AD reconnaissance to identify misconfigured permissions on domain objects.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -ResolveGUIDs | Resolves GUIDs in ACL entries to human-readable names | No |
| $GROUP_NAME | Variable holding the target group name (e.g., 'Domain Admins') for filtering | Yes |
| ?{...} | PowerShell Where-Object filter to match IdentityReferenceName against $GROUP_NAME | Yes |

## Examples

### Basic Usage

```powershell
$GROUP_NAME = 'Domain Admins'
Find-InterestingDomainAcl -ResolveGUIDs | ?{$_.IdentityReferenceName -match $GROUP_NAME}
```

### Advanced Usage

```powershell
$GROUP_NAME = 'Enterprise Admins'
Find-InterestingDomainAcl -ResolveGUIDs | ?{$_.IdentityReferenceName -match $GROUP_NAME} | Select-Object IdentityReferenceName, ActiveDirectoryRights
```

## Expected Output

The command outputs a table of ACL entries, such as:

IdentityReferenceName : DOMAIN\LowPrivGroup
ActiveDirectoryRights : GenericAll
AccessControlType     : Allow
ObjectType            : Group

Success is indicated by entries showing excessive rights (e.g., GenericAll, WriteDacl) on the target group.

## Related

- [[procedures/Enumerate-Domain-Group-ACLs-for-Abuse]]
- [[commands/get-domain-object-acl-powerview]]
