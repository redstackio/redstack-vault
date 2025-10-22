---
id: 1f12b4a9-05ed-4b6c-98c3-548d82a13b16
name: Metasploit Upload a File or Directory
type: command
executor: metasploit
data: upload "$_TARGET"
output: 'meterpreter > upload /root/.ssh/id_rsa.pub

  [*] uploading  : /root/.ssh/id_rsa.pub -> id_rsa.pub

  [*] Uploaded 391.00 B of 391.00 B (100.0%): /root/.ssh/id_rsa.pub -> id_rsa.pub

  [*] uploaded   : /root/.ssh/id_rsa.pub -> id_rsa.pub'
created_at: '2020-07-08T23:57:32.895335+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Metasploit Upload a File or Directory

```metasploit
upload "$_TARGET"
```

## Expected Output

```
meterpreter > upload /root/.ssh/id_rsa.pub
[*] uploading  : /root/.ssh/id_rsa.pub -> id_rsa.pub
[*] Uploaded 391.00 B of 391.00 B (100.0%): /root/.ssh/id_rsa.pub -> id_rsa.pub
[*] uploaded   : /root/.ssh/id_rsa.pub -> id_rsa.pub
```
