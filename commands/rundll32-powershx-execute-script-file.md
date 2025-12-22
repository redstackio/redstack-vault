---
type: command
executor: cmd
data: 'rundll32 PowerShx.dll,main -f "$_SCRIPT_PATH"'
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

# rundll32-powershx-execute-script-file

## Command

```cmd
rundll32 PowerShx.dll,main -f "$_SCRIPT_PATH"
```

## Description

Runs a script file with PowerShx.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -f | Script file path | Yes |
| $_SCRIPT_PATH | Path to .ps1 | Yes |

## Examples

### Basic Usage

```cmd
rundll32 PowerShx.dll,main -f "payload.ps1"
```

## Expected Output

Script execution results.

## Related

- [[procedures/Bypass-Constrained-Language-Mode-with-PowerShell-DLL-Runner]]
- [[tools/PowerShx]]
