---
id: 2796667f-b0c6-4394-a0a7-a2dc3e4f8328
name: WinRS-Open-CMD-on-Remote-Windows-Machine
type: command
executor: powershell
data: 'winrs -r:$_COMPUTER_NAME cmd'
output: null
created_at: '2023-01-12T07:48:43.750256+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - WinRS
  - remote-execution
verified: true
validated: true
---

# WinRS-Open-CMD-on-Remote-Windows-Machine

## Command

```powershell
winrs -r:$_COMPUTER_NAME cmd
```

## Description

This command uses WinRS to establish a remote CMD session on a Windows target machine via WinRM, relying on implicit authentication (e.g., current user credentials in a domain environment).

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -r:$_COMPUTER_NAME | Target computer name or IP address | Yes |
| cmd | Opens a remote command prompt shell | Yes |

## Examples

### Basic Usage

```powershell
winrs -r:TARGET-PC cmd
```

### Advanced Usage

```powershell
winrs -r:TARGET-PC -remote:HTTPS cmd
```
(Uses HTTPS for encrypted connection if configured on target.)

## Expected Output

Successful execution connects to the remote CMD:

```
Microsoft Windows [Version 10.0.19041.1]
(c) Microsoft Corporation. All rights reserved.

C:\Windows\system32> 
```
The prompt changes to the remote machine's context. Errors like "Access denied" indicate authentication issues.

## Related

- [[commands/WinRS-Open-CMD-on-Remote-Windows-Machine-With-Credentials]]
- [[procedures/Remote-Access-to-Windows-Machine-Using-Credentials]]
