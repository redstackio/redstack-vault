---
type: command
executor: cmd
data: 'rundll32 PowerShx.dll,main -f "$_SCRIPT_PATH" -c "$_CMDLT_NAME"'
output: null
platforms:
  - Windows
tags:
  - execute
  - cmdlet
  - bypass
verified: true
validated: true
---

# rundll32-powershx-execute-script-with-cmdlet

## Command

```cmd
rundll32 PowerShx.dll,main -f "$_SCRIPT_PATH" -c "$_CMDLT_NAME"
```

## Description

Loads a script and executes a specific cmdlet from it.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -f | Script path | Yes |
| $_SCRIPT_PATH | .ps1 file | Yes |
| -c | Cmdlet to run | Yes |
| $_CMDLT_NAME | Name of cmdlet (e.g., Invoke-WebRequest) | Yes |

## Examples

### Basic Usage

```cmd
rundll32 PowerShx.dll,main -f "script.ps1" -c "MyFunction"
```

## Expected Output

Output from the specified cmdlet.

## Related

- [[procedures/Bypass-Constrained-Language-Mode-with-PowerShell-DLL-Runner]]
- [[tools/PowerShx]]
