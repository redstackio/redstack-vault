---
id: 7aa6ce98-6766-4107-a0fb-f3212164b8d0
name: SMBMap List an SMB Share's Contents Recursively
type: command
executor: bash
data: smbmap -u $_USERNAME -p $_PASSWORD -R $_SHARE_NAME -H $_TARGET_IP
output: "root@kali:~# cat f3\nroot@kali:~# smbmap -u bob -p secretpass -R temp -H\
  \ 10.10.10.10\n[+] Finding open SMB ports....  \n[+] User SMB session establishd\
  \ on 10.10.10.10...\n[+] IP: 10.10.10.10:445 Name: 10.10.10.14\n        Disk   \
  \                                                 Permissions \n        ----   \
  \                                                 ----------- \n        msfadmin\
  \                                                READ ONLY \n        .\\       \
  \                                                                           \n \
  \       dr--r--r--                0 Thu Sep 12 14:30:21 2019    . \n        dw--w--w--\
  \                0 Fri Apr 16 02:16:01 2010    ..\n        dr--r--r--          \
  \      0 Tue Apr 27 23:44:16 2010    vulnerable \n        -r--r--r--           \
  \     4 Sun May 20 14:22:31 2012    .rhosts \n        dr--r--r--               \
  \ 0 Mon May 17 21:43:17 2010    .ssh\n        dw--w--w--                0 Sat Apr\
  \ 17 14:10:59 2010    .\n        dr--r--r--                0 Sat Apr 17 14:10:59\
  \ 2010    ..\n        -w--w--w--                0 Sat Apr 17 14:10:59 2010    cpu_localhost_0"
created_at: '2019-09-18T01:44:02.133727+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# SMBMap List an SMB Share's Contents Recursively

```bash
smbmap -u $_USERNAME -p $_PASSWORD -R $_SHARE_NAME -H $_TARGET_IP
```

## Expected Output

```
root@kali:~# cat f3
root@kali:~# smbmap -u bob -p secretpass -R temp -H 10.10.10.10
[+] Finding open SMB ports....  
[+] User SMB session establishd on 10.10.10.10...
[+] IP: 10.10.10.10:445 Name: 10.10.10.14
        Disk                                                    Permissions 
        ----                                                    ----------- 
        msfadmin                                                READ ONLY 
        .\                                                                                  
        dr--r--r--                0 Thu Sep 12 14:30:21 2019    . 
        dw--w--w--                0 Fri Apr 16 02:16:01 2010    ..
        dr--r--r--                0 Tue Apr 27 23:44:16 2010    vulnerable 
        -r--r--r--                4 Sun May 20 14:22:31 2012    .rhosts 
        dr--r--r--                0 Mon May 17 21:43:17 2010    .ssh
        dw--w--w--                0 Sat Apr 17 14:10:59 2010    .
        dr--r--r--                0 Sat Apr 17 14:10:59 2010    ..
        -w--w--w--                0 Sat Apr 17 14:10:59 2010    cpu_localhost_0
```


