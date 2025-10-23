---
id: e8906d2c-2738-4a25-958b-e4a789290821
name: List Azure Runbooks
type: command
executor: bash
data: 'Get-AzAutomationAccount

  Get-AzAutomationRunbook -AutomationAccountName <AutomationAccountName> -ResourceGroupName
  <ResourceGroupName>

  '
output: null
created_at: '2020-07-14T19:07:50.912201+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# List Azure Runbooks

```bash
Get-AzAutomationAccount
Get-AzAutomationRunbook -AutomationAccountName <AutomationAccountName> -ResourceGroupName <ResourceGroupName>

```


