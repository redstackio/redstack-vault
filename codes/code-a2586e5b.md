---
id: a2586e5b-3214-447d-844b-4d00377b7937
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:03.238577+00:00'
updated_at: '2023-04-10T20:26:35.780565+00:00'
---

# Code Snippet a2586e5b

**Language**: Powershell

```powershell
smbclient -I 10.10.10.100 -L ACTIVE -N -U ""
        Sharename       Type      Comment
        ---------       ----      -------
        ADMIN$          Disk      Remote Admin
        C$              Disk      Default share
        IPC$            IPC       Remote IPC
        NETLOGON        Disk      Logon server share
        Replication     Disk      
        SYSVOL          Disk      Logon server share
        Users           Disk
use Sharename # select a Sharename
cd Folder     # move inside a folder
ls            # list files
```


