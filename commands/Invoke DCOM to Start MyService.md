---
id: f56c3a03-6eb1-42ac-bd31-f2cc8b8fd861
name: Invoke DCOM to Start MyService
type: command
executor: bash
data: Invoke-DCOM -ComputerName '10.10.10.10' -Method ServiceStart "MyService"
output: null
created_at: '2023-04-06T03:56:07.043503+00:00'
updated_at: '2023-04-10T20:26:18.160002+00:00'
---

# Invoke DCOM to Start MyService

```bash
Invoke-DCOM -ComputerName '10.10.10.10' -Method ServiceStart "MyService"
```


