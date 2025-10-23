---
id: 5bad1e05-2a2a-4b52-b0cc-cda367c9877e
name: Configure Terminal Services Shadowing
type: command
executor: bash
data: reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows NT\Terminal
  Services" /v Shadow /t REG_DWORD /d 4
output: null
created_at: '2023-04-06T03:56:28.232297+00:00'
updated_at: '2023-04-10T20:37:27.902007+00:00'
---

# Configure Terminal Services Shadowing

```bash
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows NT\Terminal Services" /v Shadow /t REG_DWORD /d 4
```


