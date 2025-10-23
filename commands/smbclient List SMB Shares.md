---
id: 37e55e52-b286-47ea-b252-fbc6d8951356
name: smbclient List SMB Shares
type: command
executor: bash
data: smbclient -U '$_USERNAME%$_PASSWORD' -L $_TARGET_IP
output: "root@kali:~# smbclient -U '' -N -L 10.10.10.10\n\n        Sharename     \
  \  Type      Comment\n        ---------       ----      -------\n        print$\
  \          Disk      Printer Drivers\n        opt             Disk      \n     \
  \   IPC$            IPC       IPC Service (Samba 3.0.20-Debian)\n        ADMIN$\
  \          IPC       IPC Service (Samba 3.0.20-Debian)\nReconnecting with SMB1 for\
  \ workgroup listing.\n\n        Server               Comment\n        ---------\
  \            -------\n\n        Workgroup            Master\n        --------- \
  \           -------\n        WORKGROUP            HOST"
created_at: '2019-09-18T01:44:02.124491+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# smbclient List SMB Shares

```bash
smbclient -U '$_USERNAME%$_PASSWORD' -L $_TARGET_IP
```

## Expected Output

```
root@kali:~# smbclient -U '' -N -L 10.10.10.10

        Sharename       Type      Comment
        ---------       ----      -------
        print$          Disk      Printer Drivers
        opt             Disk      
        IPC$            IPC       IPC Service (Samba 3.0.20-Debian)
        ADMIN$          IPC       IPC Service (Samba 3.0.20-Debian)
Reconnecting with SMB1 for workgroup listing.

        Server               Comment
        ---------            -------

        Workgroup            Master
        ---------            -------
        WORKGROUP            HOST
```


