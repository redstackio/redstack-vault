---
id: 5ad8f02c-1bab-466b-8026-2966fba4d6f1
name: Enumerate Local Users' PowerShell History
type: command
executor: powershell
data: Get-ChildItem -Path "C:\Users\*\APPDATA\Roaming\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt"
  | Get-Content
output: 'PS C:\ > Get-ChildItem -Path "C:\Users\*\APPDATA\Roaming\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt"
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

  Get-ChildItem -Path "C:\Users\*\APPDATA\Roaming\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt"
  | Get-Content'
created_at: '2020-06-24T23:40:58.199833+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Enumerate Local Users' PowerShell History

```powershell
Get-ChildItem -Path "C:\Users\*\APPDATA\Roaming\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt" | Get-Content
```

## Expected Output

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
