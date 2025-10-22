---
id: 43a61bee-3a68-48bf-ba69-4cbf33b839ff
name: Fix CredSSP errors
type: command
executor: bash
data: 'reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server"
  /v fDenyTSConnections /t REG_DWORD /d 0 /f

  reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp"
  /v UserAuthentication /t REG_DWORD /d 0 /f'
output: null
created_at: '2023-04-06T03:56:31.036745+00:00'
updated_at: '2023-04-10T20:37:56.779209+00:00'
---

# Fix CredSSP errors

```bash
reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server" /v fDenyTSConnections /t REG_DWORD /d 0 /f
reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp" /v UserAuthentication /t REG_DWORD /d 0 /f
```
