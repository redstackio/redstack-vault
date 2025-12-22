---
id: 6c8c8100-07d0-429e-b2c9-0f73760f37e6
name: set-adcomputer-modify-samaccountname
type: command
executor: powershell
data: Set-ADComputer -Identity $_COMPUTERNAME -SamAccountName $_SAMACCOUNTNAME
output: null
created_at: '2023-04-06T03:56:04.456034+00:00'
updated_at: '2023-04-10T20:26:27.425169+00:00'
platforms:
  - Windows
tags:
  - active-directory
  - account-manipulation
verified: true
validated: true
---

# set-adcomputer-modify-samaccountname

## Command

```powershell
Set-ADComputer -Identity $_COMPUTERNAME -SamAccountName $_SAMACCOUNTNAME
```

## Description

This PowerShell command modifies an existing Active Directory computer account's SAM account name to a pre-Windows 2000 compatible format, facilitating legacy authentication or exploitation of weak passwords.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -Identity $_COMPUTERNAME | Distinguished name (DN), GUID, SID, or SAM account name of the computer to modify (e.g., "Win10Comp") | Yes |
| -SamAccountName $_SAMACCOUNTNAME | New SAM account name in pre-W2K format (e.g., "CONTOSO\\Win10Comp$") | Yes |

## Examples

### Basic Usage

```powershell
Set-ADComputer -Identity "Win10Comp" -SamAccountName "CONTOSO\\Win10Comp$"
```

### Verification

```powershell
Get-ADComputer -Identity "Win10Comp" -Properties SamAccountName
```

## Expected Output

No direct output on success. Verification shows: "SamAccountName : CONTOSO\\Win10Comp$". Errors if insufficient privileges or object not found.

## Related

- [[procedures/Password-of-Pre-Created-Computer-Account-Attack]]
- [[commands/netdom-join-domain-with-prew2k]]
