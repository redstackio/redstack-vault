---
id: e9918bd8-0003-4d1f-8821-775a72ae8989
name: SMBMap Search an SMB Share Recursively by File Name
type: command
executor: bash
data: smbmap -u $_USERNAME -p $_PASSWORD -R $_SHARE_NAME -H $_TARGET_IP -A $_FILENAME
  -q
output: "root@kali:~# smbmap -u bob -p secretpass -R stuff -H 10.10.10.10 -A secret\
  \ -q\n[+] Finding open SMB ports....\n[+] User SMB session establishd on 10.10.10.10...\n\
  [+] IP: 10.10.10.10:445 Name: 10.10.10.10 \n        Disk                       \
  \                             Permissions\n        ----                        \
  \                            -----------\n        [+] Match found! Downloading:\
  \ stuff\\.\\secret\n        stuff                                              \
  \     READ ONLY\n        [+] Starting search for files matching 'secret' on share\
  \ stuff.\n        [+] Match found! Downloading: stuff\\secret\n"
created_at: '2019-09-18T01:44:02.135506+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# SMBMap Search an SMB Share Recursively by File Name

```bash
smbmap -u $_USERNAME -p $_PASSWORD -R $_SHARE_NAME -H $_TARGET_IP -A $_FILENAME -q
```

## Expected Output

```
root@kali:~# smbmap -u bob -p secretpass -R stuff -H 10.10.10.10 -A secret -q
[+] Finding open SMB ports....
[+] User SMB session establishd on 10.10.10.10...
[+] IP: 10.10.10.10:445 Name: 10.10.10.10 
        Disk                                                    Permissions
        ----                                                    -----------
        [+] Match found! Downloading: stuff\.\secret
        stuff                                                   READ ONLY
        [+] Starting search for files matching 'secret' on share stuff.
        [+] Match found! Downloading: stuff\secret

```


