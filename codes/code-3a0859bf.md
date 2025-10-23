---
id: 3a0859bf-3ab3-4c6c-a070-6796abc25bf6
type: code
language: Powershell
verified: false
created_at: '2023-05-24T22:50:18.652986+00:00'
updated_at: '2023-05-24T22:50:53.420047+00:00'
---

# Code Snippet 3a0859bf

**Language**: Powershell

```powershell
# Check user right for automation
az extension add --upgrade -n automation
# if it doesn't return anything the user is not a part of an Automation group
az automation account list 
az ad signed-in-user list-owned-objects

# If the user is not part of an "Automation" group.
# Add him to a custom group , e.g: "Automation Admins"
Add-AzureADGroupMember -ObjectId <OBJID> -RefObjectId <REFOBJID> -Verbose

# Get the role of a user on the Automation account
# Contributor or higher = Can create and execute Runbooks
Get-AzRoleAssignment -Scope /subscriptions/<ID>/resourceGroups/<RG-NAME>/providers/Microsoft.Automation/automationAccounts/<AUTOMATION-ACCOUNT>

# List hybrid workers
Get-AzAutomationHybridWorkerGroup -AutomationAccountName <AUTOMATION-ACCOUNT> -ResourceGroupName <RG-NAME>

# Create a Powershell Runbook
PS C:\Tools> Import-AzAutomationRunbook -Name <RUNBOOK-NAME> -Path C:\Tools\username.ps1 -AutomationAccountName <AUTOMATION-ACCOUNT> -ResourceGroupName <RG-NAME> -Type PowerShell -Force -Verbose

# Publish the Runbook
Publish-AzAutomationRunbook -RunbookName <RUNBOOK-NAME> -AutomationAccountName <AUTOMATION-ACCOUNT> -ResourceGroupName <RG-NAME> -Verbose

# Start the Runbook
Start-AzAutomationRunbook -RunbookName <RUNBOOK-NAME> -RunOn Workergroup1 -AutomationAccountName <AUTOMATION-ACCOUNT> -ResourceGroupName <RG-NAME> -Verbose
```


