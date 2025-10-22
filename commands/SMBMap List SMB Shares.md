---
id: 0071c284-e546-4b48-be33-69e446d29b33
name: SMBMap List SMB Shares
type: command
executor: bash
data: smbmap -u '$_USERNAME' -p '$_PASSWORD' -H $_TARGET_IP
output: "root@kali:~# smbmap -u 'bob' -p 's3cr3t' -H 10.10.10.10\n[+] Finding open\
  \ SMB ports....\n[+] User SMB session establishd on 10.10.10.10...\n[+] IP: 10.10.10.10:445\
  \ Name: 10.10.10.10                                       \n        Disk       \
  \                                             Permissions\n        ----        \
  \                                            -----------\n        print$       \
  \                                           NO ACCESS\n        opt             \
  \                                        NO ACCESS\n        IPC$               \
  \                                     NO ACCESS\n        ADMIN$                \
  \                                  NO ACCESS"
created_at: '2019-09-18T01:44:02.132073+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# SMBMap List SMB Shares

```bash
smbmap -u '$_USERNAME' -p '$_PASSWORD' -H $_TARGET_IP
```

## Expected Output

```
root@kali:~# smbmap -u 'bob' -p 's3cr3t' -H 10.10.10.10
[+] Finding open SMB ports....
[+] User SMB session establishd on 10.10.10.10...
[+] IP: 10.10.10.10:445 Name: 10.10.10.10                                       
        Disk                                                    Permissions
        ----                                                    -----------
        print$                                                  NO ACCESS
        opt                                                     NO ACCESS
        IPC$                                                    NO ACCESS
        ADMIN$                                                  NO ACCESS
```
