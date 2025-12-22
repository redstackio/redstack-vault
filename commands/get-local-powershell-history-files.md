---
id: 5ad8f02c-1bab-466b-8026-2966fba4d6f1
name: get-local-powershell-history-files
type: command
executor: powershell
data: >-
  Get-ChildItem -Path
  "C:\Users\*\APPDATA\Roaming\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt"
  | Get-Content
output: >-
  PS C:\ > Get-ChildItem -Path
  "C:\Users\*\APPDATA\Roaming\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt"
  | Get-Content

  cd C:\users\bob\Downloads\

  set-executionpolicy Unrestricted

  Unblock-File .\install.ps1

  .\install.ps1

  dir C:\users

  exit

  net user Administrator hunter2 /dom /add

  choco install visualstudio2019community

  dir

  cd \

  Get-ChildItem -Path
  "C:\Users\*\APPDATA\Roaming\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt"
  | Get-Content
created_at: '2020-06-24T23:40:58.199833+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Windows
tags:
  - enumeration
  - powershell
verified: true
validated: true
---

# get-local-powershell-history-files

## Command

```powershell
Get-ChildItem -Path "C:\Users\*\APPDATA\Roaming\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt" | Get-Content
```

## Description

This command enumerates and displays the contents of PowerShell ConsoleHost_history.txt files from all local user profiles on a Windows system. It is used during discovery or collection to uncover previously executed commands that may contain sensitive information, such as credential setups or tool installations.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -Path | Specifies the path pattern to search for history files; uses wildcard (*) for all users | Yes |
| Get-Content | Pipes the file contents to output; no additional parameters needed here | Built-in |

## Examples

### Basic Usage

```powershell
Get-ChildItem -Path "C:\Users\*\APPDATA\Roaming\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt" | Get-Content
```

### Advanced Usage

To save output to a file for later analysis:

```powershell
Get-ChildItem -Path "C:\Users\*\APPDATA\Roaming\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt" | Get-Content | Out-File -FilePath "C:\temp\ps_history.txt"
```

## Expected Output

The command outputs a list of historical PowerShell commands from each user's history file, such as:

```
PS C:\ > Get-ChildItem -Path "C:\Users\*\APPDATA\Roaming\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt" | Get-Content
cd C:\users\bob\Downloads\
set-executionpolicy Unrestricted
Unblock-File .\install.ps1
.\install.ps1
dir C:\users
exit
net user Administrator hunter2 /dom /add
choco install visualstudio2019community
dir
cd \
Get-ChildItem -Path "C:\Users\*\APPDATA\Roaming\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt" | Get-Content
```

Success is indicated by the display of command lines from user histories; empty output may mean no history files exist or access is denied.

## Related

- [[procedures/Enumerate-Local-Users-PowerShell-History]]
