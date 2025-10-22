---
id: c0822854-6f98-4d53-be3f-2d07607005e2
name: smbclient List SMB Shares with an Authenticated Session
type: command
executor: ''
data: smbclient -U $_USERNAME%$_PASSWORD -L $_TARGET_IP
output: "root@kali:~# smbclient -U bob%secretpass -L 10.10.10.14\nEnter WORKGROUP\\\
  bob's password: \n\n        Sharename       Type      Comment\n        ---------\
  \       ----      -------\n        print$          Disk      Printer Drivers\n \
  \       opt             Disk      \n        IPC$            IPC       IPC Service\
  \ (Samba 3.0.20-Debian)\n        ADMIN$          IPC       IPC Service (Samba 3.0.20-Debian)\n\
  \        secret          Disk      Home Directories\nReconnecting with SMB1 for\
  \ workgroup listing.\n\n        Server               Comment\n        ---------\
  \            -------\n\n        Workgroup            Master\n        --------- \
  \           -------\n        WORKGROUP            HOST"
created_at: '2019-09-18T01:44:02.109554+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# smbclient List SMB Shares with an Authenticated Session

```bash
smbclient -U $_USERNAME%$_PASSWORD -L $_TARGET_IP
```

## Expected Output

```
root@kali:~# smbclient -U bob%secretpass -L 10.10.10.14
Enter WORKGROUP\bob's password: 

        Sharename       Type      Comment
        ---------       ----      -------
        print$          Disk      Printer Drivers
        opt             Disk      
        IPC$            IPC       IPC Service (Samba 3.0.20-Debian)
        ADMIN$          IPC       IPC Service (Samba 3.0.20-Debian)
        secret          Disk      Home Directories
Reconnecting with SMB1 for workgroup listing.

        Server               Comment
        ---------            -------

        Workgroup            Master
        ---------            -------
        WORKGROUP            HOST
```
