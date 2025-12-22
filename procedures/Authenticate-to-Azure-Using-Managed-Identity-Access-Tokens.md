---
id: 6691e7e9-a931-4621-b34c-ef5f5767d533
name: Authenticate-to-Azure-Using-Managed-Identity-Access-Tokens
type: procedure
verified: true
submitted: true
created_at: '2023-04-06T03:56:15.293900+00:00'
updated_at: '2023-05-30T13:47:18.352959+00:00'
tactics:
  - '[[Lateral Movement]]'
techniques:
  - '[[T1078.004]]'
  - '[[T1550.005]]'
sub_techniques: []
tags:
  - '[[tags/Cloud - Azure]]'
  - '[[tags/Token from Managed Identity]]'
  - '[[tags/Use Tokens]]'
  - cloud-access
  - token-abuse
commands:
  - '[[commands/connect-azaccount-with-access-token]]'
  - '[[commands/connect-azaccount-with-access-token-and-graph-token]]'
  - '[[commands/connect-azuread-with-aad-token]]'
  - '[[commands/import-azuread-module]]'
  - '[[commands/get-azresource]]'
  - '[[commands/set-aadtoken-variable]]'
platforms:
  - Azure
  - Windows
tools: []
validated: true
---

# Authenticate-to-Azure-Using-Managed-Identity-Access-Tokens

## Summary

This procedure demonstrates how to authenticate to Azure services using access tokens obtained from Azure Managed Identities, enabling access to Azure resources and Microsoft Graph API without traditional username/password credentials. It covers connecting via the Az PowerShell module and optionally the AzureAD module, allowing attackers with compromised managed identity access to enumerate and interact with cloud resources for lateral movement or data exfiltration.

## Description

Azure Managed Identities provide automatic authentication for Azure resources to other Azure services via Azure AD. If an attacker gains access to a system with a managed identity (e.g., via initial foothold on a VM), they can retrieve access tokens to impersonate the identity and authenticate to Azure Resource Manager (ARM), Microsoft Graph, or other services. This procedure outlines retrieving and using these tokens with Connect-AzAccount for Az module interactions and Connect-AzureAD for directory operations. It assumes the attacker has the token (e.g., from [[procedures/Retrieve-Azure-Managed-Identity-Token]] or similar) and focuses on authentication and basic resource access. This technique maps to abusing cloud account credentials for persistence and lateral movement in hybrid environments, with risks of unauthorized resource modification or data theft.

## Requirements

1. PowerShell 5.1 or later installed on a Windows system with access to the target Azure environment.
2. Az PowerShell module (version 5.0 or later) installed via Install-Module -Name Az -AllowClobber.
3. Optional: AzureAD PowerShell module installed via Install-Module -Name AzureAD.
4. Valid access token from a managed identity, including Account ID (object ID of the identity) and optional Graph access token.
5. Network access to Azure endpoints (e.g., management.azure.com, graph.microsoft.com) without firewall blocks.
6. Appropriate permissions on the managed identity to access target resources (e.g., Reader role for enumeration).

## Defense

- Limit managed identity scopes to least privilege, avoiding broad roles like Contributor on subscriptions.
- Enable Azure AD logging and monitor for anomalous token usage via Microsoft Sentinel or Azure Monitor.
- Implement conditional access policies to restrict token redemption from untrusted locations.
- Regularly rotate and audit managed identities, disabling unused ones.
- Use Azure Policy to enforce just-in-time access and detect PowerShell module imports in sensitive environments.

## Objectives

1. Authenticate to Azure Resource Manager using a managed identity access token.
2. Optionally authenticate to Microsoft Graph using a combined access and Graph token.
3. Enumerate and access Azure resources post-authentication.
4. Connect to Azure AD for directory queries if needed.
5. Validate successful authentication and troubleshoot common errors like invalid tokens or permission denials.

## Instructions

### Step 1: Prepare Access Token Variable

**Context**: Set the access token obtained from the managed identity into a PowerShell variable for use in authentication commands. This token typically has a short lifespan (e.g., 1 hour), so use it promptly.

**Command** ([[commands/set-access-token-variable]]):
```powershell
$token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6Ik...' # Replace with actual token
```

> This assigns the JWT access token to $token. Expected output: No output; verify with Write-Output $token to confirm it's set correctly. If the token is malformed, subsequent connections will fail with AADSTS50011 errors.

### Step 2: Authenticate to Az Module with Access Token Only

**Context**: Use the access token to connect to Azure Resource Manager via the Az module. This enables management plane interactions like resource listing without Graph access.

**Command** ([[commands/connect-azaccount-with-access-token]]):
```powershell
Connect-AzAccount -AccessToken $token -AccountId <ACCOUNT-ID> # Replace <ACCOUNT-ID> with managed identity object ID
```

> This authenticates the session. Expected output: A confirmation message like "EnvironmentName : AzureCloud, Account : SystemAssignedManagedIdentity, TenantId : <tenant-id>". On failure, check token validity or AccountId.

### Step 3: Authenticate to Az Module with Access and Graph Tokens

**Context**: For scenarios requiring both ARM and Graph API access (e.g., user queries), provide both tokens. This is useful for hybrid operations involving directory and resource management.

**Command** ([[commands/connect-azaccount-with-access-token-and-graph-token]]):
```powershell
$graphToken = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6Ik...' # Replace with Graph token
Connect-AzAccount -AccessToken $token -GraphAccessToken $graphToken -AccountId <ACCOUNT-ID>
```

> Expected output: Similar to Step 2, but with Graph integration enabled (verify by running Get-AzContext). Errors may indicate mismatched scopes between tokens.

### Step 4: Access Azure Resources

**Context**: Post-authentication, query resources to validate access and enumerate the environment. This lists all accessible resources across subscriptions.

**Command** ([[commands/get-azresource]]):
```powershell
Get-AzResource
```

> Expected output: A table of resources including Name, ResourceType, Location, etc. (e.g., virtual machines, storage accounts). If empty, the identity lacks Reader permissions; success indicates viable access for further exploitation.

### Step 5: (Optional) Connect to Azure AD Module

**Context**: If directory operations are needed (e.g., user enumeration), import the AzureAD module and connect using an AAD-specific token. This extends access to Entra ID resources.

**Command** ([[commands/import-azuread-module]]):
```powershell
Import-Module AzureAD
```

> Expected output: No output if successful; error if module not installed.

**Command** ([[commands/set-aadtoken-variable]]):
```powershell
$AADToken = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6Ik...' # Replace with AAD token
```

> Sets the AAD token variable.

**Command** ([[commands/connect-azuread-with-aad-token]]):
```powershell
Connect-AzureAD -AadAccessToken $AADToken -TenantId <TENANT-ID> -AccountId <ACCOUNT-ID>
```

> Expected output: "Welcome To Azure AD PowerShell" or similar. Use Get-AzureADUser to test. Decision point: If Graph token from Step 3 suffices, skip this; otherwise, use for legacy AD operations.
