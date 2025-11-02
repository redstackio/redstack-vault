---
id: 8dd58733-1c07-4ca7-88aa-994a9b3ed2a7
name: msfvenom Execute Calculator
type: command
executor: bash
data: msfvenom -p windows/exec cmd=calc.exe -a x86 -f exe > msf-calc.exe
output: 'root@hacker:~# msfvenom -p windows/exec cmd=calc.exe -a x86 -f exe > msf-calc.exe

  [-] No platform was selected, choosing Msf::Module::Platform::Windows from the payload

  No encoder or badchars specified, outputting raw payload

  Payload size: 193 bytes

  Final size of exe file: 73802 bytes

  '
created_at: '2019-10-10T18:41:08.050852+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
tools:
- '[[msfvenom]]'
---

# msfvenom Execute Calculator

```bash
msfvenom -p windows/exec cmd=calc.exe -a x86 -f exe > msf-calc.exe
```

## Expected Output

```
root@hacker:~# msfvenom -p windows/exec cmd=calc.exe -a x86 -f exe > msf-calc.exe
[-] No platform was selected, choosing Msf::Module::Platform::Windows from the payload
No encoder or badchars specified, outputting raw payload
Payload size: 193 bytes
Final size of exe file: 73802 bytes

```


