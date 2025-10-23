---
id: f4d6e582-d8c2-4763-a958-67f33247ca83
name: Run commands on VMs
type: command
executor: bash
data: 'Invoke-AzVMRunCommand -ResourceGroupName $ResourceGroupName -VMName $VMName
  -CommandId RunPowerShellScript -ScriptPath ./powershell-script.ps1

  '
output: null
created_at: '2020-07-14T19:07:50.913495+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Run commands on VMs

```bash
Invoke-AzVMRunCommand -ResourceGroupName $ResourceGroupName -VMName $VMName -CommandId RunPowerShellScript -ScriptPath ./powershell-script.ps1

```


