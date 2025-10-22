---
id: e8a6177c-c0ad-4ea7-abfe-fb7ccbd726ab
name: Copy VSS to Destination Directory
type: command
executor: bash
data: 'Import-Module .\Copy-VSS.ps1

  Copy-VSS

  Copy-VSS -DestinationDir C:\ShadowCopy\'
output: null
created_at: '2023-04-06T03:56:03.847753+00:00'
updated_at: '2023-04-10T20:26:27.031869+00:00'
---

# Copy VSS to Destination Directory

```bash
Import-Module .\Copy-VSS.ps1
Copy-VSS
Copy-VSS -DestinationDir C:\ShadowCopy\
```
