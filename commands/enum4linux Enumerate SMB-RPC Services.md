---
id: 433d22a4-beff-4106-87f1-2d69f833766d
name: enum4linux Enumerate SMB/RPC Services
type: command
executor: bash
data: enum4linux $_TARGET_IP
output: "root@kali:~/Documents# enum4linux 10.10.10.10\nStarting enum4linux v0.8.9\
  \ ( http://labs.portcullis.co.uk/application/enum4linux/ ) on Wed Sep 18 16:23:34\
  \ 2019\n\n ==========================\n|    Target Information    |\n ==========================\n\
  Target ........... 10.10.10.10\nRID Range ........ 500-550,1000-1050\nUsername .........\
  \ ''\nPassword ......... ''\nKnown Usernames .. administrator, guest, krbtgt, domain\
  \ admins, root, bin, none\n\n ==========================\n|    Target Information\
  \    |\n ==========================\nTarget ........... 10.10.10.10\nRID Range ........\
  \ 500-550,1000-1050\nUsername ......... ''\nPassword ......... ''\nKnown Usernames\
  \ .. administrator, guest, krbtgt, domain admins, root, bin, none\n\n ===================================================\n\
  |    Enumerating Workgroup/Domain on 10.10.10.10    |\n ===================================================\n\
  [+] Got domain/workgroup name: WORKGROUP\n...\n...\nenum4linux complete on Wed Sep\
  \ 18 16:23:35 2019"
created_at: '2019-09-18T20:47:12.029163+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# enum4linux Enumerate SMB/RPC Services

```bash
enum4linux $_TARGET_IP
```

## Expected Output

```
root@kali:~/Documents# enum4linux 10.10.10.10
Starting enum4linux v0.8.9 ( http://labs.portcullis.co.uk/application/enum4linux/ ) on Wed Sep 18 16:23:34 2019

 ==========================
|    Target Information    |
 ==========================
Target ........... 10.10.10.10
RID Range ........ 500-550,1000-1050
Username ......... ''
Password ......... ''
Known Usernames .. administrator, guest, krbtgt, domain admins, root, bin, none

 ==========================
|    Target Information    |
 ==========================
Target ........... 10.10.10.10
RID Range ........ 500-550,1000-1050
Username ......... ''
Password ......... ''
Known Usernames .. administrator, guest, krbtgt, domain admins, root, bin, none

 ===================================================
|    Enumerating Workgroup/Domain on 10.10.10.10    |
 ===================================================
[+] Got domain/workgroup name: WORKGROUP
...
...
enum4linux complete on Wed Sep 18 16:23:35 2019
```


