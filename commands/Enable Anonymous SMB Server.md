---
id: 702f0fc3-6c9e-46ee-bd5d-6260d09bbd9b
name: Enable Anonymous SMB Server
type: command
executor: bash
data: Import-Module .\Invoke-BuildAnonymousSMBServer.ps1; Invoke-BuildAnonymousSMBServer
  -Path C:\Share -Mode Enable
output: null
created_at: '2023-04-06T03:56:02.899026+00:00'
updated_at: '2023-04-10T20:25:42.637746+00:00'
---

# Enable Anonymous SMB Server

```bash
Import-Module .\Invoke-BuildAnonymousSMBServer.ps1; Invoke-BuildAnonymousSMBServer -Path C:\Share -Mode Enable
```


