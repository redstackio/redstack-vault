---
id: 45a9e5d8-e322-49ce-b219-dc18521136ab
name: SharPersist-Service-Persistence-Calculator
type: code
language: powershell
verified: true
created_at: '2023-04-06T03:56:27.967252+00:00'
updated_at: '2023-04-10T20:37:24.684667+00:00'
platforms:
  - Windows
tags:
  - persistence
  - service
  - powershell
validated: true
---

# SharPersist-Service-Persistence-Calculator

## Code

```powershell
SharPersist -t service -c "C:\Windows\System32\cmd.exe" -a "/c calc.exe" -n "Some Service" -m add
```

## Description

This PowerShell invocation of SharPersist creates a Windows service for persistence, configuring it to run cmd.exe which in turn launches the Calculator (calc.exe) as a benign disguise. The service auto-starts on boot, maintaining attacker access without obvious indicators.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| -t service | Persistence technique type | service |
| -c | Command to execute | "C:\Windows\System32\cmd.exe" |
| -a | Arguments for the command | "/c calc.exe" |
| -n | Service name | "Some Service" |
| -m add | Operation mode | add |

## Usage

Execute this in a PowerShell session with admin privileges on a compromised Windows machine. It is typically used post-initial access to ensure long-term presence. After running, verify with `sc query "Some Service"` and test by rebooting.

## Detection

- Monitor Event ID 7045 (new service installation) in Windows Event Logs.
- Scan for unusual services via `sc enumconfig` or tools like Autoruns.
- Behavioral detection: Calc.exe spawning from service context or unexpected cmd.exe processes.
- Registry monitoring at HKLM\SYSTEM\CurrentControlSet\Services for new entries.

## Related

- [[procedures/Create-Windows-Service-for-Persistence]]
- [[tools/SharPersist]]
