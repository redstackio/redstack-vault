---
type: command
executor: cmd
data: 'rundll32 PowerShdll,main "$_INLINE_SCRIPT"'
output: null
platforms:
  - Windows
tags:
  - execute
  - bypass
verified: true
validated: true
---

# rundll32-powershdll-execute-inline-script

## Command

```cmd
rundll32 PowerShdll,main "$_INLINE_SCRIPT"
```

## Description

Executes an inline PowerShell script using PowerShdll via rundll32, bypassing CLM.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_INLINE_SCRIPT | The PowerShell code to execute inline | Yes |

## Examples

### Basic Usage

```cmd
rundll32 PowerShdll,main "Get-Process"
```

## Expected Output

Output of the inline script, e.g., list of processes in full language mode.

## Related

- [[procedures/Bypass-Constrained-Language-Mode-with-PowerShell-DLL-Runner]]
- [[tools/PowerShdll]]
