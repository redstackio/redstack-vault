---
type: command
executor: cmd
data: 'rundll32 PowerShdll,main -h'
output: null
platforms:
  - Windows
tags:
  - help
  - bypass
verified: true
validated: true
---

# rundll32-powershdll-help

## Command

```cmd
rundll32 PowerShdll,main -h
```

## Description

Displays help and usage options for the PowerShdll DLL via rundll32, showing flags for script execution and interactive modes.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -h | Show help message | Yes |

## Examples

### Basic Usage

```cmd
rundll32 PowerShdll,main -h
```

## Expected Output

Help text: "rundll32 PowerShdll,main -h      Display this message\nrundll32 PowerShdll,main -f <path>       Run the script..." etc.

## Related

- [[procedures/Bypass-Constrained-Language-Mode-with-PowerShell-DLL-Runner]]
- [[tools/PowerShdll]]
