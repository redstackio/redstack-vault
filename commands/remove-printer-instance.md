---
id: aca12d2a-2bbb-4db3-b9e7-8a8b8909725e
name: remove-printer-instance
type: command
executor: powershell
data: Remove-Printer -Name $_FULL_PRINTER_NAME -ErrorAction SilentlyContinue
output: null
created_at: '2023-04-06T03:56:29.867342+00:00'
updated_at: '2023-04-10T20:37:34.442831+00:00'
platforms:
  - Windows
tags:
  - printer-nightmare
  - cleanup
verified: true
validated: true
---

# remove-printer-instance

## Command

```powershell
Remove-Printer -Name $_FULL_PRINTER_NAME -ErrorAction SilentlyContinue
```

## Description

Removes a printer instance from the system, suppressing errors if it doesn't exist. Used in PrinterNightmare to unload the malicious printer before re-adding to trigger escalation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_FULL_PRINTER_NAME | Full UNC path to printer (e.g., '\\host\EasySystemShell - x64') | Yes |
| -ErrorAction SilentlyContinue | Suppresses error output | No |

## Examples

### Basic Usage

```powershell
Remove-Printer -Name '\\printer-installed-host\EasySystemShell - x64' -ErrorAction SilentlyContinue
```

## Expected Output

No output if successful; errors suppressed.

## Related

- [[procedures/PrinterNightmare-Privilege-Escalation]]
