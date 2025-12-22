---
type: command
executor: powershell
data: >-
  Invoke-AzureRmVMRunCommand -ResourceGroupName <RESOURCE-GROUP> -VMName
  <VM-NAME> -CommandId RunPowerShellScript -ScriptPath <SCRIPT-PATH>
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Cloud
tags:
  - azure
  - execution
verified: true
validated: true
---

# Execute PowerShell Script on Azure VM (AzureRm)

## Command

```powershell
Invoke-AzureRmVMRunCommand -ResourceGroupName <RESOURCE-GROUP> -VMName <VM-NAME> -CommandId RunPowerShellScript -ScriptPath <SCRIPT-PATH>
```

## Description

Executes a PowerShell script on a specific Azure VM using the legacy AzureRm module's RunCommand feature, running as SYSTEM.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -ResourceGroupName | Azure resource group of the VM | Yes |
| -VMName | Name of the target VM | Yes |
| -CommandId | Set to 'RunPowerShellScript' for PS execution | Yes |
| -ScriptPath | Local path to the .ps1 script file | Yes |

## Examples

### Basic Usage

```powershell
Invoke-AzureRmVMRunCommand -ResourceGroupName TESTRESOURCES -VMName Remote-Test -CommandId RunPowerShellScript -ScriptPath Mimikatz.ps1
```

### Advanced Usage

With error handling:

```powershell
try { Invoke-AzureRmVMRunCommand -ResourceGroupName TESTRESOURCES -VMName Remote-Test -CommandId RunPowerShellScript -ScriptPath adduser.ps1 } catch { Write-Error $_.Exception.Message }
```

## Expected Output

```
Value [0] = {Status=Success; Message=...; Error=}
```

Success indicated by Status: Success in the response object.

## Related

- [[procedures/azure-vm-runcommand-execution]]
- [[codes/powershell-create-local-admin-user]]
