---
id: a0a290e2-22f2-4cce-919d-a23465df7459
name: Enumerate Group Members
type: command
executor: bash
data: Get-DomainGroup -Identity <GroupName> | Select-Object -ExpandProperty Member
output: null
created_at: '2023-04-06T03:56:02.229697+00:00'
updated_at: '2023-04-06T21:33:38.759173+00:00'
---

# Enumerate Group Members

```bash
Get-DomainGroup -Identity <GroupName> | Select-Object -ExpandProperty Member
```
