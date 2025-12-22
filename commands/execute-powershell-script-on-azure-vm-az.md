---
type: command
executor: powershell
data: >-
  Invoke-AzVMRunCommand -VMName <VM-NAME> -ResourceGroupName <RESOURCE-GROUP>
  -CommandId 'RunPowerShellScript' -ScriptPath '<SCRIPT-PATH>' -Verbose
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

# Execute PowerShell Script on Azure VM (Az)

## Command

```powershell
Invoke-AzVMRunCommand -VMName <VM-NAME> -ResourceGroupName <RESOURCE-GROUP> -CommandId 'RunPowerShellScript' -ScriptPath '<SCRIPT-PATH>' -Verbose
```

## Description

Runs a PowerShell script on an Azure VM using the modern Az module's RunCommand, providing verbose output for troubleshooting.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -VMName | Name of the target VM | Yes |
| -ResourceGroupName | Azure resource group | Yes |
| -CommandId | 'RunPowerShellScript' for PS scripts | Yes |
| -ScriptPath | Path to local .ps1 file | Yes |
| -Verbose | Enables detailed logging | No |

## Examples

### Basic Usage

```powershell
Invoke-AzVMRunCommand -VMName MyVM -ResourceGroupName MyRG -CommandId 'RunPowerShellScript' -ScriptPath '.\adduser.ps1' -Verbose
```

### Advanced Usage

Capture output:

```powershell
$result = Invoke-AzVMRunCommand -VMName MyVM -ResourceGroupName MyRG -CommandId 'RunPowerShellScript' -ScriptPath 'script.ps1'
$result.Value[0].Message
```

## Expected Output

```
VERBOSE: Performing operation 'Invoke RunCommand' on target 'MyVM'.
Value [0] = {Status=Success; ...}
```

## Related

- [[procedures/azure-vm-runcommand-execution]]
- [[commands/execute-powershell-script-on-azure-vm-azurerm]]
