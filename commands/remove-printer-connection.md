---
id: aca12d2a-2bbb-4db3-b9e7-8a8b8909725e
name: remove-printer-connection
type: command
executor: powershell
data: Remove-Printer -Name $fullprinterName -ErrorAction SilentlyContinue
output: null
created_at: '2023-04-06T03:56:29.867342+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - privilege-escalation
  - print-spooler
verified: true
validated: true
---

# remove-printer-connection

## Command

```powershell
Remove-Printer -Name $fullprinterName -ErrorAction SilentlyContinue
```

## Description

This PowerShell command removes a specified printer connection from the system, suppressing errors if the printer does not exist. It is used in privilege escalation scenarios to reset the printer state before re-adding a connection that triggers driver injection.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-Name` | The full name of the printer connection to remove (e.g., '\\server\printer - x64') | Yes |
| `$fullprinterName` | Variable holding the printer connection path | Yes |
| `-ErrorAction SilentlyContinue` | Continues execution without throwing errors if the printer is missing | No |

## Examples

### Basic Usage

```powershell
Remove-Printer -Name '\\dc.purple.lab\Universal Priv Printer - x64' -ErrorAction SilentlyContinue
```

### With Variable

```powershell
$fullprinterName = '\\dc.purple.lab\Universal Priv Printer - x64'
Remove-Printer -Name $fullprinterName -ErrorAction SilentlyContinue
```

## Expected Output

No output on success. If the printer existed, it is removed; verify with `Get-Printer` showing no matching entry. Errors are suppressed.

## Related

- [[procedures/windows-privilege-escalation-via-universal-printer-driver]]
- [[commands/add-printer-connection]]
