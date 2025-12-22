---
type: command
executor: cmd
data: 'rundll32 PowerShdll,main -i'
output: null
platforms:
  - Windows
tags:
  - interactive
  - console
  - bypass
verified: true
validated: true
---

# rundll32-powershdll-interactive-current-window

## Command

```cmd
rundll32 PowerShdll,main -i
```

## Description

Starts an interactive PowerShell console in the current window using PowerShdll.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -i | Open in current console | Yes |

## Examples

### Basic Usage

```cmd
rundll32 PowerShdll,main -i
```

## Expected Output

PowerShell prompt in current window, unrestricted.

## Related

- [[procedures/Bypass-Constrained-Language-Mode-with-PowerShell-DLL-Runner]]
- [[tools/PowerShdll]]
