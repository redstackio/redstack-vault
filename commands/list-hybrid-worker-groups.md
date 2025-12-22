---
id: 476e87a2-37c3-4cb5-ab85-995f246c1718
name: list-hybrid-worker-groups
type: command
executor: powershell
data: >-
  Get-AzAutomationHybridWorkerGroup -AutomationAccountName
  $_AUTOMATION_ACCOUNT_NAME -ResourceGroupName $_RESOURCE_GROUP_NAME
output: null
created_at: '2023-05-24T22:50:53.201551+00:00'
updated_at: '2023-05-24T22:50:54.391095+00:00'
platforms:
  - Cloud
tags:
  - azure
  - discovery
verified: true
validated: true
---

# list-hybrid-worker-groups

## Command

```powershell
Get-AzAutomationHybridWorkerGroup -AutomationAccountName $_AUTOMATION_ACCOUNT_NAME -ResourceGroupName $_RESOURCE_GROUP_NAME
```

## Description

This Azure PowerShell command lists Hybrid Runbook Worker Groups associated with an Automation Account, identifying on-premises targets for remote script execution.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_AUTOMATION_ACCOUNT_NAME | Name of the Automation Account | Yes |
| $_RESOURCE_GROUP_NAME | Resource group name | Yes |

## Examples

### Basic Usage

```powershell
Get-AzAutomationHybridWorkerGroup -AutomationAccountName "MyAccount" -ResourceGroupName "MyRG"
```

### Advanced Usage

Select active groups: Get-AzAutomationHybridWorkerGroup ... | Where-Object { $_.IsPrimary -eq $true }

## Expected Output

List of groups, e.g., HybridWorkerGroupName: Workergroup1, Credential: Deleted. Includes status (Online/Offline).

## Related

- [[procedures/Create-and-Execute-Malicious-Azure-Runbook]]
- [[commands/start-azure-runbook]]
