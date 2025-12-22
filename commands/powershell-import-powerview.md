---
type: command
executor: powershell
data: . $_PATH_TO_POWERVIEW
platforms:
  - Windows
tags:
  - active-directory
  - import
verified: true
validated: true
---

# PowerShell Import PowerView

## Command

```powershell
. $_PATH_TO_POWERVIEW
```

## Description

This command dot-sources the PowerView.ps1 script into the current PowerShell session, loading all its functions for Active Directory operations like enumeration and modification.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_PATH_TO_POWERVIEW | Full local path to the PowerView.ps1 file (e.g., C:\temp\PowerView.ps1) | Yes |

## Examples

### Basic Usage

```powershell
. .\PowerView.ps1
```

### Advanced Usage

```powershell
$scriptPath = "C:\Downloads\PowerView.ps1"
. $scriptPath
Get-Command *Domain*  # Verify functions loaded
```

## Expected Output

No output if successful. If the file is not found: "The term '. ' is not recognized..." or path error. After import, functions like Get-DomainUser become available.

## Related

- [[procedures/change-ad-domain-user-password]]
- [[tools/PowerView]]
