---
id: 272b6934-1ac3-4c62-9bbb-481bdf1c9071
name: Find Domain Shares
type: command
executor: bash
data: 'net share

  powershell Find-DomainShare -ComputerDomain domain.local'
output: null
created_at: '2023-04-06T03:56:28.696564+00:00'
updated_at: '2023-04-10T20:37:53.209844+00:00'
---

# Find Domain Shares

```bash
net share
powershell Find-DomainShare -ComputerDomain domain.local
```
