---
type: command
executor: powershell
data: >-
  Get-AzVM -Name <VM-NAME> -ResourceGroupName <RESOURCE-GROUP> | Select-Object
  -ExpandProperty NetworkProfile

  Get-AzNetworkInterface -Name <NIC-NAME>

  Get-AzPublicIpAddress -Name <PUBLIC-IP-NAME>
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Cloud
tags:
  - azure
  - recon
verified: true
validated: true
---

# Get Public IP of Azure VM

## Command

```powershell
Get-AzVM -Name <VM-NAME> -ResourceGroupName <RESOURCE-GROUP> | Select-Object -ExpandProperty NetworkProfile
Get-AzNetworkInterface -Name <NIC-NAME>
Get-AzPublicIpAddress -Name <PUBLIC-IP-NAME>
```

## Description

This sequence of commands retrieves the public IP address associated with an Azure VM by navigating from the VM object to its network interface and public IP resource. Use this after listing VMs to prepare for direct connections.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| <VM-NAME> | Name of the target Azure VM | Yes |
| <RESOURCE-GROUP> | Azure resource group containing the VM | Yes |
| <NIC-NAME> | Name of the network interface (from first command output) | Yes |
| <PUBLIC-IP-NAME> | Name of the public IP resource (from second command output) | Yes |

## Examples

### Basic Usage

```powershell
Get-AzVM -Name MyVM -ResourceGroupName MyRG | Select-Object -ExpandProperty NetworkProfile
Get-AzNetworkInterface -Name myNic
Get-AzPublicIpAddress -Name myPublicIP
```

### Advanced Usage

Pipe outputs for automation:

```powershell
$vm = Get-AzVM -Name MyVM -ResourceGroupName MyRG
$nicName = $vm.NetworkProfile.NetworkInterfaces[0].Id.Split('/')[-1]
Get-AzPublicIpAddress -Name (Get-AzNetworkInterface -Name $nicName).IpConfigurations.PublicIpAddress.Id.Split('/')[-1]
```

## Expected Output

First command:

```
Id       : /subscriptions/.../networkInterfaces/myNic

Subnets  : [...]
```

Second:

```
Name : myNic
IpConfigurations : [...]
```

Third:

```
Name : myPublicIP
IpAddress : 20.123.45.67
```

## Related

- [[procedures/azure-vm-runcommand-execution]]
- [[commands/connect-to-vm-via-winrm]]
