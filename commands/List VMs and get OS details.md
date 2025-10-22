---
id: df43329c-b032-4c85-8c8c-93a7197d7b65
name: List VMs and get OS details
type: command
executor: bash
data: 'Get-AzVM

  $vm = Get-AzVM -Name "VM Name"

  $vm.OSProfile

  '
output: null
created_at: '2020-07-14T19:07:50.913117+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# List VMs and get OS details

```bash
Get-AzVM
$vm = Get-AzVM -Name "VM Name"
$vm.OSProfile

```
