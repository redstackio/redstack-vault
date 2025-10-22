---
id: 63b26e91-f487-4f76-8cc2-672ec5d1051a
name: List of Domain Controllers using Get-ADDomainController
type: command
executor: bash
data: Get-ADDomainController -filter * | Select-Object name
output: null
created_at: '2023-04-06T03:56:02.526728+00:00'
updated_at: '2023-04-10T20:26:38.485387+00:00'
---

# List of Domain Controllers using Get-ADDomainController

```bash
Get-ADDomainController -filter * | Select-Object name
```
