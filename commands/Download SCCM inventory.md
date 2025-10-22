---
id: 34d3a881-1696-4064-b34c-dacd076feaf9
name: Download SCCM inventory
type: command
executor: bash
data: Invoke-CMLootInventory -SCCMHost sccm01.domain.local -Outfile sccmfiles.txt
output: null
created_at: '2023-04-06T03:56:08.273750+00:00'
updated_at: '2023-04-10T20:36:07.127790+00:00'
---

# Download SCCM inventory

```bash
Invoke-CMLootInventory -SCCMHost sccm01.domain.local -Outfile sccmfiles.txt
```
