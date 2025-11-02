---
id: 4a0275b1-f59a-49b6-baf8-ad85ca69e52e
name: evil-winrm.rb Connect to a WinRM Server
type: command
executor: bash
data: evil-winrm.rb -i $_TARGET_IP -u $_USER -p $_PASS
output: 'root@kali:~/Documents/evil-winrm# ./evil-winrm.rb -i 10.10.10.10 -u bob -p
  secretpass


  Evil-WinRM shell v2.3


  Info: Establishing connection to remote endpoint


  *Evil-WinRM* PS C:\Users\bob\Documents>'
created_at: '2020-03-03T01:24:01.684830+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
tools:
- '[[Evil-WinRM]]'
- '[[ps]]'
---

# evil-winrm.rb Connect to a WinRM Server

```bash
evil-winrm.rb -i $_TARGET_IP -u $_USER -p $_PASS
```

## Expected Output

```
root@kali:~/Documents/evil-winrm# ./evil-winrm.rb -i 10.10.10.10 -u bob -p secretpass

Evil-WinRM shell v2.3

Info: Establishing connection to remote endpoint

*Evil-WinRM* PS C:\Users\bob\Documents>
```


