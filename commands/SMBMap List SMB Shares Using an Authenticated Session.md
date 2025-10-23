---
id: 3dc40f29-0e1e-41e1-a874-5780c0aed25b
name: SMBMap List SMB Shares Using an Authenticated Session
type: command
executor: ''
data: smbmap -u $_USERNAME -p $_PASSWORD -H $_TARGET_IP
output: "root@kali:~# smbmap -u bob -p secretpass -H 10.10.10.10\n[+] Finding open\
  \ SMB ports....\n[+] User SMB session establishd on 10.10.10.10...\n[+] IP: 10.10.10.10:445\
  \ Name: 10.10.10.14                                       \n        Disk       \
  \                                             Permissions\n        ----        \
  \                                            -----------\n        print$       \
  \                                           READ ONLY\n        opt             \
  \                                        READ ONLY\n        IPC$               \
  \                                     NO ACCESS\n        ADMIN$                \
  \                                  NO ACCESS\n        msfadmin                 \
  \                               READ ONLY\n"
created_at: '2019-09-18T01:44:02.128329+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# SMBMap List SMB Shares Using an Authenticated Session

```bash
smbmap -u $_USERNAME -p $_PASSWORD -H $_TARGET_IP
```

## Expected Output

```
root@kali:~# smbmap -u bob -p secretpass -H 10.10.10.10
[+] Finding open SMB ports....
[+] User SMB session establishd on 10.10.10.10...
[+] IP: 10.10.10.10:445 Name: 10.10.10.14                                       
        Disk                                                    Permissions
        ----                                                    -----------
        print$                                                  READ ONLY
        opt                                                     READ ONLY
        IPC$                                                    NO ACCESS
        ADMIN$                                                  NO ACCESS
        msfadmin                                                READ ONLY

```


