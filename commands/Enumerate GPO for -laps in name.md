---
id: 29d2b8d6-ccea-4a6c-9f55-fcef8b82de51
name: Enumerate GPO for *laps in name
type: command
executor: ''
data: Get-DomainGPO | ? { $_.DisplayName -like "*laps*" } | select DisplayName, Name,
  GPCFileSysPath | fl
output: null
created_at: '2023-01-12T19:20:30.302673+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Enumerate GPO for *laps in name

```bash
Get-DomainGPO | ? { $_.DisplayName -like "*laps*" } | select DisplayName, Name, GPCFileSysPath | fl
```
