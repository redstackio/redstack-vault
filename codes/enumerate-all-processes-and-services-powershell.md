---
type: code
language: powershell
verified: true
platforms:
  - Windows
tags:
  - enumeration
  - processes
  - services
validated: true
---

# enumerate-all-processes-and-services-powershell

## Code

```powershell
tasklist /v
net start
sc query
Get-Service
Get-Process
Get-WmiObject -Query "Select * from Win32_Process" | where {$_.Name -notlike "svchost*"} | Select Name, Handle, @{Label="Owner";Expression={$_.GetOwner().User}} | ft -AutoSize
```

## Description

This PowerShell snippet combines multiple built-in commands to enumerate running processes and services, including verbose details and owner information (excluding svchost). It provides a broad view for identifying elevated processes suitable for injection or service exploitation in privilege escalation.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| N/A | No user-defined variables; uses built-in cmdlets | N/A |

## Usage

Execute in a PowerShell session with low privileges to gather process data. Pipe output to a file (e.g., | Out-File processes.txt) for offline analysis. Use in post-exploitation to scout targets before attempting T1055 Process Injection.

## Detection

- Sysmon Event ID 1 (process creation) if run via PowerShell; monitor for Get-WmiObject or Get-Process executions.
- PowerShell Operational logs (Event ID 4104) capturing script block text.
- Unusual WMI queries via Event ID 4688 (process creation with wmic.exe).

## Related

- [[procedures/windows-processes-and-tasks-enumeration-for-privilege-escalation]]
