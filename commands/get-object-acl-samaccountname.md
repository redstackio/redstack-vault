---
id: 4a256ff9-45fc-44cf-9fc1-bc950bdb676d
type: command
executor: powershell
data: Get-ObjectAcl -SamAccountName $_ACCOUNT_NAME -ResolveGUIDs
output: null
created_at: '2023-04-06T03:56:02.230483+00:00'
updated_at: '2023-04-06T21:33:38.759173+00:00'
platforms:
  - Windows
tags:
  - recon
  - ad
verified: true
validated: true
---

# Get ACLs for Specified Account

## Command

```powershell
Get-ObjectAcl -SamAccountName $_ACCOUNT_NAME -ResolveGUIDs
```

## Description

Gets ACLs for a specific account, resolving GUIDs.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -SamAccountName | Account name | Yes |
| -ResolveGUIDs | Resolves SIDs to names | No |

## Examples

### Basic Usage

```powershell
Get-ObjectAcl -SamAccountName 'admin' -ResolveGUIDs
```

## Expected Output

ACL entries for the account.

## Related

- [[procedures/Active-Directory-Recon-with-PowerView]]
