---
id: 9606780e-e37d-4fb0-b440-a2d788e2155e
name: publish-azure-runbook
type: command
executor: powershell
data: >-
  Publish-AzAutomationRunbook -RunbookName $_RUNBOOK_NAME -AutomationAccountName
  $_AUTOMATION_ACCOUNT_NAME -ResourceGroupName $_RESOURCE_GROUP_NAME -Verbose
output: null
created_at: '2023-05-24T22:50:53.202914+00:00'
updated_at: '2023-05-24T22:50:54.391095+00:00'
platforms:
  - Cloud
tags:
  - azure
  - execution
verified: true
validated: true
---

# publish-azure-runbook

## Command

```powershell
Publish-AzAutomationRunbook -RunbookName $_RUNBOOK_NAME -AutomationAccountName $_AUTOMATION_ACCOUNT_NAME -ResourceGroupName $_RESOURCE_GROUP_NAME -Verbose
```

## Description

This Azure PowerShell command publishes a draft runbook, making it available for execution. Essential after importing malicious content to activate it.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_RUNBOOK_NAME | Name of the runbook to publish | Yes |
| $_AUTOMATION_ACCOUNT_NAME | Automation Account name | Yes |
| $_RESOURCE_GROUP_NAME | Resource group name | Yes |
| -Verbose | Detailed output | No |

## Examples

### Basic Usage

```powershell
Publish-AzAutomationRunbook -RunbookName "MaliciousRunbook" -AutomationAccountName "MyAccount" -ResourceGroupName "MyRG" -Verbose
```

### Advanced Usage

Publish with confirmation: Publish-AzAutomationRunbook ... -Confirm

## Expected Output

Verbose success: "Runbook published successfully, State: Published."

## Related

- [[procedures/Create-and-Execute-Malicious-Azure-Runbook]]
- [[commands/create-powershell-runbook]]
