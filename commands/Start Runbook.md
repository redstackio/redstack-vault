---
id: 8f46ec37-39c0-4ec7-b0db-31684ff0eb98
name: Start Runbook
type: command
executor: bash
data: Start-AzAutomationRunbook -RunbookName <RUNBOOK-NAME> -RunOn Workergroup1 -AutomationAccountName
  <AUTOMATION-ACCOUNT> -ResourceGroupName <RG-NAME> -Verbose
output: null
created_at: '2023-05-24T22:50:53.203523+00:00'
updated_at: '2023-05-24T22:50:54.391095+00:00'
---

# Start Runbook

```bash
Start-AzAutomationRunbook -RunbookName <RUNBOOK-NAME> -RunOn Workergroup1 -AutomationAccountName <AUTOMATION-ACCOUNT> -ResourceGroupName <RG-NAME> -Verbose
```


