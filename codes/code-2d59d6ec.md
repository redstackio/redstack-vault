---
id: 2d59d6ec-88dd-410b-aeeb-a4c0a35933f1
type: code
language: Powershell
verified: false
created_at: '2023-05-25T03:23:08.771193+00:00'
updated_at: '2023-05-25T03:23:29.839469+00:00'
---

# Code Snippet 2d59d6ec

**Language**: Powershell

```powershell
# Red Stack Labs

# Variables
$automationAccountName = "<YourAutomationAccountName>"
$resourceGroupName = "<YourResourceGroupName>"
$location = "<YourResourceLocation>"
$runbookName = "runbook.ps1"
$webhookName = "<YourWebhookName>"
$webhookExpiryDate = (Get-Date).AddYears(1) # The webhook will expire in 1 year.

# Create an Automation Account with 'Run As' account
New-AzAutomationAccount -Name $automationAccountName -Location $location -ResourceGroupName $resourceGroupName -Plan Free 

# Import the runbook
Import-AzAutomationRunbook -AutomationAccountName $automationAccountName -ResourceGroupName $resourceGroupName -Path $runbookName -Type PowerShell -Force -LogVerbose

# Publish the runbook
Publish-AzAutomationRunbook -AutomationAccountName $automationAccountName -Name $runbookName

# Generate a webhook URI
$webhookURI = New-AzAutomationWebhookURI

# Create a webhook for the runbook
New-AzAutomationWebhook -ResourceGroupName $resourceGroupName -AutomationAccountName $automationAccountName -RunbookName $runbookName -ExpiryTime $webhookExpiryDate -IsEnabled $true -Name $webhookName -URI $webhookURI

# Output the webhook URI
$webhookURI

```


