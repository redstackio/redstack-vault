---
type: code
language: powershell
verified: true
created_at: '2023-05-24T07:13:54Z'
updated_at: '2023-05-24T07:13:54Z'
platforms:
  - Cloud
tags:
  - kudu
  - managed-identity
  - token-retrieval
validated: true
---

# kudu-powershell-retrieve-system-assigned-identity-token

## Code

```powershell
# or KUDU Debug Console Powershell - System Assigned Managed Identity
$resourceURI = "https://storage.azure.com"
$tokenAuthURI = $env:IDENTITY_ENDPOINT + "?resource=$resourceURI&api-version=2019-08-01"
$tokenResponse = Invoke-RestMethod -Method Get -Headers @{"X-IDENTITY-HEADER"="$env:IDENTITY_HEADER"} -Uri $tokenAuthURI
$accessToken = $tokenResponse.access_token
$accessToken
```

## Description

This PowerShell script retrieves an access token for a system-assigned Managed Identity via the Kudu debug console on an Azure App Service. It uses environment variables provided by Azure ($env:IDENTITY_ENDPOINT and $env:IDENTITY_HEADER) to request a token from the identity service for a specified resource URI.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $resourceURI | The target Azure resource endpoint for the token | "https://storage.azure.com" |

## Usage

Execute this script directly in the PowerShell environment of the Kudu debug console (accessible via https://yourapp.scm.azurewebsites.net/DebugConsole). Ensure the App Service has a system-assigned Managed Identity enabled. Update $resourceURI as needed for different services (e.g., "https://management.azure.com" for ARM). The script is useful in post-compromise scenarios to obtain tokens for lateral movement without CLI tools.

## Detection

- Monitor Azure Activity Logs for GET requests to the IDENTITY_ENDPOINT (/metadata/identity/oauth2/token).
- Enable Kudu access logging and audit PowerShell executions in App Service diagnostics.
- Look for anomalous token requests in Microsoft Defender for Cloud alerts on identity misuse.
- Network traffic to 169.254.169.254 (IMDS) or identity endpoints from App Services.

## Related

- [[procedures/Retrieve-Access-Tokens-from-Azure-Managed-Identity]]
