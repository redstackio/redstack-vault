---
id: 502d9858-d9ff-4a3a-81a4-7c4ecd749394
name: Disable UAC Remote Restriction
type: command
executor: bash
data: reg add HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System
  /v LocalAccountTokenFilterPolicy /t REG_DWORD /d 1 /f
output: null
created_at: '2023-04-06T03:56:28.232421+00:00'
updated_at: '2023-04-10T20:37:27.902007+00:00'
---

# Disable UAC Remote Restriction

```bash
reg add HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v LocalAccountTokenFilterPolicy /t REG_DWORD /d 1 /f
```
