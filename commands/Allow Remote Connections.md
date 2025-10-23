---
id: fac244e2-1c07-48ac-942e-56da5ffd9a1f
name: Allow Remote Connections
type: command
executor: bash
data: reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server"
  /v fDenyTSConnections /t REG_DWORD /d 0 /f
output: null
created_at: '2023-04-06T03:56:28.232386+00:00'
updated_at: '2023-04-10T20:37:27.902007+00:00'
---

# Allow Remote Connections

```bash
reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server" /v fDenyTSConnections /t REG_DWORD /d 0 /f
```


