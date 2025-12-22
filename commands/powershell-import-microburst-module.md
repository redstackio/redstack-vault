---
type: command
executor: powershell
data: Import-Module Microburst.psm1
output: null
platforms:
  - Windows
tags:
  - azure
  - import
verified: true
validated: true
---

# powershell-import-microburst-module

## Command

```powershell
Import-Module Microburst.psm1
```

## Description

This command loads the Microburst PowerShell module, which provides Azure penetration testing cmdlets like Get-AzurePasswords. Use it at the start of any Microburst-based procedure after ensuring the .psm1 file is in the current directory.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Microburst.psm1 | Path to the module file (defaults to current directory) | Yes |

## Examples

### Basic Usage

```powershell
Import-Module Microburst.psm1
```

### With Full Path

```powershell
Import-Module C:\Tools\Microburst.psm1
```

## Expected Output

Import-Module : The specified module 'Microburst.psm1' was loaded successfully.

If successful, subsequent commands like Get-Command Get-AzurePasswords will list the available functions.

## Related

- [[procedures/Retrieve-Azure-Passwords-Using-Microburst]]
- [[tools/Microburst]]
