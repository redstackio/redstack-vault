---
id: new-uuid-for-import
name: import-powerpxe-module
type: command
executor: powershell
data: Import-Module $_MODULE_PATH
output: null
created_at: '2023-04-06T03:56:08.387910+00:00'
updated_at: '2023-04-10T20:36:00.785400+00:00'
platforms:
  - Windows
tags:
  - pxe
  - exploitation
verified: true
validated: true
---

# Import PowerPXE Module

## Command

```powershell
Import-Module $_MODULE_PATH
```

## Description

Loads the PowerPXE PowerShell module for PXE boot exploitation, enabling functions like Get-PXEcreds to intercept and parse boot files.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_MODULE_PATH | Path to PowerPXE.ps1 (e.g., .\PowerPXE.ps1) | Yes |

## Examples

### Basic Usage

```powershell
Import-Module .\PowerPXE.ps1
```

## Expected Output

No output on success; the module functions become available. Check with `Get-Command Get-PXEcreds`.

## Related

- [[tools/powerpxe]]
- [[procedures/pxe-boot-image-attack-local-admin-hijack]]
