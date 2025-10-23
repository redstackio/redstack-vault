---
id: d897cc11-c8ef-4ed7-8537-afb63634fa7e
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:18.861356+00:00'
updated_at: '2023-04-10T20:34:28.305848+00:00'
---

# Code Snippet d897cc11

**Language**: Powershell

```powershell
╭─swissky@lab ~  
╰─$ /usr/bin/getcap -r  /usr/bin
/usr/bin/fping                = cap_net_raw+ep
/usr/bin/dumpcap              = cap_dac_override,cap_net_admin,cap_net_raw+eip
/usr/bin/gnome-keyring-daemon = cap_ipc_lock+ep
/usr/bin/rlogin               = cap_net_bind_service+ep
/usr/bin/ping                 = cap_net_raw+ep
/usr/bin/rsh                  = cap_net_bind_service+ep
/usr/bin/rcp                  = cap_net_bind_service+ep
```


