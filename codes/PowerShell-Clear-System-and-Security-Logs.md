---
id: 2060a6cd-0cb2-450d-ac15-21c44acffe81
name: PowerShell-Clear-System-and-Security-Logs
type: code
language: powershell
verified: true
created_at: '2023-04-06T03:56:27.717880+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - defense-evasion
  - log-clearing
  - powershell
validated: true
---

# PowerShell-Clear-System-and-Security-Logs

## Code

```powershell
cmd.exe /c wevtutil.exe cl System
cmd.exe /c wevtutil.exe cl Security
```

## Description

This PowerShell snippet executes Command Prompt commands to clear the System and Security event logs using wevtutil.exe. It provides a simple way to run the clearance operations within a PowerShell session, useful for scripting evasion techniques without leaving additional PowerShell traces.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | This code has no variables; it targets fixed log names (System and Security). Customize by editing the log names directly in the code. | N/A |

## Usage

Execute this snippet in an elevated PowerShell session on a compromised Windows host after gaining admin rights. It can be pasted directly into PowerShell or saved as a .ps1 file and invoked with `powershell.exe -ExecutionPolicy Bypass -File clear_logs.ps1`. Use it as part of a larger post-exploitation script to cover tracks before persistence or exfiltration. For automation, wrap in a function or combine with other evasion codes.

## Detection

- Monitor PowerShell ScriptBlock logging for invocations of cmd.exe /c wevtutil cl.
- EDR tools can detect wevtutil.exe with 'cl' argument, especially from non-admin processes.
- Anomalous drops in event log sizes or audit events for log clearing (Event ID 1102 in Security log, if not yet cleared).
- Process tree analysis showing PowerShell spawning cmd.exe targeting wevtutil.

## Related

- [[procedures/Clear-Windows-Event-Logs-for-Evasion]]
