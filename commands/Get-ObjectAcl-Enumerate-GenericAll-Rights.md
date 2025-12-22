---
id: e0dc72e2-10cb-4f34-abe5-f73d891a95a1
name: Get-ObjectAcl-Enumerate-GenericAll-Rights
type: command
executor: powershell
data: >-
  Get-ObjectAcl -SamAccountName $USERNAME -ResolveGUIDs | ?
  {$_.ActiveDirectoryRights -eq "GenericAll"}
output: |-
  (...)
  IdentityReference: DOMAIN\User
  ActiveDirectoryRights: GenericAll
  (...)
created_at: '2023-01-12T18:36:32.650238+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Windows
tags:
  - enumeration
  - active-directory
verified: true
validated: true
---

# Get-ObjectAcl-Enumerate-GenericAll-Rights

## Command

```powershell
Get-ObjectAcl -SamAccountName $USERNAME -ResolveGUIDs | ? {$_.ActiveDirectoryRights -eq "GenericAll"}
```

## Description

This PowerShell command uses PowerView's Get-ObjectAcl to retrieve ACLs for all AD objects associated with a specific SamAccountName (username), resolves GUIDs to human-readable names, and filters the results to show only entries where the user has GenericAll rights. Use this during Active Directory enumeration to discover full-control permissions on objects like users or groups.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -SamAccountName | The username (SamAccountName) to check for permissions (use variable like $USERNAME) | Yes |
| -ResolveGUIDs | Resolves schema GUIDs to friendly names for better readability | No (recommended) |
| ? {$_.ActiveDirectoryRights -eq "GenericAll"} | PowerShell Where-Object filter to match only GenericAll rights | Yes |

## Examples

### Basic Usage

```powershell
$USERNAME = "attackeruser"
Get-ObjectAcl -SamAccountName $USERNAME -ResolveGUIDs | ? {$_.ActiveDirectoryRights -eq "GenericAll"}
```

### Advanced Usage

```powershell
Get-ObjectAcl -SamAccountName $USERNAME -ResolveGUIDs | ? {$_.ActiveDirectoryRights -eq "GenericAll"} | Select-Object ObjectDN, IdentityReference, ActiveDirectoryRights
```

This adds Select-Object to focus on key fields like object distinguished name.

## Expected Output

If GenericAll rights exist:

```
ObjectDN              : CN=TargetGroup,CN=Users,DC=domain,DC=com
IdentityReference     : DOMAIN\attackeruser
ActiveDirectoryRights : GenericAll
AccessControlType     : Allow
...
```

If no rights found, the output is empty. Look for 'GenericAll' to confirm exploitable permissions.

## Related

- [[procedures/Enumerate-GenericAll-Rights-on-AD-Object-for-Specific-User]]
- [[tools/PowerView]]
