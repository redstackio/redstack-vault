---
id: 4c263ea4-b7b3-4cc7-8ee0-8f852a780963
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:29.377962+00:00'
updated_at: '2023-04-10T20:37:39.718796+00:00'
---

# Code Snippet 4c263ea4

**Language**: Powershell

```powershell
wmic startup get caption,command
reg query HKLM\Software\Microsoft\Windows\CurrentVersion\R
reg query HKCU\Software\Microsoft\Windows\CurrentVersion\Run
reg query HKCU\Software\Microsoft\Windows\CurrentVersion\RunOnce
dir "C:\Documents and Settings\All Users\Start Menu\Programs\Startup"
dir "C:\Documents and Settings\%username%\Start Menu\Programs\Startup"
```


