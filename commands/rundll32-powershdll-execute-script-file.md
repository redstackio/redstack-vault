---
type: command
executor: cmd
data: 'rundll32 PowerShdll,main -f "$_SCRIPT_PATH"'
output: null
platforms:
  - Windows
tags:
  - execute
  - file
  - bypass
verified: true
validated: true
---

# rundll32-powershdll-execute-script-file

## Command

```cmd
rundll32 PowerShdll,main -f "$_SCRIPT_PATH"
```

## Description

Runs a PowerShell script file using PowerShdll, enabling full execution in CLM environments.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -f | Flag to specify script file | Yes |
| $_SCRIPT_PATH | Path to the .ps1 file | Yes |

## Examples

### Basic Usage

```cmd
rundll32 PowerShdll,main -f "C:\temp\payload.ps1"
```

## Expected Output

The script's output or effects, unrestricted by CLM.

## Related

- [[procedures/Bypass-Constrained-Language-Mode-with-PowerShell-DLL-Runner]]
- [[tools/PowerShdll]]
