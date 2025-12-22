---
id: 252e554d-270a-4a3f-b678-0601ee26f288
name: Azure-Resource-Management-and-Privilege-Checking-with-PowerShell
type: procedure
verified: true
submitted: true
created_at: '2023-04-06T03:56:15.193985+00:00'
updated_at: '2023-05-24T08:08:13.420439+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
  - '[[tactics/Persistence|TA0003 - Persistence]]'
techniques:
  - '[[techniques/Account Manipulation|T1098 - Account Manipulation]]'
  - '[[techniques/Application Access Token|T1527 - Application Access Token]]'
sub_techniques: []
tags:
  - '[[tags/Azure API via Powershell]]'
  - '[[tags/Cloud - Azure]]'
  - '[[tags/Token from Managed Identity]]'
commands: []
platforms:
  - Azure
  - Cloud
tools: []
validated: true
---

# Azure-Resource-Management-and-Privilege-Checking-with-PowerShell

## Summary

This procedure utilizes PowerShell and the Invoke-RestMethod cmdlet to interact with Azure resources via the REST API. It covers authentication with an access token, retrieving subscription lists, accessing resource details, and checking for specific privileges like runCommand within resource groups. This is useful for privilege escalation or lateral movement in Azure environments where managed identity tokens are available.

## Description

In cloud environments like Azure, attackers with initial access to a token (e.g., from a managed identity) can query the Management API to enumerate subscriptions, resources, and permissions. This procedure demonstrates how to use PowerShell to send authenticated GET requests to Azure endpoints, allowing discovery of accessible resources and verification of high-privilege actions such as executing commands on virtual machines. It assumes the token has sufficient scope for read access to management resources and is applicable in scenarios involving compromised workloads or service principals.

## Requirements

1. PowerShell 5.1 or later installed on a system with internet access.
2. Azure PowerShell modules (Az.Accounts, Az.Resources) installed via Install-Module -Name Az -AllowClobber, though only core cmdlets like Invoke-RestMethod are used.
3. A valid Azure access token (e.g., obtained from managed identity via curl 'http://169.254.169.254/metadata/identity/oauth2/token' or similar).
4. Network access to Azure Management API endpoints (https://management.azure.com).
5. Permissions implied by the token scope (at least Reader role on subscriptions).

## Defense

- Rotate and monitor access tokens regularly, using short-lived tokens where possible.
- Enable Azure Activity Logs and integrate with SIEM for API call monitoring, alerting on unusual Invoke-RestMethod patterns or permission queries.
- Implement least-privilege RBAC, avoiding broad scopes like Contributor on managed identities.
- Use Azure Policy to restrict API access and audit token usage via Microsoft Entra ID logs.

## Objectives

1. Authenticate API requests using a bearer token to access Azure Management endpoints.
2. Enumerate available subscriptions and resource details for reconnaissance.
3. Verify permissions for actions like runCommand to identify escalation paths.
4. Gather intelligence on resource groups and virtual machines for further exploitation.

## Instructions

### Step 1: Retrieve List of Subscriptions

**Context**: Begin by authenticating with the access token and querying the Azure Management API to list all accessible subscriptions. This provides an overview of the attacker's scope and potential targets for further enumeration.

**Code** ([[codes/PowerShell-Retrieve-Azure-Subscriptions]]):

```powershell
# Retrieve a list of subscriptions
$Token = 'eyJ0eX..'
$URI = 'https://management.azure.com/subscriptions?api-version=2020-01-01'
# $URI = 'https://graph.microsoft.com/v1.0/applications'
$RequestParams = @{
 Method = 'GET'
 Uri = $URI
 Headers = @{
 'Authorization' = "Bearer $Token"
 }
}
(Invoke-RestMethod @RequestParams).value 
```

> Replace the $Token placeholder with a valid Azure access token. This script sends a GET request and outputs subscription details including IDs and names. Expected output includes a list of subscription objects if the token has read access.

### Step 2: List Resources in a Subscription

**Context**: Using a specific subscription ID, query for resources to identify virtual machines, resource groups, and other assets. This step helps map the environment for targeted privilege checks.

**Code** ([[codes/PowerShell-List-Azure-Resources-and-Permissions]]):

```powershell
# Retrieve a list of subscriptions
$Token = 'eyJ0eX..'
$URI = 'https://management.azure.com/subscriptions/b3d2186f-0d10-4944-1c88-d7d853d36886/resources?api-version=2020-10-01'
$RequestParams = @{
 Method = 'GET'
 Uri = $URI
 Headers = @{
 'Authorization' = "Bearer $Token"
 }
}
(Invoke-RestMethod @RequestParams).value 

# List resources and check for runCommand privileges
$URI = 'https://management.azure.com/subscriptions/b3d2186f-0d10-4944-1c88-d7d853d36886/resourceGroups/<RG-NAME>/providers/Microsoft.Compute/virtualMachines/<RESOURCE/providers/Microsoft.Authorization/permissions?apiversion=2015-07-01'
```

> Update the subscription ID in the URI and replace $Token. The first part lists resources; the second sets a URI for permissions (execute the request params on this URI in a follow-up). Output shows resource types, locations, and IDs.

### Step 3: Check for RunCommand Privileges

**Context**: Target a specific resource group and virtual machine to query permissions, focusing on Microsoft.Compute/virtualMachines/runCommand/actions/write to detect if command execution is possible for lateral movement or persistence.

**Code** ([[codes/PowerShell-Check-Azure-RunCommand-Privileges]]):

```powershell
# Check for runCommand privileges
$Token = 'eyJ0eX..'
$URI = 'https://management.azure.com/subscriptions/b3d2186f-0d10-4944-1c88-d7d853d36886/resourceGroups/<RG-NAME>/providers/Microsoft.Compute/virtualMachines/<RESOURCE/providers/Microsoft.Authorization/permissions?apiversion=2015-07-01'
$RequestParams = @{
 Method = 'GET'
 Uri = $URI
 Headers = @{
 'Authorization' = "Bearer $Token"
 }
}
(Invoke-RestMethod @RequestParams).value 
```

> Replace placeholders for subscription ID, RG-NAME, and RESOURCE. This queries the Authorization endpoint for permissions. Look for 'runCommand' in the output to confirm write access.
