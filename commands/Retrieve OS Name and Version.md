---
id: ff55c6fa-e4f1-408f-b6e3-a84a67e9aa79
name: Retrieve OS Name and Version
type: command
executor: bash
data: systeminfo | findstr /B /C:"OS Name" /C:"OS Version"
output: null
created_at: '2023-04-06T03:56:28.589156+00:00'
updated_at: '2023-04-10T20:37:36.292864+00:00'
---

# Retrieve OS Name and Version

```bash
systeminfo | findstr /B /C:"OS Name" /C:"OS Version"
```
