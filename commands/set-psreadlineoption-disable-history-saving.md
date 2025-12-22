---
type: command
executor: powershell
data: Set-PSReadlineOption -HistorySaveStyle SaveNothing
platforms:
  - Windows
tags:
  - defense-evasion
  - powershell
verified: true
validated: true
---

# set-psreadlineoption-disable-history-saving

## Command

```powershell
Set-PSReadlineOption -HistorySaveStyle SaveNothing
```

## Description

This command configures the PSReadLine module in PowerShell to disable saving command history to a file, preventing the logging of subsequent commands during an engagement. Use this early in a session to evade detection via history analysis.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -HistorySaveStyle | Sets the history saving behavior; 'SaveNothing' prevents file writes | Yes |
| SaveNothing | Specific value to disable saving (other options: SaveIncrementally, AddToHistory) | Yes |

## Examples

### Basic Usage

```powershell
Set-PSReadlineOption -HistorySaveStyle SaveNothing
```

### Verification

```powershell
Get-PSReadlineOption | Select-Object HistorySaveStyle
```

## Expected Output

No direct output from the command itself. Upon verification with Get-PSReadlineOption, expect:

HistorySaveStyle : SaveNothing

This confirms the option is set, and no further history will be appended to the file.

## Related

- [[procedures/Windows-Privilege-Escalation-via-Powershell-History-Looting]]
