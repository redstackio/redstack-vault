---
id: 54e7239c-8dfd-4cbb-a807-0dc883882543
name: lookupsid.py Get a Domain SID from the Domain Controller
type: command
executor: bash
data: lookupsid.py '$_DOMAIN/$_USERNAME:$_PASSWORD'@$_TARGET_IP
output: 'root@kali:~# lookupsid.py ''bank.local/bsmith:hunter2''@10.10.10.5

  Impacket v0.9.22.dev1+20200428.191254.96c7a512 - Copyright 2020 SecureAuth Corporation

  [*] Brute forcing SIDs at 10.10.10.5

  [*] StringBinding ncacn_np:10.10.10.5[\pipe\lsarpc]

  [*] Domain SID is: S-1-5-21-2291914956-2855975875-54887866952

  ...

  ...'
created_at: '2020-06-24T05:08:26.191958+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# lookupsid.py Get a Domain SID from the Domain Controller

```bash
lookupsid.py '$_DOMAIN/$_USERNAME:$_PASSWORD'@$_TARGET_IP
```

## Expected Output

```
root@kali:~# lookupsid.py 'bank.local/bsmith:hunter2'@10.10.10.5
Impacket v0.9.22.dev1+20200428.191254.96c7a512 - Copyright 2020 SecureAuth Corporation

[*] Brute forcing SIDs at 10.10.10.5
[*] StringBinding ncacn_np:10.10.10.5[\pipe\lsarpc]
[*] Domain SID is: S-1-5-21-2291914956-2855975875-54887866952
...
...
```
