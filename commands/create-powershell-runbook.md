---
id: 25ff7b95-7411-4c1f-a56f-20d737a2b48c
name: create-powershell-runbook
type: command
executor: powershell
data: >-
  Import-AzAutomationRunbook -Name $_RUNBOOK_NAME -Path $_SCRIPT_PATH
  -AutomationAccountName $_AUTOMATION_ACCOUNT_NAME -ResourceGroupName
  $_RESOURCE_GROUP_NAME -Type PowerShell -Force -Verbose
output: null
created_at: '2023-05-24T22:50:53.202289+00:00'
updated_at: '2023-05-24T22:50:54.391095+00:00'
platforms:
  - Cloud
tags:
  - azure
  - execution
verified: true
validated: true
---

# create-powershell-runbook

## Command

```powershell
Import-AzAutomationRunbook -Name $_RUNBOOK_NAME -Path $_SCRIPT_PATH -AutomationAccountName $_AUTOMATION_ACCOUNT_NAME -ResourceGroupName $_RESOURCE_GROUP_NAME -Type PowerShell -Force -Verbose
```

## Description

This Azure PowerShell command imports a local PowerShell script as a new runbook into an Automation Account, allowing automation of malicious tasks. The script path points to the malicious payload file.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_RUNBOOK_NAME | Name for the new runbook | Yes |
| $_SCRIPT_PATH | Local path to the PowerShell script file | Yes |
| $_AUTOMATION_ACCOUNT_NAME | Name of the target Automation Account | Yes |
| $_RESOURCE_GROUP_NAME | Resource group containing the account | Yes |
| -Type PowerShell | Specifies the runbook type | Yes |
| -Force | Overwrites if runbook exists | No |
| -Verbose | Detailed output | No |

## Examples

### Basic Usage

```powershell
Import-AzAutomationRunbook -Name "MaliciousRunbook" -Path "C:\Tools\malicious.ps1" -AutomationAccountName "MyAccount" -ResourceGroupName "MyRG" -Type PowerShell -Verbose
```

### Advanced Usage

Use with error handling: try { Import-AzAutomationRunbook ... } catch { Write-Error $_.Exception }

## Expected Output

Verbose confirmation of import, including runbook state (e.g., "Runbook imported successfully, State: New"). Includes runbook resource ID.

## Related

- [[procedures/Create-and-Execute-Malicious-Azure-Runbook]]
- [[commands/publish-azure-runbook]]
