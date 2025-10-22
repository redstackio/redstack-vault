---
id: 8fca16c0-388c-4971-b61f-0d2934d0f051
name: Get Public IP of VM
type: command
executor: bash
data: 'Get-AzVM -Name <RESOURCE> -ResourceGroupName <RG-NAME> | select -ExpandProperty
  NetworkProfile

  Get-AzNetworkInterface -Name <RESOURCE368>

  Get-AzPublicIpAddress -Name <RESOURCEIP>'
output: null
created_at: '2023-05-28T03:59:38.555951+00:00'
updated_at: '2023-05-28T03:59:38.880779+00:00'
---

# Get Public IP of VM

```bash
Get-AzVM -Name <RESOURCE> -ResourceGroupName <RG-NAME> | select -ExpandProperty NetworkProfile
Get-AzNetworkInterface -Name <RESOURCE368>
Get-AzPublicIpAddress -Name <RESOURCEIP>
```
