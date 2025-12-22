---
id: 170c0c3c-0a41-4d5e-bb2d-92ce0610b5fd
type: code
language: Powershell
verified: true
created_at: '2023-05-24T08:08:13.412352+00:00'
updated_at: '2023-05-24T08:08:13.433836+00:00'
tags:
  - azure
  - api
  - subscriptions
  - recon
platforms:
  - Azure
  - Cloud
validated: true
---

# PowerShell-Retrieve-Azure-Subscriptions

## Code

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

## Description

This PowerShell script authenticates to the Azure Management API using a bearer token and retrieves a list of accessible subscriptions. It uses Invoke-RestMethod to send a GET request, providing subscription IDs, names, and states for reconnaissance in cloud environments.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $Token | Azure access token (bearer) obtained from managed identity or service principal | 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6Ik...' |
| $URI | API endpoint for subscriptions (modifiable for other queries like applications) | 'https://management.azure.com/subscriptions?api-version=2020-01-01' |

## Usage

Execute in PowerShell after obtaining a token (e.g., via managed identity endpoint). Useful as the first step in Azure enumeration to scope accessible environments. Integrate into procedures for cloud lateral movement.

## Detection

- Monitor Azure Sign-in logs for unusual token usage from managed identities.
- PowerShell execution logs (Module Logging, Script Block Logging) showing Invoke-RestMethod to management.azure.com.
- Network traffic to Azure IP ranges with bearer token headers.

## Related

- [[procedures/Azure-Resource-Management-and-Privilege-Checking-with-PowerShell]]
