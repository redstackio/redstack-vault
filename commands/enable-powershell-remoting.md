---
id: 00000000-0000-0000-0000-000000000001
name: enable-powershell-remoting
type: command
executor: powershell
data: |-
  Enable-PSRemoting -Force
  net start winrm
output: null
created_at: '2023-04-06T03:56:31.140924+00:00'
updated_at: '2023-04-10T20:37:59.190248+00:00'
platforms:
  - Windows
tags:
  - winrm
  - setup
verified: true
validated: true
---

# enable-powershell-remoting

## Command

```powershell
Enable-PSRemoting -Force
net start winrm
```

## Description

Enables PowerShell remoting on a Windows machine by configuring WinRM and starting the service. Use this on the target to allow incoming remote sessions; requires admin privileges.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -Force | Suppresses all prompts and restarts WinRM if needed | Yes |

## Examples

### Basic Usage

```powershell
Enable-PSRemoting -Force
net start winrm
```

### Verification

```powershell
Get-Service winrm
```

## Expected Output

No errors; output like:

WinRM Quick Configuration

WinRM has been updated for remote management.

Status   Name               DisplayName
------   ----               -----------
Running  winrm              Windows Remote Management (WS-Management)

## Related

- [[procedures/windows-powershell-remoting-with-pssession]]
- [[commands/set-trusted-hosts]]
