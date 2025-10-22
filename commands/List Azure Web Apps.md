---
id: 999ef99c-98af-4839-8418-7d786923db5e
name: List Azure Web Apps
type: command
executor: bash
data: Get-AzWebApp | ?{$_.Kind -notmatch "functionapp"}
output: null
created_at: '2023-05-23T19:23:37.742098+00:00'
updated_at: '2023-05-23T19:23:39.396554+00:00'
---

# List Azure Web Apps

```bash
Get-AzWebApp | ?{$_.Kind -notmatch "functionapp"}
```
