---
id: ac8832c9-c0c1-451e-b014-1366a6bb7923
type: code
language: Powershell
verified: false
created_at: '2023-05-30T13:38:03.980345+00:00'
updated_at: '2023-05-30T13:47:18.352784+00:00'
---

# Code Snippet ac8832c9

**Language**: Powershell

```powershell
# Import the AzureAD module by running the 'Import-Module' command with the path to the AzureAD.psd1 file.
Import-Module C:\Tools\AzureAD\AzureAD.psd1

# Create an access token for Azure AD by setting the '$AADToken' variable to the access token value.
$AADToken = 'eyJ0…'

# Connect to Azure AD using the 'Connect-AzureAD' command with the '-AadAccessToken', '-TenantId', and '-AccountId' arguments. Replace <TENANT-ID> with your tenant ID and <ACCOUNT-ID> with your account ID.
Connect-AzureAD -AadAccessToken $AADToken -TenantId <TENANT-ID> -AccountId <ACCOUNT-ID>
```
