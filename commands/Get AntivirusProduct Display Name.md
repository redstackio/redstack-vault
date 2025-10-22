---
id: 7b8e774e-b67a-4490-96a3-746fe8a62b24
name: Get AntivirusProduct Display Name
type: command
executor: bash
data: WMIC /Node:localhost /Namespace:\\root\SecurityCenter2 Path AntivirusProduct
  Get displayName
output: null
created_at: '2023-04-06T03:56:28.745109+00:00'
updated_at: '2023-04-10T20:37:53.522638+00:00'
---

# Get AntivirusProduct Display Name

```bash
WMIC /Node:localhost /Namespace:\\root\SecurityCenter2 Path AntivirusProduct Get displayName
```
