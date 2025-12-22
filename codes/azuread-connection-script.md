---
id: bb39d7eb-494e-4245-a9bc-82ba5d83fc06
name: azuread-connection-script
type: code
language: powershell
verified: true
created_at: '2023-05-30T13:47:18.322169+00:00'
updated_at: '2023-05-30T13:47:19.181302+00:00'
platforms:
  - Windows
tags:
  - cloud-auth
  - azuread
validated: true
---

# azuread-connection-script

## Code

```powershell
# Import the AzureAD module by running the 'Import-Module' command with the path to the AzureAD.psd1 file.
Import-Module C:\Tools\AzureAD\AzureAD.psd1

# Create an access token for Azure AD by setting the '$AADToken' variable to the access token value.
$AADToken = 'eyJ0…'

# Connect to Azure AD using the 'Connect-AzureAD' command with the '-AadAccessToken', '-TenantId', and '-AccountId' arguments. Replace <TENANT-ID> with your tenant ID and <ACCOUNT-ID> with your account ID.
Connect-AzureAD -AadAccessToken $AADToken -TenantId <TENANT-ID> -AccountId <ACCOUNT-ID>
```

## Description

This script imports the AzureAD PowerShell module, sets an AAD access token variable, and connects to Azure AD for directory operations, enabling queries like user enumeration in a non-interactive manner using stolen or managed identity tokens.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $AADToken | AAD access token | 'eyJ0eXAiOiJKV1Qi...' |
| <TENANT-ID> | Azure AD tenant GUID | 'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx' |
| <ACCOUNT-ID> | Account object ID | '12345678-1234-1234-1234-123456789012' |

## Usage

Run in PowerShell after installing AzureAD module. Adjust path if module is in a custom location. Use post-connection for cmdlets like Get-AzureADUser. Ideal for lateral movement in Azure AD environments.

## Detection

- Module import logs in PowerShell transcription.
- Unusual Connect-AzureAD calls with -AadAccessToken in audit logs.
- Anomalous directory queries from service principals.

## Related

- [[procedures/Authenticate-to-Azure-Using-Managed-Identity-Access-Tokens]]
- [[tools/AzureAD-PowerShell-Module]]
