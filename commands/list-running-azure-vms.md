---
type: command
executor: powershell
data: >-
  Get-AzureRmVM -Status | Where-Object {$_.PowerState -eq "VM running"} |
  Select-Object ResourceGroupName, Name
output: |-
  ResourceGroupName    Name       
  -----------------    ----       
  TESTRESOURCES        Remote-Test
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Cloud
tags:
  - azure
  - discovery
verified: true
validated: true
---

# List Running Azure VMs

## Command

```powershell
Get-AzureRmVM -Status | Where-Object {$_.PowerState -eq "VM running"} | Select-Object ResourceGroupName, Name
```

## Description

Queries Azure for all VMs in the subscription and filters to show only those in a running state, displaying resource group and name for targeting.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -Status | Includes power state in query | Built-in |
| Where-Object {$_.PowerState -eq "VM running"} | Filters for powered-on VMs | Built-in |
| Select-Object ResourceGroupName, Name | Outputs only relevant fields | Built-in |

## Examples

### Basic Usage

```powershell
Get-AzureRmVM -Status | Where-Object {$_.PowerState -eq "VM running"} | Select-Object ResourceGroupName, Name
```

### Advanced Usage

Add sorting:

```powershell
Get-AzureRmVM -Status | Where-Object {$_.PowerState -eq "VM running"} | Select-Object ResourceGroupName, Name | Sort-Object ResourceGroupName
```

## Expected Output

```
ResourceGroupName    Name       
-----------------    ----       
TESTRESOURCES        Remote-Test
```

## Related

- [[procedures/azure-vm-runcommand-execution]]
- [[commands/get-public-ip-of-azure-vm]]
