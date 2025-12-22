---
id: 13e85fef-b352-4b4a-8e59-6cb3fa834119
name: Azure-Automation-Account-Setup-Script
type: code
language: powershell
verified: true
created_at: '2023-05-25T03:23:29.834679+00:00'
updated_at: '2023-05-25T03:23:29.850067+00:00'
platforms:
  - Azure
tags:
  - cloud-azure
  - persistence
  - automation-account
  - setup
validated: true
---

# Azure-Automation-Account-Setup-Script

## Code

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

## Description

This PowerShell script sets up an Azure Automation Account, imports a specified Runbook (runbook.ps1), publishes it, generates a webhook URI, and creates an enabled webhook with a 1-year expiry. It uses the Free plan and enables the Run As account for service principal authentication, preparing the environment for persistent Runbook execution via remote triggers.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $automationAccountName | Name of the new Automation Account | MyPersistAccount |
| $resourceGroupName | Existing or new Resource Group name | MyRG |
| $location | Azure region for deployment | eastus |
| $runbookName | Path to the Runbook script file | ./runbook.ps1 |
| $webhookName | Name for the webhook | PersistHook |
| $webhookExpiryDate | Expiry date for the webhook (defaults to 1 year from now) | (Get-Date).AddYears(1) |

## Usage

Run this script after Az login in PowerShell with appropriate permissions (see [[procedures/Azure-Automation-Account-Runbook-Persistence]]). Substitute variables before execution. The script outputs the webhook URI; store it securely for triggering. Verify setup in Azure portal under Automation Accounts.

## Detection

- Azure Activity Logs: Creations of Automation Accounts, Runbook imports, publications, and webhook setups from suspicious IPs or accounts.
- Resource Group changes: New Automation resources in monitored groups.
- Service principal usage: Logs for Run As connection activations post-setup.

## Related

- [[procedures/Azure-Automation-Account-Runbook-Persistence]]
- [[codes/Azure-Automation-Runbook-User-Creation-Script]]
