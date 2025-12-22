---
id: 8f46ec37-39c0-4ec7-b0db-31684ff0eb98
name: start-azure-runbook
type: command
executor: powershell
data: >-
  Start-AzAutomationRunbook -RunbookName $_RUNBOOK_NAME -RunOn
  $_WORKER_GROUP_NAME -AutomationAccountName $_AUTOMATION_ACCOUNT_NAME
  -ResourceGroupName $_RESOURCE_GROUP_NAME -Verbose
output: null
created_at: '2023-05-24T22:50:53.203523+00:00'
updated_at: '2023-05-24T22:50:54.391095+00:00'
platforms:
  - Cloud
tags:
  - azure
  - execution
verified: true
validated: true
---

# start-azure-runbook

## Command

```powershell
Start-AzAutomationRunbook -RunbookName $_RUNBOOK_NAME -RunOn $_WORKER_GROUP_NAME -AutomationAccountName $_AUTOMATION_ACCOUNT_NAME -ResourceGroupName $_RESOURCE_GROUP_NAME -Verbose
```

## Description

This Azure PowerShell command starts a runbook job, optionally targeting a Hybrid Worker Group for on-premises execution of malicious scripts.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_RUNBOOK_NAME | Name of the published runbook | Yes |
| $_WORKER_GROUP_NAME | Hybrid Worker Group to run on (e.g., Workergroup1); omit for cloud execution | No |
| $_AUTOMATION_ACCOUNT_NAME | Automation Account name | Yes |
| $_RESOURCE_GROUP_NAME | Resource group name | Yes |
| -Verbose | Detailed output | No |

## Examples

### Basic Usage

```powershell
Start-AzAutomationRunbook -RunbookName "MaliciousRunbook" -AutomationAccountName "MyAccount" -ResourceGroupName "MyRG" -Verbose
```

### Advanced Usage

Target hybrid: Start-AzAutomationRunbook ... -RunOn "Workergroup1"

## Expected Output

Job object with ID, e.g., "Job started with ID: guid-1234, Status: Running."

## Related

- [[procedures/Create-and-Execute-Malicious-Azure-Runbook]]
- [[commands/list-hybrid-worker-groups]]
