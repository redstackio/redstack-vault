---
type: command
executor: powershell
data: >-
  Invoke-ACLScanner -ResolveGUIDs | Where-Object { $_.IdentityReferenceName
  -match "RDPUsers" }
output: null
platforms:
  - Windows
tags:
  - active-directory
  - acl-abuse
verified: true
validated: true
---

# powerview-invoke-aclscanner-check-permissions

## Command

```powershell
Invoke-ACLScanner -ResolveGUIDs | Where-Object { $_.IdentityReferenceName -match "RDPUsers" }
```

## Description

This command uses PowerView's Invoke-ACLScanner to enumerate ACLs on Active Directory objects and filters for permissions granted to the RDPUsers group, identifying potential GenericAll abuses for Kerberoasting or roasting.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -ResolveGUIDs | Resolves GUIDs to friendly names for readability | No (default behavior) |
| RDPUsers | Filter string for IdentityReferenceName (customizable to other groups) | Yes |

## Examples

### Basic Usage

```powershell
Invoke-ACLScanner -ResolveGUIDs | Where-Object { $_.IdentityReferenceName -match "RDPUsers" }
```

### Broader Scan

```powershell
Invoke-ACLScanner -ResolveGUIDs | Where-Object { $_.ActiveDirectoryRights -match "GenericAll" }
```

## Expected Output

A table of ACL entries:

ObjectDN              : CN=TargetUser,CN=Users,DC=domain,DC=local
IdentityReference     : domain\RDPUsers
ActiveDirectoryRights : GenericAll
AccessControlType     : Allow

## Related

- [[procedures/Active-Directory-ACL-Abuse-via-Kerberoasting-and-AS-REP-Roasting]]
- [[tools/PowerView]]
