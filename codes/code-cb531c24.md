---
id: cb531c24-0d8b-4845-b97b-41f4def7df65
type: code
language: Powershell
verified: false
created_at: '2023-05-24T22:50:53.195152+00:00'
updated_at: '2023-05-24T22:50:54.385125+00:00'
---

# Code Snippet cb531c24

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


