---
id: 148c7992-29b9-4159-b6db-ab716ba8b581
name: import-mso-lspray-powershell-module
type: command
executor: powershell
data: Import-Module .\MSOLSpray.ps1
output: null
created_at: '2023-05-23T16:38:53.036313+00:00'
updated_at: '2023-05-23T16:38:53.084754+00:00'
platforms:
  - Windows
  - Linux
tags:
  - setup
  - powershell
verified: true
validated: true
---

# import-mso-lspray-powershell-module

## Command

```powershell
Import-Module .\MSOLSpray.ps1
```

## Description

This command imports the MSOLSpray PowerShell module into the current session, enabling the Invoke-MSOLSpray function for password spraying.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| .\MSOLSpray.ps1 | Path to the script file | Yes |

## Examples

### Basic Usage

```powershell
Import-Module .\MSOLSpray.ps1
```

### Full Path Usage

```powershell
Import-Module C:\Tools\MSOLSpray\MSOLSpray.ps1
```

## Expected Output

No output on success. Verify with: Get-Command Invoke-MSOLSpray

## Related

- [[procedures/Azure-AD-Password-Spray]]
