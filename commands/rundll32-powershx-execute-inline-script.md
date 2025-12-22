---
type: command
executor: cmd
data: 'rundll32 PowerShx.dll,main -e "$_INLINE_SCRIPT"'
output: null
platforms:
  - Windows
tags:
  - execute
  - bypass
verified: true
validated: true
---

# rundll32-powershx-execute-inline-script

## Command

```cmd
rundll32 PowerShx.dll,main -e "$_INLINE_SCRIPT"
```

## Description

Executes an inline PowerShell script with PowerShx via rundll32.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -e | Execute inline script | Yes |
| $_INLINE_SCRIPT | The script content | Yes |

## Examples

### Basic Usage

```cmd
rundll32 PowerShx.dll,main -e "Get-Process"
```

## Expected Output

Script output in full mode.

## Related

- [[procedures/Bypass-Constrained-Language-Mode-with-PowerShell-DLL-Runner]]
- [[tools/PowerShx]]
