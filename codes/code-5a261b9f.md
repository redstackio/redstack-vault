---
id: 5a261b9f-dcca-432e-bba4-a9a4781a3b99
type: code
language: ps1
verified: false
created_at: '2023-04-06T03:56:08.273670+00:00'
updated_at: '2023-04-10T20:36:07.124928+00:00'
---

# Code Snippet 5a261b9f

**Language**: ps1

```ps1
Invoke-CMLootInventory -SCCMHost sccm01.domain.local -Outfile sccmfiles.txt
Invoke-CMLootDownload -SingleFile \\sccm\SCCMContentLib$\DataLib\SC100001.1\x86\MigApp.xml
Invoke-CMLootDownload -InventoryFile .\sccmfiles.txt -Extension msi
```


