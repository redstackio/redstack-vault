---
id: da3b4c8b-8e95-4c5c-b042-99a93ae9f58d
name: Backup ntds.dit file using esentutl.exe
type: command
executor: bash
data: esentutl.exe /y /vss c:\windows\ntds\ntds.dit /d c:\folder\ntds.dit
output: null
created_at: '2023-04-06T03:56:03.932787+00:00'
updated_at: '2023-04-10T20:25:54.587753+00:00'
---

# Backup ntds.dit file using esentutl.exe

```bash
esentutl.exe /y /vss c:\windows\ntds\ntds.dit /d c:\folder\ntds.dit
```
