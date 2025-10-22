---
id: 25ff7b95-7411-4c1f-a56f-20d737a2b48c
name: Create PowerShell Runbook
type: command
executor: bash
data: Import-AzAutomationRunbook -Name <RUNBOOK-NAME> -Path C:\Tools\username.ps1
  -AutomationAccountName <AUTOMATION-ACCOUNT> -ResourceGroupName <RG-NAME> -Type PowerShell
  -Force -Verbose
output: null
created_at: '2023-05-24T22:50:53.202289+00:00'
updated_at: '2023-05-24T22:50:54.391095+00:00'
---

# Create PowerShell Runbook

```bash
Import-AzAutomationRunbook -Name <RUNBOOK-NAME> -Path C:\Tools\username.ps1 -AutomationAccountName <AUTOMATION-ACCOUNT> -ResourceGroupName <RG-NAME> -Type PowerShell -Force -Verbose
```
